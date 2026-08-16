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
   - `works/thirukkural/translations/en/reviews/PART_009_REVIEW.md`;
   - `works/thirukkural/translations/en/reviews/PART_008_RELEASE_REPORT.md`;
   - `works/thirukkural/AUDIT_PART_009.md`.

Repository state is authoritative.

## Source rule

The supplied Tamil scans are controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

Source PDFs are working/control sources and are not to be committed to GitHub unless the user explicitly requests that.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Keep these as separate gates.

# Established state

## Tamil

Parts **001–009 are audited / ARCHIVAL-READY continuously** through:

- overall scan **191**;
- printed page **158**;
- Kural **780**.

Latest Tamil audit: `works/thirukkural/AUDIT_PART_009.md`.

## English project translation

Parts **001–008 are fully released** continuously through Kural **670**.

Part 009 English has completed:

- first-pass translation: **22 / 22**;
- direct source-check: **22 / 22**;
- editorial consistency / glossary reconciliation: **22 / 22**.

All 22 Part 009 English pages are now `editorial-reviewed`. The release gate has not yet begun.

Every English page must identify:

```yaml
translation_type: "project_translation"
```

Released Parts 001–008 must not be revised merely to harmonize later vocabulary.

Permanent earlier protections remain binding, including chapter 38 `ஊழ்` → **Oozh**, `இயற்கை நிலை` → **natural condition**, and Kural 543's Kalaignar-directed `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**.

# Part 009 Tamil — ARCHIVAL-READY

Controlling source: `திருக்குறள்_கலைஞர்_உரை_part_009_pages_170-191.pdf`

Final Tamil scope:

- physical pages: **22**;
- scans **170–191**;
- printed pages **137–158**;
- Kural **671–780**;
- chapters **68–78**;
- `verified`: **22 / 22**;
- audit decision: **PASS / ARCHIVAL-READY**.

Protected Tamil readings:

- Kural **717**: `கற்றறிந்தார் கல்வி விளங்கும் கசடறச் / சொற்றெரிதல் முன்னர் இழுக்கு.`
- Kural **725 commentary**: `தருக்கமென்படும் அளவைக் திறமும்`
- Kural **733 commentary**: `மளவுக்கு வளம்`
- Kural **771 commentary**: `நடுகல்லாய்ப் போனவர்கள்`.

The source-visible section sequence is:

`அமைச்சியல்` → `அரணியல்` → `கூழியல்` → `படையியல்`.

Part 008 printed page **136** / Kural **670** continues into Part 009 printed page **137** / Kural **671**.

The supplied Part 010 first page has been inspected for boundary continuity only: printed page **159**, chapter `79. நட்பு`, Kural **781**. Part 010 remains untranscribed.

# Part 009 English — EDITORIAL REVIEW COMPLETE / RELEASE PENDING

Scope:

- scans **170–191**;
- printed pages **137–158**;
- Kural **671–780**;
- chapters **68–78**;
- aligned English records: **22 / 22**.

Current status:

- `draft`: **0**;
- `source-checked`: **0**;
- `editorial-reviewed`: **22 / 22**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

Editorial review artefact:

`works/thirukkural/translations/en/reviews/PART_009_REVIEW.md`

## Controlled Part 009 chapter headings

- 68 `வினை செயல்வகை` → **The Method of Action**;
- 69 `தூது` → **The Envoy**;
- 70 `மன்னரைச் சேர்ந்து ஒழுகல்` → **Conduct in the Presence of Kings**;
- 71 `குறிப்பறிதல்` → **Understanding Signs**;
- 72 `அவை அறிதல்` → **Knowing the Assembly**;
- 73 `அவை அஞ்சாமை` → **Fearlessness in the Assembly**;
- 74 `நாடு` → **The Country**;
- 75 `அரண்` → **Fortress**;
- 76 `பொருள் செயல்வகை` → **The Way of Acquiring Wealth**;
- 77 `படை மாட்சி` → **Excellence of the Army**;
- 78 `படைச் செருக்கு` → **Martial Pride**.

