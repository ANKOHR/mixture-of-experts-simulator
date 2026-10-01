import json

from mixture_of_experts_simulator.cli import load_input
from mixture_of_experts_simulator.fixtures import generate
from mixture_of_experts_simulator.core import simulate
from pathlib import Path


def test_fixtures_labelled_synthetic(tmp_path):
    generate(tmp_path)
    assert (tmp_path / "records.jsonl").read_text(encoding="utf-8").startswith("# SYNTHETIC")
    records, config, _ = load_input(tmp_path)
    assert len(records) == 200
    assert all(r["synthetic"] is True for r in records)
    assert config["synthetic"] is True
    assert json.loads((tmp_path / "expectations.json").read_text())["synthetic"] is True
    assert "SYNTHETIC" in (tmp_path / "SYNTHETIC.md").read_text()


def test_fixture_generation_deterministic(tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    generate(a)
    generate(b)
    assert {p.name: p.read_bytes() for p in a.iterdir()} == {p.name: p.read_bytes() for p in b.iterdir()}


def test_five_record_handwritten_example():
    directory = Path(__file__).resolve().parents[1] / "examples" / "five"
    records, config, _ = load_input(directory)
    expected = json.loads((directory / "expectations.json").read_text(encoding="utf-8"))
    result = simulate(records, config)
    assert result["totals"] == expected["totals"]
    assert [r["id"] for r in result["routes"] if r["dropped"]] == expected["dropped_ids"]
