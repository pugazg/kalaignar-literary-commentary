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

Part 001 scans **1–20** have completed:

**first pass → source-check → editorial consistency / glossary reconciliation → release gate.**

Final status:

- aligned English records: **20 / 20**;
- `release-ready`: **19** — scans 1–7 and 9–20;
- `source-limited`: **1** — scan 8;
- `editorial-reviewed`: **0**;
- `source-checked`: **0**;
- `draft`: **0**;
- `blocked`: **0**.

Final release decision:

**RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS.**

## Part 001 release artefacts

- review: `works/thirukkural/translations/en/reviews/PART_001_REVIEW.md`
- release report: `works/thirukkural/translations/en/reviews/PART_001_RELEASE_REPORT.md`

## Controlled Part 001 decisions

- `முப்பால்` → **Muppaal**;
- verified source form `திருவிடம்` → **Tiruvidam**, deliberately retained rather than normalized;
- `ஊழ்` → **Oozh** as heading/concept title and *oozh* in running prose where the Tamil term itself is named;
- `இயற்கை நிலை` → **natural condition** only as Professor Nannan's explicit attribution of Kalaignar's interpretation;
- `வாயுறை` → **counsel**;
- `பெண்வழிச் சேறல்` → **Following a Woman's Lead**;
- `பிறிது மொழிதல்` → ***pirithu mozhithal*** with the gloss “saying one thing in order to convey another”;
- `அடுத்தூர்வது அஃதொப்பதில்` → intentionally retained exactly in Tamil because the audited source does not support a sufficiently secure English expansion;
- `பா நலம்` → **Poetic Quality**;
- `அணி நலம்` → **Excellence of Poetic Figure**;
- `அடை நலம்` → **Excellence of Epithets**.

The source-title distinction remains mandatory:

- `கடவுள் வாழ்த்து` → **Invocation to God** when that source title is named;
- `வழிபாடு` → **Worship** for Kalaignar's adopted chapter title.

## Scan 8 — source limitation remains after release

`works/thirukkural/translations/en/pages/0008-handwritten-note.md` remains `source-limited`.

Securely established English content is limited to the title, decorative divider presence, Kalaignar's signature presence, date **27/12/2007**, and page-condition / bleed-through description. The continuous handwritten body remains untranslated and unreconstructed.

Do not promote scan 8 unless a clearer controlling source is supplied and the Tamil archival record itself can first be improved safely.

## Scan 19 — documented retained Tamil phrase

`அடுத்தூர்வது அஃதொப்பதில்` remains visible in Tamil with a translation note. The earlier speculative English expansion was withdrawn. Do not import an external Kural translation or another commentator to force a reading.

## Scan 20 — quoted Kural examples

Kurals **1101, 1098 and 17** and their adjacent Kalaignar explanations remain project translations based on this archived Tamil source. No published English Kural wording was substituted.

# Part 002 English — NOT STARTED

Tamil source: `திருக்குறள்_கலைஞர்_உரை_part_002_pages_21-41.pdf`

Tamil state: **21/21 verified; ARCHIVAL-READY**.

Part 002 structure:

- scans 21–26 — Professor Ma. Nannan's `மதிப்புரை` / **Critical Appreciation** continuation and completion;
- scan 27 — `பதிப்புரை` / **Publisher's Note**;
- scans 28–29 — `திருக்குறள் அதிகார அகர வரிசை` / alphabetical chapter index;
- scans 30–31 — `அதிகார அருஞ்சொற்பொருள் அகரவரிசை` / chapter-term glossary index;
- scan 32 — `திருக்குறள் / கலைஞர் உரை / அறம்` section title;
- scan 33 — blank / reverse-side bleed-through;
- scans 34–35 — `1. வழிபாடு`, Kural 1–10;
- scans 36–37 — `2. வான் சிறப்பு`, Kural 11–20;
- scans 38–39 — `3. நீத்தார் பெருமை`, Kural 21–30;
- scans 40–41 — `4. அறன் வலியுறுத்தல்`, Kural 31–40.

# Next exact activity

Begin **Part 002 English first-pass translation with scans 21–27**.

1. Fetch Tamil archival files:
   - `works/thirukkural/pages/0021-mathippurai-08.md`
   - `0022-mathippurai-09.md`
   - `0023-mathippurai-10.md`
   - `0024-mathippurai-11.md`
   - `0025-mathippurai-12.md`
   - `0026-mathippurai-13.md`
   - `0027-pathippurai.md`.
2. Create matching English files under `works/thirukkural/translations/en/pages/`.
3. Use `status: "draft"` for these newly translated pages.
4. Preserve source paragraph / heading / numbered-item structure and all source-specific terminology.
5. Continue Part 001 controlled glossary terms where the same concepts recur.
6. Add or revise glossary entries only where the audited Part 002 source genuinely introduces a new or contextually different term.
7. Do not import external English Kural wording, another Tamil edition, web text or outside commentary.
8. After scans 21–27 drafts are complete, synchronize English translation status and documentation before proceeding to scans 28–33.

## Source authority rule

The supplied scans remain the controlling sources. The project English translation must preserve the meaning and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
