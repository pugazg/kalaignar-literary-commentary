# Next Chat Prompt — குறளோவியம் archival / bilingual project

Continue directly in:

`pugazg/kalaignar-literary-commentary`

Branch: `main`

Active work: `works/kuraloviyam/`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve any newer durable state. Do not reset, repeat or reopen completed Tamil work or completed English batches because a copied prompt or root multi-work handover contains an older checkpoint.

## Mandatory startup

Read completely before any Kuraloviyam change:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this `NEXT_CHAT_PROMPT_KURALOVIYAM.md`
5. `works/kuraloviyam/HANDOVER.md` — current work-specific frontier
6. `works/kuraloviyam/README.md`
7. `works/kuraloviyam/PART_001_AUDIT.md`
8. `works/kuraloviyam/PART_001_FINAL_STATUS_SYNC.md`
9. `works/kuraloviyam/metadata/source.md`
10. `works/kuraloviyam/metadata/transcription-policy.md`
11. `works/kuraloviyam/indexes/page-map.md`
12. `works/kuraloviyam/translations/en/README.md`
13. `works/kuraloviyam/translations/en/TRANSLATION_GUIDE.md`
14. `works/kuraloviyam/translations/en/GLOSSARY.md`
15. `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`

For normal Part 001 English work, the audited Tamil repository page records are the translation basis. Do not reopen the Part 001 PDF unless a newly discovered source/provenance issue specifically requires it.

## Source / split identity

Complete source reported by user: **666 physical pages**, split into six 111-page Parts.

- Part 001: 1–111
- Part 002: 112–222
- Part 003: 223–333
- Part 004: 334–444
- Part 005: 445–555
- Part 006: 556–666

Repository `scan_page` never restarts per split.

Part 002 has not been supplied or started.

## Part 001 Tamil state — CLOSED

Part 001 Tamil is **ARCHIVAL-READY**:

- source intake: 111/111;
- Pass 1: 111/111;
- Pass 2A: 111/111;
- Pass 2B: 111/111;
- Pass 3: 111/111;
- Part audit: PASS;
- final status sync: PASS;
- Tamil statuses: **107 `verified` + 4 `partial`**;
- partial scans: **13, 14, 15, 19**;
- visual fidelity: **111/111 `verified`**.

Do not reconstruct the handwritten/facsimile bodies on scans 13–15 or the faint/washed-out material on scan 19.

## English project translation controls

The Part 001 English layer is under:

`works/kuraloviyam/translations/en/`

It is explicitly a **project translation**, not an official/publisher-issued English edition.

Every English page carries:

```yaml
translation_type: "project_translation"
```

Permanent English cadence:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

Do not import standard Thirukkural wording, published English Kural translations, web text, another commentator or memory.

## English Batch 1 — COMPLETE

First-pass draft pages exist for **scans 1–8**:

- scans 1–3 — cover / publication matter;
- scans 4–8 / printed iii–vii — complete Preface.

Current English counts:

- draft: **8 / 111**;
- source-checked: **0 / 111**;
- editorial-reviewed: **0 / 111**;
- release-ready: **0 / 111**.

Do not redo Batch 1 merely for stylistic harmonization. Later source-check/editorial passes are the proper place for deliberate translation refinement.

## Exact next activity

If live `main` has not advanced beyond this frontier, execute **Part 001 English Batch 2 — scans 9–17**.

1. fetch the audited Tamil records for scans 9–17;
2. create matching English files under `works/kuraloviyam/translations/en/pages/`;
3. scans 9–12 translate `மதிப்புரை` as the controlled heading **Critical Appreciation**;
4. scans 13–15 are audited Tamil `partial` handwritten/facsimile records: create `source-limited` English records from securely established material only and do not reconstruct continuous handwriting;
5. translate scans 16–17 from their audited Tamil records;
6. keep ordinary new English pages at `status: "draft"`;
7. preserve source paragraph, quotation, verse and continuation structure as appropriate in clear English;
8. do not import standard Kural or external English wording;
9. update `translations/en/TRANSLATION_STATUS.md` after the batch;
10. audit the changed-file set from the pre-batch live SHA to the new head;
11. record the exact next English frontier before advancing to scan 18.

Do not begin English source-check while Part 001 first-pass drafting remains incomplete unless a newer live workflow explicitly changes that cadence.

Do not begin Part 002 until Part 001 English/final closure is complete and Part 002 source is supplied.
