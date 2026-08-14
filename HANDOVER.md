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

## Completed English drafts — scans 21–27

Seven aligned English records now exist, all `status: "draft"`:

- `0021-mathippurai-08.md` — Critical Appreciation / Various Distinctive Merits;
- `0022-mathippurai-09.md` — Clarity / Concise Explanation / New Meaning;
- `0023-mathippurai-10.md` — New Meaning / `புத்தேளிர்` discussion;
- `0024-mathippurai-11.md` — Entirely Fresh Explanation / Subtle Penetrating Insight;
- `0025-mathippurai-12.md` — Subtle Penetrating Insight / Gratitude;
- `0026-mathippurai-13.md` — completion of Nannan's Gratitude section;
- `0027-pathippurai.md` — Publisher's Note.

Current Part 002 English status:

- aligned English records: **7 / 21**;
- `draft`: **7**;
- `source-checked`: **0**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

## New/provisional Part 002 terminology

The glossary now records draft treatments including:

- `உரைக் குறள்` → **Commentary in Kural Form**;
- `இடைமிடை சொல்நலம்` → **Grace of Interposed Words**;
- `தெளிவு` → **Clarity**;
- `சுருக்க விளக்கம்` → **Concise Explanation**;
- `புதுப்பொருள்` → **New Meaning**;
- `புத்தம்புது விளக்கம்` → **Entirely Fresh Explanation**;
- `நுண்மாண் நுழைபுலம்` → **Subtle Penetrating Insight**;
- `நன்றி` → **Gratitude** in Nannan's concluding section;
- `புத்தேளிர் / புத்தேள் உலகு` → source-specific draft treatment centred on **newness / new world**;
- `ஒப்புரவு` → **helpfulness / helping others** in the source's own explanation.

## Review-sensitive Part 002 items

### Scan 25 / `அடுத்தூர்வது அஃதொப்பதில்`

Part 001 scan 19 was released with the compact phrase retained exactly in Tamil because that immediate source context did not support a sufficiently secure English expansion.

Part 002 scan 25 now supplies the **complete quoted Kural** and the first-pass Part 002 draft provisionally renders its second line as:

**“nothing equals pressing forward to meet it.”**

This is **draft only**. Do not modify the released Part 001 scan-19 English record yet. Re-evaluate the Part 002 wording during source-check; only then consider a separately documented cross-part editorial change.

### Scan 26 / `மக்கள் நெஞ்சின் மலிவுப் பதிப்பு`

The Tamil phrase is retained visibly and accompanied by a contextual gloss rather than being assigned a falsely certain literal equivalent. Recheck during Part 002 source-check/editorial review.

### Scan 27 pagination

`printed_page: "xxvi"` is retained with `printed_page_basis` explaining that the numeral is inferred from the contents page and surrounding sequence; it is not visibly printed on the scan.

## Remaining Part 002 structure

- scans 28–29 — `திருக்குறள் அதிகார அகர வரிசை` / Alphabetical Index of Chapters;
- scans 30–31 — `அதிகார அருஞ்சொற்பொருள் அகரவரிசை` / Alphabetical Glossary of Chapter Terms;
- scan 32 — `திருக்குறள் / கலைஞர் உரை / அறம்` section title;
- scan 33 — blank / reverse-side bleed-through;
- scans 34–35 — `1. வழிபாடு`, Kural 1–10;
- scans 36–37 — `2. வான் சிறப்பு`, Kural 11–20;
- scans 38–39 — `3. நீத்தார் பெருமை`, Kural 21–30;
- scans 40–41 — `4. அறன் வலியுறுத்தல்`, Kural 31–40.

# Next exact activity

Continue **Part 002 English first-pass translation with scans 28–33**.

1. Fetch Tamil archival files:
   - `0028-athikara-akara-varisai-01.md`
   - `0029-athikara-akara-varisai-02.md`
   - `0030-athikara-arunchol-akaravarisai-01.md`
   - `0031-athikara-arunchol-akaravarisai-02.md`
   - `0032-aram-title.md`
   - `0033-blank.md`.
2. Create matching English files under `works/thirukkural/translations/en/pages/`.
3. Use `status: "draft"` for all six new records.
4. Preserve index entry order, numbering and page references exactly; translate labels consistently from the controlled glossary.
5. For scan 32, preserve the source title-page hierarchy and its inferred printed page **xxxi** with the documented basis from the Tamil record.
6. For scan 33, represent only the blank / reverse-side bleed-through page condition; do not invent text from bleed-through.
7. Do not begin scans 34–41 / Kural 1–40 until scans 28–33 are complete and documentation is synchronized.
8. Do not source-check scans 21–27 in the same activity; first complete the Part 002 first-pass sequence.

## Source authority rule

The supplied scans remain the controlling sources. The project English translation must preserve the meaning and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
