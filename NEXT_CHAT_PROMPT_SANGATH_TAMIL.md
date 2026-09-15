# NEXT CHAT PROMPT — சங்கத் தமிழ் / Gate B Structural Fidelity / scans 151–175

Continue directly in `pugazg/kalaignar-literary-commentary`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Authoritative controls

1. `works/sangatamil/PRODUCTIVE_COMPLETION_PLAN.md`;
2. `works/sangatamil/GEMINI_TEXT_LOCK.md`;
3. `works/sangatamil/GATE_A_HYGIENE_REPORT.md`;
4. `works/sangatamil/STRUCTURAL_FIDELITY_PROGRESS.md`;
5. `SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`;
6. root `HANDOVER.md`.

## Durable repository state

Gate A — **COMPLETE / PASS**:

- **497/497** canonical page files;
- duplicate aliases — **0**;
- missing scans — **0**.

Gate B completed batches:

- B01 — scans **1–25** — COMPLETE / PASS;
- B02 — scans **26–50** — COMPLETE / PASS;
- B03 — scans **51–75** — COMPLETE / PASS;
- B04 — scans **76–100** — COMPLETE / PASS;
- B05 — scans **101–125** — COMPLETE / PASS;
- B06 — scans **126–150** — COMPLETE / PASS.

Current cumulative Gate B state:

- structurally reviewed — **150/497**;
- structurally remaining — **347**;
- current frontier — **scan 151**;
- Gate C — **NOT STARTED**.

Latest durable progress commit after B06:

`5348f9a12e785df93213056ae808a36184532ea9`

Latest B06 page-layer endpoint:

`19628594048c44b9b5edda402ce7c8dc6916220d`

## Current gate

**Gate B — Gemini-locked structural fidelity.**

Normal batch: **25 physical scans**.

Authority split:

- PDF scan — physical and structural authority;
- Gemini File1–File10 — locked lexical wording;
- repository — preservation layer.

For Gate B:

- preserve Gemini lexical wording;
- correct page placement, headings, paragraph order, punctuation, quotation structure, speaker labels, verse lineation, spacing, separators and provenance/gloss block placement;
- remove non-source OCR/stamp/handwriting/extraction garbage from body text;
- preserve illustration/divider/blank pages;
- use the controlling PDF, not Gemini extraction order, for physical page boundaries and placement;
- do not silently source-correct legitimate locked lexical words;
- if the source visibly contains wording omitted by Gemini, document the omission rather than inventing/recovering it during Gate B;
- if Gemini contains obvious non-source extraction debris unsupported by the scan, exclude it and document the exception;
- do not promote page status merely because Gate B structure was corrected unless the workflow explicitly requires it.

## Durable B06 notes that must not regress

The following section identities were reconciled during scans 126–150:

- `தேனாகச் சொட்டும் : தேளாகக் கொட்டும்!`
- `இளையோன் எதற்கும் இளையான்!`
- `குக்கூ! என்றது கோழி!`
- `கவிஞர்கள் தெளித்த பன்னீரும் வடித்த கண்ணீரும்!`

Known extraction-debris exceptions already documented:

- scan 130 — stray File3 numeric `6`;
- scan 131 — stray File3 heading token `மு`;
- scan 137 — malformed heading fragments `அதில் ... தி ... வி`;
- scan 143 — stray `A...` and malformed `மேமதிலி`.

Do not reintroduce these into literary body text.

## Exact next activity

Process **Gate B scans 151–175**.

Use:

- controlling PDF — `TVA_BOK_0042551_சங்கத்_தமிழ்_part_004_pages_151-200.pdf`;
- Gemini lexical lock — `File4.md`.

Important mapping:

- split-PDF page **1 = physical scan 151**;
- therefore split-PDF pages **1–25 = physical scans 151–175**.

Review all 25 physical scans visually against the PDF and reconcile each canonical page record to File4 under the Gate-B authority split.

Expected page range:

`works/sangatamil/pages/0151-*.md` through `0175-*.md`.

Do not assume existing filenames or section labels are lexically authoritative; preserve canonical filenames during Gate B, but reconcile metadata/body section identities where the PDF/File4 authorities require it.

## Batch-close requirements

After scans 151–175:

1. update `works/sangatamil/STRUCTURAL_FIDELITY_PROGRESS.md` with a new durable Batch B07 record;
2. record:
   - batch base commit;
   - page-layer endpoint commit;
   - count of changed page records;
   - count reviewed with no change;
   - all locked omissions / extraction-debris exceptions;
   - illustration/divider/blank-page handling;
   - exact changed-page-file set;
3. compare the batch base to page-layer endpoint and verify:
   - only intended page files changed before the progress-record commit;
4. commit the progress update separately;
5. report the final live-main commit and cumulative Gate B totals.

## Stop condition

After B07, the next frontier should be **scan 176**.

**Do not start Gate C.**
**Do not broad-sync README / HANDOVER / indexes unless explicitly requested.**
