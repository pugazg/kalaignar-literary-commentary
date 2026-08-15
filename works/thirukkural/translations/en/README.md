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

## Parts 001–003 — RELEASE COMPLETE

- Part 001: 19 `release-ready` + scan 8 `source-limited`;
- Part 002: **21/21 `release-ready`**;
- Part 003: **21/21 `release-ready`**, through Kural 145.

## Part 004 — EDITORIAL REVIEW COMPLETE

Tamil Part 004 is **ARCHIVAL-READY**, covering scans **63–84 / printed pages 30–51 / Kural 146–255**.

English state:

- aligned English records: **22 / 22**;
- `editorial-reviewed`: **22**;
- `source-checked`: **0**;
- `draft`: **0**;
- `release-ready`: **0**.

The editorial-consistency / glossary-reconciliation review is recorded in:

- [`reviews/PART_004_REVIEW.md`](reviews/PART_004_REVIEW.md)

The review confirms Part 003 → Part 004 continuity, preserves all source-sensitive Kalaignar readings established during source-check, and controls the Part 004 main-body titles through chapter 26. The structural section `துறவறவியல்` is now controlled as **Renunciant Life**.

Four main-body titles deliberately refine the earlier Part 002 index-local wording: **Not Speaking Ill Behind Another's Back**, **Fear of Evil Deeds**, **Understanding Helpfulness**, and **Abstaining from Flesh**. The released index records remain unchanged because those translations are retained as their own index-local layer.

`GLOSSARY.md` now records the controlled main-body extension through Kural 255 and the Part 004 recurring terminology decisions for compassion, *oppuravu* / helpfulness, giving, fame and flesh.

The review made only small readability and consistency edits after source-check; no source-supported metaphor, relationship, social category, or Kalaignar interpretation was softened.

## Part 005

Tamil Part 005 is archival-ready, but its English translation has not started. Finish the Part 004 release gate before beginning Part 005 English.

## Next activity

Perform the separate **Part 004 English release gate**. Verify all 22 `editorial-reviewed` records, metadata, review decisions and glossary alignment; create `reviews/PART_004_RELEASE_REPORT.md`; and promote pages to `release-ready` only if the gate passes.

Do not begin Part 005 English translation in the same release-gate activity.

See [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md) for detailed state.
