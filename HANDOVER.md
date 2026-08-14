# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. The English layer is a **project-created translation**, not an official/publisher English edition, and must not import external English Kural wording or another commentator's interpretation.

## English fidelity rule — MANDATORY

The translation must retain **Kalaignar's own language, images, emphases and interpretive direction** as closely as clear English allows. Do not replace his explanation with the familiar or conventional interpretation of a Kural. If Kalaignar deliberately reads a term in a particular way, the English must translate that reading, not correct it toward another commentator.

The same source-fidelity rule applies to Professor Nannan and publisher prose. Do not silently smooth away metaphors, repetition, rhetoric or source-specific terminology merely because a more conventional English phrase is available.

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
- `source-checked`: **7** — scans 21–27;
- `draft`: **14** — scans 28–41;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

## Source-check completed — scans 21–27

Each English page was compared directly with its verified Tamil record. Source-supported changes only:

- **scan 21** — removed the first-pass addition that Kalaignar's commentary has the “compactness” of a Kural. `பாட்டும் குறள்; ... உரையும் குறளாக அமைந்திருப்பது` is now represented simply as the verse being a Kural and Kalaignar's commentary itself being formed as a Kural.
- **scan 22** — `நேர்மை பிறழாப் புதுமை` is now kept closer to the source as **“innovation that does not depart from fidelity”**, instead of “unfailing originality and integrity.”
- **scan 23** — Kural 58 now uses **“If women obtain a husband worthy of being obtained...”**, guided by Kalaignar's immediately adjacent explanation while keeping verse and commentary separate.
- **scan 24** — no source-fidelity correction required.
- **scan 25** — the draft **“pressing forward to meet it”** for `அடுத்தூர்வது அஃதொப்பதில்` added an image not securely demanded by this source. The source-checked full-Kural line is now **“nothing equals that for driving it away.”** Part 001 scan 19 remains unchanged in this batch.
- **scan 26** — the source metaphor `மக்கள் நெஞ்சின் மலிவுப் பதிப்பு` is no longer softened into “an edition readily accessible to the people's hearts.” It is retained closely as **“the low-priced edition of the people's hearts”**, with a source-check note. This awkwardness is intentional at the fidelity stage; editorial review may later consider wording only if the source image remains intact.
- **scan 27** — text required no correction. `printed_page: "xxvi"` remains explicitly marked as inferred from the contents / surrounding same-source sequence; the numeral is not visible on the scan.

## Released Part 001 / later context

Part 002 now gives fuller context for `அடுத்தூர்வது அஃதொப்பதில்`, but **do not revise Part 001 scan 19 during source-check**. Any cross-part revision must be made during a separately documented editorial consistency decision after Part 002 source-check is complete.

# Remaining Part 002 source-check

- scans 28–33 — index, chapter-term glossary, Aram title page, blank verso;
- scans 34–41 — Kural 1–40 + Kalaignar commentary.

For scans 34–41, special attention is required for preserving Kalaignar's own reading of:

- Kural 1 / `ஆதி பகவன்`;
- Kurals 5 and 10 / `இறைவன்`;
- Kurals 8 and 30 / `அந்தணர்`;
- Kural 25 / Indra;
- Kural 38 / `வாழ்நாள் வழியடைக்கும் கல்`.

Do not replace those with conventional external interpretations.

# Part 003 English — NOT STARTED

Tamil scans 42–62 are audited / archival-ready and contain Kural 41–145 plus Kalaignar commentary. Do not start Part 003 English until Part 002 completes source-check, editorial review and release gate.

# Next exact activity

Continue the dedicated **Part 002 English source-check with scans 28–33**.

1. Fetch the current English records and exact verified Tamil source files for scans 28–33.
2. Compare every index/glossary entry for omissions, numbering errors, meaning drift and over-normalized chapter-title wording.
3. Preserve the source's own `அருஞ்சொற்பொருள்` explanations rather than replacing them with standard definitions from another edition.
4. Confirm scan 32 retains `printed_page: "xxxi"` only as the documented same-source inference; numeral not visible on scan.
5. Confirm scan 33 remains a blank / reverse-side bleed-through record only.
6. Promote each completed page to `source-checked`.
7. Do not begin scans 34–41 source-check until 28–33 are complete and documentation is synchronized.
8. Do not begin Part 002 editorial consistency review until all 21 Part 002 records are source-checked.

## Source authority rule

The supplied scans remain the controlling sources. The project English translation must preserve the meaning, voice and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
