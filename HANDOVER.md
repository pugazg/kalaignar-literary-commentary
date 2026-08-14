# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. The English layer is a **project-created translation**, not an official/publisher English edition, and must not import external English Kural wording or another commentator's interpretation.

# திருக்குறள் — Tamil archival state

- Part 001 — scans 1–20: **ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**; 19 verified + scan 8 partial.
- Part 002 — scans 21–41: **ARCHIVAL-READY**, 21/21 verified.
- Part 003 — scans 42–62: **ARCHIVAL-READY**, 21/21 verified; printed pages 9–29; Kural 41–145.

Do not redo or renumber Parts 001–003. Future Tamil intake may continue from overall scan 63 only if the next supplied scan itself confirms continuity after scan 62 / printed page 29 / Kural 145.

# English project translation

Permanent cadence:

**Tamil transcription → Tamil visual verification → Tamil audit → English draft → English source-check → editorial consistency review → English part release report.**

Framework:

- `works/thirukkural/translations/en/README.md`
- `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`
- `works/thirukkural/translations/en/GLOSSARY.md`
- `works/thirukkural/translations/en/TRANSLATION_STATUS.md`
- `works/thirukkural/translations/en/reviews/PART_001_REVIEW.md`

Every English page must retain:

`translation_type: "project_translation"`

# Part 001 English progress

## First pass — COMPLETE

One-to-one aligned English records exist for all **20/20** scans.

## Source-check — COMPLETE

Every fully translatable page was compared against its audited Tamil record. Scan 8 completed a source-limited alignment check without reconstructing unreadable handwriting.

## Editorial consistency / glossary reconciliation — COMPLETE

Current page status:

- `editorial-reviewed`: **19** — scans 1–7 and 9–20;
- `source-limited`: **1** — scan 8; source-limited alignment and editorial checks complete;
- `source-checked`: **0**;
- `draft`: **0**;
- `release-ready`: **0**.

Editorial review artefact:

`works/thirukkural/translations/en/reviews/PART_001_REVIEW.md`

### Controlled Part 001 editorial decisions

- `முப்பால்` → **Muppaal**;
- verified source form `திருவிடம்` → **Tiruvidam**, deliberately retained rather than normalized;
- `ஊழ்` → **Oozh** as heading/concept title and *oozh* in running prose where the Tamil term itself is named;
- `இயற்கை நிலை` → **natural condition** only as Professor Nannan's explicit attribution of Kalaignar's interpretation;
- `வாயுறை` → **counsel**;
- `பெண்வழிச் சேறல்` → **Following a Woman's Lead**;
- `பிறிது மொழிதல்` → ***pirithu mozhithal*** with the gloss “saying one thing in order to convey another”;
- `அடுத்தூர்வது அஃதொப்பதில்` → intentionally retained exactly in Tamil because the audited source does not support a sufficiently secure English expansion;
- `பா நலம்` → **Poetic Quality**;
- `அணி நலம்` → **Excellence of Poetic Figure**;
- `அடை நலம்` → **Excellence of Epithets**.

The source-title distinction remains mandatory:

- `கடவுள் வாழ்த்து` → **Invocation to God** when that source title is named;
- `வழிபாடு` → **Worship** for Kalaignar's adopted chapter title.

### Editorial corrections made in the full-set pass

- scan 5 — normalized English punctuation in edition details;
- scan 10 — smoothed the `Muppaal ... counsel` word order and finalized deliberate retention of **Tiruvidam**;
- scan 15 — improved English readability in the sentence introducing Kalaignar's lucid commentary without changing Nannan's argument;
- scan 16 — clarified how earlier explanations of `பெண்வழிச் சேறல்` became established;
- scan 17 — improved syntax of numbered point 7;
- scan 19 — finalized the documented non-translation of `அடுத்தூர்வது அஃதொப்பதில்`.

The scan-20 Kural examples **1101, 1098 and 17** remain project translations from this archived Tamil source; no published English Kural wording was substituted.

## Scan 8 — source limitation remains

`works/thirukkural/translations/en/pages/0008-handwritten-note.md` remains `source-limited`.

Securely established English content is limited to:

- heading **An Introduction to the Preface!**;
- decorative divider presence;
- Kalaignar's signature presence;
- date **27/12/2007**;
- page-condition / bleed-through description.

The continuous handwritten body remains untranslated and unreconstructed. Editorial review does not remove this limitation.

# Next exact activity

Create and execute the **Part 001 English release gate**.

1. Verify all **20/20** aligned English page files exist.
2. Verify scans **1–7 and 9–20** are all `editorial-reviewed`.
3. Verify scan **8** remains `source-limited` and its documented limitation is carried into the release decision.
4. Verify consistency between:
   - `reviews/PART_001_REVIEW.md`;
   - `GLOSSARY.md`;
   - `TRANSLATION_STATUS.md`;
   - English page metadata;
   - English README / work README.
5. Confirm scan 19's retained Tamil phrase `அடுத்தூர்வது அஃதொப்பதில்` is explicitly documented and not hidden.
6. Confirm no external/published English Kural translation has been substituted for the scan-20 examples.
7. Create `works/thirukkural/translations/en/reviews/PART_001_RELEASE_REPORT.md` documenting the release checks and decision.
8. If the release gate passes, promote the 19 fully translatable pages from `editorial-reviewed` to `release-ready`.
9. Keep scan 8 as `source-limited`; do not falsely promote the unreadable body.
10. Update `TRANSLATION_STATUS.md`, English README, work README, root README and this handover after release.
11. Do not begin Part 002 English translation until the Part 001 release gate is complete.

## Source authority rule

The supplied scans remain the controlling sources. The project English translation must preserve the meaning and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
