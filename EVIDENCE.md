# Real-use evidence and decision log

Status: no real-use trial has been measured during the build. The two-week
window has not begun. Verdict: pending the evidence window. Synthetic fixture
checks are implementation evidence, not evidence of daily usefulness.

Build acceptance evidence is in `evidence/acceptance.json` and
`evidence/demo-report.md`: an actual local CLI wall-clock measurement on the
synthetic fixture, exact expected counts, all 40 planted drops found, and zero
false positives. This measurement is not real model throughput or time saved.

Keep Henry's actual input records and trial outcomes locally, outside published
fixtures. Copy this log to a private local file for the window. Record actual
dates and outcomes rather than filling placeholders with estimates.

| Run date | Used for actual work? | Hand-checked records | Wrong records | Top discrepancy cause |
| --- | --- | ---: | ---: | --- |

Primary metric: exact per-record routing accuracy against a hand-applied top-k
and capacity calculation in the same input order. Check at least 20 records per
used run (all records if fewer than 20). Preserve preceding capacity state when
checking a sampled record. One mismatch in selected, accepted or dropped experts
makes that record wrong. Aggregate error rate = wrong / checked; with zero checked
records the error rate is unmeasured, not zero. Also record actual used-run count.

At the end of 14 days from first real use, record:

- Window start and end, used-run count, checked and wrong counts.
- Measured error rate, or unmeasured if no checked records.
- The single top observed failure cause and one concrete fix, if error > 10 percent.
- Recheck evidence for any fix; if it cannot meet acceptance criteria, kill.
- One explicit verdict and reason: expand, integrate, commercialise, maintain, or kill.

Kill if never used. Expand for daily use or revenue, integrate for demonstrated
overlap, commercialise for a demonstrated buyer, otherwise maintain if used and
accurate as portfolio evidence. A build cannot honestly select a post-window
verdict before the window has elapsed.
