# English Translation Guide — Kuraloviyam

This guide governs the **project-created English translation** of the audited Tamil archive of Kalaignar M. Karunanidhi's `குறளோவியம்`.

It follows the repository-wide literary-commentary workflow and the completed Thirukkural English benchmark, while preserving Kuraloviyam's own source structure.

## 1. Translation identity

This English layer is a project translation. It is **not** a publisher-issued or official English edition.

Every English page must carry:

```yaml
translation_type: "project_translation"
```

If a published English Kuraloviyam source is supplied later, archive it separately. Do not overwrite or silently retrofit this project translation.

## 2. Authority order

For normal translation work:

1. audited Tamil page record under `works/kuraloviyam/pages/`;
2. completed Tamil audit/status-sync records;
3. this translation guide and `GLOSSARY.md`;
4. `TRANSLATION_STATUS.md` and part-level English review/release records.

The original Tamil scan remains the ultimate source authority if a new provenance or fidelity problem is discovered, but a closed Part does not require routine PDF reopening for translation.

Never silently import:

- a standard Thirukkural text;
- a published English Kural translation;
- another commentator's explanation;
- web text;
- memory of a familiar Kural;
- a modernized or normalized Tamil reading.

## 3. Translation objective

Produce faithful, readable English that preserves the meaning, imagery, rhetoric, narrative movement and interpretive voice of the audited Tamil record.

Do not turn the translation into a new commentary, explanatory adaptation or ideological harmonization. Natural English syntax is expected, but additions that are not present in the Tamil must not be introduced merely to help the reader.

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

- `draft` — complete first English rendering exists for the safely translatable Tamil content.
- `source-checked` — English has been compared against the audited Tamil record paragraph-by-paragraph / block-by-block for omissions, additions and meaning drift.
- `editorial-reviewed` — readability, terminology, names, repeated phrasing, quotations and consistency have received a second review.
- `release-ready` — included in a completed Part-level English release report.
- `source-limited` — English is necessarily incomplete because the Tamil record itself is partial.
- `blocked` — a documented source or interpretive problem prevents safe translation.

## 6. Permanent Part 001 source limitations

Part 001 Tamil is archival-ready with four intentional `partial` records:

- scans 13–15 — handwritten/facsimile bodies cannot safely be established word-for-word;
- scan 19 — physically washed-out/faint central printed text cannot safely be recovered.

The English layer must not become more complete than those Tamil records. Translate only securely established material and mark the English page `source-limited`. Do not infer missing words from context, OCR, other editions or memory.

## 7. Kural handling inside Kuraloviyam

Kuraloviyam frequently embeds Kurals inside narrative, dialogue, criticism and illustrative scenes.

- Translate the exact Kural wording preserved in the audited Tamil page, not a standard edition.
- Preserve a two-line Kural block when the Tamil record preserves it as a two-line block.
- Preserve quoted Kural fragments as quoted fragments when they occur inside prose.
- Keep a Kural translation distinct from Kalaignar's surrounding explanation or narrative.
- If a compressed Kural needs interpretive help, Kalaignar's adjacent explanation in the audited record is the first permitted aid.
- Record materially interpretive choices during review rather than silently borrowing a conventional published rendering.

## 8. Front matter and literary prose

Prefaces, critical appreciations, publication notes and other prose are translated paragraph-by-paragraph, preserving source order, rhetorical questions, repeated emphasis, quotations and meaningful paragraph boundaries.

Poetry or verse quoted inside prose should preserve source-supported lineation and stanza grouping in English where practicable.

Source emphasis may be reflected when it carries rhetorical structure, but exact colour/font reproduction is not required.

## 9. Visual and non-body material

Translate factual archival descriptions of illustrations, photographs, signatures, stamps and other non-body material when they help preserve page meaning.

Do not turn visual descriptions into invented captions. Non-printed marks remain clearly identified as non-printed material.

## 10. Names and controlled terms

Use the project glossary as a context-aware default, not a mechanical word-substitution table.

Existing literary-commentary baseline terms retained where applicable include:

- `குறளோவியம்` → **Kuraloviyam**;
- `திருக்குறள்` → **Thirukkural**;
- `குறள்` → **Kural**;
- `முகப்புரை` → **Preface**;
- `மதிப்புரை` → **Critical Appreciation**;
- `அறத்துப்பால்` → **Book of Aram (Virtue / Right Conduct)** on first significant use, then **Book of Aram**;
- `பொருட்பால்` → **Book of Porul**;
- `இன்பத்துப்பால்` → **Book of Inbam**.

Personal names and periodical/book titles should be rendered consistently and not anglicized beyond established project usage.

## 11. Review workflow for each Part

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

Part 002 must not begin until Part 001 English closure is complete and Part 002 source is supplied.

## 12. Iteration discipline

The current user-directed cadence is **15 physical scan pages per normal iteration**. A final Part remainder may be shorter.

For first-pass drafting:

