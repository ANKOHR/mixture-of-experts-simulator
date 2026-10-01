import csv
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

import pytest

from mixture_of_experts_simulator.cli import execute, build_parser
from mixture_of_experts_simulator.fixtures import generate


ROOT = Path(__file__).resolve().parents[1]


def cli(*args, cwd=ROOT):
    # Absolute source entry remains importable in a fresh cwd without installation.
    import os
    env = dict(os.environ, PYTHONPATH=str(ROOT))
    return subprocess.run([sys.executable, "-m", "mixture_of_experts_simulator.cli", *map(str, args)],
                          cwd=cwd, env=env, capture_output=True, encoding="utf-8")


def test_run_completes_on_fixture(tmp_path):
    start = time.perf_counter()
    assert cli("fixtures", "--out", tmp_path / "demo").returncode == 0
    assert cli("run", "--input", tmp_path / "demo", cwd=tmp_path).returncode == 0
    output = cli("report", "--format", "md", cwd=tmp_path)
    assert output.returncode == 0
    assert "200 synthetic fixture records" in output.stdout
    assert time.perf_counter() - start < 5


def test_empty_input_renders_without_traceback(tmp_path):
    assert cli("run", "--input", tmp_path, cwd=tmp_path).returncode == 0
    output = cli("report", "--format", "json", cwd=tmp_path)
    assert output.returncode == 0
    assert all(v == 0 for v in json.loads(output.stdout)["totals"].values())


@pytest.mark.parametrize("name,content,line", [
    ("bad.jsonl", '# synthetic\n{"id":\n', 2),
    ("bad.json", '[\n{"id":\n]', 3),
    ("bad.csv", 'id,scores,synthetic\na,"[1,2],true\n', 2),
    ("bad.yaml", 'scores: [broken\n', 1),
])
def test_malformed_input_named_error(tmp_path, name, content, line):
    (tmp_path / name).write_text(content, encoding="utf-8")
    result = cli("run", "--input", tmp_path, cwd=tmp_path)
    assert result.returncode == 2
    assert name in result.stderr
    assert f"line {line}" in result.stderr
    assert "Error:" in result.stderr
    assert "Traceback" not in result.stderr


def test_determinism_byte_identical(tmp_path):
    generate(tmp_path / "demo")
    for output in ("a.json", "b.json"):
        assert cli("run", "--input", tmp_path / "demo", "--results", tmp_path / output).returncode == 0
    assert (tmp_path / "a.json").read_bytes() == (tmp_path / "b.json").read_bytes()
    for fmt in ("md", "json"):
        a = cli("report", "--results", tmp_path / "a.json", "--format", fmt)
        b = cli("report", "--results", tmp_path / "b.json", "--format", fmt)
        assert a.stdout == b.stdout


def test_cli_smoke_all_subcommands(tmp_path):
    generate(tmp_path / "demo")
    for name in ("fixtures", "run", "report", "route", "sweep"):
        result = cli(name, "--help")
        assert result.returncode == 0
        assert "Example:" in result.stdout
    result = cli("route", "--input", tmp_path / "demo", "--id", "token-0-49")
    assert result.returncode == 0
    assert json.loads(result.stdout)["routes"][0]["dropped"] == [0]
    result = cli("sweep", "--input", tmp_path / "demo", "--capacities", 0, 40, 50)
    assert result.returncode == 0
    parsed = json.loads(result.stdout)
    assert [s["totals"]["dropped"] for s in parsed["scenarios"]] == [200, 40, 0]
    assert "Hypothetical" in result.stdout
    assert "200 synthetic fixture records" in result.stdout


def test_handles_unicode_and_long_inputs(tmp_path):
    record = dict(id="猫" * 4000, text="Zürich 猫 C:\\data\\input " * 3000,
                  scores=[9, 0, 0, 0], synthetic=False)
    (tmp_path / "records.jsonl").write_text(json.dumps(record, ensure_ascii=False) + "\n", encoding="utf-8")
    result_path = tmp_path / "result.txt"
    assert cli("run", "--input", tmp_path, "--results", result_path).returncode == 0
    output = cli("report", "--results", result_path, "--format", "json")
    assert output.returncode == 0
    assert json.loads(output.stdout)["routes"][0]["id"] == record["id"]


