"""Deterministic serialization and provenance-aware report rendering."""

import json


def safe_text(text):
    # Escape this character even when it appears in user data or paths.
    return text.replace(chr(0x2014), "\\u2014")


def json_text(value):
    return safe_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2)) + "\n"


def banner(result):
    p = result["provenance"]
    return (f"Data provenance: {p['synthetic_records']} synthetic fixture records; "
            f"{p['user_supplied_records']} user-supplied records labelled real by the input author "
            "(ownership and authenticity not independently verified). "
            "All figures are computed routing simulation counts from supplied scores. "
            "Model quality, real throughput, time saved and money saved are unmeasured.")


def render(result, format="md"):
    if format == "json":
        return json_text(dict(result, provenance_banner=banner(result)))
    if format != "md":
        raise ValueError("format must be md or json")
    lines = ["# Mixture-of-Experts Simulator", "", banner(result), "",
             "## Configuration", "", "```json", json_text(result["config"]).rstrip(),
             "```", "", "## Computed counts", "", "| Figure | Count |", "| --- | ---: |"]
    lines += [f"| {key} | {value} |" for key, value in result["totals"].items()]
    lines += ["", "## Expert loads", "", "| Expert | Attempted | Accepted | Dropped |",
              "| ---: | ---: | ---: | ---: |"]
    lines += [f"| {e['expert']} | {e['attempted']} | {e['accepted']} | {e['dropped']} |"
              for e in result["experts"]]
    lines += ["", "## Traceability", "", "Input hashes (SHA-256, raw file bytes):", ""]
    lines += [f"- {item['path']!r}: `{item['sha256']}`" for item in result.get("inputs", [])]
    if not result.get("inputs"):
        lines.append("- No record input files.")
    lines += ["", "Per-record routing trace (JSON preserves IDs and avoids Markdown ambiguity):",
              "", "```json", json_text(result["routes"]).rstrip(), "```", ""]
    return safe_text("\n".join(lines))
