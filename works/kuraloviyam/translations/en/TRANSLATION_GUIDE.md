# English Translation Guide — Kuraloviyam

This guide governs the **project-created English translation** of the audited Tamil archive of Kalaignar M. Karunanidhi's `குறளோவியம்`.

It follows the repository-wide literary-commentary workflow while preserving Kuraloviyam's own source structure.

## 1. Translation identity

This English layer is a project translation. It is **not** a publisher-issued or official English edition.

Every English page must carry:

```yaml
translation_type: "project_translation"
```

If a published English Kuraloviyam source is supplied later, archive it separately. Do not overwrite or silently retrofit this project translation.

## 2. Authority order

For normal translation/review work:

1. audited Tamil page record under `works/kuraloviyam/pages/`;
2. completed Tamil audit/status-sync records;
3. this translation guide and `GLOSSARY.md`;
4. `TRANSLATION_STATUS.md` and Part-level English review/release records.

The original Tamil scan remains the ultimate source authority if a new provenance or fidelity problem is discovered, but a closed Part does not require routine PDF reopening for translation.

Never silently import:

- a standard Thirukkural text;
- a published English Kural translation;
- another commentator's explanation;
- web text;
- memory of a familiar Kural;
- a modernized or normalized Tamil reading.

## 3. Translation objective

Produce faithful, readable English that preserves meaning, imagery, rhetoric, narrative movement and interpretive voice of the audited Tamil record.

Do not turn the translation into new commentary, explanatory adaptation or ideological harmonization. Natural English syntax is expected, but additions unsupported by Tamil must not be introduced merely to help the reader.

## 4. Page alignment

Every English page mirrors the Tamil filename.

Example:

```text
Tamil:
works/kuraloviyam/pages/0034-kuraloviyam-17.md

English:
works/kuraloviyam/translations/en/pages/0034-kuraloviyam-17.md
```

Recommended front matter:

```yaml
---
source_scan_page: 34
source_tamil_file: "../../../pages/0034-kuraloviyam-17.md"
printed_page: "17"
work: "kuraloviyam"
section: "Kalaignar's Kuraloviyam"
language: "en"
translation_type: "project_translation"
status: "draft"
source_tamil_status: "verified"
translation_basis: "audited Tamil archival record; controlling scan remains ultimate source authority"
---
```

Tamil archival status and English translation status are separate. Never copy Tamil `verified` into English as if it implied translation review.

## 5. English statuses

- `draft` — complete first English rendering exists for safely translatable Tamil content.
- `source-checked` — English has been compared against the audited Tamil record paragraph-by-paragraph / block-by-block for omissions, additions and meaning drift.
- `editorial-reviewed` — readability, terminology, names, repeated phrasing, quotations and consistency have received a second review.
- `release-ready` — included in a completed Part-level English release report.
- `source-limited` — English is necessarily incomplete because the Tamil record itself is partial.
- `blocked` — a documented source or interpretive problem prevents safe translation.

## 6. Permanent Part 001 source limitations

Part 001 Tamil is archival-ready with four intentional `partial` records:

- scans 13–15 — handwritten/facsimile bodies cannot safely be established word-for-word;
- scan 19 — physically washed-out/faint central printed text cannot safely be recovered.

The English layer must not become more complete than those Tamil records. Translate only securely established material and retain `source-limited`. Do not infer missing words from context, OCR, other editions or memory.

## 7. Kural handling inside Kuraloviyam

Kuraloviyam frequently embeds Kurals inside narrative, dialogue, criticism and illustrative scenes.

- Translate the exact Kural wording preserved in the audited Tamil page, not a standard edition.
- Preserve a two-line Kural block when the Tamil record preserves it as a two-line block.
- Preserve quoted Kural fragments as fragments when they occur inside prose.
- Keep a Kural translation distinct from Kalaignar's surrounding explanation or narrative.
- If a compressed Kural needs interpretive help, Kalaignar's adjacent explanation in the audited record is the first permitted aid.
- Record materially interpretive choices during review rather than silently borrowing a conventional published rendering.

## 8. Front matter and literary prose

Translate prefaces, critical appreciations, publication notes and other prose paragraph-by-paragraph, preserving source order, rhetorical questions, repeated emphasis, quotations and meaningful paragraph boundaries.

