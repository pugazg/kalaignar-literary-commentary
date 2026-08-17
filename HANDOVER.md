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

## Tamil Parts 001–014

Parts **001–014 are audited / ARCHIVAL-READY continuously** through:

- overall scan **302**;
- printed page **269**;
- Kural **1325**.

Audits exist as `works/thirukkural/AUDIT_PART_001.md` through `AUDIT_PART_014.md`.

## English Parts 001–014

Parts **001–014 are fully released continuously** through:

- overall scan **302**;
- printed page **269**;
- Kural **1325**.

Part 014 passed Tamil audit, English source-check, editorial review and the separate release gate. Its 20 English pages are `release-ready`.

## Part 015 source structure

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_015_pages_303-323.pdf`

The actual scan establishes:

- **21 physical scans**, overall scans **303–323**;
- scan **303 / printed page 270** continues chapter 133 `ஊடலுவகை` with Kurals **1326–1330**;
- Kural **1330** is the end of the Thirukkural commentary;
- scans **304–321 / printed pages 271–288** are `குறள் முதற்குறிப்பு அகரவரிசை`;
- scan **322** is an unnumbered blank leaf;
- scan **323** is the plain back cover.

The Part 014 → Part 015 boundary is source-confirmed as **Kural 1325 → 1326**.

## Part 015 repository state

All **21/21** physical-page records now exist.

Verified:

- scan 303 — `0303-inbam-oodaluvagai-02.md`;
- scan 304 — `0304-kural-mutharkurippu-01.md`;
- scan 305 — `0305-kural-mutharkurippu-02.md`;
- scan 306 — `0306-kural-mutharkurippu-03.md`.

First-pass complete but still `needs-review`:

- scans **307–321** — remaining alphabetical index pages;
- scan **322** — blank leaf;
- scan **323** — back cover.

Part 015 is therefore **FIRST-PASS COMPLETE 21/21**, but **not ARCHIVAL-READY**. Do not create `AUDIT_PART_015.md` yet.

# Exact next activity

Perform **Part 015 Tamil direct visual verification for scans 307–323**.

For scans 307–321:

1. compare every index entry and Kural-number reference directly against the controlling image;
2. preserve source-visible spacing, punctuation, hyphens and unusual forms rather than normalizing them;
3. correct only source-supported transcription differences;
4. promote a record to `verified` only after the whole page passes.

For scan 322, confirm that no printed text is present and verify the blank-page record. For scan 323, confirm the plain back-cover description and verify the record.

After scans 307–323 all pass, stop and perform the **Part 015 audit as a separate gate**. Only after `AUDIT_PART_015.md` passes may Part 015 English translation begin.
