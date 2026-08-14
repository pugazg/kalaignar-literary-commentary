# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. The English layer is a **project-created translation**, not an official/publisher English edition, and must not import external English Kural wording or another commentator's interpretation.

## English fidelity rule — MANDATORY

The translation must retain **Kalaignar's own language, images, emphases and interpretive direction** as closely as clear English allows. Do not replace his explanation with the familiar or conventional interpretation of a Kural. If Kalaignar deliberately reads a term in a particular way, the English must translate that reading, not correct it toward another commentator.

The same source-fidelity rule applies to Professor Nannan, publisher prose, indexes and source glossaries. Do not silently smooth away or normalize metaphors, repetition, rhetoric, definitions or source-specific terminology merely because a more conventional English phrase is available.

Natural English syntax is allowed. Source meaning and voice outrank elegance.

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
- `works/thirukkural/translations/en/reviews/PART_001_RELEASE_REPORT.md`

Every English page must retain:

`translation_type: "project_translation"`

# Part 001 English — RELEASE COMPLETE

- aligned English records: **20 / 20**;
- `release-ready`: **19** — scans 1–7 and 9–20;
- `source-limited`: **1** — scan 8;
- release decision: **RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS**.

Do not silently revise released Part 001 wording because later Part 002 context appears. Any cross-part change must follow source-check/editorial review and be explicitly documented.

# Part 002 English — SOURCE-CHECK COMPLETE

Tamil source: `திருக்குறள்_கலைஞர்_உரை_part_002_pages_21-41.pdf`

Tamil state: **21/21 verified; ARCHIVAL-READY**.

Current English state:

- aligned English records: **21 / 21**;
- `source-checked`: **21** — scans 21–41;
- `draft`: **0**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

All Part 002 pages have completed direct English-vs-verified-Tamil source-check. No editorial-review promotion has yet been performed.

## Source-check record — scans 21–27

Fidelity-first corrections restored Nannan's source metaphors and removed unsupported interpretive additions. Scan 25 now uses **“nothing equals that for driving it away”** for the full Kural containing `அடுத்தூர்வது அஃதொப்பதில்`; scan 26 preserves `மக்கள் நெஞ்சின் மலிவுப் பதிப்பு` closely as **“the low-priced edition of the people's hearts.”** Released Part 001 scan 19 remains unchanged pending a separately documented cross-part editorial decision.

## Source-check record — scans 28–33

The full chapter index and this edition's own `அருஞ்சொற்பொருள்` glosses were checked entry-by-entry. Source order, chapter numbers and source-specific glosses are preserved. Scan 32 retains inferred `printed_page: "xxxi"` with its same-source basis documented; scan 33 remains blank / reverse-side bleed-through only.

## Source-check record — scans 34–41 / Kural 1–40

Every Kural verse and Kalaignar commentary paragraph was compared with the verified Tamil record. Key decisions:

- **Kural 1 / `ஆதி பகவன்`** — retained as **Aadhi Bhagavan** because Kalaignar's commentary itself uses the expression directly. Do not replace it with a doctrinal title.
- **Kural 5 / `இறைவன்`** — verse retains `iraivan`; Kalaignar explicitly directs attention to the meaning of the word itself.
- **Kural 8 / `அந்தணர்`** — verse retains `anthanar`; Kalaignar immediately explains it as **worthy people** (`சான்றோர்`).
- **Kural 10** — preserve Kalaignar's reading of `பிறவிப் பெருங்கடல்` as **the great sea called life** and `இறைவன்` as **the one who stands foremost**.
- **Kural 12** — preserve Kalaignar's unusual formulation that rain becomes **the food they drink**; do not silently reduce it to “water.”
- **Kural 17** — wording remains aligned with the released Part 001 example and preserves Kalaignar's social analogy.
- **Kural 20** — preserve Kalaignar's explicit warning that conduct itself may deteriorate without rain.
- **Kural 25 / Indra** — preserve Kalaignar's own Indra reading: he is presented as an example of one who goes astray through failure to control the senses, while the commentary points to the power of those who control sense-born desires. Do not substitute another commentator's explanation.
- **Kural 30 / `அந்தணர்`** — retain `anthanar`; Kalaignar defines the term through worthy people who love all living beings and shower compassion upon them.
- **Kural 34** — `ஆரவாரம்` is **clamour**. The first-pass addition “display” was removed.
- **Kural 38 / `வாழ்நாள் வழியடைக்கும் கல்`** — preserve Kalaignar's path-and-stone image: the good deeds become **the stone that sets the path of life in order**. The first-pass word “shapes” was removed.

These are source-fidelity decisions and must not be undone merely to make the English conform to familiar published Kural translations.

# Part 003 English — NOT STARTED

Tamil scans 42–62 are audited / archival-ready and contain Kural 41–145 plus Kalaignar commentary. Do not start Part 003 English until Part 002 completes editorial review and release gate.

# Next exact activity

Begin the **Part 002 English editorial-consistency / glossary-reconciliation review across scans 21–41**.

1. Fetch `TRANSLATION_GUIDE.md`, `GLOSSARY.md`, `TRANSLATION_STATUS.md`, all Part 002 English pages 21–41, and the Part 001 review artefact as the process reference.
2. Review the 21-page English set as a whole for terminology, repeated Kural wording, chapter titles, names, punctuation, quotation handling and readable English.
3. Preserve every source-check decision above. Editorial review may improve English only where the source meaning, imagery and Kalaignar's interpretive direction remain intact.
4. Reconcile the full chapter-index renderings with the controlled glossary without importing a standard external English chapter-title list.
5. Review provisional Part 002 analytical headings and source-sensitive expressions from scans 21–31.
6. Consider the cross-part treatment of `அடுத்தூர்வது அஃதொப்பதில்` as a **separately documented editorial decision**. Do not silently alter released Part 001 scan 19.
7. Create `works/thirukkural/translations/en/reviews/PART_002_REVIEW.md` if that matches the established Part 001 review convention after inspection.
8. Promote eligible Part 002 pages from `source-checked` to `editorial-reviewed` only after the full-set review is complete.
9. Synchronize `GLOSSARY.md`, `TRANSLATION_STATUS.md`, English README, work README, root README and this handover.
10. Do **not** perform the Part 002 release gate or create the release report in the same activity. The activity after editorial review is the separate Part 002 English release gate.

## Source authority rule

The supplied scans remain the controlling sources. The project English translation must preserve the meaning, voice and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
