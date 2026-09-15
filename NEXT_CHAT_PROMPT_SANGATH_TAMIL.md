# NEXT CHAT PROMPT — சங்கத் தமிழ் / Gate B Structural Fidelity / scans 426–450

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

Gate B completed batches: **B01–B17 / scans 1–425**.

Current cumulative Gate B state:
- structurally reviewed — **425/497**
- structurally remaining — **72**
- current frontier — **scan 426**
- Gate C — **NOT STARTED**

Latest B17 page-layer endpoint:
`6f56beb69657525a74f55dd08f0fffa6ce85e6f5`

Latest durable B17 progress commit:
`a57048627789246b18e6bff20f5937b16b206fa0`

## Current gate

**Gate B — Gemini-locked structural fidelity.**

Normal batch: **25 physical scans**.

Authority split:
- Gemini File1–File10 — locked lexical wording
- PDF scan — physical-page and structural authority
- repository — preservation layer

## Durable B17 notes that must not regress

- scans **413–424** expose a demonstrated File9 segmentation/replacement anomaly: File9 Book Pages 401–412 are not reliable one-to-one lexical blocks for those physical scans.
- do not fabricate a synthetic lexical mapping for those scans and do not silently source-rewrite their wording during Gate B.
- scan **425** divider authority is `ஒருதலைக் காதல்`; unsupported repository heading `கைக்கிளை` was removed.
- scan **402** omits source-visible `உன்` because File9 does not lock that token.
- scan **404** preserves File9-locked `போல்` / `கருகில்` despite visible-source differences.
- scan **410** preserves File9-locked `கொலைஏறு`.
- earlier durable correction remains: scan **359** is mixed text/illustration, not illustration-only.

## Exact next activity — B18

Process **Gate B scans 426–450**.

Use:
- controlling PDF — `TVA_BOK_0042551_சங்கத்_தமிழ்_part_009_pages_401-450.pdf`
- Gemini lexical lock — `File9.md`

Mapping:
- split-PDF pages **26–50 = physical scans 426–450**

Expected canonical page range:
`works/sangatamil/pages/0426-*.md` through `0450-*.md`.

Preserve the Gemini lexical lock when a reliable File9 block exists. Where File9 is demonstrably mis-segmented/replaced, document the defect and use the PDF only for physical/structural placement; do not invent lexical alignment.

At batch close: update `STRUCTURAL_FIDELITY_PROGRESS.md`, audit page-only changes, synchronize operational docs, and stop with expected frontier **451**.

**Do not start Gate C.**
