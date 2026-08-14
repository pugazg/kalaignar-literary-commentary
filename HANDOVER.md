# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Project scope

Archive Kalaignar M. Karunanidhi's literary commentary works in source-faithful, page-by-page Markdown, with a clearly separate project-created English translation layer where requested.

# திருக்குறள் — Tamil archival state

## Part 001

Source: `திருக்குறள்_கலைஞர்_உரை_part_001_pages_1-20.pdf`

- overall scans: **1–20**
- audit complete
- release decision: **ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**
- `verified`: 19
- `partial`: 1 — scan 8 handwritten facsimile
- audit: `works/thirukkural/AUDIT_PART_001.md`

Do not redo or renumber Part 001.

## Part 002

Source: `திருக்குறள்_கலைஞர்_உரை_part_002_pages_21-41.pdf`

- overall scans: **21–41**
- `verified`: **21 / 21**
- audit complete
- release decision: **ARCHIVAL-READY**
- audit: `works/thirukkural/AUDIT_PART_002.md`

Do not redo or renumber Part 002.

## Part 003

Source: `திருக்குறள்_கலைஞர்_உரை_part_003_pages_42-62.pdf`

- overall scans: **42–62**
- printed pages: **9–29**
- Kural range: **41–145**
- `verified`: **21 / 21**
- audit complete
- release decision: **ARCHIVAL-READY**
- audit: `works/thirukkural/AUDIT_PART_003.md`

Do not redo or renumber Part 003.

Tamil source intake can later continue from overall scan **63** only if the next supplied scan confirms continuity after scan 62 / printed page 29 / Kural 145.

# English project translation

English proceeds after each Tamil PDF part has completed Tamil verification and audit.

Permanent cadence:

**Tamil transcription → Tamil visual verification → Tamil audit → English draft → English source-check → editorial consistency review → English part release report.**

## Translation identity

The current English layer is a **project-created English translation**, not an official/publisher English edition. Every English page must carry:

```yaml
translation_type: "project_translation"
```

Authority order:

1. supplied Tamil scan;
2. corresponding audited/verified Tamil page;
3. English `TRANSLATION_GUIDE.md` and `GLOSSARY.md`;
4. review notes.

Do not silently import another Tamil edition, web Kural, another commentator, or an existing English Kural translation.

## English framework files

- `works/thirukkural/translations/en/README.md`
- `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`
- `works/thirukkural/translations/en/GLOSSARY.md`
- `works/thirukkural/translations/en/TRANSLATION_STATUS.md`

## Part 001 English progress

Aligned English records now exist for **scans 1–12**:

- scans 1–7 — `draft`;
- scan 8 — `source-limited`;
- scans 9–12 — `draft`.

Current English counts:

- page files: **12**
- `draft`: **11**
- `source-limited`: **1** — scan 8
- `source-checked`: **0**
- `editorial-reviewed`: **0**
- `release-ready`: **0**
- `blocked`: **0**

No English source-check has yet been performed. First-pass creation and review remain separate stages.

### Scans 9–12 — completed first-pass batch

Created:

- `translations/en/pages/0009-aninthurai-01.md`
- `translations/en/pages/0010-aninthurai-02.md`
- `translations/en/pages/0011-aninthurai-03.md`
- `translations/en/pages/0012-aninthurai-04.md`

These translate `பேராசிரியரின் அணிந்துரை` / **The Professor's Foreword** by K. Anbazhagan. All four use `status: "draft"` and preserve the poem-like line structure, quotations, rhetorical repetition and source-supported emphasis.

Source-sensitive decisions deliberately left reviewable:

- `முப்பால்` → **Muppaal** provisionally;
- `திருவிடம்` → **Tiruvidam** because that is the verified source form; scan 10 carries a translation note instead of silently normalizing it;
- `ஊழ்` → **oozh** in the foreword's explicit discussion of the term;
- `வாயுறை` → **counsel** provisionally, flagged in the glossary for source-check review;
- Periyar, Anna and K. Anbazhagan retained in established source-supported English forms.

The controlled glossary has been expanded for these terms.

### Scan 8 — source-limited

`translations/en/pages/0008-handwritten-note.md` remains `source-limited`. It translates only securely established heading/date/signature/page-condition information; the unreadable continuous handwriting is not reconstructed.

## Files synchronized after scans 9–12

- four new English page drafts `0009`–`0012`;
- `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
- `works/thirukkural/translations/en/README.md`;
- `works/thirukkural/translations/en/GLOSSARY.md`;
- `works/thirukkural/README.md`;
- root `README.md`;
- this `HANDOVER.md`.

# Next exact activity

Continue Part 001 English first-pass translation with **scans 13–20**, covering `மதிப்புரை` / Critical Appreciation and the remaining literary-analysis front matter.

1. Fetch Tamil page files `0013-mathippurai-01.md` through `0020-mathippurai-paa-nalam.md`.
2. Inspect their exact headings, quotations, Kural citations and paragraph structure before translating.
3. Create exact matching filenames under `works/thirukkural/translations/en/pages/`.
4. Use `translation_type: "project_translation"` and `status: "draft"`.
5. Translate only audited Tamil source content.
6. Preserve source Kural quotations/citations without substituting familiar English Kural translations.
7. Preserve analytical headings and distinctions rather than harmonizing terminology prematurely.
8. Add concise translation notes only where a source-specific form materially affects interpretation.
9. Do not source-check or editorially promote these pages in the same activity.
10. After all scans 13–20 drafts exist, update translation status/README/work README/handover. The next stage after that will be the separate Part 001 English source-check pass.

## Source authority rule

The supplied scans remain the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. The project English translation must preserve the meaning and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
