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
6. inspect the actual controlling source required by the active gate;
7. for English work additionally fresh-read:
   - `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`;
   - `works/thirukkural/translations/en/GLOSSARY.md`;
   - `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
   - latest relevant English review/release artefacts.

Repository state is authoritative.

## Source rule

The supplied Tamil scans are controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

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

Permanent earlier protections remain binding, including:

- chapter 38 `ஊழ்` → **Oozh**;
- Kalaignar's `இயற்கை நிலை` → **natural condition**;
- Kural 543 `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**, not an automatic caste-specific conventional gloss;
- preservation of Kalaignar's governance, citizens, working-people, justice, public-resource and rational/inquiry vocabulary where the Tamil explicitly uses it.

# Established baseline

## Tamil

Parts **001–012 are audited / ARCHIVAL-READY continuously** through:

- overall scan **260**;
- printed page **227**;
- Kural **1115**.

Latest Tamil audit:

`works/thirukkural/AUDIT_PART_012.md` — **PASS / ARCHIVAL-READY**.

## English

Parts **001–012 are fully released continuously through Kural 1115**.

Latest English artefacts:

- `works/thirukkural/translations/en/reviews/PART_012_REVIEW.md`;
- `works/thirukkural/translations/en/reviews/PART_012_RELEASE_REPORT.md` — **PASS / RELEASE APPROVED**.

All 23 Part 012 English page records are now `release-ready`.

Released Parts 001–012 must remain untouched during Part 013 Tamil work.

# Closed Part 012 release baseline

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_012_pages_238-260.pdf`

Part 012 Tamil audit:

`works/thirukkural/AUDIT_PART_012.md` — **PASS / ARCHIVAL-READY**.

Part 012 English release report:

`works/thirukkural/translations/en/reviews/PART_012_RELEASE_REPORT.md` — **PASS / RELEASE APPROVED**.

Closed scope:

- physical pages **23 / 23**;
- scans **238–260**;
- Part-local pages **1–23**;
- printed pages **205–218**, two unnumbered leaves, then **221–227**;
- Kural **1011–1115**;
- Tamil `verified`: **23 / 23**;
- English `release-ready`: **23 / 23**.

Released structural sequence:

1. scans **238–251** — `பொருள் — குடியியல்` → **Porul — Civic Life**;
2. scan **252** — standalone `இன்பம்` / **Inbam** title leaf;
3. scan **253** — blank/reverse-show-through leaf;
4. scans **254–260** — `இன்பம் — களவியல்` → **Inbam — Clandestine Love**.

Released chapter headings 102–112:

- 102 `நாணுடைமை` → **Modesty**;
- 103 `குடிசெயல் வகை` → **Working for the Community**;
- 104 `உழவு` → **Agriculture**;
- 105 `நல்குரவு` → **Poverty**;
- 106 `இரவு` → **Begging**;
- 107 `இரவச்சம்` → **Dread of Begging**;
- 108 `கயமை` → **Baseness**;
- 109 `தகை அணங்குறுத்தல்` → **The Torment of Beauty**;
- 110 `குறிப்பறிதல்` → **Understanding Signs**;
- 111 `புணர்ச்சி மகிழ்தல்` → **Delight in Union**;
- 112 `நலம் புனைந்து உரைத்தல்` → **Praising Her Beauty**, through Kural **1115** only.

Protected Part 012 treatments remain binding, including the verified Kural **1018 / 1035 / 1048** commentary directions, Kural **1062** creator challenge, supplied unusual Kural **1077 / 1098** readings, Kural **1103** `lotus-eyed one` comparison and Kural **1115** anicham-stalk / broken-waist / absent-auspicious-drum explanation.

# Supplied later sources

- Part 013 — `திருக்குறள்_கலைஞர்_உரை_part_013_pages_261-282.pdf` — **22 pages** — source received, not started;
- Part 014 — `திருக்குறள்_கலைஞர்_உரை_part_014_pages_283-302.pdf` — **20 pages** — source received, not started;
- Part 015 — `திருக்குறள்_கலைஞர்_உரை_part_015_pages_303-323.pdf` — **21 pages** — source received, not started.

Part 013 supplied-file identity currently available in the user's file library:

`file_0000000081a08208a863fa44b7c0e9b9`

The completed Part 012 audit inspected only the Part 013 first page for boundary context. It confirms:

- printed page **228**;
- Kural **1116–1120**;
- continuation of chapter 112 `நலம் புனைந்து உரைத்தல்`.

This boundary information does **not** authorize assumptions about later Part 013 pages. The actual Part 013 scan must be inspected during the next activity.

# Exact next activity

**Part 013 Tamil source inspection and first-pass transcription — all 22 supplied physical pages / overall scans 261–282.**

Required procedure:

1. fresh-read the mandatory startup files above;
2. locate and inspect the actual supplied source `திருக்குறள்_கலைஞர்_உரை_part_013_pages_261-282.pdf` before creating any metadata or page records;
3. inspect the existing `works/thirukkural/pages/` tree first and confirm no Part 013 work has already started; continue existing work if present rather than creating duplicates;
4. use the scan itself to determine printed-page sequence, source-visible section hierarchy, chapter transitions, Kural ranges and physical-page types;
5. use the known incoming boundary only as a continuity check: Part 012 ends at printed page **227 / Kural 1115**, while the already inspected Part 013 first page begins printed page **228 / Kural 1116** and continues chapter 112;
6. create one Tamil Markdown record for every supplied Part 013 physical page, aligned to overall scans **261–282** and Part-local pages **1–22**;
7. preserve the source's exact Tamil wording, punctuation, two-line Kural structure, headings, repetitions, unusual forms and page hierarchy; do not normalize from another edition;
8. distinguish printed text from bleed-through, marks, damage, stamps or other non-body material;
9. first-pass records must use the repository's normal pre-verification status/method conventions; inspect the latest previous first-pass implementation before writing rather than inventing metadata values;
10. update progress/status documentation after the complete first-pass unit is created;
11. stop after the Part 013 Tamil first-pass transcription gate;
12. do **not** perform Part 013 direct visual verification in the same activity;
13. do **not** perform the Part 013 Tamil audit in the same activity;
14. do **not** begin Part 013 English translation;
15. do **not** alter released English Parts 001–012;
16. do **not** begin Parts 014–015 in the same activity.

After a complete Part 013 first pass, the next separate activity is **Part 013 Tamil direct visual verification**.
