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

## Part 001 English first pass — COMPLETE

Aligned English records exist for all **20/20** Part 001 scans:

- scans 1–7 — `draft`;
- scan 8 — `source-limited`;
- scans 9–20 — `draft`.

Current English counts:

- page files: **20**
- `draft`: **19**
- `source-limited`: **1** — scan 8
- `source-checked`: **0**
- `editorial-reviewed`: **0**
- `release-ready`: **0**
- `blocked`: **0**

No English source-check has yet been performed. First-pass creation and review remain separate stages.

### Scans 1–7

Cover, title page, blank-page record, publication details, edition details, contents, and Kalaignar's Preface are present as aligned drafts.

### Scan 8 — source-limited

`translations/en/pages/0008-handwritten-note.md` remains `source-limited`. It translates only securely established heading/date/signature/page-condition information; the unreadable continuous handwriting is not reconstructed.

### Scans 9–12 — The Professor's Foreword

Created:

- `translations/en/pages/0009-aninthurai-01.md`
- `translations/en/pages/0010-aninthurai-02.md`
- `translations/en/pages/0011-aninthurai-03.md`
- `translations/en/pages/0012-aninthurai-04.md`

These translate K. Anbazhagan's poetic foreword and preserve poem-like line structure, quotations and emphasis. Review-sensitive choices include **Muppaal**, **Tiruvidam**, **oozh**, and provisional `வாயுறை` → `counsel`.

### Scans 13–20 — Critical Appreciation

Created:

- `translations/en/pages/0013-mathippurai-01.md`
- `translations/en/pages/0014-mathippurai-02.md`
- `translations/en/pages/0015-mathippurai-03.md`
- `translations/en/pages/0016-mathippurai-04.md`
- `translations/en/pages/0017-mathippurai-05.md`
- `translations/en/pages/0018-mathippurai-06.md`
- `translations/en/pages/0019-mathippurai-07.md`
- `translations/en/pages/0020-mathippurai-paa-nalam.md`

All eight use `status: "draft"` and translate Professor Ma. Nannan's `மதிப்புரை` / **Critical Appreciation**.

Coverage:

- scans 13–14 — `தேவை` / **Need**;
- scan 15 — `வழிபாடு` / **Worship**;
- scans 16–17 — `பெண்வழிச் சேறல்` / **Following a Woman's Lead**;
- scans 18–19 — `ஊழ்` / **Oozh**;
- scans 19–20 — `பல்வகைச் சிறப்புகள்` / **Various Distinctive Merits**.

Review-sensitive decisions deliberately left visible:

- `பெண்வழிச் சேறல்` → **Following a Woman's Lead** provisionally;
- `ஊழ்` retained as **Oozh**; Nannan's stated explanation is rendered as **natural condition**;
- `பிறிது மொழிதல்` → ***pirithu mozhithal*** with the gloss “saying one thing in order to convey another”;
- `அடுத்தூர்வது அஃதொப்பதில்` → provisional **“to meet what comes upon us in like measure”** on scan 19;
- `பா நலம்` → **Poetic Quality**;
- `அணி நலம்` → **Excellence of Poetic Figure**;
- `அடை நலம்` → **Excellence of Epithets**.

The Kural examples on scan 20 were translated directly from the audited Tamil source and Kalaignar's adjacent explanation. Do not replace them with familiar published English Kural translations during review.

## Files synchronized after Part 001 first pass

- eight new English page drafts `0013`–`0020`;
- `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
- `works/thirukkural/translations/en/README.md`;
- `works/thirukkural/translations/en/GLOSSARY.md`;
- `works/thirukkural/README.md`;
- root `README.md`;
- this `HANDOVER.md`.

# Next exact activity

Begin the separate Part 001 English **source-check cycle with scans 1–7**.

1. Fetch each English draft `0001`–`0007` and its corresponding audited Tamil file.
2. Compare heading, metadata, every translated source element, paragraph/line structure, omissions and additions.
3. Correct only translation differences supported by the audited Tamil source / controlling scan.
4. Preserve project-translation identity and do not import external English wording.
5. Promote a page from `draft` to `source-checked` only after its comparison is complete.
6. Do not perform `editorial-reviewed` promotion in the same activity.
7. After scans 1–7, inspect scan 8's source-limited English alignment separately; do not invent the missing handwriting.
8. Then source-check scans 9–12 and 13–20 in later batches.
9. Only after the complete Part 001 source-check should the editorial consistency review begin.

## Source authority rule

The supplied scans remain the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. The project English translation must preserve the meaning and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
