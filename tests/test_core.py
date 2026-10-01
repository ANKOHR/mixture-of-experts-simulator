import copy

import pytest

from mixture_of_experts_simulator.core import SchemaError, compare_capacity, select_experts, simulate
from mixture_of_experts_simulator.fixtures import fixture_data


def test_fixture_ground_truth_matches_hand_computed():
    records, config, expected = fixture_data()
    result = simulate(records, config)
    assert result["totals"] == expected["totals"]
    assert result["experts"] == expected["experts"]
    for record, route in zip(records, result["routes"]):
        assert route["selected"] == [record["ground_truth"]["expert"]]
        assert bool(route["dropped"]) is record["ground_truth"]["dropped"]


def test_top_k_ties_capacity_and_reconciliation():
    config = dict(experts=3, top_k=2, capacity=1, synthetic=True, reference_date="2026-09-30")
    records = [dict(id=str(i), scores=[5, 5, 5], synthetic=True) for i in range(2)]
    result = simulate(records, config)
    assert result["routes"][0]["accepted"] == [0, 1]
    assert result["routes"][1]["dropped"] == [0, 1]
    assert result["totals"]["attempted"] == 4
    assert result["totals"]["accepted"] + result["totals"]["dropped"] == 4
    assert result["totals"]["boundary_ties"] == 2


@pytest.mark.parametrize("field,value", [
    ("scores", [-1, 0, 0, 0]), ("scores", [True, 0, 0, 0]),
    ("scores", [1.5, 0, 0, 0]), ("scores", [10**12, 0, 0, 0]),
    ("scores", [float("nan"), 0, 0, 0]), ("scores", [1]),
    ("date", "2026-10-01"), ("date", "bad"), ("text", "x" * 100001),
    ("id", "x" * 4097), ("synthetic", "true"), ("amount", -1),
], ids=["negative-score", "bool-score", "float-score", "huge-score", "nan-score",
        "score-width", "future-date", "bad-date", "long-text", "long-id",
        "bad-provenance", "unknown-amount"])
def test_rejects_adversarial_values(field, value):
    records, config, _ = fixture_data()
    record = dict(records[0], **{field: value})
    with pytest.raises(SchemaError, match=field):
        simulate([record], config)


@pytest.mark.parametrize("field,value", [("capacity", -1), ("top_k", 5),
                                        ("experts", 0), ("reference_date", "tomorrow")])
def test_invalid_config(field, value):
    records, config, _ = fixture_data()
    with pytest.raises(SchemaError, match=field):
        simulate(records, dict(config, **{field: value}))


def test_duplicate_ids_rejected():
    records, config, _ = fixture_data()
    with pytest.raises(SchemaError, match="duplicate"):
        simulate([records[0], records[0]], config)


def test_corrupted_fixture_changes_computed_counts():
    records, config, expected = fixture_data()
    changed = copy.deepcopy(records)
    changed[0]["scores"] = [0, 0, 10, 0]
    result = simulate(changed, config)
    assert result["experts"] != expected["experts"]
    assert result["totals"]["boundary_ties"] == 49
    from mixture_of_experts_simulator.report import render
    assert render(result, "json") != render(simulate(records, config), "json")
    # Corrupting labels alone cannot change a computed result.
    changed = copy.deepcopy(records)
    changed[0]["ground_truth"] = dict(expert=3, dropped=True)
    assert simulate(changed, config) == simulate(records, config)


def test_pure_and_repeatable():
    records, config, _ = fixture_data()
    original = copy.deepcopy((records, config))
    assert simulate(records, config) == simulate(records, config)
    assert (records, config) == original


def test_selection_and_sweep():
    assert select_experts([5, 9, 9, 0], 2) == [1, 2]
    records, config, _ = fixture_data()
    scenarios = compare_capacity(records, config, [0, 40, 50])
    assert [s["totals"]["accepted"] for s in scenarios] == [0, 160, 200]


def test_partial_acceptance_is_counted():
    config = dict(experts=3, top_k=2, capacity=1, synthetic=True, reference_date="2026-09-30")
    records = [dict(id="a", scores=[9, 8, 0], synthetic=True),
               dict(id="b", scores=[9, 0, 8], synthetic=True)]
    result = simulate(records, config)
    assert result["routes"][1]["accepted"] == [2]
    assert result["routes"][1]["dropped"] == [0]
    assert result["totals"]["records_with_drops"] == 1
    assert result["totals"]["records_fully_dropped"] == 0
