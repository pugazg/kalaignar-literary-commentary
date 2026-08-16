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

Permanent workflow:

**English first pass (`draft`) → direct source-check → editorial consistency / glossary reconciliation → release gate.**

These English gates begin only after the corresponding Tamil part is audited / archival-ready.

## Status model

- `draft` — first complete English rendering;
- `source-checked` — compared against the audited Tamil page;
- `editorial-reviewed` — consistency/readability/glossary review complete;
- `release-ready` — part-level release gate complete;
- `source-limited` — completeness limited by controlling source;
- `blocked` — safe translation cannot proceed.

## Parts 001–007 — RELEASE COMPLETE

- Part 001: 19 `release-ready` + scan 8 `source-limited`;
- Part 002: **21/21 `release-ready`**;
- Part 003: **21/21 `release-ready`**, through Kural 145;
- Part 004: **22/22 `release-ready`**, through Kural 255;
- Part 005: **22/22 `release-ready`**, through Kural 365;
- Part 006: **21/21 `release-ready`**, through Kural 460;
- Part 007: **21/21 `release-ready`**, through Kural 565.

Latest completed review/release model:

- [`reviews/PART_007_REVIEW.md`](reviews/PART_007_REVIEW.md)
- [`reviews/PART_007_RELEASE_REPORT.md`](reviews/PART_007_RELEASE_REPORT.md)

Released Parts 001–007 must not be changed merely to harmonize later wording. Any project-wide revision must be deliberate, source-supported and documented.

## Part 008 — ENGLISH SOURCE-CHECK COMPLETE

Part 008 Tamil is audited / **ARCHIVAL-READY** for scans **149–169 / printed pages 116–136 / Kural 566–670**.

The aligned English layer has now completed both first pass and direct source-check:

- aligned English pages: **21 / 21**;
- `draft`: **0**;
- `source-checked`: **21 / 21**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

The source-check compared every Kural and every Kalaignar commentary paragraph against the audited Tamil record. Six fidelity corrections were made across five pages:

- scan 151 / Kural 579 — restored Kalaignar's stronger **seek one's destruction** sense;
- scan 157 / Kural 606 commentary — **recipients of the affection**, not the first-pass implication **worthy of the affection**;
- scan 161 / Kural 626 — clarified the failure to guard what had been gained;
- scan 161 / Kural 627 — removed the unclear **helpless refuge** wording and followed Kalaignar's suffering/distress explanation;
- scan 163 / Kural 638 — removed the unsupported insertion of **ruler / those in authority**;
- scan 164 / Kural 644 — **equal to**, not **greater than**.

All other Part 008 body text passed without substantive source-check correction.

The source-visible transition at scan **162 / Kural 631** remains represented as:

`Porul — Statecraft` → **`Porul — Ministerial Affairs`**.

`Ministerial Affairs` preserves the distinction from `அரசியல்` at source-check stage; the editorial/glossary gate must still decide whether this becomes the final controlled main-body wording for `அமைச்சியல்`.

Protected source-sensitive readings retained through source-check include the institutional government/intelligence language, Kural 610's untiring-ruler explanation, Kural 615's relatives/friends/people-of-the-country circle, the rational/inquiry framing of Kurals 618–620, **Oozh** in Kural 620, the council-of-ministers/citizens language of Kural 632, **seventy crore** in Kural 639, and the source images of the unbaked clay pot and chariot linchpin.

See [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md) for the detailed source-check record.

## Next activity

Perform the separate **Part 008 English editorial consistency / glossary-reconciliation review** for all 21 `source-checked` pages.

At that gate, reconcile chapter headings and recurring terms, decide the controlled structural wording for `அமைச்சியல்`, create `reviews/PART_008_REVIEW.md`, and promote passing pages to `editorial-reviewed` only after the review.

Do not combine that review with the release gate or Part 009 Tamil transcription.