Poetry or verse quoted inside prose should preserve source-supported lineation and stanza grouping in English where practicable.

## 9. Visual and non-body material

Translate factual archival descriptions of illustrations, photographs, signatures, stamps and other non-body material when they help preserve page meaning.

Do not turn visual descriptions into invented captions. Non-printed marks remain clearly identified as non-body material.

## 10. Names and controlled terms

Use `GLOSSARY.md` as a context-aware default, not a mechanical word-substitution table.

Core controls include:

- `குறளோவியம்` → **Kuraloviyam**;
- `திருக்குறள்` → **Thirukkural**;
- `குறள்` → **Kural**;
- `முகப்புரை` → **Preface**;
- `மதிப்புரை` → **Critical Appreciation**;
- `அறத்துப்பால்` → **Book of Aram**;
- `பொருட்பால்` → **Book of Porul**;
- `இன்பத்துப்பால்` → **Book of Inbam**;
- `காமத்துப்பால்` → **Book of Love**;
- `ஊடல்` → **lovers' quarrel** contextually;
- `கூடல்` → **lovers' union** contextually;
- `யாழ்` → **yaazh**.

Personal names and periodical/book titles should be rendered consistently and not anglicized beyond established project usage. Context-sensitive kinship/direct-address terms must not be forced into one English equivalent when relationships differ.

## 11. Permanent Part workflow

For each Tamil Part:

1. Tamil archival-ready checkpoint;
2. English page-aligned first-pass translation;
3. English source-check against audited Tamil records;
4. glossary / recurring terminology reconciliation;
5. editorial consistency review;
6. Part-level review record;
7. Part-level release report;
8. page promotion to `release-ready` only after release approval;
9. final Part checkpoint before the next Part begins.

Do not begin a later Part until the active Part's required English review/release and final closure are complete.

## 12. Iteration discipline — current user directive

**Current normal iteration size: 33 physical scan pages.**

This user-directed cadence applies to active Kuraloviyam English page-batched workflow iterations. Historical completed batches retain the sizes at which they were actually processed. A final Part remainder may be shorter than 33 pages. Part-level review and release report are whole-Part gates.

For first-pass drafting:

- use 33 consecutive `scan_page` records per normal future iteration unless the user explicitly changes the cadence again;
- a batch boundary does not imply a narrative, quotation or Kural boundary;
- preserve cross-page continuation exactly;
- source-limited pages count toward the batch and remain `source-limited`.

For source-check:

- use 33 consecutive `scan_page` records per normal future iteration unless a final remainder is shorter;
- compare English against audited Tamil paragraph-by-paragraph / block-by-block;
- check omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual-page function and cross-page continuations;
- only a passing page may move from `draft` to `source-checked`;
- do not use source-check for stylistic rewriting unrelated to fidelity.

For glossary / recurring-terminology reconciliation:

- use **33 consecutive scan pages per normal iteration**;
- compare recurring names, work/section names, controlled literary terms, publication names, chapter labels, citation metadata and repeated English renderings against `GLOSSARY.md` and audited Tamil context;
- update `GLOSSARY.md` only for terms actually evidenced in the active source;
- do not mechanically force one English word where context requires a different rendering;
- this gate does **not** promote `source-checked` pages to `editorial-reviewed`;
- do not import terminology from external editions, web sources or memory.

For editorial review:

- use the current 33-page normal cadence unless the user changes it;
- review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity;
- consult matching audited Tamil whenever an editorial change could affect meaning;
- make only source-faithful editorial improvements;
- passing `source-checked` pages may move to `editorial-reviewed`.

For Part-level review:

- review the completed Part as a whole rather than repeating page-level batches;
- verify page inventory/alignment, final statuses, source-limited integrity, terminology, names, Kural metadata, page functions and accumulated continuities;
- create a durable review record under `translations/en/reviews/`;
- do **not** promote pages to `release-ready` at this gate.

For release report:

- use the completed Part-level review as the authoritative prior gate;
- explicitly approve or block release;
- if approved, promote only eligible `editorial-reviewed` pages to `release-ready` without changing wording;
- preserve `source-limited` or `blocked` states where applicable;
- record any deferred split-boundary check rather than inferring unsupplied source content.

