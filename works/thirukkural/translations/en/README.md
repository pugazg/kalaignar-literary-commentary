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

Part 001 has **20/20 aligned English records**:

- scans **1–7**: `source-checked`;
- scan **8**: `source-limited`;
- scans **9–20**: `draft`.

No page has yet undergone the later editorial-consistency stage.

### Source-check scans 1–7

The first source-check batch is complete. Scans 1–5 required no translation-text changes. Scan 6 now uses the controlled title **The Professor's Foreword**. The Preface on scan 7 was tightened to restore source meaning in `நிறைவேற்றி மகிழ்`, `உண்மை நிலை`, and `இனமான ஏந்தல்`, while preserving Kalaignar's distinction between **Invocation to God** and **Worship**.

Scan 8 remains intentionally source-limited and is not to be reconstructed from uncertain handwriting.

See:

- [`TRANSLATION_GUIDE.md`](TRANSLATION_GUIDE.md)
- [`GLOSSARY.md`](GLOSSARY.md)
- [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md)

## Next activity

Review scan **8** against the partial Tamil archival record as a source-limited alignment check. Keep it `source-limited`; translate no uncertain handwriting. Then continue source-checking scans **9–12**.
