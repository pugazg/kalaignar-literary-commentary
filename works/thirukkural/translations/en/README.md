# Thirukkural — Kalaignar's Commentary — English project translation

This directory contains the **project-created English translation layer** for the archived Tamil source `திருக்குறள் — கலைஞர் உரை`.

## Important status statement

This is **not being presented as an official or publisher-issued English edition** of Kalaignar's commentary.

Unless a separately published English source is later supplied and archived independently, every English page under this directory is identified as:

`translation_type: "project_translation"`

The supplied Tamil scan remains the ultimate controlling source; the audited Tamil archival record is the working translation basis.

## Authority order

1. exact supplied Tamil scan;
2. corresponding verified/audited Tamil archival page;
3. `TRANSLATION_GUIDE.md` and `GLOSSARY.md`;
4. project translation notes created during review.

Do not silently import wording from an existing English Thirukkural translation, another Tamil edition, another commentator, or a web text.

## One-to-one page alignment

English page files mirror Tamil filenames exactly under `translations/en/pages/`.

## Translation statuses

- `draft` — first complete English rendering exists;
- `source-checked` — English has been checked line/paragraph-wise against the audited Tamil source record;
- `editorial-reviewed` — fidelity, terminology, consistency and English readability review completed;
- `release-ready` — final page-level review completed and included in the part-level release report;
- `source-limited` — English completeness is limited because the controlling Tamil source itself is partial;
- `blocked` — translation cannot safely proceed for a documented reason.

A page must not jump directly from `draft` to `release-ready`.

## Current Tamil source readiness

- Part 001 — audited / archival-ready, with scan 8 documented partial;
- Part 002 — audited / archival-ready;
- Part 003 — audited / archival-ready.

The currently archived main-body Tamil reaches Kural **145**.

## English progress

Translation framework: **established**.

### Part 001 first-pass translation — COMPLETE

Part 001 now has **20/20 aligned English page records**:

- scans **1–7** — `draft`;
- scan **8** — `source-limited`;
- scans **9–20** — `draft`.

Current Part 001 English totals:

- `draft`: **19**;
- `source-limited`: **1**;
- `source-checked`: **0**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**.

Scans 13–20 complete the first-pass translation of Professor Ma. Nannan's `மதிப்புரை` / **Critical Appreciation**, including `Need`, `Worship`, `Following a Woman's Lead`, `Oozh`, and the opening discussion of the commentary's various literary merits.

The scan-20 Kural examples were translated from this project's audited Tamil source rather than copied from a published English Thirukkural.

Review-sensitive terms remain intentionally provisional and visible in `GLOSSARY.md`, including **Muppaal**, **Tiruvidam**, **Oozh**, **Following a Woman's Lead**, ***pirithu mozhithal***, and the three literary headings rendered as **Poetic Quality**, **Excellence of Poetic Figure**, and **Excellence of Epithets**.

Scan 8 remains `source-limited`; its unreadable handwritten body has not been reconstructed.

See:

- [`TRANSLATION_GUIDE.md`](TRANSLATION_GUIDE.md)
- [`GLOSSARY.md`](GLOSSARY.md)
- [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md)

## Next activity

Begin the dedicated **Part 001 English source-check cycle with scans 1–7**. Compare each draft with the audited Tamil page for completeness and fidelity, correct only source-supported translation issues, and promote a page to `source-checked` only after that comparison is complete. Editorial consistency review remains a later separate stage.