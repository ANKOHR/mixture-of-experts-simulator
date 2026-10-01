import json

from mixture_of_experts_simulator.core import compare_capacity, simulate
from mixture_of_experts_simulator.fixtures import fixture_data
from mixture_of_experts_simulator.report import json_text, render


def test_report_matches_ground_truth_exact():
    records, config, expected = fixture_data()
    result = json.loads(render(simulate(records, config), "json"))
    assert result["totals"] == expected["totals"]
    assert result["experts"] == expected["experts"]
    md = render(result)
    for key, value in expected["totals"].items():
        assert f"| {key} | {value} |" in md


def test_report_zero_false_positives():
    records, config, expected = fixture_data()
    result = json.loads(render(simulate(records, config), "json"))
    detected = {r["id"] for r in result["routes"] if r["dropped"]}
    planted = set(expected["dropped_ids"])
    assert detected == planted
    assert len(detected - planted) == 0
    assert len(planted - detected) == 0


def test_report_carries_provenance_banner():
    records, config, _ = fixture_data()
    records[0]["synthetic"] = False
    result = simulate(records, config)
    for fmt in ("md", "json"):
        text = render(result, fmt)
        assert "199 synthetic fixture records" in text
        assert "1 user-supplied records" in text
        assert "not independently verified" in text


def test_hypothetical_figures_labelled():
    records, config, _ = fixture_data()
    text = json_text(compare_capacity(records, config, [20]))
    assert "Hypothetical" in text
    assert "not measured model performance" in text
    assert "time saved and money saved are unmeasured" in render(simulate(records, config))


def test_no_em_dashes_in_outputs():
    records, config, _ = fixture_data()
    records[0]["id"] += chr(0x2014)
    result = simulate(records, config)
    for fmt in ("md", "json"):
        assert chr(0x2014) not in render(result, fmt)
    assert json.loads(render(result, "json"))["routes"][0]["id"] == records[0]["id"]
