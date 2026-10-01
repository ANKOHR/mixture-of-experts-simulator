# Mixture-of-Experts Simulator

Data provenance: 200 synthetic fixture records; 0 user-supplied records labelled real by the input author (ownership and authenticity not independently verified). All figures are computed routing simulation counts from supplied scores. Model quality, real throughput, time saved and money saved are unmeasured.

## Configuration

```json
{
  "capacity": 40,
  "experts": 4,
  "reference_date": "2026-09-30",
  "synthetic": true,
  "top_k": 1
}
```

## Computed counts

| Figure | Count |
| --- | ---: |
| accepted | 160 |
| attempted | 200 |
| boundary_ties | 50 |
| dropped | 40 |
| records | 200 |
| records_fully_dropped | 40 |
| records_with_drops | 40 |

## Expert loads

| Expert | Attempted | Accepted | Dropped |
| ---: | ---: | ---: | ---: |
| 0 | 50 | 40 | 10 |
| 1 | 50 | 40 | 10 |
| 2 | 50 | 40 | 10 |
| 3 | 50 | 40 | 10 |

## Traceability

Input hashes (SHA-256, raw file bytes):

- 'config.json': `4a86ce8bc4e5ca5072332978a02a0d32a5908aa1e4c2568bed9daff5214a2037`
- 'records.jsonl': `cdcc82eb771cbc276fb4839ec4fd7753850abff3f2e667c52ce363647010a641`

Per-record routing trace (JSON preserves IDs and avoids Markdown ambiguity):

```json
[
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-00",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-01",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-02",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-03",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-04",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-05",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-06",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-07",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-08",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-09",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-10",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-11",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-12",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-13",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-14",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-15",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-16",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-17",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-18",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-19",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-20",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-21",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-22",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-23",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-24",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-25",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-26",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-27",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-28",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-29",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-30",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-31",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-32",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-33",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-34",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-35",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-36",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-37",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-38",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      0
    ],
    "boundary_tie": true,
    "dropped": [],
    "id": "token-0-39",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": true,
    "dropped": [
      0
    ],
    "id": "token-0-40",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": true,
    "dropped": [
      0
    ],
    "id": "token-0-41",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": true,
    "dropped": [
      0
    ],
    "id": "token-0-42",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": true,
    "dropped": [
      0
    ],
    "id": "token-0-43",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": true,
    "dropped": [
      0
    ],
    "id": "token-0-44",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": true,
    "dropped": [
      0
    ],
    "id": "token-0-45",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": true,
    "dropped": [
      0
    ],
    "id": "token-0-46",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": true,
    "dropped": [
      0
    ],
    "id": "token-0-47",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": true,
    "dropped": [
      0
    ],
    "id": "token-0-48",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": true,
    "dropped": [
      0
    ],
    "id": "token-0-49",
    "selected": [
      0
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-00",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-01",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-02",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-03",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-04",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-05",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-06",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-07",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-08",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-09",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-10",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-11",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-12",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-13",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-14",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-15",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-16",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-17",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-18",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-19",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-20",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-21",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-22",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-23",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-24",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-25",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-26",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-27",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-28",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-29",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-30",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-31",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-32",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-33",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-34",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-35",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-36",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-37",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-38",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      1
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-1-39",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      1
    ],
    "id": "token-1-40",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      1
    ],
    "id": "token-1-41",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      1
    ],
    "id": "token-1-42",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      1
    ],
    "id": "token-1-43",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      1
    ],
    "id": "token-1-44",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      1
    ],
    "id": "token-1-45",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      1
    ],
    "id": "token-1-46",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      1
    ],
    "id": "token-1-47",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      1
    ],
    "id": "token-1-48",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      1
    ],
    "id": "token-1-49",
    "selected": [
      1
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-00",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-01",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-02",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-03",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-04",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-05",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-06",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-07",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-08",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-09",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-10",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-11",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-12",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-13",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-14",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-15",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-16",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-17",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-18",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-19",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-20",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-21",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-22",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-23",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-24",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-25",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-26",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-27",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-28",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-29",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-30",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-31",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-32",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-33",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-34",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-35",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-36",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-37",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-38",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      2
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-2-39",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      2
    ],
    "id": "token-2-40",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      2
    ],
    "id": "token-2-41",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      2
    ],
    "id": "token-2-42",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      2
    ],
    "id": "token-2-43",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      2
    ],
    "id": "token-2-44",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      2
    ],
    "id": "token-2-45",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      2
    ],
    "id": "token-2-46",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      2
    ],
    "id": "token-2-47",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      2
    ],
    "id": "token-2-48",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      2
    ],
    "id": "token-2-49",
    "selected": [
      2
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-00",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-01",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-02",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-03",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-04",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-05",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-06",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-07",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-08",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-09",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-10",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-11",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-12",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-13",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-14",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-15",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-16",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-17",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-18",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-19",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-20",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-21",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-22",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-23",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-24",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-25",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-26",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-27",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-28",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-29",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-30",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-31",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-32",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-33",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-34",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-35",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-36",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-37",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-38",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [
      3
    ],
    "boundary_tie": false,
    "dropped": [],
    "id": "token-3-39",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      3
    ],
    "id": "token-3-40",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      3
    ],
    "id": "token-3-41",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      3
    ],
    "id": "token-3-42",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      3
    ],
    "id": "token-3-43",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      3
    ],
    "id": "token-3-44",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      3
    ],
    "id": "token-3-45",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      3
    ],
    "id": "token-3-46",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      3
    ],
    "id": "token-3-47",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      3
    ],
    "id": "token-3-48",
    "selected": [
      3
    ],
    "synthetic": true
  },
  {
    "accepted": [],
    "boundary_tie": false,
    "dropped": [
      3
    ],
    "id": "token-3-49",
    "selected": [
      3
    ],
    "synthetic": true
  }
]
```
