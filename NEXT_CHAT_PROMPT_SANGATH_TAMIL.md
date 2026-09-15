# NEXT CHAT PROMPT — சங்கத் தமிழ் / Gate B Structural Fidelity / scans 351–375

Continue directly in pugazg/kalaignar-literary-commentary, branch main. LIVE MAIN IS AUTHORITATIVE.

## Authoritative controls

Read in this order before writing:

1. works/sangatamil/PRODUCTIVE_COMPLETION_PLAN.md
2. works/sangatamil/GEMINI_TEXT_LOCK.md
3. works/sangatamil/STRUCTURAL_FIDELITY_PROGRESS.md
4. works/sangatamil/GATE_A_HYGIENE_REPORT.md
5. SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md
6. root HANDOVER.md
7. works/sangatamil/README.md

Historical/superseded methodology files may be consulted for background only:

- works/sangatamil/MULTI_PASS_WORKFLOW.md
- works/sangatamil/GEMINI_RECONCILIATION_PLAN.md

## Durable repository state

Gate A — COMPLETE / PASS:

- canonical page files — 497/497
- duplicate aliases — 0
- missing scans — 0

Gate B completed batches:

- B01 1–25; B02 26–50; B03 51–75; B04 76–100
- B05 101–125; B06 126–150; B07 151–175; B08 176–200
- B09 201–225; B10 226–250; B11 251–275; B12 276–300
- B13 301–325; B14 326–350

Current cumulative Gate B state:

- structurally reviewed — 350/497
- structurally remaining — 147
- current frontier — scan 351
- Gate C — NOT STARTED

Latest B14 page-layer endpoint:

c227e5f2d95b6ad464fdf6e730639827c7c92941

Latest durable progress / live-main checkpoint after B14:

dfc23c0f9366248c7a2fa301dc4fb215cf374bf0

## Current gate

Gate B — Gemini-locked structural fidelity.

Normal batch: 25 physical scans.

Authority split:

- Gemini File1.md … File10.md — locked lexical wording
- PDF scan — physical-page and structural authority
- repository — preservation layer

For Gate B:

- preserve legitimate Gemini lexical wording
- correct physical page placement, headings, paragraph order, punctuation, quotation structure, speaker labels, verse lineation, spacing, separators, continuation order and provenance / பொருள் விளக்கம் block placement from the PDF
- preserve illustration/divider/blank pages
- exclude clearly unsupported extraction debris, scanner artefacts, page-wrapper text, merged running headers/page numbers, handwriting OCR garbage and similar non-source material
- if the PDF visibly differs lexically from a legitimate Gemini word, record the discrepancy but do not silently source-correct it
- if the PDF visibly contains lexical material omitted by Gemini, document the omission rather than source-recovering it during Gate B unless the user explicitly authorizes lexical recovery
- do not promote page status merely because structural correction occurred

## Exact next activity — B15

Process Gate B scans 351–375.

Use:

- controlling PDF — TVA_BOK_0042551_சங்கத்_தமிழ்_part_008_pages_351-400.pdf
- Gemini lexical lock — File8.md

Mapping:

- split-PDF page 1 = physical scan 351
- split-PDF pages 1–25 = physical scans 351–375

Expected canonical page range:

works/sangatamil/pages/0351-*.md through 0375-*.md

## Batch-close requirements

After B15:

1. update works/sangatamil/STRUCTURAL_FIDELITY_PROGRESS.md with a durable B15 record
2. record batch base, page-layer endpoint, changed-page count, reviewed/no-change count, all locked omissions/extraction-debris exceptions, illustration/divider/blank handling and exact changed-page-file set
3. compare batch base → page-layer endpoint and confirm only intended page records changed
4. commit the progress record separately
5. synchronize the operational current-state documents so they do not retain an obsolete frontier:
   - NEXT_CHAT_PROMPT_SANGATH_TAMIL.md
   - SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md current-state block
   - root HANDOVER.md
   - works/sangatamil/README.md
   - root README.md
6. report final live-main commit and cumulative Gate B totals

The large deferred derived indexes/section READMEs remain governed by later gates unless their current-state banner itself becomes false.

## Stop condition

After B15, expected frontier: scan 376.

Do not start Gate C.
