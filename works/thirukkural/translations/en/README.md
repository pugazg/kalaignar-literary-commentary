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
- scan **8**: `source-limited`, with source-limited alignment check complete;
- scans **9–12**: `source-checked`;
- scans **13–20**: `draft`.

Current counts:

- `source-checked`: **11**
- `source-limited`: **1**
- `draft`: **8**
- `editorial-reviewed`: **0**
- `release-ready`: **0**

### Source-check scans 9–12 — The Professor's Foreword

K. Anbazhagan's four-page poetic foreword has now completed the source-check stage. Scan 9 received one fidelity tightening in the line corresponding to `சிறப்பொவ்வா செய்தொழில் வேற்றுமையான்`; scan 10 clarified the reference to the ten commentators. Scans 11–12 required no translation-text correction.

Source-sensitive forms remain deliberately reviewable rather than normalized:

- **Muppaal** for `முப்பால்`;
- **Tiruvidam** for the verified source form `திருவிடம்`;
- **oozh** where the poem explicitly names `ஊழ்`;
- **counsel** provisionally for `வாயுறை`, with final poetic nuance deferred to editorial review.

Scan 8 remains `source-limited`; its unreadable continuous handwriting is not reconstructed.

See:

- [`TRANSLATION_GUIDE.md`](TRANSLATION_GUIDE.md)
- [`GLOSSARY.md`](GLOSSARY.md)
- [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md)

## Next activity

Source-check Part 001 scans **13–20**, covering Professor Ma. Nannan's **Critical Appreciation**. Compare each English draft directly with its audited Tamil page, preserve the quoted Kural examples from this source, and keep editorial-consistency review as the next separate stage.
