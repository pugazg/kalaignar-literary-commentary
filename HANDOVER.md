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

- aligned English records: **20 / 20**;
- `release-ready`: **19** — scans 1–7 and 9–20;
- `source-limited`: **1** — scan 8;
- release decision: **RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS**.

Do not silently revise released Part 001 wording because later Part 002 context appears. Any cross-part change must follow source-check/editorial review and be explicitly documented.

# Part 002 English — FIRST PASS COMPLETE

Tamil source: `திருக்குறள்_கலைஞர்_உரை_part_002_pages_21-41.pdf`

Tamil state: **21/21 verified; ARCHIVAL-READY**.

Current English state:

- aligned English records: **21 / 21**;
- `draft`: **21**;
- `source-checked`: **0**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

## Completed first-pass coverage

### Scans 21–27

- completion of Professor Ma. Nannan's **Critical Appreciation**;
- **Publisher's Note**.

### Scans 28–33

- **Alphabetical Index of Chapters**;
- **Alphabetical Glossary of Chapter Terms**;
- `Thirukkural / Kalaignar's Commentary / Aram` section-title page;
- blank verso / reverse-side bleed-through page condition.

### Scans 34–41 — Kural 1–40

- scans 34–35 — `1. வழிபாடு` → **Worship**, Kural 1–10;
- scans 36–37 — `2. வான் சிறப்பு` → **The Excellence of Rain**, Kural 11–20;
- scans 38–39 — `3. நீத்தார் பெருமை` → **The Greatness of Renunciants**, Kural 21–30;
- scans 40–41 — `4. அறன் வலியுறுத்தல்` → **Affirming Aram**, Kural 31–40.

All 21 English records remain `status: "draft"`. Kural number and two-line structure are preserved, with Kalaignar's commentary translated separately. No published English Thirukkural translation, another Tamil edition, web text or outside commentary was imported.

## Main-body draft consistency

- Kural **17** uses the same project wording already released in Part 001 scan 20, with matching Kalaignar commentary.
- Kural **29** and Kural **37** reuse the wording already drafted in Part 002's Critical Appreciation examples.

## Review-sensitive Part 002 items

### Scan 25 / `அடுத்தூர்வது அஃதொப்பதில்`

The complete Kural is now present in Part 002. Its draft second line is **“nothing equals pressing forward to meet it.”** Part 001 scan 19 remains unchanged until Part 002 source-check and later editorial review establish whether a cross-part revision is justified.

### Scan 26 / `மக்கள் நெஞ்சின் மலிவுப் பதிப்பு`

The compressed Tamil metaphor is retained visibly with a contextual gloss. Recheck during source-check/editorial review.

### Scans 27 and 32 pagination

- scan 27 `xxvi` is a same-source pagination inference;
- scan 32 `xxxi` is supported by the Part 001 contents entry and surrounding sequence.

The numerals are not visibly printed on those scans; preserve the metadata basis.

### Main-body terminology / interpretation

Recheck deliberately during source-check:

- Kural 1 / `ஆதி பகவன்` — draft retains **Aadhi Bhagavan** rather than importing a doctrinal English title;
- Kurals 5 and 10 / `இறைவன்` — drafts follow Kalaignar's adjacent non-doctrinal explanatory direction;
- Kurals 8 and 30 / `அந்தணர்` — drafts use `anthanar` / worthy people according to Kalaignar's explanation, not an outside caste/religious definition;
- Kural 25 — retain and check Kalaignar's explicit Indra example concerning inability/control of the senses;
- Kural 38 — check the interpretation of `வாழ்நாள் வழியடைக்கும் கல்` against Kalaignar's commentary, where the good deeds are described as a stone that shapes/sets the life-path in order.

# Part 003 English — NOT STARTED

Tamil scans 42–62 are audited / archival-ready and contain Kural 41–145 plus Kalaignar commentary. Do not start Part 003 English until Part 002 completes source-check, editorial review and release gate.

# Next exact activity

Begin the dedicated **Part 002 English source-check with scans 21–27**.

1. Fetch the current English drafts and their exact verified Tamil source files for scans 21–27.
2. Compare each page directly, paragraph-by-paragraph / verse-by-verse, for omissions, additions, agency reversal, meaning drift, headings, quotations and metadata.
3. Correct only source-supported English fidelity issues.
4. Promote a page from `draft` to `source-checked` only after the direct comparison is complete.
5. On scan 25, re-evaluate the complete Kural containing `அடுத்தூர்வது அஃதொப்பதில்`; do **not** revise released Part 001 scan 19 in this same source-check activity.
6. Recheck scan 26's `மக்கள் நெஞ்சின் மலிவுப் பதிப்பு` treatment and scan 27's inferred `xxvi` metadata.
7. Keep terminology decisions provisional where source-check alone cannot settle an editorial preference.
8. After scans 21–27 source-check is complete, synchronize `TRANSLATION_STATUS.md`, English README, work README, root README and this handover.
9. The next source-check batch after that should continue with scans **28–33**, then **34–41**.
10. Do not begin Part 002 editorial consistency review until all 21 pages are `source-checked`.

## Source authority rule

The supplied scans remain the controlling sources. The project English translation must preserve the meaning and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
