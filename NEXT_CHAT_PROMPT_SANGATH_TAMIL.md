# NEXT CHAT PROMPT — சங்கத் தமிழ் / Gate B Structural Fidelity / scans 451–475

Continue directly in `pugazg/kalaignar-literary-commentary`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Authoritative controls

Read in this order before writing:
1. `works/sangatamil/PRODUCTIVE_COMPLETION_PLAN.md`
2. `works/sangatamil/GEMINI_TEXT_LOCK.md`
3. `works/sangatamil/STRUCTURAL_FIDELITY_PROGRESS.md`
4. `works/sangatamil/GATE_A_HYGIENE_REPORT.md`
5. `SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`
6. root `HANDOVER.md`
7. `works/sangatamil/README.md`

Historical/superseded methodology files may be consulted for background only:
- `works/sangatamil/MULTI_PASS_WORKFLOW.md`
- `works/sangatamil/GEMINI_RECONCILIATION_PLAN.md`

## Durable repository state

Gate A — **COMPLETE / PASS**:
- canonical page files — **497/497**
- duplicate aliases — **0**
- missing scans — **0**

Gate B completed batches: **B01–B18 / scans 1–450**.

Current cumulative Gate B state:
- structurally reviewed — **450/497**
- structurally remaining — **47**
- current frontier — **scan 451**
- Gate C — **NOT STARTED**

Latest B18 page-layer endpoint:
`0b77065c14ab3495fd3282c7697db5fb86b2cbcc`

Latest durable B18 progress commit:
`3342dcf878f72692bfa86b19f4b73e8ea56fc434`

## Current gate

**Gate B — Gemini-locked structural fidelity.**

Normal batch: **25 physical scans**.

Authority split:
- Gemini File1–File10 — locked lexical wording
- PDF scan — physical-page and structural authority
- repository — preservation layer

## Durable notes that must not regress

- scans **413–424** expose a File9 segmentation/replacement anomaly: File9 Book Pages 401–412 are not reliable one-to-one lexical blocks.
- File9 Phase 20 advertises Book Pages **413–438 / PDF 426–450**, but the supplied payload actually stops at **Page 425**.
- usable File9 Page **414–425** blocks cover physical scans **426–437**; physical scans **438–450** have no File9 lexical block.
- for scans **438–450**, existing source-aligned repository wording was retained and the PDF was used only for physical/structural review; no synthetic lexical mapping was created.
- scan **430** omits source-visible `துடிப்பதாய்ச்` because File9 does not lock that token.
- scan **431** omits source-visible `இவ்வாறு` because File9 does not lock that token.
- scan **430** records File9 `விரைந்தோடிிட` as an obvious in-token extraction duplication and does not promote it over the existing usable Tamil form.
- scan **448** received punctuation-only structural repair: `களிப்பும்,,` → `களிப்பும்,`.
- scan **425** divider authority remains `ஒருதலைக் காதல்`.
- earlier durable correction remains: scan **359** is mixed text/illustration, not illustration-only.

## Exact next activity — B19

Process **Gate B scans 451–475**.

Use:
- controlling PDF — `TVA_BOK_0042551_சங்கத்_தமிழ்_part_010_pages_451-497.pdf`
- Gemini lexical lock — `File10.md`

Mapping:
- split-PDF pages **1–25 = physical scans 451–475**

Expected canonical page range:
`works/sangatamil/pages/0451-*.md` through `0475-*.md`.

Resolve File10's internal page-comment mapping against the PDF before applying lexical wording. Gemini comment labels are navigation aids, not physical scan authority. If a block is demonstrably duplicated, shifted, replaced, or missing, document the defect and retain the same no-synthetic-alignment rule rather than inventing a lexical mapping.

At batch close: update `STRUCTURAL_FIDELITY_PROGRESS.md`, audit page-only changes, synchronize operational docs, and stop with expected frontier **476**.

**Do not start Gate C.**
