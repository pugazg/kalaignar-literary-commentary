# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

Active work: `works/thirukkural/`

Last repository-state synchronization: **2026-08-17**.

## Mandatory startup

Before making changes:

1. read `THIRUKKURAL_ARCHIVAL_GUIDELINES.md` completely;
2. read `LITERARY_COMMENTARY_PROCESSING_GUIDE.md` completely;
3. read this `HANDOVER.md` completely;
4. read `works/thirukkural/README.md`;
5. inspect the existing target files before writing;
6. inspect the actual controlling source required by the active gate;
7. for English work additionally fresh-read:
   - `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`;
   - `works/thirukkural/translations/en/GLOSSARY.md`;
   - `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
   - the latest relevant English review/release artefacts.

## Repository-state precedence

When documents disagree about current progress, use this order:

1. actual files on `main` and their page-level metadata;
2. completed Tamil audits and English review/release reports;
3. `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
4. this handover and current READMEs;
5. older continuation guides / saved prompts only for permanent procedural rules, not for their historical status snapshots.

Do not infer missing work from a stale README or from a truncated directory response. Inspect the complete tree or the exact target file.

## Source rule

The supplied Tamil scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

Source PDFs are working/control sources and are not to be committed to GitHub unless the user explicitly requests that.

OCR/parsed text may assist but is never authoritative over direct inspection of the scan.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Keep these as separate gates.

Every project-created English page must identify:

```yaml
translation_type: "project_translation"
```

Released English material must not be revised merely to harmonize later vocabulary.

Permanent protections remain binding, including:

- chapter 38 `ஊழ்` → **Oozh**;
- Kalaignar's `இயற்கை நிலை` → **natural condition**;
- Kural 543 `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**, not an automatic caste-specific conventional gloss;
- preservation of Kalaignar's governance, citizens, working-people, justice, public-resource and rational/inquiry vocabulary where the Tamil explicitly uses it;
- Part 013 `கற்பியல்` → **Wedded Love** as the controlled structural rendering established by the Part 013 editorial/release review;
- Part 013 Kural 1125: do not reintroduce the unsupported draft nuance **“warring-eyed”**.

# Canonical current state

## Tamil

Parts **001–014 are audited / ARCHIVAL-READY continuously** through:

- overall scan **302**;
- printed page **269**;
- Kural **1325**.

Audits exist as `works/thirukkural/AUDIT_PART_001.md` through `AUDIT_PART_014.md`.

Part 001 remains archival-ready with one documented partial handwritten facsimile at scan 8. Parts 002–014 have passed their respective archival gates.

Part 014 specifically covers:

- scans **283–302**;
- Part-local pages **1–20**;
- printed pages **250–269**;
- Kural **1226–1325**;
- all **20/20** Tamil records `verified`;
- audit result: **ARCHIVAL-READY**.

Part 014 completes chapter 123 `பொழுதுகண்டு இரங்கல்`, covers chapters 124–132, and begins chapter 133 `ஊடலுவகை` through Kural 1325.

## English project translation

Parts **001–013 are fully released continuously** through:

- overall scan **282**;
- printed page **249**;
- Kural **1225**.

Latest released English baseline:

- Tamil audit: `works/thirukkural/AUDIT_PART_013.md` — **PASS / ARCHIVAL-READY**;
- editorial review: `works/thirukkural/translations/en/reviews/PART_013_REVIEW.md`;
- release report: `works/thirukkural/translations/en/reviews/PART_013_RELEASE_REPORT.md` — **PASS / RELEASE APPROVED**.

Part **014 English first pass is complete 20/20**:

- scans **283–302**;
- printed pages **250–269**;
- Kural **1226–1325**;
- all aligned page records exist;
- current page status: **`draft`**;
- source-check: **not yet completed**;
- editorial review: **not yet completed**;
- release report: **does not yet exist**.

Do not recreate Part 014 English pages.

## Part 015

Source inventory records the supplied file:

`திருக்குறள்_கலைஞர்_உரை_part_015_pages_303-323.pdf`

No Part 015 Tamil archival records exist on `main` in the current canonical state. Do not infer its content from the expected continuation; inspect the actual source before creating records.

# Exact next activity

**Part 014 English source-check gate.**

Required procedure:

1. fresh-read the mandatory startup files above;
2. inspect the complete existing English Part 014 set, scans **283–302**;
3. compare each English draft line-by-line / paragraph-by-paragraph against its verified Tamil archival page;
4. check Kural/commentary separation, omissions, additions, meaning drift, gender specificity, rhetorical force, imagery and chapter/section metadata;
5. retain the controlled `இன்பம் — கற்பியல்` → **Inbam — Wedded Love** structural treatment unless actual source evidence requires a separately documented revision;
6. make only source-supported corrections;
7. promote a page to `source-checked` only after that page passes the comparison;
8. after all 20 pages pass, synchronize `TRANSLATION_STATUS.md`, the English README, work README and this handover;
9. stop after the source-check gate.

Do **not** in the same activity:

- perform Part 014 editorial review;
- create `PART_014_RELEASE_REPORT.md`;
- promote Part 014 pages directly to `release-ready`;
- begin Part 015 Tamil transcription;
- revise released English Parts 001–013 merely for harmonization.

After Part 014 source-check passes, the following separate activity is its **editorial consistency / glossary-reconciliation review**, followed by a separate **release gate**.
