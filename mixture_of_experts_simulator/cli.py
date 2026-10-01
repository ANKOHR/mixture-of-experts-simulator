"""Local-file CLI. No networking, GPU dependencies, or model calls."""

import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile

from .core import DEFAULT_CONFIG, SchemaError, compare_capacity, simulate, validate_config, validate_records
from .fixtures import generate
from .report import banner, json_text, render, safe_text


class InputError(ValueError):
    """Named input failure suitable for presentation without a traceback."""


class SafeArgumentParser(argparse.ArgumentParser):
    def _print_message(self, message, file=None):
        if message:
            super()._print_message(safe_text(message), file)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate field {key!r}")
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError(f"nonfinite number {value}")


def check_json_depth(value):
    stack = [(value, 0)]
    while stack:
        item, depth = stack.pop()
        if depth > 64:
            raise ValueError("excessive JSON nesting: maximum depth 64")
        if isinstance(item, dict):
            stack.extend((child, depth + 1) for child in item.values())
        elif isinstance(item, list):
            stack.extend((child, depth + 1) for child in item)
    return value


def read_text(path):
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        raise InputError(f"ParseError: {path}: line 1: invalid UTF-8 at byte {exc.start}") from None


def decode_json(text, path, line_offset=0):
    try:
        return check_json_depth(json.loads(text, parse_constant=reject_constant,
                                           object_pairs_hook=unique_object))
    except json.JSONDecodeError as exc:
        raise InputError(f"ParseError: {path}: line {exc.lineno + line_offset}: {exc.msg}") from None
    except ValueError as exc:
        raise InputError(f"ParseError: {path}: line {line_offset + 1}: {exc}") from None
    except RecursionError:
        raise InputError(f"ParseError: {path}: line {line_offset + 1}: excessive JSON nesting") from None


def load_input(directory):
    directory = Path(directory)
    if not directory.is_dir():
        raise InputError(f"MissingInput: {directory}: use --input <existing directory>; try moes fixtures --out demo")
    config_path = directory / "config.json"
    config = dict(DEFAULT_CONFIG)
    inputs = []

    def fingerprint(path):
        inputs.append(dict(path=path.relative_to(directory).as_posix(),
                           sha256=hashlib.sha256(path.read_bytes()).hexdigest()))

    if config_path.exists():
        config = decode_json(read_text(config_path), config_path)
        fingerprint(config_path)
    try:
        config = validate_config(config)
    except SchemaError as exc:
        raise InputError(f"SchemaError: {config_path}: line 1: {exc}") from None
    records, locations = [], []
    for path in sorted(directory.iterdir(), key=lambda p: p.name):
        if not path.is_file() or path.name in {"config.json", "expectations.json", ".moes-results.json"}:
            continue
        if path.suffix.lower() in {".yaml", ".yml"}:
            raise InputError(f"SchemaError: {path}: line 1: unsupported YAML; use JSON, JSONL or CSV")
        if path.suffix.lower() not in {".json", ".jsonl", ".csv"}:
            continue
        text = read_text(path)
        fingerprint(path)
        if path.suffix.lower() == ".jsonl":
            for line_number, line in enumerate(text.splitlines(), 1):
                if not line.strip() or line.lstrip().startswith("#"):
                    continue
                records.append(decode_json(line, path, line_number - 1))
                locations.append((path, line_number))
        elif path.suffix.lower() == ".json":
            data = decode_json(text, path)
            if not isinstance(data, list):
                raise InputError(f"SchemaError: {path}: line 1: field records: expected JSON array")
            records.extend(data)
            locations.extend((path, 1) for _ in data)
        else:
            reader = csv.DictReader(io.StringIO(text), strict=True)
            try:
                if reader.fieldnames is None or not {"id", "scores", "synthetic"}.issubset(reader.fieldnames):
                    raise InputError(f"SchemaError: {path}: line 1: fields id,scores,synthetic required")
                if len(set(reader.fieldnames)) != len(reader.fieldnames):
                    raise InputError(f"SchemaError: {path}: line 1: duplicate header field")
                unknown = sorted(set(reader.fieldnames) - {"id", "scores", "synthetic", "text", "date", "ground_truth"})
                if unknown:
                    raise InputError(f"SchemaError: {path}: line 1: field {unknown[0]}: unknown field")
                for row in reader:
                    line_number = reader.line_num
                    if None in row or any(value is None for value in row.values()):
                        raise InputError(f"ParseError: {path}: line {line_number}: CSV column count mismatch")
                    if row["synthetic"] not in {"true", "false"}:
                        raise InputError(f"SchemaError: {path}: line {line_number}: field synthetic: use true or false")
                    row["synthetic"] = row["synthetic"] == "true"
                    row["scores"] = decode_json(row["scores"], path, line_number - 1)
                    if "ground_truth" in row:
                        row["ground_truth"] = decode_json(row["ground_truth"], path, line_number - 1)
                    records.append(row)
                    locations.append((path, line_number))
            except csv.Error as exc:
                raise InputError(f"ParseError: {path}: line {reader.reader.line_num}: {exc}") from None
    # Validate each row for accurate file and line attribution, then duplicates globally.
    seen = set()
    for record, (path, line) in zip(records, locations):
        try:
            validate_records([record], config)
            if record["id"] in seen:
                raise SchemaError(f"field id: duplicate {record['id']!r}")
            seen.add(record["id"])
        except SchemaError as exc:
            raise InputError(f"SchemaError: {path}: line {line}: {exc}") from None
    return records, config, inputs


