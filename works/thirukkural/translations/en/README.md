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

The same source-first discipline applies to Nannan, the publisher, indexes and the edition's own glossaries. Source-specific metaphors, definitions and unusual formulations must not be silently normalized away.

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

Release decision: **RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS**.

Review artefacts:

- [`reviews/PART_001_REVIEW.md`](reviews/PART_001_REVIEW.md)
- [`reviews/PART_001_RELEASE_REPORT.md`](reviews/PART_001_RELEASE_REPORT.md)

## Part 002 — EDITORIAL REVIEW COMPLETE

Part 002 has **21/21 aligned English records**, and all **21/21 are now `editorial-reviewed`**.

- `editorial-reviewed`: **21** — scans 21–41
- `source-checked`: **0**
- `draft`: **0**
- `release-ready`: **0**

Review artefact:

- [`reviews/PART_002_REVIEW.md`](reviews/PART_002_REVIEW.md)

The review preserved all fidelity-first source-check decisions. **Aadhi Bhagavan**, *iraivan*, *anthanar*, Kalaignar's Kural-25 Indra interpretation, Kural 12's **food they drink**, Kural 20's warning about conduct, Kural 34's **clamour**, and Kural 38's **stone that sets the path of life in order** remain source-controlled choices rather than conventionalized replacements.

The full chapter index on scans 28–29 is treated as an **index-local project translation**, not an imported standard English chapter-title set. The edition's own source glosses on scans 30–31 remain distinct from chapter-title English. Examples include **Worship | Following**, **Following a Woman's Lead | Becoming obsessed with women**, and **Women Beyond Bounds | Women for hire**.

The review also finalized two source-sensitive expressions:

- `மக்கள் நெஞ்சின் மலிவுப் பதிப்பு` remains **“the low-priced edition of the people's hearts”** to preserve Nannan's metaphor;
- Part 002 renders `அடுத்தூர்வது அஃதொப்பதில்` as **“nothing equals that for driving it away”** from the complete Kural plus Nannan's adjacent explanation, while released Part 001 scan 19 remains unchanged with the compact Tamil phrase retained. The difference is explicitly documented in the review and glossary.

See [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md) for the detailed state.

## Next activity

Perform the separate **Part 002 English release gate**. Verify all 21 pages, the Part 002 review, glossary, metadata and documented cross-part decisions; create `reviews/PART_002_RELEASE_REPORT.md`; and, if the gate passes, promote all 21 Part 002 pages to `release-ready`.

Do not begin Part 003 English in the same activity.
