# Thirukkural — Kalaignar's Commentary — English project translation

This directory contains the **project-created English translation layer** for the archived Tamil source `திருக்குறள் — கலைஞர் உரை`.

This is **not an official or publisher-issued English edition**. Every English page carries `translation_type: "project_translation"`.

Authority order:

1. supplied Tamil scan;
2. verified/audited Tamil archival page;
3. `TRANSLATION_GUIDE.md` and `GLOSSARY.md`;
4. project translation/review notes.

Do not import a published English Thirukkural translation, another Tamil edition, another commentator or web text.

## Translation fidelity

The English should retain the source author's language, images, emphases and interpretive direction as closely as clear English allows. Kalaignar's commentary must remain Kalaignar's commentary: a familiar conventional interpretation must never replace what he actually says merely because it sounds more standard in English.

## Status model

- `draft` — first complete English rendering;
- `source-checked` — compared against the audited Tamil page;
- `editorial-reviewed` — consistency/readability/glossary review complete;
- `release-ready` — part-level release gate complete;
- `source-limited` — completeness limited by controlling source;
- `blocked` — safe translation cannot proceed.

## Part 001 — RELEASE COMPLETE

- aligned English records: **20 / 20**;
- `release-ready`: **19**;
- `source-limited`: **1** — scan 8 handwritten facsimile.

## Part 002 — RELEASE COMPLETE

- aligned English records: **21 / 21**;
- `release-ready`: **21** — scans 21–41.

## Part 003 — EDITORIAL REVIEW COMPLETE

Tamil scans **42–62** are audited / archival-ready and cover Kural **41–145** with Kalaignar's commentary.

Current English state:

- aligned English records: **21 / 21** — scans 42–62;
- `editorial-reviewed`: **21** — scans 42–62;
- `source-checked`: **0**;
- `draft`: **0**;
- `release-ready`: **0**.

Formal review artefact:

- [`reviews/PART_003_REVIEW.md`](reviews/PART_003_REVIEW.md)

The editorial review preserves all source-sensitive Kalaignar decisions established during source-check. It also finalized chapter headings 5–15, reconciled glossary terms, verified repeated Kural wording against released Part 002 occurrences, and made only small readability/pronoun corrections that do not alter source meaning.

Examples explicitly retained include Kural 42 **those without protection**, Kural 55's slave/rain interpretation, Kural 58 **new world**, Kural 77 **conscience**, Kural 86 **heaven of fame**, Kural 87 hospitality-as-**sacrifice**, Kural 121's deathless/darkness verse versus **imperishable fame / life itself dark** commentary, Kural 126's **seven lives** versus protection **through all time**, Kural 130's **Aram waiting upon the path**, explicit birth/lineage and **Brahmin** language in Kurals 133–134, and **another man's wife** in the supplied Kural 141–145 material.

See [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md) and [`reviews/PART_003_REVIEW.md`](reviews/PART_003_REVIEW.md) for detailed decisions.

## Next activity

Run the separate **Part 003 English release gate**. Verify all 21 editorial-reviewed pages, metadata, glossary alignment, repeated-Kural consistency and source-fidelity decisions; create `reviews/PART_003_RELEASE_REPORT.md`; and promote pages to `release-ready` only if the gate passes.

Do not begin Part 004 English work in the same activity.
