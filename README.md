# Mixture-of-Experts Simulator

`moes` explores routing behaviour using supplied expert scores, top-k selection,
and batch capacity limits. It is a deterministic Python CLI for Henry and research
collaborators. It uses only the standard library at runtime, local files, and the
CPU. It makes no network requests or language-model calls.

## Hypothesis and acceptance criteria

A small tested simulator can make routing decisions inspectable and reproducible.
On the 200-record synthetic fixture, every count and every dropped-record ID must
match independent hand-computed ground truth, with zero false positives and zero
missed planted drops. The complete demo must run in under five seconds. These
checks validate this simulator, not the quality of a real MoE model.

## Quickstart

Python 3.10 or newer is required. From this directory, install using already
available setuptools, without fetching dependencies:

```powershell
python -m pip install --no-deps --no-build-isolation -e .
moes fixtures --out demo
moes run --input demo
moes report --format md
python -m pytest -q
```

In shells supporting `&&`, the demo is:

```text
moes fixtures --out demo && moes run --input demo && moes report --format md
```

If Windows does not have Python's Scripts directory on PATH, use
`python -m mixture_of_experts_simulator.cli` in place of `moes`, or add the Scripts
directory printed by the installation to the current shell's PATH. Pytest is the
only test dependency; it must already be installed for offline testing.

The demo generates 200 synthetic records. It computes 200 attempted assignments,
160 accepted assignments, 40 dropped assignments, 40 records with drops,
40 fully dropped records, and 50 boundary ties. Each of four experts has
50 attempts, 40 acceptances, and 10 drops. `demo/expectations.json` explains the
arithmetic; reports contain the complete per-record trace and input hashes.

For the smallest hand-written five-record example:

```text
moes run --input examples/five --results five-results.json
moes report --results five-results.json --format md
```

Expected counts: 5 attempts, 3 acceptances, 2 drops, 2 fully dropped records,
and 1 boundary tie. This example is also synthetic.

## Input format reference

An input directory contains optional `config.json` and one or more UTF-8 record
files. JSONL is recommended. Files are read in ascending filename order and rows
in their existing order. Capacity is shared across the entire directory, with no
reset between files. Ordering is part of the experiment.

```json
{
  "experts": 4,
  "top_k": 1,
  "capacity": 40,
  "reference_date": "2026-09-30",
  "synthetic": false
}
```

All five config fields are required when a config is present. Without it, the
above values are used. `experts` is an integer from 1 to 1024, `top_k` from 1 to
`experts`, and `capacity` from 0 to 1000000000. Capacity counts accepted assignments
per expert, across the whole run. `reference_date` is a fixed ISO date, never the
machine's current date. The config's synthetic field labels the configuration;
each record's flag determines the report's data provenance counts.

A record is:

```json
{"id":"token-001","scores":[9,4,0,1],"synthetic":false,"text":"Optional note","date":"2026-09-29"}
```

| Field | Rules |
| --- | --- |
| `id` | Required unique string, 1 to 4096 Unicode characters; exact comparison |
| `scores` | Required list of exactly `experts` nonnegative integers, each at most 1000000000; booleans and floats refused |
| `synthetic` | Required JSON boolean; `false` means author-labelled real input |
| `text` | Optional string, at most 100000 characters; ignored for routing |
| `date` | Optional canonical YYYY-MM-DD, no later than the explicit reference date; ignored for routing |
| `ground_truth` | Optional object of fixture labels; never used to compute routes |

Scores are abstract priorities, not probabilities or measured quality. Unknown
fields, negative scores, duplicate IDs, future dates, excessive strings, and
schema drift are rejected with a named error. Amounts and savings are outside the
schema and are refused. Unicode and Windows paths in text are supported. There
is no tokenization, model execution, training, or score generation.
Duplicate JSON fields, nonfinite numeric constants, JSON nesting beyond depth 64, and
unpaired Unicode surrogates in IDs or text are also rejected.

Supported record files:

- `.jsonl`: one object per nonempty line; `#` comment lines are allowed.
- `.json`: an array of record objects. Standard JSON cannot contain comments.
- `.csv`: header containing `id,scores,synthetic`, with optional record fields;
  `scores` is a quoted JSON array, `synthetic` is exactly `true` or `false`,
  and `ground_truth`, if present, is a JSON object. Use CSV quoting for commas.

YAML is explicitly rejected with the filename and line 1, even when malformed.
Other file extensions are ignored. `config.json`, `expectations.json` and the
default `.moes-results.json` are reserved and excluded from record discovery.
Do not put custom result JSON or unrelated JSON files in the input directory.
An empty existing directory is valid and produces a zero-count report.

## Routing rules and count definitions

For each record, sort expert indices by descending score and then ascending
index. Select the first `top_k` experts. Each selected expert receives one attempt.
Accept it if that expert has spare capacity; otherwise record a drop. Overflow
is never rerouted. A record can be partially accepted when `top_k > 1`.

