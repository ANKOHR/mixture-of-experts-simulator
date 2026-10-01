# Lessons for KOML

This build separates routing priority from expert capacity. A deterministic
top-k selection can still drop assignments once an expert fills, and exact ties
need an explicit stable rule. Aggregate counts alone hide which records lose
routes, so the engine retains a per-record trace and reconciles all expert totals.

The planted-fixture hypothesis is checked by independent arithmetic: four blocks
of 50 attempts, capacity 40 each, imply 160 accepted and 40 dropped assignments.
Tests also alter scores and verify that computed outputs change. Altering labels
alone leaves routing unchanged, confirming that ground truth is not used by the
engine. This validates correctness for the specified rules; usefulness on real
research work remains an untested assumption until the two-week window.

Operating rule for future builds: specify ordering, tie-breaking, and overflow
semantics before implementing metrics, then prove both aggregate reconciliation
and per-record outcomes against independent planted labels. Keep scenario counts
clearly distinct from measured model performance or real-use benefit.
