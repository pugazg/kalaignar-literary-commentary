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

Scan 8 remains source-limited and unreconstructed. Part 001 scan 19 deliberately retains `அடுத்தூர்வது அஃதொப்பதில்` in Tamil; later Part 002 context does not silently alter that released record.

### Part 002 — FIRST PASS IN PROGRESS

Part 002 now has **13/21 aligned English drafts**, covering scans **21–33**.

- scans **21–26** — completion of Professor Ma. Nannan's **Critical Appreciation**;
- scan **27** — **Publisher's Note**;
- scans **28–29** — **Alphabetical Index of Chapters**;
- scans **30–31** — **Alphabetical Glossary of Chapter Terms**;
- scan **32** — **Thirukkural / Kalaignar's Commentary / Aram** section-title page;
- scan **33** — blank verso / reverse-side bleed-through only.

Current Part 002 counts:

- `draft`: **13**
- `source-checked`: **0**
- `editorial-reviewed`: **0**
- `release-ready`: **0**
- `source-limited`: **0**
- `blocked`: **0**

The index records preserve source entry order and chapter numbers. Existing controlled titles are reused; English titles newly introduced by the full 133-chapter index remain first-pass renderings until Part 002 source-check/editorial review. The chapter-term glossary pages translate the source's own glosses rather than replacing them with definitions from another edition.

Review-sensitive index/glossary decisions remain explicit. `வழிபாடு` is still the controlled title **Worship**, while the source glossary explains it as `பின்பற்றுதல்` / **Following**. `பெண்வழிச் சேறல்` remains **Following a Woman's Lead**, while the source gloss is drafted as **becoming obsessed with women**. `வரைவின் மகளிர்` is provisionally **Women Beyond Bounds**, with the source gloss `விலை மகளிர்` translated directly as **Women for hire**; that title wording is not yet settled.

Scan 32 preserves inferred printed page **xxxi** with the same-source basis documented in metadata. Scan 33 records only the absence of distinct printed text and faint reverse-side bleed-through; no bleed-through text is transcribed or translated.

Earlier Part 002 review-sensitive items also remain open: scan 25's provisional rendering of the complete Kural containing `அடுத்தூர்வது அஃதொப்பதில்`, scan 26's retained `மக்கள் நெஞ்சின் மலிவுப் பதிப்பு`, and scan 27's inferred printed page **xxvi**.

See:

- [`TRANSLATION_GUIDE.md`](TRANSLATION_GUIDE.md)
- [`GLOSSARY.md`](GLOSSARY.md)
- [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md)

## Next activity

Complete the **Part 002 first-pass translation with scans 34–41**, covering Kural **1–40** and Kalaignar's commentary:

- scans 34–35 — **Worship**, Kural 1–10;
- scans 36–37 — **The Excellence of Rain**, Kural 11–20;
- scans 38–39 — **The Greatness of Renunciants**, Kural 21–30;
- scans 40–41 — **Affirming Aram**, Kural 31–40.

Create all eight aligned English files as `draft`, preserve each Kural's two-line structure, translate Kalaignar's commentary separately, and do not substitute published English Thirukkural wording. Part 002 source-check begins only after the first pass reaches 21/21.
