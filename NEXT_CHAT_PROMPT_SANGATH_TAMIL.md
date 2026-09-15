# NEXT CHAT PROMPT — சங்கத் தமிழ் / Gate B Structural Fidelity / scans 376–400

Continue directly in `pugazg/kalaignar-literary-commentary`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Authoritative controls

Read in this order before writing:

1. `works/sangatamil/PRODUCTIVE_COMPLETION_PLAN.md`;
2. `works/sangatamil/GEMINI_TEXT_LOCK.md`;
3. `works/sangatamil/STRUCTURAL_FIDELITY_PROGRESS.md`;
4. `works/sangatamil/GATE_A_HYGIENE_REPORT.md`;
5. `SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`;
6. root `HANDOVER.md`;
7. `works/sangatamil/README.md`.

Historical/superseded methodology files may be consulted for background only:

- `works/sangatamil/MULTI_PASS_WORKFLOW.md`;
- `works/sangatamil/GEMINI_RECONCILIATION_PLAN.md`.

## Durable repository state

Gate A — **COMPLETE / PASS**:

- canonical page files — **497/497**;
- duplicate aliases — **0**;
- missing scans — **0**.

Gate B completed batches:

- B01 — scans **1–25**;
- B02 — **26–50**;
- B03 — **51–75**;
- B04 — **76–100**;
- B05 — **101–125**;
- B06 — **126–150**;
- B07 — **151–175**;
- B08 — **176–200**;
- B09 — **201–225**;
- B10 — **226–250**;
- B11 — **251–275**;
- B12 — **276–300**;
- B13 — **301–325**;
- B14 — **326–350**;
- B15 — **351–375**.

Current cumulative Gate B state:

- structurally reviewed — **375/497**;
- structurally remaining — **122**;
- current frontier — **scan 376**;
- Gate C — **NOT STARTED**.

Latest B15 page-layer endpoint:

`ca5e6c6037517d7bdb2c1d73deb87fcc0edc5b8e`

Latest durable B15 progress commit:

`c38b23f81d35957d560ec3b56ebfac48f8bac47f`

## Current gate

**Gate B — Gemini-locked structural fidelity.**

Normal batch: **25 physical scans**.

Authority split:

- **Gemini File1–File10** — locked lexical wording;
- **PDF scan** — physical-page and structural authority;
- **repository** — preservation layer.

For Gate B:

- preserve legitimate Gemini lexical wording;
- correct physical page placement, headings, paragraph order, punctuation, quotation structure, speaker labels, verse lineation, spacing, separators, continuation order and provenance / `பொருள் விளக்கம்` block placement from the PDF;
- preserve illustration/divider/blank pages;
- exclude clearly unsupported extraction debris, scanner artefacts, page-wrapper text, merged running headers/page numbers, handwriting OCR garbage and similar non-source material;
- if the PDF visibly differs lexically from a legitimate Gemini word, record the discrepancy but do not silently source-correct it;
- if the PDF visibly contains lexical material omitted by Gemini, document the omission rather than source-recovering it during Gate B unless the user explicitly authorizes lexical recovery;
- do not promote page status merely because structural correction occurred.

## Durable B15 notes that must not regress

- scan **352** — File8 omits source-visible heading word `மங்கை`; body remains locked as `கண்ட மகிழ்ச்சி!`; wrapper `YOM` excluded.
- scan **360** — locked `செலஇருந்த தடங் குறித்துத்` restored.
- scan **361** — locked `வீழ்த்துக்கின்ற` retained despite visible-source difference.
- scan **363** — source-recovered `இத்தி` removed after glossary equals sign; locked `கெடாதகள்` restored; numeric `6` excluded.
- scan **364** — locked `சுளீப்பீர்!` retained; numeric `66` excluded.
- scan **366** — locked `கொங்கையினை` and `சாய்ந்திடிலோ` retained.
- scan **367** — narrative `ஒரேர்` / `கைப்பிசைந்து` retained, while poet-name forms remain distinct.
- scan **370** — locked `கண்ணா` / `ஓருயிராய்` retained; numeric `66` excluded.
- scan **373** — source section identity `ஓர் உவமை; இரு காட்சி!`; File8 body heading `ஒர் உவமை; இரு காட்சி!`; metadata/body split preserved.
- scan **358** is a mixed text/illustration opener, not illustration-only.

## Exact next activity — B16

Process **Gate B scans 376–400**.

Use:

- controlling PDF — `TVA_BOK_0042551_சங்கத்_தமிழ்_part_008_pages_351-400.pdf`;
- Gemini lexical lock — `File8.md`.

Mapping:

- split-PDF pages **26–50 = physical scans 376–400**.

Expected canonical page range:

`works/sangatamil/pages/0376-*.md` through `0400-*.md`.

Do not assume filenames or existing section labels are lexically authoritative. Preserve canonical filenames during Gate B, but reconcile metadata/body section identity according to the authority split.

## Batch-close requirements

After B16:

1. update `works/sangatamil/STRUCTURAL_FIDELITY_PROGRESS.md` with a durable B16 record;
2. record batch base, page-layer endpoint, changed-page count, reviewed/no-change count, locked omissions / extraction-debris exceptions, illustration/divider/blank handling and exact changed-page-file set;
3. compare batch base → page-layer endpoint and confirm only intended page records changed;
4. commit the progress record separately;
5. synchronize operational current-state documents so they do not retain an obsolete frontier;
6. report final live-main commit and cumulative Gate B totals.

## Stop condition

After B16, expected frontier: **scan 401**.

**Do not start Gate C.**
