# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. The English layer is a **project-created translation**, not an official/publisher English edition, and must not import external English Kural wording or another commentator's interpretation.

## English fidelity rule — MANDATORY

The translation must retain **Kalaignar's own language, images, emphases and interpretive direction** as closely as clear English allows. Do not replace his explanation with the familiar or conventional interpretation of a Kural. Natural English syntax is allowed, but source meaning and voice outrank elegance.

# திருக்குறள் — Tamil archival state

- Part 001 — scans 1–20: **ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**; 19 verified + scan 8 partial.
- Part 002 — scans 21–41: **ARCHIVAL-READY**, 21/21 verified.
- Part 003 — scans 42–62: **ARCHIVAL-READY**, 21/21 verified; printed pages 9–29; Kural 41–145.

Do not redo or renumber Parts 001–003.

# English project translation

Permanent cadence:

**Tamil transcription → Tamil visual verification → Tamil audit → English draft → English source-check → editorial consistency review → English part release report.**

Every English page must retain `translation_type: "project_translation"`.

# Part 001 English — RELEASE COMPLETE

- aligned English records: **20 / 20**;
- `release-ready`: **19**;
- `source-limited`: **1** — scan 8.

# Part 002 English — RELEASE COMPLETE

- aligned English records: **21 / 21**;
- `release-ready`: **21** — scans 21–41.

Binding Part 002 source-fidelity decisions remain in force, including **Aadhi Bhagavan**, *iraivan*, *anthanar*, Kalaignar's Kural-25 Indra reading, Kural 12 **the food they drink**, Kural 20's conduct warning, Kural 34 **clamour**, Kural 38's path-and-stone image, Nannan's ***puththelir* / new world**, and **“the low-priced edition of the people's hearts.”**

# Part 003 English — SOURCE-CHECK COMPLETE

Tamil source: `திருக்குறள்_கலைஞர்_உரை_part_003_pages_42-62.pdf`

Current English state:

- aligned English records: **21 / 21** — scans 42–62;
- `source-checked`: **21** — scans 42–62;
- `draft`: **0**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**.

## Source-check coverage

- `0042-aram-ilvaazhkkai-01.md` through `0062-aram-piranil-vizhaiyaamai-01.md` are all `status: "source-checked"`.
- coverage: Kural **41–145**.

## Binding source-check decisions to carry into editorial review

Earlier decisions remain active, including Kural 42 **those without protection**, Kural 55's slave/rain interpretation, Kural 58 **new world**, Kural 62 **seven births** versus **seven times seven generations**, Kural 67 singular **son** versus broader **children**, Kural 77 **conscience**, Kural 78 verse **hard barren ground** versus commentary **desert**, Kural 85 seed-for-hospitality, Kural 86 **heaven of fame**, Kural 87 hospitality as **sacrifice**, Kural 90 **anicham flower**, Kural 101 **“a great gem that came unbidden”**, Kural 104 millet/palmyra, and Kural 107 seven-times-seven/no-time-limit.

Final-batch decisions:

- **Kural 111** — keep Kalaignar's **enemy / neighbour / friend** explanation in commentary; do not force that list into the verse.
- **Kural 112** — use **wealth**, aligned with Kalaignar's `செல்வம்` explanation.
- **Kural 117** — verse uses **low state / decline**; commentary separately retains poverty caused by wealth not accumulating.
- **Kural 118** — retain balance / needle and justice imagery.
- **Kural 121** — keep verse deathless/deep-darkness imagery distinct from commentary **imperishable fame / life itself dark**.
- **Kural 126** — keep **seven lives** in the verse distinct from protection **through all time** in commentary.
- **Kural 128** — retain **drop of poison in a pot of milk**.
- **Kural 130** — retain **Aram waiting upon the path**.
- **Kural 132** — verse no longer imports the commentary's explicit hardship/suffering clause.
- **Kural 135** — no added **true** before prosperity.
- **Kural 136** — use **those of firm mind**, aligned with Kalaignar's prose.
- **Kurals 133–134** — preserve explicit birth/lineage and **Brahmin** wording; do not neutralize the source.
- **Kural 140** — verse remains **live in accord with the world**; commentary separately explains conduct **accepted by the great**.
- **Kural 141** — verse says those who have **discerned aram and wealth**; commentary separately expands this to works on aram and works on wealth.
- **Kurals 141–145** — preserve repeated **another man's wife** wording and Kural 143's living-man-as-**corpse** image.

No editorial consistency review has begun.

# Next exact activity

Begin the dedicated **Part 003 English editorial-consistency / glossary-reconciliation review across scans 42–62**.

1. Fetch current `TRANSLATION_GUIDE.md`, `GLOSSARY.md`, `TRANSLATION_STATUS.md`, and all 21 source-checked Part 003 English pages.
2. Review chapter headings 5–15 for consistency with the controlled glossary.
3. Reconcile recurring concepts such as `அறம்`, `அன்பு`, `நன்றி`, `நடுவுநிலைமை`, `அடக்கம்`, `ஒழுக்கம்`, and source-specific relationship/gender terms without flattening contextual differences.
4. Verify repeated Kural wording against already released occurrences where applicable.
5. Review punctuation, quotation handling, pronouns, singular/plural choices, transliterated terms, and verse/commentary separation.
6. Preserve all source-check decisions above unless a deliberate, source-supported editorial change is documented.
7. Create `works/thirukkural/translations/en/reviews/PART_003_REVIEW.md` documenting review decisions.
8. Update `GLOSSARY.md` only for genuinely controlled recurring decisions.
9. Promote all qualifying Part 003 pages to `status: "editorial-reviewed"` after the review is complete.
10. Synchronize status, READMEs and this handover.
11. Do **not** create the Part 003 release report or promote pages to `release-ready` in the same activity.

After the editorial-consistency review, the following activity is the separate **Part 003 English release gate**.

## Source authority rule

The supplied scans remain the controlling sources. The project English translation must preserve the meaning, voice and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
