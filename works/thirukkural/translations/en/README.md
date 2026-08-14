# Thirukkural — Kalaignar's Commentary — English project translation

This directory contains the **project-created English translation layer** for the archived Tamil source `திருக்குறள் — கலைஞர் உரை`.

## Important status statement

This is **not an official or publisher-issued English edition** of Kalaignar's commentary. Every English page is identified as:

`translation_type: "project_translation"`

Authority order:

1. exact supplied Tamil scan;
2. corresponding verified/audited Tamil archival page;
3. `TRANSLATION_GUIDE.md` and `GLOSSARY.md`;
4. project translation/review notes.

Do not silently import an existing English Thirukkural translation, another Tamil edition, another commentator, or a web text.

## One-to-one alignment

English page filenames mirror the Tamil archival filenames exactly under `translations/en/pages/`.

## Translation statuses

- `draft` — first complete English rendering exists;
- `source-checked` — compared against the audited Tamil page for omissions, additions and meaning drift;
- `editorial-reviewed` — terminology/readability/consistency review completed;
- `release-ready` — included in a completed part-level English release review;
- `source-limited` — completeness is limited by the controlling Tamil source;
- `blocked` — a documented issue prevents safe translation.

## Current Tamil source readiness

- Part 001 — audited / archival-ready, with scan 8 documented partial;
- Part 002 — audited / archival-ready;
- Part 003 — audited / archival-ready.

The currently archived main-body Tamil reaches Kural **145**.

## English progress

### Part 001 — RELEASE COMPLETE

Part 001 has **20/20 aligned English records** and has completed first pass, source-check, editorial consistency review and release gate.

- `release-ready`: **19** — scans 1–7 and 9–20
- `source-limited`: **1** — scan 8

Release decision: **RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS**.

Review artefacts:

- [`reviews/PART_001_REVIEW.md`](reviews/PART_001_REVIEW.md)
- [`reviews/PART_001_RELEASE_REPORT.md`](reviews/PART_001_RELEASE_REPORT.md)

Scan 8 remains source-limited and unreconstructed. Part 001 scan 19 deliberately retains `அடுத்தூர்வது அஃதொப்பதில்` in Tamil; the Part 001 release is not altered merely because later source context appears.

### Part 002 — FIRST PASS IN PROGRESS

Part 002 now has **7/21 aligned English drafts**, covering scans **21–27**:

- scans **21–26** — completion of Professor Ma. Nannan's **Critical Appreciation**;
- scan **27** — **Publisher's Note**.

Current Part 002 counts:

- `draft`: **7**
- `source-checked`: **0**
- `editorial-reviewed`: **0**
- `release-ready`: **0**
- `source-limited`: **0**
- `blocked`: **0**

New draft terminology from this batch is recorded in [`GLOSSARY.md`](GLOSSARY.md), including **Commentary in Kural Form**, **Grace of Interposed Words**, **Clarity**, **Concise Explanation**, **New Meaning**, **Entirely Fresh Explanation**, **Subtle Penetrating Insight**, and the source-specific `புத்தேளிர்` discussion.

Two items are deliberately marked for later Part 002 review:

- scan 25 supplies the full quoted Kural containing `அடுத்தூர்வது அஃதொப்பதில்`; the current Part 002 rendering **“nothing equals pressing forward to meet it”** is only a first-pass draft and must be source-checked before any cross-part revision;
- scan 26 retains `மக்கள் நெஞ்சின் மலிவுப் பதிப்பு` in Tamil with a contextual gloss because the metaphor does not yet have a settled project equivalent.

Scan 27 preserves printed page **xxvi** as an explicit same-source pagination inference; the numeral is not visibly printed on that scan.

See:

- [`TRANSLATION_GUIDE.md`](TRANSLATION_GUIDE.md)
- [`GLOSSARY.md`](GLOSSARY.md)
- [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md)

## Next activity

Continue **Part 002 first-pass translation with scans 28–33**: the alphabetical chapter index, chapter-term glossary index, `அறம்` section-title page, and blank verso. Create all six aligned English files as `draft`, preserving entry order, numbers, inferred-pagination notes, and blank-page status exactly. The Kural 1–40 translation batch begins only after scans 28–33 are complete.
