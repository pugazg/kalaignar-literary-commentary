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
5. older continuation guides / saved prompts only for permanent procedural rules, not historical progress snapshots.

## Source rule

The supplied Tamil scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

Source PDFs are working/control sources and are not to be committed to GitHub unless the user explicitly requests that.

OCR/parsed text may assist but is never authoritative over direct inspection of the scan.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Keep these as separate gates.

Permanent English protections remain binding, including:

- `ஊழ்` → **Oozh**;
- Kalaignar's `இயற்கை நிலை` → **natural condition**;
- Kural 543 `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**;
- `இன்பம் — கற்பியல்` → **Inbam — Wedded Love**;
- `ஊடலுவகை` → **Joy of Lovers' Quarrel**;
- preservation of Kalaignar's governance, citizens, working-people, justice, public-resource and rational/inquiry vocabulary;
- no revision of released Parts merely for later stylistic harmonization.

# Canonical current state

## Tamil Parts 001–015

Parts **001–015 are audited / ARCHIVAL-READY continuously** through the end of the supplied Thirukkural volume:

- overall scans **1–323**;
- commentary through printed page **270**;
- Kural sequence through **1330**;
- index back matter through printed page **288**;
- scan 322 blank leaf;
- scan 323 plain back cover.

Audits exist as `works/thirukkural/AUDIT_PART_001.md` through `AUDIT_PART_015.md`.

Part 001 scan 8 remains the documented source-limited exception already covered by its audit.

## English Parts 001–014

Parts **001–014 are fully released continuously** through:

- overall scan **302**;
- printed page **269**;
- Kural **1325**.

Part 014 passed Tamil audit, English source-check, editorial review and the separate release gate. Its 20 English pages are `release-ready`.

## Part 015 source structure and Tamil result

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_015_pages_303-323.pdf`

Source-confirmed structure:

- scan **303 / printed page 270** continues and completes chapter 133 `ஊடலுவகை` with Kurals **1326–1330**;
- Kural **1330** is the end of the Thirukkural commentary;
- scans **304–321 / printed pages 271–288** are `குறள் முதற்குறிப்பு அகரவரிசை`;
- scan **322** is an unnumbered blank leaf;
- scan **323** is the plain back cover.

All **21/21** Part 015 physical-page records are directly visually verified. During verification, scan 318 received the source-supported correction `பொளளென` → `பொள்ளென` for Kural 487.

Tamil audit: `works/thirukkural/AUDIT_PART_015.md` — **PASS / ARCHIVAL-READY**.

# Exact next activity

Begin **Part 015 English first-pass drafting** as a separate gate.

Required startup for that activity:

1. fresh-read `works/thirukkural/translations/en/TRANSLATION_GUIDE.md` completely;
2. fresh-read `works/thirukkural/translations/en/GLOSSARY.md`;
3. fresh-read `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
4. inspect the released Part 014 English records and review/release artefacts for format and controlled vocabulary;
5. use the verified Part 015 Tamil archival records as the translation basis.

Retain Kalaignar's interpretive language and rhetorical character. Keep the Kural and Kalaignar's commentary distinct. Do not replace his interpretation with a generic modern Thirukkural explanation.

Stop after first-pass drafting. Do not combine drafting with source-check, editorial review or release promotion.
