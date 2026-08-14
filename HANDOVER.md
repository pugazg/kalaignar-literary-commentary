# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. The English layer is a **project-created translation**, not an official/publisher English edition, and must not import external English Kural wording or another commentator's interpretation.

# திருக்குறள் — Tamil archival state

- Part 001 — scans 1–20: **ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**; 19 verified + scan 8 partial.
- Part 002 — scans 21–41: **ARCHIVAL-READY**, 21/21 verified.
- Part 003 — scans 42–62: **ARCHIVAL-READY**, 21/21 verified; printed pages 9–29; Kural 41–145.

Do not redo or renumber Parts 001–003. Future Tamil intake may continue from overall scan 63 only if the next supplied scan itself confirms continuity after scan 62 / printed page 29 / Kural 145.

# English project translation

Permanent cadence:

**Tamil transcription → Tamil visual verification → Tamil audit → English draft → English source-check → editorial consistency review → English part release report.**

Framework:

- `works/thirukkural/translations/en/README.md`
- `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`
- `works/thirukkural/translations/en/GLOSSARY.md`
- `works/thirukkural/translations/en/TRANSLATION_STATUS.md`
- `works/thirukkural/translations/en/reviews/PART_001_REVIEW.md`
- `works/thirukkural/translations/en/reviews/PART_001_RELEASE_REPORT.md`

Every English page must retain:

`translation_type: "project_translation"`

# Part 001 English — RELEASE COMPLETE

Final state:

- aligned English records: **20 / 20**;
- `release-ready`: **19** — scans 1–7 and 9–20;
- `source-limited`: **1** — scan 8;
- release decision: **RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS**.

Part 001 controlled terminology and documented source limitations remain in force. Do not silently revise released Part 001 wording merely because later Part 002 context appears; any cross-part change must follow source-check/editorial review and be explicitly documented.

# Part 002 English — FIRST PASS IN PROGRESS

Tamil source: `திருக்குறள்_கலைஞர்_உரை_part_002_pages_21-41.pdf`

Tamil state: **21/21 verified; ARCHIVAL-READY**.

Current English state:

- aligned English records: **13 / 21**;
- `draft`: **13** — scans 21–33;
- `source-checked`: **0**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

## Completed English drafts — scans 21–27

- `0021-mathippurai-08.md` — Critical Appreciation / Various Distinctive Merits;
- `0022-mathippurai-09.md` — Clarity / Concise Explanation / New Meaning;
- `0023-mathippurai-10.md` — New Meaning / `புத்தேளிர்` discussion;
- `0024-mathippurai-11.md` — Entirely Fresh Explanation / Subtle Penetrating Insight;
- `0025-mathippurai-12.md` — Subtle Penetrating Insight / Gratitude;
- `0026-mathippurai-13.md` — completion of Nannan's Gratitude section;
- `0027-pathippurai.md` — Publisher's Note.

Review-sensitive items remain:

- scan 25 gives the complete Kural containing `அடுத்தூர்வது அஃதொப்பதில்`; draft second line is **“nothing equals pressing forward to meet it.”** Do not change released Part 001 scan 19 before Part 002 source-check/editorial review;
- scan 26 retains `மக்கள் நெஞ்சின் மலிவுப் பதிப்பு` with a contextual gloss;
- scan 27 has inferred `printed_page: "xxvi"` with its source basis documented because the numeral is not visibly printed.

## Completed English drafts — scans 28–33

Created and synchronized:

- `0028-athikara-akara-varisai-01.md` — **Alphabetical Index of Chapters**, first page;
- `0029-athikara-akara-varisai-02.md` — **Alphabetical Index of Chapters**, second page;
- `0030-athikara-arunchol-akaravarisai-01.md` — **Alphabetical Glossary of Chapter Terms**, first page;
- `0031-athikara-arunchol-akaravarisai-02.md` — **Alphabetical Glossary of Chapter Terms**, second page;
- `0032-aram-title.md` — `Thirukkural / Kalaignar's Commentary / Aram` section-title page;
- `0033-blank.md` — blank verso / reverse-side bleed-through page condition.

All six are `status: "draft"`.

### Index translation policy

- source entry order, chapter numbers and paired-column structure are preserved;
- chapter titles already controlled from Part 001 retain those controlled forms;
- title translations newly introduced by the full 133-chapter index are **first-pass project renderings only** and must be reconsidered at Part 002 source-check/editorial review before becoming controlled glossary forms;
- no outside standard English chapter-title list was imported.

### Source glossary policy

Scans 30–31 translate this edition's own `அருஞ்சொற்பொருள்` explanations rather than replacing them with definitions from another edition.

Important review-sensitive examples:

- `வழிபாடு` remains the controlled chapter title **Worship**, while the source's gloss `பின்பற்றுதல்` is translated as **Following**;
- `பெண்வழிச் சேறல்` remains **Following a Woman's Lead**, while the source gloss `பெண் பித்தராதல்` is drafted as **becoming obsessed with women**;
- `வரைவின் மகளிர்` is provisionally **Women Beyond Bounds**, while the source gloss `விலை மகளிர்` is directly rendered **Women for hire**. The title-level English is not settled.

### Scan 32

Retain:

`printed_page: "xxxi"`

with the exact documented basis from the Tamil record: Part 001 contents entry `அறத்துப்பால் — xxxi` plus surrounding source sequence; the numeral is not visibly printed on scan 32.

### Scan 33

No distinct printed text. Reverse-side bleed-through is only a page-condition observation and must not be transcribed or translated as current-page body text.

# Remaining Part 002 structure

Only the main-body first-pass batch remains:

- scans 34–35 — `1. வழிபாடு`, Kural 1–10;
- scans 36–37 — `2. வான் சிறப்பு`, Kural 11–20;
- scans 38–39 — `3. நீத்தார் பெருமை`, Kural 21–30;
- scans 40–41 — `4. அறன் வலியுறுத்தல்`, Kural 31–40.

# Next exact activity

Complete **Part 002 English first-pass translation with scans 34–41**.

1. Fetch verified Tamil archival files:
   - `0034-aram-vazhipadu-01.md`
   - `0035-aram-vazhipadu-02.md`
   - `0036-aram-vaan-sirappu-01.md`
   - `0037-aram-vaan-sirappu-02.md`
   - `0038-aram-neeththar-perumai-01.md`
   - `0039-aram-neeththar-perumai-02.md`
   - `0040-aram-aran-valiyuruththal-01.md`
   - `0041-aram-aran-valiyuruththal-02.md`.
2. Create matching English files under `works/thirukkural/translations/en/pages/`.
3. Use `status: "draft"` for all eight.
4. Preserve Kural number and two-line verse structure.
5. Translate the Kural itself and Kalaignar's commentary as separate layers.
6. Use controlled chapter titles:
   - `வழிபாடு` → **Worship**;
   - `வான் சிறப்பு` → **The Excellence of Rain**;
   - `நீத்தார் பெருமை` → **The Greatness of Renunciants**;
   - `அறன் வலியுறுத்தல்` → **Affirming Aram**.
7. Translate only from the verified Tamil archival record / controlling scan. Do not import a published English Thirukkural translation, another Tamil edition, web text, or outside commentary.
8. Do **not** source-check scans 21–33 in the same activity. First complete all eight drafts so Part 002 first pass reaches **21/21**.
9. After scans 34–41 are drafted, synchronize `TRANSLATION_STATUS.md`, English README, work README, root README and this handover.
10. The activity after that is the dedicated Part 002 source-check, beginning from scan 21 in source order.

## Source authority rule

The supplied scans remain the controlling sources. The project English translation must preserve the meaning and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
