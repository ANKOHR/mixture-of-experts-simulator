"""Pure routing logic. Scores are supplied inputs, never predicted probabilities.

Capacity and routing outcomes describe a simulation, not real model performance.
"""

from datetime import date


class SchemaError(ValueError):
    """An explicit input field violates the documented schema."""


def integer(value, field, minimum, maximum):
    if type(value) is not int or not minimum <= value <= maximum:
        raise SchemaError(f"field {field}: expected integer {minimum}..{maximum}")
    return value


def valid_unicode(value, field):
    if any(0xD800 <= ord(character) <= 0xDFFF for character in value):
        raise SchemaError(f"field {field}: unpaired Unicode surrogate")


def validate_config(config):
    if not isinstance(config, dict):
        raise SchemaError("field config: expected object")
    allowed = {"experts", "top_k", "capacity", "reference_date", "synthetic"}
    unknown = sorted(set(config) - allowed)
    if unknown:
        raise SchemaError(f"field {unknown[0]}: unknown config field")
    for field in allowed:
        if field not in config:
            raise SchemaError(f"field {field}: required")
    experts = integer(config["experts"], "experts", 1, 1024)
    integer(config["top_k"], "top_k", 1, experts)
    integer(config["capacity"], "capacity", 0, 1_000_000_000)
    if type(config["synthetic"]) is not bool:
        raise SchemaError("field synthetic: expected boolean")
    try:
        parsed = date.fromisoformat(config["reference_date"])
        if parsed.isoformat() != config["reference_date"]:
            raise ValueError()
    except (ValueError, TypeError):
        raise SchemaError("field reference_date: expected YYYY-MM-DD") from None
    return dict(config)


DEFAULT_CONFIG = dict(experts=4, top_k=1, capacity=40,
                      reference_date="2026-09-30", synthetic=False)


def validate_records(records, config):
    config = validate_config(config)
    seen = set()
    checked = []
    allowed = {"id", "scores", "synthetic", "text", "date", "ground_truth"}
    for index, record in enumerate(records, 1):
        prefix = f"record {index}"
        if not isinstance(record, dict):
            raise SchemaError(f"{prefix} field record: expected object")
        unknown = sorted(set(record) - allowed)
        if unknown:
            raise SchemaError(f"{prefix} field {unknown[0]}: unknown field")
        for field in ("id", "scores", "synthetic"):
            if field not in record:
                raise SchemaError(f"{prefix} field {field}: required")
        ident = record["id"]
        if not isinstance(ident, str) or not 1 <= len(ident) <= 4096:
            raise SchemaError(f"{prefix} field id: expected 1..4096 characters")
        valid_unicode(ident, f"{prefix}.id")
        if ident in seen:
            raise SchemaError(f"{prefix} field id: duplicate {ident!r}")
        seen.add(ident)
        if type(record["synthetic"]) is not bool:
            raise SchemaError(f"{prefix} field synthetic: expected boolean")
        scores = record["scores"]
        if not isinstance(scores, list) or len(scores) != config["experts"]:
            raise SchemaError(f"{prefix} field scores: expected {config['experts']} scores")
        for score in scores:
            integer(score, f"{prefix}.scores", 0, 1_000_000_000)
        if "text" in record and (not isinstance(record["text"], str)
                                  or len(record["text"]) > 100_000):
            raise SchemaError(f"{prefix} field text: expected at most 100000 characters")
        if "text" in record:
            valid_unicode(record["text"], f"{prefix}.text")
        if "date" in record:
            try:
                parsed = date.fromisoformat(record["date"])
                if parsed.isoformat() != record["date"]:
                    raise ValueError()
            except (ValueError, TypeError):
                raise SchemaError(f"{prefix} field date: expected YYYY-MM-DD") from None
            if record["date"] > config["reference_date"]:
                raise SchemaError(f"{prefix} field date: after reference_date")
        if "ground_truth" in record and not isinstance(record["ground_truth"], dict):
            raise SchemaError(f"{prefix} field ground_truth: expected object")
        checked.append(dict(record))
    return checked


def select_experts(scores, top_k):
    """Descending integer score, then ascending expert index for exact ties."""
    if not isinstance(scores, list) or not scores:
        raise SchemaError("field scores: expected nonempty list")
    for score in scores:
        integer(score, "scores", 0, 1_000_000_000)
    integer(top_k, "top_k", 1, len(scores))
    return sorted(range(len(scores)), key=lambda e: (-scores[e], e))[:top_k]


def simulate(records, config):
    """Attempt each top-k route once, in input order, without overflow rerouting."""
    config = validate_config(config)
    records = validate_records(records, config)
    loads = [dict(expert=e, attempted=0, accepted=0, dropped=0)
             for e in range(config["experts"])]
    routes = []
    ties = 0
    for record in records:
        selected = select_experts(record["scores"], config["top_k"])
        cutoff = record["scores"][selected[-1]]
        boundary_tie = sum(s >= cutoff for s in record["scores"]) > config["top_k"]
        ties += int(boundary_tie)
        accepted, dropped = [], []
        for expert in selected:
            load = loads[expert]
            load["attempted"] += 1
            if load["accepted"] < config["capacity"]:
                load["accepted"] += 1
                accepted.append(expert)
            else:
                load["dropped"] += 1
                dropped.append(expert)
        routes.append(dict(id=record["id"], selected=selected, accepted=accepted,
                           dropped=dropped, boundary_tie=boundary_tie,
                           synthetic=record["synthetic"]))
    totals = dict(records=len(records), attempted=sum(x["attempted"] for x in loads),
                  accepted=sum(x["accepted"] for x in loads),
                  dropped=sum(x["dropped"] for x in loads),
                  records_with_drops=sum(bool(r["dropped"]) for r in routes),
                  records_fully_dropped=sum(not r["accepted"] for r in routes),
                  boundary_ties=ties)
    return dict(config=config, totals=totals, experts=loads, routes=routes,
                provenance=dict(synthetic_records=sum(r["synthetic"] for r in records),
                                user_supplied_records=sum(not r["synthetic"] for r in records)))


def compare_capacity(records, config, capacities):
    """Hypothetical scenarios recomputed from the same supplied scores."""
    return [dict(label="Hypothetical capacity scenario, not measured model performance",
                 capacity=capacity,
                 totals=simulate(records, dict(config, capacity=capacity))["totals"])
            for capacity in capacities]
