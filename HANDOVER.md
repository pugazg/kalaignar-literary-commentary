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

Every English page must retain:

`translation_type: "project_translation"`

## Part 001 English first pass — COMPLETE

One-to-one aligned English records exist for all **20/20** scans.

## Part 001 source-check — COMPLETE

Current status:

- `source-checked`: **19** — scans 1–7 and 9–20
- `source-limited`: **1** — scan 8; source-limited alignment check complete
- `draft`: **0**
- `editorial-reviewed`: **0**
- `release-ready`: **0**

All fully translatable Part 001 English pages have now been compared against the audited Tamil source. Scan 8 remains source-limited because its continuous handwriting is not securely readable in the controlling scan.

### Source-check history

- scans 1–7 — complete;
- scan 8 — source-limited alignment check complete;
- scans 9–12 — complete;
- scans 13–20 — complete.

### Scans 13–20 source-check results

Professor Ma. Nannan's `மதிப்புரை` / **Critical Appreciation** is now source-checked page by page.

Important source-supported corrections:

- scan 13 — clarified the `ஈகை அறம்` and possession/ownership sentences without changing Nannan's argument;
- scan 14 — corrected an agency reversal in `மாந்தர் பிறர் பொருளைச் சுரண்டாமல் காப்பது`; English now states that people must be prevented from exploiting the property of others;
- scan 15 — tightened `கட்டிக்காத்து` to **safeguard them all**;
- scan 16 — restored the omitted `கற்பித்துப் பேச` element by representing fabricated claims used to demean and blame women;
- scan 17 — clarified numbered points 7 and 9 so agency and evaluative force align with the Tamil;
- scan 18 — no translation-text correction required;
- scan 19 — `ஊக்கம்` tightened to **initiative**. The first-pass English expansion of `அடுத்தூர்வது அஃதொப்பதில்` was withdrawn as insufficiently supported; the phrase is now retained exactly in Tamil with a source-check note;
- scan 20 — quoted Kurals **1101, 1098 and 17**, their Kalaignar explanations and the literary headings were source-checked without importing published English Kural wording.

### Review-sensitive terms carried into editorial review

- `முப்பால்` → **Muppaal**;
- source form `திருவிடம்` → **Tiruvidam**;
- `ஊழ்` → **oozh / Oozh** when explicitly named;
- `வாயுறை` → **counsel** provisionally;
- `பெண்வழிச் சேறல்` → **Following a Woman's Lead**;
- `இயற்கை நிலை` → **natural condition**, specifically as Nannan's attribution of Kalaignar's interpretation;
- `பிறிது மொழிதல்` → ***pirithu mozhithal*** with explanatory gloss;
- `அடுத்தூர்வது அஃதொப்பதில்` → retained in Tamil pending a secure editorial decision;
- `பா நலம்` → **Poetic Quality**;
- `அணி நலம்` → **Excellence of Poetic Figure**;
- `அடை நலம்` → **Excellence of Epithets**.

The controlled glossary has been updated to reflect these source-check outcomes.

# Next exact activity

Run the **Part 001 English editorial-consistency / glossary reconciliation pass** across all scans 1–20.

1. Review all 19 `source-checked` English pages as one editorial set rather than page-by-page in isolation.
2. Review scan 8 separately while preserving its `source-limited` status and source limitation.
3. Check English consistency for:
   - work/section/chapter titles;
   - Aram / aram capitalization and contextual rendering;
   - transliterated forms such as **Muppaal**, **Tiruvidam**, **oozh / Oozh**, *Sangathamizh*, *Kuraloviyam*;
   - names and honorifics;
   - quoted source titles **Invocation to God** / **Worship**;
   - poetic line style in scans 9–12;
   - analytical prose/register in scans 13–20;
   - punctuation, emphasis, quotation marks and recurring phrase treatment;
   - literary terms on scan 20.
4. Resolve or explicitly preserve the review-sensitive terms listed above. Do not use external Kural translations or silently normalize source-specific Tamil.
5. Create `works/thirukkural/translations/en/reviews/PART_001_REVIEW.md` documenting the editorial decisions, corrections and any intentionally unresolved/source-limited items.
6. Apply editorial corrections consistently to all affected English page files.
7. Promote eligible fully translatable pages from `source-checked` to `editorial-reviewed` only after the full consistency pass is complete.
8. Scan 8 must retain its source limitation; do not pretend the unreadable body has been translated.
9. Update `GLOSSARY.md`, `TRANSLATION_STATUS.md`, English README, work README, root README and this handover after the review.
10. Do **not** create `PART_001_RELEASE_REPORT.md` until the editorial review is complete. That release report is the activity after this one.

## Source authority rule

The supplied scans remain the controlling sources. The project English translation must preserve the meaning and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
