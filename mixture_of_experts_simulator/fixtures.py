"""Labelled planted fixture, generated without randomness (no seed needed)."""

from pathlib import Path

from .report import json_text


def fixture_data():
    records = []
    # Hand calculation: four blocks of 50, capacity 40, top_k 1.
    # Each block sends 50 to its expert: 40 accepted and 10 dropped.
    for expert in range(4):
        for position in range(50):
            scores = [0, 0, 0, 0]
            scores[expert] = 9
            if expert == 0:
                scores[1] = 9  # 50 boundary ties, won by lower index 0.
            ident = f"token-{expert}-{position:02}"
            records.append(dict(id=ident, scores=scores, synthetic=True,
                                text="Synthetic token: Zürich 猫 C:\\tokens\\input",
                                ground_truth=dict(expert=expert, dropped=position >= 40)))
    expectations = dict(
        synthetic=True,
        label="Synthetic hand-computed ground truth, independent of simulator",
        calculation="4 blocks * 50 = 200; 4 * 40 = 160 accepted; 4 * 10 = 40 dropped; block 0 has 50 ties",
        totals=dict(records=200, attempted=200, accepted=160, dropped=40,
                    records_with_drops=40, records_fully_dropped=40, boundary_ties=50),
        experts=[dict(expert=e, attempted=50, accepted=40, dropped=10) for e in range(4)],
        dropped_ids=[f"token-{e}-{p:02}" for e in range(4) for p in range(40, 50)])
    config = dict(experts=4, top_k=1, capacity=40, reference_date="2026-09-30", synthetic=True)
    return records, config, expectations


def generate(out):
    """Refuse to overwrite fixture files in an existing directory."""
    out = Path(out)
    names = ("records.jsonl", "config.json", "expectations.json", "SYNTHETIC.md")
    if any((out / name).exists() for name in names):
        raise FileExistsError("fixture output already exists; choose a new --out directory")
    out.mkdir(parents=True, exist_ok=True)
    records, config, expectations = fixture_data()
    # JSON does not allow comments. JSONL has an explicit labelled comment header.
    (out / "records.jsonl").write_text(
        "# SYNTHETIC fixture records; synthetic: true\n" +
        "".join(json_text(r).replace("\n", "") + "\n" for r in records), encoding="utf-8")
    (out / "config.json").write_text(json_text(config), encoding="utf-8")
    (out / "expectations.json").write_text(json_text(expectations), encoding="utf-8")
    (out / "SYNTHETIC.md").write_text(
        "<!-- SYNTHETIC; synthetic: true -->\nAll files in this set are synthetic.\n",
        encoding="utf-8")
    return expectations
