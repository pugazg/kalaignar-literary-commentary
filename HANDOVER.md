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

- local PDF pages: **21**
- overall scans: **21–41**
- `verified`: **21 / 21**
- audit complete
- release decision: **ARCHIVAL-READY**
- audit report: `works/thirukkural/AUDIT_PART_002.md`

Do not redo or renumber Part 002.

## Part 003

Source: `திருக்குறள்_கலைஞர்_உரை_part_003_pages_42-62.pdf`

- local PDF pages: **21**
- overall scans: **42–62**
- printed pages: **9–29**
- Kural range: **41–145**
- `verified`: **21 / 21**
- audit complete
- release decision: **ARCHIVAL-READY**
- audit report: `works/thirukkural/AUDIT_PART_003.md`

Chapter coverage:

- `5. இல்வாழ்க்கை` — 41–50
- `6. வாழ்க்கைத் துணைநலம்` — 51–60
- `7. மக்கட்பேறு` — 61–70
- `8. அன்புடைமை` — 71–80
- `9. விருந்தோம்பல்` — 81–90
- `10. இனியவை கூறல்` — 91–100
- `11. செய்ந்நன்றியறிதல்` — 101–110
- `12. நடுவு நிலைமை` — 111–120
- `13. அடக்கம் உடைமை` — 121–130
- `14. ஒழுக்கம் உடைமை` — 131–140
- `15. பிறனில் விழையாமை` — 141–145 in this supplied part

Do not redo or renumber Part 003.

# English project translation framework — established

The user chose **not to wait until the entire Thirukkural book is supplied**. English should proceed after each Tamil PDF part has completed Tamil verification and audit.

Permanent cadence:

**Tamil transcription → Tamil visual verification → Tamil audit → English draft → English source-check → editorial consistency review → English part release report.**

## Translation identity

The Thirukkural English layer currently being created is a **project-created English translation**, not an official/publisher English edition.

Every English page must carry:

```yaml
translation_type: "project_translation"
```

If a published English edition of Kalaignar's Thirukkural commentary is later supplied, archive it separately and do not overwrite this project translation.

## Translation authority

1. supplied Tamil scan — ultimate authority;
2. corresponding audited/verified Tamil page — working translation basis;
3. English translation guide and controlled glossary;
4. review notes.

Do not import a web Kural, another Tamil edition, another commentator, or an existing English Kural translation silently.

## English framework files created

- `works/thirukkural/translations/en/README.md`
- `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`
- `works/thirukkural/translations/en/GLOSSARY.md`
- `works/thirukkural/translations/en/TRANSLATION_STATUS.md`

The repository-level `LITERARY_COMMENTARY_PROCESSING_GUIDE.md` was also expanded to distinguish:

- published/official English source editions;
- project-created English translations.

## English page alignment

Each English page must mirror the Tamil archival filename exactly.

Example:

```text
works/thirukkural/pages/0034-aram-vazhipadu-01.md
works/thirukkural/translations/en/pages/0034-aram-vazhipadu-01.md
```

Recommended English status progression:

- `draft`
- `source-checked`
- `editorial-reviewed`
- `release-ready`

Exceptional states:

- `source-limited`
- `blocked`

Tamil `verified` and English `release-ready` are separate concepts.

## Special source-limited page

Part 001 scan 8 is a handwritten facsimile whose Tamil archival record is intentionally `partial` after high-resolution review.

Its English page, when created, must:

- translate only securely established source content;
- use `status: "source-limited"`;
- state that the continuous handwritten body could not be safely read;
- never reconstruct or infer the missing English content.

## Controlled glossary starting point

`translations/en/GLOSSARY.md` now defines provisional English editorial defaults through chapter 15 and core recurring terms.

Important policy:

- `அறம்` is not forced into one English word everywhere;
- structural labels may retain `Aram` with an explanatory gloss;
- running prose translates contextually;
- source gender specificity is preserved;
- source chapter headings, not headings from other editions, control the English chapter-title mapping.

# Files kept synchronized

Tamil archive:

- `works/thirukkural/metadata/source.md`
- `works/thirukkural/indexes/page-map.md`
- `works/thirukkural/README.md`
- root `README.md`
- `works/thirukkural/AUDIT_PART_001.md`
- `works/thirukkural/AUDIT_PART_002.md`
- `works/thirukkural/AUDIT_PART_003.md`

Translation framework:

- `works/thirukkural/translations/en/README.md`
- `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`
- `works/thirukkural/translations/en/GLOSSARY.md`
- `works/thirukkural/translations/en/TRANSLATION_STATUS.md`
- repository `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`

# Next exact activity

Begin the **Part 001 English first-pass translation for scans 1–7**.

1. Fetch Tamil page files `0001` through `0007` from `works/thirukkural/pages/`.
2. Create matching filenames under `works/thirukkural/translations/en/pages/`.
3. Use the English translation front matter defined in `TRANSLATION_GUIDE.md`.
4. Mark every new page in this batch `status: "draft"`.
5. Translate only source-supported content from the audited Tamil records.
6. Preserve headings, paragraph boundaries, names, numbers and structural distinctions.
7. Do not include scan 8 in this first batch; it will be handled separately as `source-limited`.
8. Update `TRANSLATION_STATUS.md`, work README and this handover after the batch.
9. Do **not** perform the English source-check/review in the same activity; keep first-pass creation and review separate.

Tamil source intake can continue later from overall scan **63** when the next PDF is supplied and its continuity after scan 62 / printed page 29 / Kural 145 is confirmed.

## Source authority rule

The supplied scans remain the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. The project English translation must preserve the meaning and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
