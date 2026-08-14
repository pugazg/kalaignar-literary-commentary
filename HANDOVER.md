# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Project scope

Archive Kalaignar M. Karunanidhi's literary commentary works in source-faithful, page-by-page Markdown.

Planned works:

1. திருக்குறள் — கலைஞர் உரை
2. திருக்குறள் — project-created English translation of Kalaignar's commentary
3. சங்கத்தமிழ் — Tamil
4. Sangatamil — published English translation when source is supplied
5. குறளோவியம் — Tamil
6. Kuraloviyam — published English translation when source is supplied

Reference implementation: `pugazg/tolkappiyap-poonga`.

Core rules: scan authority, one record per scan page, stable filenames, explicit review status, metadata/manifests, no silent normalization, and visible uncertainty.

# திருக்குறள் — Tamil archival state

## Part 001

Source: `திருக்குறள்_கலைஞர்_உரை_part_001_pages_1-20.pdf`

- overall scans: **1–20**
- audit complete
- release decision: **ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**
- `verified`: 19
- `partial`: 1 — scan 8 handwritten facsimile
- audit report: `works/thirukkural/AUDIT_PART_001.md`

Do not redo or renumber Part 001.

## Part 002

Source: `திருக்குறள்_கலைஞர்_உரை_part_002_pages_21-41.pdf`

- overall scans: **21–41**
- `verified`: **21 / 21**
- audit complete
- release decision: **ARCHIVAL-READY**
- audit report: `works/thirukkural/AUDIT_PART_002.md`

Do not redo or renumber Part 002.

## Part 003

Source: `திருக்குறள்_கலைஞர்_உரை_part_003_pages_42-62.pdf`

- overall scans: **42–62**
- printed pages: **9–29**
- Kural range: **41–145**
- `verified`: **21 / 21**
- audit complete
- release decision: **ARCHIVAL-READY**
- audit report: `works/thirukkural/AUDIT_PART_003.md`

Do not redo or renumber Part 003.

# English project translation

English proceeds after each Tamil PDF part has completed Tamil verification and audit.

Permanent cadence:

**Tamil transcription → Tamil visual verification → Tamil audit → English draft → English source-check → editorial consistency review → English part release report.**

## Translation identity

The current English layer is a **project-created English translation**, not an official/publisher English edition.

Every English page must carry:

```yaml
translation_type: "project_translation"
```

If a published English edition is later supplied, archive it separately and do not overwrite the project translation.

## Translation authority

1. supplied Tamil scan — ultimate authority;
2. corresponding audited/verified Tamil page — working translation basis;
3. English translation guide and controlled glossary;
4. review notes.

Do not silently import a web Kural, another Tamil edition, another commentator, or an existing English Kural translation.

## English framework files

- `works/thirukkural/translations/en/README.md`
- `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`
- `works/thirukkural/translations/en/GLOSSARY.md`
- `works/thirukkural/translations/en/TRANSLATION_STATUS.md`

## Part 001 English progress

Aligned English records now exist for **scans 1–8**:

- `0001-cover.md` — draft
- `0002-title-page.md` — draft
- `0003-blank.md` — draft
- `0004-publication-details.md` — draft
- `0005-edition-details.md` — draft
- `0006-contents.md` — draft
- `0007-mugavurai.md` — draft
- `0008-handwritten-note.md` — source-limited

Current English counts:

- page files: **8**
- `draft`: **7**
- `source-checked`: **0**
- `editorial-reviewed`: **0**
- `release-ready`: **0**
- `source-limited`: **1** — scan 8
- `blocked`: **0**

No English source-check has yet been performed; first-pass creation and review remain separate.

### Preface translation decisions established

The scan 7 draft preserves Kalaignar's distinction between:

- `கடவுள் வாழ்த்து` → `Invocation to God` when translating the source title he discusses;
- `வழிபாடு` → `Worship` for the title Kalaignar says he adopted.

### Scan 8 — source-limited English record

The Tamil archival record `works/thirukkural/pages/0008-handwritten-note.md` remains intentionally `partial` after high-resolution source review.

The aligned English record:

`works/thirukkural/translations/en/pages/0008-handwritten-note.md`

uses `status: "source-limited"` and translates only securely established content.

Established English content includes:

- heading: **“An Introduction to the Preface!”**;
- decorative divider presence;
- Kalaignar's signature presence;
- clearly readable date **27/12/2007**;
- factual note that reverse-side bleed-through is not current-page handwriting.

The continuous handwritten body remains untranslated because the controlling Tamil source does not support a reliable transcription. Do not reconstruct it unless a clearer scan/facsimile is supplied.

## Files synchronized after scan 8

- `works/thirukkural/translations/en/pages/0008-handwritten-note.md`
- `works/thirukkural/translations/en/TRANSLATION_STATUS.md`
- `works/thirukkural/translations/en/README.md`
- `works/thirukkural/README.md`
- this `HANDOVER.md`

# Next exact activity

Continue Part 001 English first-pass translation with **scans 9–12**, `பேராசிரியரின் அணிந்துரை`.

1. Fetch Tamil page files `0009-aninthurai-01.md` through `0012-aninthurai-04.md`.
2. Create exact matching filenames under `works/thirukkural/translations/en/pages/`.
3. Use `translation_type: "project_translation"`.
4. Use `status: "draft"` for all four new pages.
5. Translate only audited Tamil source content.
6. Preserve the poem-like line structure, repetitions, quotations, names and emphasis as closely as natural English permits.
7. Do not normalize unusual Tamil source forms before translating.
8. Do not perform source-check/editorial promotion in the same activity.
9. Update translation status, translation README, work README and this handover after the batch.

Tamil source intake can continue later from overall scan **63** when the next PDF is supplied and its continuity after scan 62 / printed page 29 / Kural 145 is confirmed.

## Source authority rule

The supplied scans remain the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. The project English translation must preserve the meaning and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