def atomic_write(path, content):
    """Replace only after a complete write; remove temporary files on failure."""
    path = Path(path)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n",
                                         dir=path.parent, prefix=".moes-", delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    except OSError as exc:
        raise InputError(f"WriteError: {path}: {exc.strerror or exc}") from None
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def build_parser():
    parser = SafeArgumentParser(description="Compute deterministic routing simulation counts from local scores.")
    subs = parser.add_subparsers(dest="command", required=True)
    fixtures = subs.add_parser("fixtures", help="Generate 200 labelled synthetic records",
                               epilog="Example: moes fixtures --out demo")
    fixtures.add_argument("--out", required=True, type=Path)
    run = subs.add_parser("run", help="Simulate top-k routing with capacity limits",
                          epilog="Example: moes run --input demo --results results.json")
    run.add_argument("--input", required=True, type=Path)
    run.add_argument("--results", type=Path, default=Path(".moes-results.json"))
    report = subs.add_parser("report", help="Render saved results with data provenance",
                             epilog="Example: moes report --format md --out report.md")
    report.add_argument("--format", choices=("md", "json"), default="md")
    report.add_argument("--results", type=Path, default=Path(".moes-results.json"))
    report.add_argument("--out", type=Path)
    route = subs.add_parser("route", help="Show per-record selected, accepted and dropped experts",
                            epilog="Example: moes route --input demo --id token-0-49")
    route.add_argument("--input", required=True, type=Path)
    route.add_argument("--id", help="Filter to an exact record ID")
    sweep = subs.add_parser("sweep", help="Recompute hypothetical capacity scenarios",
                            epilog="Example: moes sweep --input demo --capacities 0 40 50")
    sweep.add_argument("--input", required=True, type=Path)
    sweep.add_argument("--capacities", required=True, type=int, nargs="+")
    return parser


def execute(args):
    if args.command == "fixtures":
        generate(args.out)
        return "Generated 200 SYNTHETIC records and hand-computed expectations.\n"
    if args.command == "report":
        if not args.results.is_file():
            raise InputError(f"MissingInput: {args.results}: first run moes run --input <directory>")
        result = decode_json(read_text(args.results), args.results)
        try:
            output = render(result, args.format)
        except (KeyError, TypeError, AttributeError, ValueError):
            raise InputError(f"SchemaError: {args.results}: line 1: field results: invalid saved result") from None
        if args.out:
            atomic_write(args.out, output)
            return f"Report written to {args.out}\n"
        return output
    records, config, inputs = load_input(args.input)
    result = simulate(records, config)
    result["inputs"] = inputs
    if args.command == "run":
        atomic_write(args.results, render(result, "json"))
        return (f"Computed routing simulation for {len(records)} records. "
                f"Synthetic: {result['provenance']['synthetic_records']}; "
                f"user-supplied: {result['provenance']['user_supplied_records']}. "
                f"Results: {args.results}\n")
    if args.command == "route":
        if args.id is not None:
            routes = [r for r in result["routes"] if r["id"] == args.id]
            if not routes:
                raise InputError(f"MissingInput: field id: {args.id!r} not found")
            result["routes"] = routes
        return render(result, "json")
    scenarios = compare_capacity(records, config, args.capacities)
    return json_text(dict(provenance_banner=banner(result),
                          provenance=result["provenance"], inputs=inputs, scenarios=scenarios))


def main(argv=None):
    # Explicit UTF-8 avoids Windows console mojibake, including redirected output.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    args = build_parser().parse_args(argv)
    try:
        output = execute(args)
    except (InputError, SchemaError, OSError) as exc:
        name = "" if isinstance(exc, InputError) else ("SchemaError: " if isinstance(exc, SchemaError) else "FileError: ")
        print(safe_text(name + str(exc)), file=sys.stderr)
        return 2
    print(safe_text(output), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
