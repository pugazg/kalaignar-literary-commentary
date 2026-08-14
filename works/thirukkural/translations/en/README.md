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

Part 001 has **20/20 aligned English records** and has completed both source-check and editorial-consistency review:

- scans **1–7**: `editorial-reviewed`;
- scan **8**: `source-limited`, with source-limited alignment and editorial consistency checks complete;
- scans **9–20**: `editorial-reviewed`.

Current counts:

- `editorial-reviewed`: **19**
- `source-limited`: **1**
- `source-checked`: **0**
- `draft`: **0**
- `release-ready`: **0**

Review artefact:

- [`reviews/PART_001_REVIEW.md`](reviews/PART_001_REVIEW.md)

### Editorial decisions now controlled for Part 001

The review finalized the current treatment of **Muppaal**, source-specific **Tiruvidam**, **Oozh / oozh**, `வாயுறை` → **counsel**, **Following a Woman's Lead**, ***pirithu mozhithal***, and the scan-20 literary headings. It also confirms that `அடுத்தூர்வது அஃதொப்பதில்` remains intentionally in Tamil because the audited source does not support a sufficiently secure English expansion.

The distinction between **Invocation to God** and **Worship** remains mandatory. The scan-20 Kural examples 1101, 1098 and 17 remain project translations from this archived Tamil edition; no published English Kural wording has been substituted.

Scan 8 remains `source-limited`; its unreadable continuous handwriting is not reconstructed.

See:

- [`TRANSLATION_GUIDE.md`](TRANSLATION_GUIDE.md)
- [`GLOSSARY.md`](GLOSSARY.md)
- [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md)
- [`reviews/PART_001_REVIEW.md`](reviews/PART_001_REVIEW.md)

## Next activity

Create the separate **Part 001 English release report** at `reviews/PART_001_RELEASE_REPORT.md`. Verify all 20 aligned records, the 19 `editorial-reviewed` pages, scan 8's continuing `source-limited` status, glossary/review consistency, and the documented unresolved Tamil phrase on scan 19. Only after the release gate passes should eligible pages be promoted to `release-ready`.
