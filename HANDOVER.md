# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

Active work: `works/thirukkural/`

## Mandatory startup

Before making changes:

1. read `THIRUKKURAL_ARCHIVAL_GUIDELINES.md` completely;
2. read `LITERARY_COMMENTARY_PROCESSING_GUIDE.md` completely;
3. read this `HANDOVER.md` completely;
4. read `works/thirukkural/README.md`;
5. inspect existing target files before writing;
6. for English work also read:
   - `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`;
   - `works/thirukkural/translations/en/GLOSSARY.md`;
   - `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
   - `works/thirukkural/translations/en/reviews/PART_008_REVIEW.md`;
   - `works/thirukkural/translations/en/reviews/PART_008_RELEASE_REPORT.md`;
   - `works/thirukkural/AUDIT_PART_009.md`.

Repository state is authoritative.

## Source rule

The supplied Tamil scans are controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

Source PDFs are working/control sources and are not to be committed to GitHub unless the user explicitly requests that.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Keep these as separate gates.

## Established state

### Tamil

Parts **001–009 are audited / ARCHIVAL-READY continuously** through:

- overall scan **191**;
- printed page **158**;
- Kural **780**.

Latest audit: `works/thirukkural/AUDIT_PART_009.md`.

### English project translation

Parts **001–008 are fully released** continuously through Kural **670**.

Part 009 English has not started.

Every English page must identify:

```yaml
translation_type: "project_translation"
```

Released Parts 001–008 must not be revised merely to harmonize later vocabulary.

Permanent earlier protections remain binding, including chapter 38 `ஊழ்` → **Oozh**, `இயற்கை நிலை` → **natural condition**, and Kural 543's Kalaignar-directed `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**.

## Part 009 Tamil — ARCHIVAL-READY

Controlling source: `திருக்குறள்_கலைஞர்_உரை_part_009_pages_170-191.pdf`

Final scope:

- physical pages: **22**;
- scans **170–191**;
- printed pages **137–158**;
- Kural **671–780**;
- chapters **68–78**;
- `verified`: **22 / 22**;
- `needs-review`: **0**;
- `partial`: **0**;
- `blocked`: **0**;
- audit decision: **PASS / ARCHIVAL-READY**.

Chapter map:

- 68 `வினை செயல்வகை` — 671–680;
- 69 `தூது` — 681–690;
- 70 `மன்னரைச் சேர்ந்து ஒழுகல்` — 691–700;
- 71 `குறிப்பறிதல்` — 701–710;
- 72 `அவை அறிதல்` — 711–720;
- 73 `அவை அஞ்சாமை` — 721–730;
- 74 `நாடு` — 731–740;
- 75 `அரண்` — 741–750;
- 76 `பொருள் செயல்வகை` — 751–760;
- 77 `படை மாட்சி` — 761–770;
- 78 `படைச் செருக்கு` — 771–780.

Source-visible section sequence:

`அமைச்சியல்` → `அரணியல்` → `கூழியல்` → `படையியல்`.

Do not flatten these distinctions in later English work.

### Verification correction retained

Scan **190 / Kural 771 commentary**:

- first pass: `நடுகல்லைப் போனவர்கள்`
- verified source: **`நடுகல்லாய்ப் போனவர்கள்`**.

### Source-sensitive readings protected

The following were directly verified from the scan and must not be silently normalized:

- Kural **717**: `கற்றறிந்தார் கல்வி விளங்கும் கசடறச் / சொற்றெரிதல் முன்னர் இழுக்கு.`
- Kural **725 commentary**: `தருக்கமென்படும் அளவைக் திறமும்`
- Kural **733 commentary**: `மளவுக்கு வளம்`
- Kural **771 commentary**: `நடுகல்லாய்ப் போனவர்கள்`

### Adjacent continuity

Part 008 printed page **136** / Kural **670** continues into Part 009 printed page **137** / Kural **671**.

The supplied Part 010 first page was inspected for boundary continuity only: it carries printed page **159**, chapter `79. நட்பு`, beginning Kural **781**. Part 010 remains untranscribed.

# Exact next activity

Perform **Part 009 English project translation — first pass** for all **22 aligned pages**, scans **170–191 / printed pages 137–158 / Kural 671–780**.

Before writing, fresh-read the English translation guide, glossary, translation status, Part 008 review/release artefacts, Part 009 audit, and all audited Part 009 Tamil pages. Inspect the target English directory first and continue existing work if any rather than creating duplicates.

Requirements:

- mirror each Tamil filename under `works/thirukkural/translations/en/pages/`;
- use `translation_type: "project_translation"`;
- keep every first-pass page at `status: "draft"`;
- preserve page alignment, Kural numbering and two-line structure;
- keep Kural translation and Kalaignar commentary translation separate;
- retain Kalaignar's wording, images, institutional/social vocabulary and interpretive direction;
- use the verified Part 009 source-sensitive readings above as the Tamil basis;
- stop after first-pass translation.

Do not promote Part 009 English pages to later statuses, create review/release artefacts, begin Part 010 Tamil transcription, or alter released English Parts 001–008 during this first-pass activity.

After all 22 Part 009 English pages exist as `draft`, the next separate activity is **Part 009 English direct source-check**.