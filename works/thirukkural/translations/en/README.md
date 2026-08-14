# Thirukkural — Kalaignar's Commentary — English project translation

This directory contains the **project-created English translation layer** for the archived Tamil source `திருக்குறள் — கலைஞர் உரை`.

## Important status statement

This is **not being presented as an official or publisher-issued English edition** of Kalaignar's commentary.

Unless a separately published English source is later supplied and archived as its own source-controlled edition, every English page under this directory must be identified as:

`translation_type: "project_translation"`

The translation is produced from the repository's audited Tamil transcription, while the **supplied Tamil scan remains the ultimate controlling source** if any discrepancy is discovered.

## Authority order

1. exact supplied Tamil scan;
2. corresponding verified/audited Tamil archival page in `works/thirukkural/pages/`;
3. `TRANSLATION_GUIDE.md` and `GLOSSARY.md`;
4. project translation notes created during review.

Do **not** silently import wording from an existing English Thirukkural translation, another Tamil edition, another commentator, or a web text.

## One-to-one page alignment

English page files mirror the Tamil archival page filenames exactly:

```text
works/thirukkural/pages/0034-aram-vazhipadu-01.md
works/thirukkural/translations/en/pages/0034-aram-vazhipadu-01.md
```

## Translation statuses

- `draft` — first complete English rendering exists;
- `source-checked` — English has been checked line/paragraph-wise against the verified Tamil source record;
- `editorial-reviewed` — fidelity, terminology, consistency and English readability review completed;
- `release-ready` — final page-level review completed and included in the part-level release report;
- `source-limited` — English completeness is limited because the controlling Tamil source itself is partial;
- `blocked` — translation cannot safely proceed for a documented reason.

A page must not jump directly from `draft` to `release-ready`.

## Translation method

Where present in the archived Tamil page, translate titles, Kural text, Kalaignar's commentary, prefaces, forewords, reviews, publisher's notes, and useful contents/index material. Kural and commentary layers remain visibly separate.

The English may use natural syntax, but must not modernize Kalaignar's interpretation, harmonize him with another commentator, or repair unusual Tamil by substitution from another edition.

For Part 001 scan 8, whose Tamil archival record is deliberately `partial`, the aligned English record uses `status: "source-limited"` and does not reconstruct the unreadable handwriting.

## Current Tamil source readiness

- Part 001 — audited / archival-ready, with scan 8 documented partial;
- Part 002 — audited / archival-ready;
- Part 003 — audited / archival-ready.

The currently archived main-body Tamil reaches Kural **145**.

## English progress

Translation framework: **established**.

Part 001 English production now has **12 aligned page records**:

- scans **1–7**: `draft`;
- scan **8**: `source-limited`;
- scans **9–12**: `draft`;
- scans **13–20**: not yet translated;
- no page has yet completed the separate source-check or editorial-review stages.

### Scans 9–12 — The Professor's Foreword

The four-page poetic foreword by **K. Anbazhagan** is now present as a first-pass English draft. The translation preserves the source's poem-like line structure, quotations, repeated rhetorical emphasis and highlighted lines rather than reducing the text to prose.

A source-sensitive note is carried on scan 10 because the verified Tamil source reads `திருவிடம்`; the English draft therefore retains **Tiruvidam** instead of silently substituting a different Tamil form. `முப்பால்` is provisionally retained as **Muppaal**, and `ஊழ்` as **oozh**, pending the dedicated source-check/editorial review.

See:

- [`TRANSLATION_GUIDE.md`](TRANSLATION_GUIDE.md)
- [`GLOSSARY.md`](GLOSSARY.md)
- [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md)

## Next activity

Create Part 001 English first-pass `draft` files for **scans 13–20**, covering `மதிப்புரை` / Critical Appreciation and the remaining literary-analysis front matter.

Preserve source headings, quotations, Kural references, paragraph structure and emphasis. Review/promotion remains a separate later activity.
