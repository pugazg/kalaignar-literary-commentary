# NEXT CHAT PROMPT — சங்கத் தமிழ் / Gate B Structural Fidelity / final scans 476–497

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

Historical/superseded methodology files are background only:
- `works/sangatamil/MULTI_PASS_WORKFLOW.md`
- `works/sangatamil/GEMINI_RECONCILIATION_PLAN.md`

## Durable repository state

Gate A — **COMPLETE / PASS**:
- canonical page files — **497/497**
- duplicate aliases — **0**
- missing scans — **0**

Gate B completed batches: **B01–B19 / scans 1–475**.

Current cumulative Gate B state:
- structurally reviewed — **475/497**
- structurally remaining — **22**
- current frontier — **scan 476**
- Gate C — **NOT STARTED**

Latest B19 page-layer endpoint:
`123bdff3d39b248639f217216f112067e8ca0782`

Latest durable B19 progress commit:
`a532ba40528a9228f25087e75a0644a349990b0f`

## Current gate

**Gate B — Gemini-locked structural fidelity.**

Authority split:
- Gemini File1–File10 — locked lexical wording
- PDF scan — physical-page and structural authority
- repository — preservation layer

## Durable mapping exceptions that must not regress

- File9 scans **413–424**: demonstrated segmentation/replacement anomaly.
- File9 B18 tail: scans **438–450** have no usable File9 lexical block.
- File10 B19:
  - physical scans **451–461** map to File10 comments **439–449**;
  - File10 Page **449** is reliable only through `இனி ஆற்றுவதுதான் எவ்வாறு தோழி?`; its tail is replacement material;
  - physical scan **462 / printed 450** has no reliable File10 lexical block;
  - physical scans **463–468** map to File10 comments **450–455**;
  - File10 Page **456** is a phantom `(Image Page)` with no corresponding physical scan;
  - physical scans **469–475** realign to File10 comments **457–463**.
- malformed extraction tokens documented in B19 must not be promoted: `மிகக்குடிக்குமோ`, `புக்பாட்டு`, `போட்டுடைட்டதேனோ`, stray `ற`, stray `தன்`.
- earlier durable mixed-page correction remains: scan **359** is mixed text/illustration.

## Exact next activity — B20 final remainder

Process **Gate B scans 476–497 / 22 scans** in one final Gate-B batch.

Use:
- controlling PDF — `TVA_BOK_0042551_சங்கத்_தமிழ்_part_010_pages_451-497.pdf`
- Gemini lexical lock — `File10.md`

Mapping:
- split-PDF pages **26–47 = physical scans 476–497**

Expected canonical page range:
`works/sangatamil/pages/0476-*.md` through `0497-*.md`.

For each scan, resolve File10's actual content against the physical PDF before applying locked wording. Do not assume comment labels remain reliable merely because the B19 tail realigned. If another block is missing, duplicated, replaced, shifted, or phantom, document it and preserve the no-synthetic-alignment rule.

At batch close:
1. audit the B20 page-only change set;
2. update `STRUCTURAL_FIDELITY_PROGRESS.md`;
3. synchronize operational current-state docs;
4. declare Gate B **COMPLETE / PASS — 497/497 structurally reviewed** if all 22 scans close cleanly;
5. record Gate C as the next gate.

**Do not start Gate C in the B20 execution.**