For every iteration or gate, fetch live `main` first, preserve newer durable state, update `TRANSLATION_STATUS.md`, and audit the exact changed-file set before advancing.

## 13. Historical Part 001 English record

Part 001 covers overall scans 1–111.

- first-pass drafting: **COMPLETE 111/111**;
- source-check: **COMPLETE 111/111**;
- glossary reconciliation: **COMPLETE 111/111**;
- editorial review: **COMPLETE — 107 editorial-reviewed + 4 source-limited**;
- Part-level review: **PASS**;
- release: **CLOSED — 107 release-ready + 4 source-limited**.

Historical Part 001 batch sizes are retained in the durable status/review records and are not retroactively changed by the current 33-page directive.

## 14. Part 002 current English record

Part 002 covers scans **112–222 / printed 95–205**.

- Tamil: **ARCHIVAL-READY / CLOSED — 111/111 textual + visual verified**;
- first-pass drafting: **COMPLETE 111/111**;
- source-check: **COMPLETE 111/111**;
- glossary reconciliation: **COMPLETE / CLOSED 111/111**;
- editorial review: **COMPLETE / CLOSED 111/111**;
- Part-level review: **PASS / CLOSED**;
- release report: **APPROVED / CLOSED**;
- release-ready: **111/111 COMPLETE / CLOSED**.

Durable Part-level review: `reviews/PART_002_ENGLISH_REVIEW.md`.

The Part-level review passed inventory/alignment, exact status state, terminology/names, chapter/Kural metadata, page functions/non-body material and accumulated continuities.

Durable release report: `reviews/PART_002_ENGLISH_RELEASE_REPORT.md` — **APPROVED / CLOSED**. All scans **112–222** are now `release-ready`; the release changed only the English status field and changed no approved wording or Tamil record.

The internal Part ending at scan **222** is closed. The external **222→223** split boundary remains deferred until Part 003 intake.

Final Part 002 checkpoint: **PASS / CLOSED**. The next activity is **Part 003 source intake when the controlling source is supplied**, beginning with source identity and the real 222→223 boundary before continuing at overall scan **223**.

## 15. Part 003 closed English record

Part 003 covers scans **223–333 / printed 206–316**.

- Tamil: **ARCHIVAL-READY / CLOSED — 111/111 textual + visual verified / 0 exceptions**;
- first-pass drafting: **COMPLETE / CLOSED 111/111**;
- source-check: **COMPLETE / CLOSED 111/111**;
- glossary reconciliation: **COMPLETE / CLOSED 111/111**;
- editorial review: **COMPLETE / CLOSED 111/111**;
- Part-level review: **PASS / CLOSED**;
- release report: **APPROVED / CLOSED**;
- release-ready: **111/111 COMPLETE / CLOSED**;
- final Part checkpoint: **PASS / CLOSED**.

Durable records:

- `reviews/PART_003_ENGLISH_REVIEW.md`;
- `reviews/PART_003_ENGLISH_RELEASE_REPORT.md`;
- `../../PART_003_FINAL_CLOSURE.md`.

All release page changes were status-token-only; approved English wording and Tamil archival records were unchanged. The internal Part ending at scan **333** is closed. External **333→334** remains deferred until Part 004 source intake.

Part 004 has now completed source intake and the full Tamil archival workflow.

## 16. Part 004 active English record

- Tamil — **ARCHIVAL-READY / CLOSED**;
- English drafting — **COMPLETE / CLOSED 111/111**;
- source-check — **COMPLETE / CLOSED 111/111**;
- glossary reconciliation — **IN PROGRESS 66/111**;
- GR1 **334–366 — COMPLETE / PASS 33/33**;
- GR2 **367–399 — COMPLETE / PASS 33/33**;
- current page state — **111 source-checked / 0 draft / 0 source-limited / 0 blocked**;
- GR2 terminology corrections — **6 page files**;
- exact next batch — **GR3 scans 400–432 / printed 383–415 — 33 pages**;
- external **444→445 DEFERRED / UNRESOLVED**.

Glossary reconciliation remains terminology-only: use audited Tamil + `GLOSSARY.md`, make only source-supported corrections, preserve page status, and do not perform general stylistic rewriting.