def test_write_failure_no_partial_files(tmp_path):
    generate(tmp_path / "demo")
    results = tmp_path / "result.txt"
    assert cli("run", "--input", tmp_path / "demo", "--results", results).returncode == 0
    output = cli("report", "--results", results, "--out", tmp_path / "missing" / "report.md")
    assert output.returncode == 2
    assert "WriteError:" in output.stderr
    assert not list(tmp_path.rglob(".moes-*"))
    existing_dir = tmp_path / "blocked"
    existing_dir.mkdir()
    output = cli("report", "--results", results, "--out", existing_dir)
    assert output.returncode == 2
    assert existing_dir.is_dir()
    assert not list(tmp_path.rglob(".moes-*"))


def test_missing_input_named_error(tmp_path):
    for args in (("run", "--input", tmp_path / "missing"), ("report", "--results", tmp_path / "missing")):
        output = cli(*args)
        assert output.returncode == 2
        assert "MissingInput:" in output.stderr
        assert "Traceback" not in output.stderr


def test_schema_drift_names_field_file_line(tmp_path):
    (tmp_path / "bad.jsonl").write_text('# synthetic\n{"id":"a","scores":[1],"synthetic":true}\n')
    output = cli("run", "--input", tmp_path)
    assert output.returncode == 2
    assert "SchemaError:" in output.stderr
    assert "scores" in output.stderr and "line 2" in output.stderr


def test_csv_real_input_and_hash(tmp_path):
    path = tmp_path / "records.csv"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["id", "scores", "synthetic", "text"])
        writer.writerow(["猫", "[0,9,0,0]", "false", "C:\\data\\input"])
    args = build_parser().parse_args(["route", "--input", str(tmp_path)])
    result = json.loads(execute(args))
    assert result["routes"][0]["selected"] == [1]
    assert result["provenance"]["user_supplied_records"] == 1
    assert result["inputs"][0]["sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()


def test_fixture_refuses_overwrite(tmp_path):
    generate(tmp_path)
    before = (tmp_path / "records.jsonl").read_bytes()
    assert cli("fixtures", "--out", tmp_path).returncode == 2
    assert (tmp_path / "records.jsonl").read_bytes() == before


def test_no_em_dashes_in_source():
    for directory in (ROOT / "mixture_of_experts_simulator", ROOT / "tests"):
        for path in directory.glob("*.py"):
            assert chr(0x2014) not in path.read_text(encoding="utf-8"), path


@pytest.mark.parametrize("content,error", [
    ('{"id":"a","id":"b","scores":[0,0,0,0],"synthetic":true}', "duplicate field"),
    ('{"id":"a","scores":[NaN,0,0,0],"synthetic":true}', "nonfinite"),
    ('{"id":"\\ud800","scores":[0,0,0,0],"synthetic":true}', "surrogate"),
    ("[" * 2000 + "]" * 2000, "nesting"),
], ids=["duplicate-json-key", "nonfinite-json", "unpaired-surrogate", "excessive-nesting"])
def test_adversarial_json_named_errors(tmp_path, content, error):
    (tmp_path / "records.jsonl").write_text(content + "\n", encoding="utf-8")
    result = cli("run", "--input", tmp_path)
    assert result.returncode == 2
    assert error in result.stderr
    assert "Traceback" not in result.stderr


def test_repeat_empty_run_ignores_default_results(tmp_path):
    for _ in range(2):
        assert cli("run", "--input", tmp_path, cwd=tmp_path).returncode == 0
    result = cli("report", "--format", "json", cwd=tmp_path)
    assert json.loads(result.stdout)["totals"]["records"] == 0


def test_argument_errors_escape_prohibited_punctuation():
    result = cli("report", "--format", chr(0x2014))
    assert result.returncode == 2
    assert chr(0x2014) not in result.stderr
