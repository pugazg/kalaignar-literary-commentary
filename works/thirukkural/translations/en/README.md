# Thirukkural — Kalaignar's Commentary — English project translation

This directory contains the **project-created English translation layer** for the archived Tamil source `திருக்குறள் — கலைஞர் உரை`.

## Important status statement

This is **not being presented as an official or publisher-issued English edition** of Kalaignar's commentary.

Unless a separately published English source is later supplied and archived as its own source-controlled edition, every English page under this directory must be identified as:

`translation_type: "project_translation"`

The translation is produced from the repository's audited Tamil transcription, while the **supplied Tamil scan remains the ultimate controlling source** if any discrepancy is discovered.

## Authority order

For this project translation, use the following authority order:

1. exact supplied Tamil scan;
2. corresponding verified Tamil archival page in `works/thirukkural/pages/`;
3. this translation guide and controlled glossary;
4. project translation notes created during review.

Do **not** silently import wording from an existing English Thirukkural translation, another Tamil edition, another commentator, or a web text.

## One-to-one page alignment

English page files must mirror the Tamil archival page filenames exactly:

```text
works/thirukkural/pages/0034-aram-vazhipadu-01.md
works/thirukkural/translations/en/pages/0034-aram-vazhipadu-01.md
```

This keeps scan, Tamil transcription and English translation permanently alignable.

## Translation-file front matter

Use this pattern:

```yaml
---
source_scan_page: 34
source_tamil_file: "../../../pages/0034-aram-vazhipadu-01.md"
work: "thirukkural"
language: "en"
translation_type: "project_translation"
status: "draft"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
---
```

For Part 001 scan 8, whose Tamil archival record is deliberately `partial`, use `status: "source-limited"` and translate only what the Tamil source review has safely established. Never reconstruct the unreadable handwriting in English.

## Translation statuses

- `draft` — first complete English rendering exists;
- `source-checked` — English has been checked line/paragraph-wise against the verified Tamil source record;
- `editorial-reviewed` — fidelity, terminology, consistency and English readability review completed;
- `release-ready` — final page-level review completed and included in the part-level release report;
- `source-limited` — English completeness is limited because the controlling Tamil source itself is partial;
- `blocked` — translation cannot safely proceed for a documented reason.

A page must not jump directly from `draft` to `release-ready`.

## What is translated

Where present in the archived Tamil page, translate:

- titles and section headings;
- Kural text;
- Kalaignar's commentary;
- prefaces, forewords, reviews and publisher's notes;
- contents/index explanatory material when useful for a complete English archival layer.

Non-text artefacts, bleed-through and unreadable handwriting are described or left source-limited; they are not invented as English prose.

## Verse/commentary separation

The English rendering of each Kural and the English translation of Kalaignar's commentary must remain visibly separate. Do not replace the Kural translation with a prose summary of the commentary.

Where the compressed Tamil verse permits more than one English reading, use Kalaignar's own adjacent commentary as the first interpretive aid and record a translation note if the choice is materially interpretive. Do not import a different commentator's interpretation without an explicit research task.

## Current Tamil source readiness

- Part 001 — audited / archival-ready, with scan 8 documented partial;
- Part 002 — audited / archival-ready;
- Part 003 — audited / archival-ready.

The currently archived main-body Tamil reaches Kural **145**.

## English progress

Translation framework: **established**.

Page translation: **not yet started**.

See:

- [`TRANSLATION_GUIDE.md`](TRANSLATION_GUIDE.md)
- [`GLOSSARY.md`](GLOSSARY.md)
- [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md)

## Next activity

Begin **Part 001 English translation** in small page-aligned batches. Start with scans **1–7**, create matching English page files, and keep them `draft` until the separate source-check pass.