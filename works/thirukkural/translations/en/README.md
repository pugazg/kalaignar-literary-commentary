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

Part 001 has **20/20 aligned English records** and its source-check stage is now complete for all fully translatable pages:

- scans **1–7**: `source-checked`;
- scan **8**: `source-limited`, with source-limited alignment check complete;
- scans **9–20**: `source-checked`.

Current counts:

- `source-checked`: **19**
- `source-limited`: **1**
- `draft`: **0**
- `editorial-reviewed`: **0**
- `release-ready`: **0**

### Source-check outcome

The source-check compared each English page directly with its audited Tamil page. Corrections were limited to source-supported fidelity issues. Among the more important fixes:

- scan 14 corrected the agency in `மாந்தர் பிறர் பொருளைச் சுரண்டாமல் காப்பது`, now rendered as **people being prevented from exploiting the property of others**;
- scan 16 restored the omitted source element `கற்பித்துப் பேச`, explicitly representing fabricated claims used to demean and blame women;
- scan 19 withdrew the speculative first-pass expansion of `அடுத்தூர்வது அஃதொப்பதில்`; the phrase is now retained exactly in Tamil with a note rather than presented with an insecure English meaning;
- scan 20's Kural examples 1101, 1098 and 17 were source-checked against this archived Tamil edition and Kalaignar's adjacent explanations without substituting published English Kural wording.

Review-sensitive terms remain visible for the editorial stage, including **Muppaal**, **Tiruvidam**, **oozh / Oozh**, `வாயுறை` → **counsel**, **Following a Woman's Lead**, *pirithu mozhithal*, and the scan-20 literary headings.

Scan 8 remains `source-limited`; its unreadable continuous handwriting is not reconstructed.

See:

- [`TRANSLATION_GUIDE.md`](TRANSLATION_GUIDE.md)
- [`GLOSSARY.md`](GLOSSARY.md)
- [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md)

## Next activity

Run the full **Part 001 editorial-consistency / glossary reconciliation pass** across scans 1–20. Review repeated terminology, titles, poetic/register choices, transliteration, punctuation and English readability as one set. Document decisions in `reviews/PART_001_REVIEW.md`, promote eligible fully translatable pages to `editorial-reviewed` only after that pass, and preserve scan 8's source limitation. The Part 001 release report comes only after the editorial review is complete.