Chapter 71 was refined from **Understanding Signs (Porul)** to **Understanding Signs**. `(Porul)` was a project-added first-pass disambiguator not present in the Tamil title; scans 176–177 have been updated consistently. No substantive Kural/commentary body text was changed during editorial review.

## Controlled structural vocabulary through Part 009

- `அமைச்சியல்` → **Ministerial Affairs**;
- `அரணியல்` → **Fortification Affairs**;
- `கூழியல்` → **Wealth**;
- `படையியல்` → **Military Affairs**.

Do not flatten these source-visible distinctions.

## Source-check corrections that must remain intact

1. **Kural 680** — **“those with little support ... the trembling among their own”**; do not restore the unsupported territorial “smaller domain” wording.
2. **Kural 691** — **“kings”**; do not restore unsupported “contentious.”
3. **Kural 717** — retain the source-checked clause ending **“there is a lapse”**, grounded in the supplied edition's verified final `இழுக்கு`.

## Protected source-sensitive English treatments

- Kural **717** remains based on this edition's unusual verified Tamil and retains its source-check note.
- Kural **725 commentary** retains **“the skill of measure called logic”** from `தருக்கமென்படும் அளவைக் திறமும்` without repairing the Tamil.
- Kural **733 commentary** retains **“possesses wealth to that measure”** from `மளவுக்கு வளம்` without normalizing the source.
- Kural **771 commentary** retains **“have become memorial stones”** from `நடுகல்லாய்ப் போனவர்கள்`.
- Kural **773** retains Kalaignar's explicit **great manliness / manliness** framing.

Kalaignar's institutional/public vocabulary remains protected: government, tax/revenue, customs duties, tribute, country, fortification, wealth, army, ruler/leader and public responsibility.

Direct images remain protected, including elephant-capturing-elephant, warming by fire, cashew-nut comparison, nectar in an unclean courtyard, love/compassion/nurse/material-resources, elephants fighting from a hill, rats/sea/cobra breath, victory garland, memorial stones, spear pulled from a warrior's chest, honourable wounds and warrior's anklet.

# Exact next activity

Perform the separate **Part 009 English release gate** for all **22 `editorial-reviewed` pages**, scans **170–191 / printed pages 137–158 / Kural 671–780**.

## Required release-gate procedure

1. fresh-read this handover, `TRANSLATION_GUIDE.md`, `GLOSSARY.md`, `TRANSLATION_STATUS.md`, `reviews/PART_009_REVIEW.md`, the prior `reviews/PART_008_RELEASE_REPORT.md`, and `AUDIT_PART_009.md`;
2. inspect all 22 Part 009 English records and confirm every page begins at `status: "editorial-reviewed"`;
3. verify exact scan/printed-page/Kural continuity and one-to-one English/Tamil filename alignment;
4. confirm every record retains `translation_type: "project_translation"`, `source_tamil_status: "verified"`, and the correct `source_tamil_file`;
5. verify final controlled chapter headings and the section sequence **Ministerial Affairs → Fortification Affairs → Wealth → Military Affairs**;
6. confirm the Kural 680, 691 and 717 source-check corrections remain intact;
7. confirm the protected Kural 717 / 725 / 733 / 771 / 773 treatments and direct source images remain intact;
8. create `works/thirukkural/translations/en/reviews/PART_009_RELEASE_REPORT.md` only if the release checks pass;
9. promote all passing Part 009 pages from `editorial-reviewed` to `release-ready` only after the release decision is recorded;
10. synchronize `TRANSLATION_STATUS.md`, English README, work README, root README and this handover after release;
11. stop after the Part 009 release gate.

## Do not start alongside release unless explicitly requested

Do **not**:

- begin Part 010 Tamil transcription;
- alter released English Parts 001–008 merely for harmonization;
- revise the Part 009 English body merely for stylistic preference during release;
- create any Part 010 English material.

# After Part 009 English release

If the release gate passes, the next separate activity is **Part 010 Tamil first-pass transcription**, beginning at overall scan **192 / printed page 159 / Kural 781 / chapter 79 `நட்பு`**, using the supplied Part 010 scan as controlling source.
