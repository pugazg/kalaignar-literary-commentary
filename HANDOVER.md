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

The user chose **not to wait until the entire Thirukkural book is supplied**. English proceeds after each Tamil PDF part has completed Tamil verification and audit.

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

First-pass English drafts now exist for **scans 1–7** with exact filename alignment under `works/thirukkural/translations/en/pages/`:

- `0001-cover.md` — draft
- `0002-title-page.md` — draft
- `0003-blank.md` — draft
- `0004-publication-details.md` — draft
- `0005-edition-details.md` — draft
- `0006-contents.md` — draft
- `0007-mugavurai.md` — draft

Current English counts:

- page files: **7**
- `draft`: **7**
- `source-checked`: **0**
- `editorial-reviewed`: **0**
- `release-ready`: **0**
- `source-limited`: **0**
- `blocked`: **0**

No English source-check was performed during this first-pass creation activity; draft creation and review remain separate.

### Preface translation decisions now established

The draft preserves Kalaignar's distinction between:

- `கடவுள் வாழ்த்து` → `Invocation to God` when translating the source title he discusses;
- `வழிபாடு` → `Worship` for the title Kalaignar says he adopted.

The controlled glossary was expanded for Part 001 front matter, including `முன்னுரை`, `பொருட்பால்`, `இன்பத்துப்பால்`, `கடவுள் வாழ்த்து`, `அதிகார அகர வரிசை`, `அதிகார அருஞ்சொற்பொருள் அகரவரிசை`, `குறள் முதற்குறிப்பு அகரவரிசை`, `முரசொலி`, `நன்னன்`, and `அன்பழகனார்`.

## Special source-limited page — scan 8

Part 001 scan 8 is a handwritten facsimile whose Tamil archival record remains intentionally `partial` after high-resolution review.

Its English page must:

- mirror `0008-handwritten-note.md`;
- use `status: "source-limited"`;
- translate only the heading/date/signature description and other securely established content in the Tamil record;
- explicitly state that the continuous handwritten body cannot be safely translated from the controlling source;
- never reconstruct or infer the unreadable English content.

## Files synchronized after scans 1–7

- `works/thirukkural/translations/en/pages/0001-cover.md` through `0007-mugavurai.md`
- `works/thirukkural/translations/en/GLOSSARY.md`
- `works/thirukkural/translations/en/TRANSLATION_STATUS.md`
- `works/thirukkural/translations/en/README.md`
- `works/thirukkural/README.md`
- root `README.md`
- this `HANDOVER.md`

# Next exact activity

Create the aligned English record for **Part 001 scan 8**.

1. Fetch Tamil `works/thirukkural/pages/0008-handwritten-note.md`.
2. Create `works/thirukkural/translations/en/pages/0008-handwritten-note.md`.
3. Use `translation_type: "project_translation"`.
4. Use `status: "source-limited"`, not `draft`.
5. Translate only securely established source content and factual source-limit notes.
6. Do not infer the continuous handwritten body.
7. Update `TRANSLATION_STATUS.md`, translation README, work README and this handover.
8. After scan 8, the next first-pass translation batch is scans **9–12** (`பேராசிரியரின் அணிந்துரை`).

Tamil source intake can continue later from overall scan **63** when the next PDF is supplied and its continuity after scan 62 / printed page 29 / Kural 145 is confirmed.

## Source authority rule

The supplied scans remain the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. The project English translation must preserve the meaning and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