A boundary tie means more than `top_k` scores are greater than or equal to the
last selected score. Ties entirely inside the selected set do not count.
`records_with_drops` counts any record losing an assignment;
`records_fully_dropped` counts records losing all selected assignments.
Always: `attempted = records * top_k = accepted + dropped`. Expert counts sum
exactly to the corresponding totals. No rounding, floating point, randomness,
or seeds are involved.

## Subcommand catalogue

| Command | Purpose and example |
| --- | --- |
| `fixtures` | Create labelled fixtures; `moes fixtures --out demo` |
| `run` | Compute and atomically save results; `moes run --input demo --results results.json` |
| `report` | Render Markdown or JSON; `moes report --results results.json --format json --out report.json` |
| `route` | Inspect routes; `moes route --input demo --id token-0-49` |
| `sweep` | Recompute hypothetical capacity scenarios; `moes sweep --input demo --capacities 0 40 50` |

Every command supports `--help` with an example. `run` defaults to
`.moes-results.json` in the working directory. `report` reads that result;
it does not rerun inputs. Use `run` again after changing inputs. Keep saved
results unedited: they are local computed artifacts, not authenticated records.
Reports use SHA-256 hashes of raw input files, including the config when present.
Paths are relative to the input directory so moving an identical fixture does
not change output bytes. Output is UTF-8 with deterministic JSON ordering and LF
line endings in saved files. User punctuation prohibited by the build brief is
escaped as a JSON Unicode escape, preserving decoded data.

## Architecture

```text
fixtures.py -> labelled local files + independent expectations
local files -> cli.py parsing and validation -> core.py pure routing
                                             -> computed result JSON
computed result JSON -> report.py -> Markdown / JSON with provenance
same records + explicit capacities -> core.py -> hypothetical sweep
```

`core.py` has no file or network I/O. Tests exercise independent planted labels,
top-k ties and partial drops, malformed files, unknown fields, numeric boundaries,
duplicate IDs, deterministic bytes, Unicode, and atomic output failures. Altering
fixture scores changes computed figures; altering ground-truth labels alone does
not. Ground truth is an oracle used by tests, never an engine input.

## Honesty boundary and fixture labelling

All counts describe the supplied-score routing simulation. Even with real scores,
capacity sweeps are explicitly hypothetical model scenarios. No result discovers
or predicts expert suitability, model accuracy, actual throughput, time saved,
or money saved. Savings remain unmeasured and are never assigned a number.
Provenance banners report record flags and say that user-labelled ownership and
authenticity were not independently verified. Henry can enter his own real records
by hand with `synthetic: false`; real trial data and outcomes are not shipped.

Synthetic JSONL has a header comment and every record has `synthetic: true`.
Synthetic JSON config and expectations carry `synthetic: true` because JSON has
no comment syntax. The fixture Markdown carries a synthetic header comment.
Hand-written examples follow the same policy. Fixtures refuse to overwrite an
existing set. Reports and domain outputs retain provenance.

## Failure modes

| Failure | Behaviour |
| --- | --- |
| Malformed JSON, JSONL or CSV | `ParseError` naming file and parser line; invalid UTF-8 reports byte offset and line 1 |
| Missing directory or saved result | `MissingInput` with usage hint, exit 2 |
| Wrong fields or unsupported YAML | `SchemaError` naming offending field and file; JSONL/CSV row line or JSON object line 1 plus record context |
| Duplicate IDs across files | `SchemaError`, never silently discarded |
| Bad report/result output path | `WriteError`, exit 2; atomic replacement leaves no partial report or temporary file and preserves existing target |
| Other filesystem failures | `FileError`, exit 2, no traceback |

Error output contains no traceback for documented invalid inputs. Invalid input
leaves any previous result intact. Fixture generation is not a multi-file
transaction if storage fails partway; use a new directory after such a failure.
Reports can be large since every route is retained. This is a small in-memory
research simulator, not a streaming production router.

## Evidence-based improvement hook and verdict

Start a two-week window on the first real use, not the build date. Measure routing
accuracy against at least 20 hand-checked records per used run: a record is wrong
if any selected, accepted or dropped expert differs from the manual application
of the documented rules. Error rate is wrong records divided by checked records.
Record actual used-run count, checked-record count and wrong-record count locally.
Do not record invented usage or time savings. See `EVIDENCE.md` for the log and
decision procedure. If error exceeds 10 percent, fix the top observed cause and
recheck, or kill with the cause recorded. If there is no real usage, kill.

The post-window verdict is deliberately pending; synthetic correctness does not
prove usefulness. After real evidence: expand for daily use or revenue, integrate
for substantial overlap with a sibling, commercialise for a demonstrated buyer,
maintain for portfolio evidence when used but none of those apply, or kill for no
use or unmet acceptance criteria. Record one explicit verdict and its reason.
Publishing is handled separately; this build makes no external calls.