- use exactly 15 consecutive `scan_page` records in each normal iteration;
- the final drafting iteration of a Part may be shorter when fewer than 15 pages remain;
- a batch boundary does not imply a narrative, quotation or Kural boundary;
- source-limited pages count toward the batch and remain `source-limited`.

For source-check:

- use exactly 15 consecutive `scan_page` records in each normal iteration;
- compare English against the audited Tamil page paragraph-by-paragraph / block-by-block;
- check omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual-page function and cross-page continuations;
- only a page that passes this comparison may move from `draft` to `source-checked`;
- `source-limited` pages remain `source-limited` even after their securely established material is reviewed;
- do not use the source-check stage for stylistic rewriting that is unrelated to fidelity.

For glossary / recurring-terminology reconciliation:

- use the same **15 consecutive scan-page** cadence;
- compare recurring names, work/section names, controlled literary terms, publication names, chapter labels and repeated English renderings against `GLOSSARY.md` and their audited Tamil context;
- update `GLOSSARY.md` only for recurring terms actually evidenced in Part 001;
- do not mechanically force one English word where the Tamil context requires a different rendering;
- this gate does **not** by itself promote `source-checked` pages to `editorial-reviewed`; source-limited pages remain `source-limited`;
- do not import terminology from external editions, web sources or memory.

For editorial review:

- review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity;
- consult the matching audited Tamil whenever an editorial change could affect meaning;
- make only source-faithful editorial improvements;
- passing `source-checked` pages may move to `editorial-reviewed`; source-limited pages remain `source-limited`.

For Part-level review:

- review the completed Part as a whole rather than repeating page-level batches;
- verify page inventory/alignment, final statuses, source-limited integrity, terminology, names, Kural metadata, page functions and accumulated cross-page continuities;
- create a durable review record under `translations/en/reviews/`;
- do **not** promote pages to `release-ready` at this gate.

For every iteration or gate, fetch live `main` first, preserve newer durable state, update `TRANSLATION_STATUS.md`, and audit the exact changed-file set before advancing.

## 13. Part 001 drafting record

Part 001 covers overall scans 1–111.

Completed first-pass batches:

- Batch 1: scans 1–8;
- Batch 2: scans 9–17;
- Batch 3: scans 18–27;
- Batch 4: scans 28–37;
- Batch 5: scans 38–48 — 11-page cadence;
- Batch 6: scans 49–59 — 11-page cadence;
- Batch 7: scans 60–74 — 15 pages;
- Batch 8: scans 75–89 — 15 pages;
- Batch 9: scans 90–104 — 15 pages;
- Batch 10: scans 105–111 — final 7-page remainder.

Part 001 first-pass English drafting is **COMPLETE: 111/111 page records**.

## 14. Part 001 source-check record

**COMPLETE — 111/111 physical scans reviewed.**

- SC1: scans 1–15;
- SC2: scans 16–30;
- SC3: scans 31–45;
- SC4: scans 46–60;
- SC5: scans 61–75;
- SC6: scans 76–90;
- SC7: scans 91–105;
- SC8: scans 106–111 — final 6-page remainder.

Source-check closure state: **107 `source-checked` + 4 `source-limited`** (scans 13, 14, 15, 19), with no `draft` pages.

## 15. Part 001 glossary-reconciliation record

**COMPLETE — 111/111 physical scans reconciled.**

- GR1: scans 1–15;
- GR2: scans 16–30;
- GR3: scans 31–45;
- GR4: scans 46–60;
- GR5: scans 61–75;
- GR6: scans 76–90;
- GR7: scans 91–105;
- GR8: scans 106–111 — final 6-page remainder.

`GLOSSARY.md` is the durable context-aware terminology authority for the Part.

## 16. Part 001 editorial-review record

**COMPLETE — 111/111 physical scans reviewed.**

- ER1: scans 1–15;
- ER2: scans 16–30;
- ER3: scans 31–45;
- ER4: scans 46–60;
- ER5: scans 61–75;
- ER6: scans 76–90;
- ER7: scans 91–105;
- ER8: scans 106–111 — final 6-page remainder.

Editorial-review closure state: **107 `editorial-reviewed` + 4 `source-limited`**, with `draft=0`, `source-checked=0`, and `release-ready=0`.

## 17. Part 001 Part-level English review record

**COMPLETE — PASS.**

Durable review record: `reviews/PART_001_ENGLISH_REVIEW.md`.

The Part-level review confirmed 111/111 Tamil-English filename alignment, preserved all four source limitations, found no unresolved controlled-term or continuity defect, and retained scan **111→112** as an explicitly deferred boundary until Part 002 is supplied.

The Part-level review did not alter any English page text or status.

## Current gate

Proceed with the **Part 001 Part-level English release report** gate.

The release-report gate must use the completed Part-level review record and current English state to decide release approval. Do not promote pages to `release-ready` before that report is completed and approved. Source-limited scans **13, 14, 15 and 19** must remain source-limited unless better source evidence is supplied.

Do not begin Part 002 until Part 001 English/final closure is complete and Part 002 source is supplied. The **111→112** split boundary remains deferred until then.