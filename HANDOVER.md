# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. The English layer is a **project-created translation**, not an official/publisher English edition, and must not import external English Kural wording or another commentator's interpretation.

## English fidelity rule — MANDATORY

The translation must retain **Kalaignar's own language, images, emphases and interpretive direction** as closely as clear English allows. Do not replace his explanation with the familiar or conventional interpretation of a Kural. If Kalaignar deliberately reads a term in a particular way, the English must translate that reading, not correct it toward another commentator.

The same source-fidelity rule applies to Professor Nannan, publisher prose, indexes and source glossaries. Do not silently smooth away or normalize metaphors, repetition, rhetoric, definitions or source-specific terminology merely because a more conventional English phrase is available.

Natural English syntax is allowed. Source meaning and voice outrank elegance.

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

- aligned English records: **20 / 20**;
- `release-ready`: **19** — scans 1–7 and 9–20;
- `source-limited`: **1** — scan 8;
- release decision: **RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS**.

Do not silently revise released Part 001 wording because later Part 002 context appears. Any cross-part change must follow source-check/editorial review and be explicitly documented.

# Part 002 English — FIRST PASS COMPLETE / SOURCE-CHECK IN PROGRESS

Tamil source: `திருக்குறள்_கலைஞர்_உரை_part_002_pages_21-41.pdf`

Tamil state: **21/21 verified; ARCHIVAL-READY**.

Current English state:

- aligned English records: **21 / 21**;
- `source-checked`: **13** — scans 21–33;
- `draft`: **8** — scans 34–41;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

## Source-check completed — scans 21–27

Fidelity-first corrections include restoring Nannan's source metaphors and removing unsupported interpretive additions. Scan 25 now uses **“nothing equals that for driving it away”** for the full Kural containing `அடுத்தூர்வது அஃதொப்பதில்`; scan 26 preserves `மக்கள் நெஞ்சின் மலிவுப் பதிப்பு` closely as **“the low-priced edition of the people's hearts.”** Released Part 001 scan 19 remains unchanged at this stage.

## Source-check completed — scans 28–33

All six English pages were compared against their verified Tamil records and promoted to `source-checked`.

Source-supported decisions:

- scan 28 — source order and chapter numbers verified; `அருளுடைமை` corrected from **Compassionate Conduct** to **Possession of Compassion**, avoiding the added idea of conduct;
- scan 29 — source order and numbers verified; `புல்லறிவாண்மை` → **Possession of Little Understanding** and `நெஞ்சொடு புலத்தல்` → **Sulking with the Heart**, guided by this edition's own explanatory glossary;
- scan 30 — this edition's own glosses are preserved. `நடுவு நிலைமை | பொதுவாக இருத்தல்` is represented as **Impartiality | Being common to all**, not silently normalized to a conventional definition; `நாணத்தை மீறுதலைக் கூறுதல்` is **Speaking of transgressing modesty**;
- scan 31 — source gloss distinctions remain explicit: `பெண் வழிச் சேறல் | பெண் பித்தராதல்` → **Following a Woman's Lead | Becoming obsessed with women**; `வரைவின் மகளிர் | விலை மகளிர்` retains the gloss **Women for hire**; `வழிபாடு | பின்பற்றுதல்` → **Worship | Following**;
- scan 32 — `printed_page: "xxxi"` remains a same-source pagination inference supported by the Part 001 contents entry and surrounding sequence; the numeral is not visible on the scan;
- scan 33 — blank verso / reverse-side bleed-through only; no bleed-through text is current-page body text.

Do not convert the full index to a standard external English chapter-title list during source-check or editorial review. Any stylistic refinement must remain grounded in this edition and be documented.

# Remaining Part 002 source-check

Only scans **34–41** remain: Kural **1–40** plus Kalaignar commentary.

Special attention is required for preserving Kalaignar's own reading of:

- Kural 1 / `ஆதி பகவன்`;
- Kurals 5 and 10 / `இறைவன்`;
- Kurals 8 and 30 / `அந்தணர்`;
- Kural 25 / Indra;
- Kural 38 / `வாழ்நாள் வழியடைக்கும் கல்`.

Do not replace those with conventional external interpretations.

# Part 003 English — NOT STARTED

Tamil scans 42–62 are audited / archival-ready and contain Kural 41–145 plus Kalaignar commentary. Do not start Part 003 English until Part 002 completes source-check, editorial review and release gate.

# Next exact activity

Complete the dedicated **Part 002 English source-check with scans 34–41**.

1. Fetch the current English drafts and exact verified Tamil source files for scans 34–41.
2. Compare every Kural verse and every Kalaignar commentary paragraph directly for omissions, additions, meaning drift, doctrinal normalization, imagery and metadata.
3. Preserve each Kural number and two-line verse structure.
4. Translate Kalaignar's explanation as **his explanation**. Do not replace it with standard Thirukkural wording or another commentator's reading.
5. Pay special attention to `ஆதி பகவன்`, `இறைவன்`, `அந்தணர்`, Indra and Kural 38's stone/path image.
6. Correct only source-supported fidelity issues.
7. Promote each completed page from `draft` to `source-checked`.
8. After all eight are complete, synchronize status/docs and make the next activity the Part 002 editorial-consistency / glossary-reconciliation review.
9. Do not begin editorial review in the same source-check activity.

## Source authority rule

The supplied scans remain the controlling sources. The project English translation must preserve the meaning, voice and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
