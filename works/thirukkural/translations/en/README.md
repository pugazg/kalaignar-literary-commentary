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

Final state:

- scans **1–7**: `release-ready`;
- scan **8**: `source-limited`;
- scans **9–20**: `release-ready`.

Counts:

- `release-ready`: **19**
- `source-limited`: **1**
- `editorial-reviewed`: **0**
- `source-checked`: **0**
- `draft`: **0**
- `blocked`: **0**

Release decision: **RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS**.

Review artefacts:

- [`reviews/PART_001_REVIEW.md`](reviews/PART_001_REVIEW.md)
- [`reviews/PART_001_RELEASE_REPORT.md`](reviews/PART_001_RELEASE_REPORT.md)

### Documented source limitations

Scan 8 remains `source-limited` because its continuous handwritten body is not securely readable in the controlling Tamil facsimile. The English record does not reconstruct it.

On scan 19, `அடுத்தூர்வது அஃதொப்பதில்` remains intentionally in Tamil with a translation note because the audited source does not establish a sufficiently secure English expansion. This is a documented editorial retention, not a hidden omission.

The scan-20 Kural examples **1101, 1098 and 17** remain project translations from this archived Tamil source; no published English Kural wording has been substituted.

### Controlled terminology

Part 001 release retains the reviewed treatment of **Muppaal**, source-specific **Tiruvidam**, **Oozh / oozh**, **counsel** for `வாயுறை`, **Following a Woman's Lead**, ***pirithu mozhithal***, and the scan-20 literary headings. The distinction between **Invocation to God** and **Worship** remains mandatory.

See:

- [`TRANSLATION_GUIDE.md`](TRANSLATION_GUIDE.md)
- [`GLOSSARY.md`](GLOSSARY.md)
- [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md)
- [`reviews/PART_001_REVIEW.md`](reviews/PART_001_REVIEW.md)
- [`reviews/PART_001_RELEASE_REPORT.md`](reviews/PART_001_RELEASE_REPORT.md)

## Next activity

Begin **Part 002 English first-pass translation with scans 21–27**: the remaining pages of Professor Ma. Nannan's **Critical Appreciation** followed by the **Publisher's Note**. Create matching English records as `draft` and continue the Part 001 controlled glossary unless new source context requires a documented addition or revision.
