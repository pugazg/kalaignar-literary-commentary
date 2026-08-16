# Next Chat Prompt — Continue Thirukkural Kalaignar Commentary Archive

Copy/paste the prompt below into a new chat window. Attach the active Part 008 PDF again if the new chat does not already have access to it.

---

Continue the **Thirukkural — Kalaignar Commentary archival project** directly in:

`pugazg/kalaignar-literary-commentary`

Active work path:

`works/thirukkural/`

The controlling source for the current activity is the attached Part 008 PDF covering overall scans 149–169 / printed pages 116–136 / Kural 566–670.

## MANDATORY STARTUP

Before making any repository change:

1. Read `THIRUKKURAL_ARCHIVAL_GUIDELINES.md` completely.
2. Read `LITERARY_COMMENTARY_PROCESSING_GUIDE.md` completely.
3. Read `HANDOVER.md` completely.
4. Read `works/thirukkural/README.md`.
5. Inspect the repository state and existing target files. Continue existing work; do not create duplicates.
6. Inspect the actual attached source scan pages needed for the current activity. The scan is authoritative; OCR/parsed text is only assistance.

## SOURCE AUTHORITY

The supplied scan is the controlling source.

Do not silently modernize, normalize, correct, reconstruct or improve the Tamil. Preserve source-supported spelling, joins, punctuation, grammar, names, numbers, repetition, chapter structure and Kalaignar commentary exactly as printed.

Do not substitute memorized/internet Thirukkural text for the printed source.

Distinguish printed text from bleed-through, stamps, handwriting and scanner artefacts.

The PDF itself must not be uploaded into GitHub.

## CURRENT VERIFIED PROJECT STATE

Tamil Parts 001–007 are `ARCHIVAL-READY` through overall scan 148 / printed page 115 / Kural 565.

English Parts 001–007 are fully released through Kural 565.

Part 008 Tamil first-pass transcription is complete 21/21.

Part 008 verification state:

- 14/21 `verified` — scans 149–162 / Kural 566–635;
- 7/21 `needs-review` — scans 163–169 / Kural 636–670;
- 0 partial;
- 0 blocked.

Part 008 audit has not started.

Part 008 English translation has not started.

Verification correction already made earlier:

- scan 153 / Kural 589 commentary: `ஒத்திருந் தால்` → `ஒத்திருந்தால்`.

Scan 162 directly confirms the structural transition:

`பொருள் — அரசியல்` → `பொருள் — அமைச்சியல் — அமைச்சு`.

## EXACT NEXT ACTIVITY

Perform **Part 008 Tamil direct visual verification — Batch 3 only** for:

- scan 163 / printed page 130 — Kural 636–640, completes `அமைச்சு`;
- scan 164 / printed page 131 — Kural 641–645, begins `சொல்வன்மை`;
- scan 165 / printed page 132 — Kural 646–650, completes `சொல்வன்மை`;
- scan 166 / printed page 133 — Kural 651–655, begins `வினைத் தூய்மை`;
- scan 167 / printed page 134 — Kural 656–660, completes `வினைத் தூய்மை`;
- scan 168 / printed page 135 — Kural 661–665, begins `வினைத்திட்பம்`;
- scan 169 / printed page 136 — Kural 666–670, continues/completes this Part's `வினைத்திட்பம்` range.

For every page:

1. visually compare the existing Tamil Markdown against the scan line-by-line;
2. verify Kural text, joins, punctuation, line breaks, headings, running header and every commentary sentence;
3. make only corrections directly supported by the scan;
4. document every correction found;
5. once a page passes, change `status` to `verified` and `transcription_method` to `direct visual comparison with source scan`.

When all seven pages are complete, synchronize root `README.md`, `works/thirukkural/README.md`, and `HANDOVER.md`.

Then STOP.

## DO NOT DO IN THIS ACTIVITY

Do not create `AUDIT_PART_008.md` yet.

Do not declare Part 008 `ARCHIVAL-READY` in the verification activity even if all 21 pages become verified. The audit is a separate gate.

Do not begin Part 008 English translation.

Do not begin Part 009 Tamil transcription.

Do not alter released English Parts 001–007.

## PERMANENT ENGLISH FIDELITY REQUIREMENT FOR LATER STAGES

When Part 008 eventually reaches English translation, retain Kalaignar's language and interpretation exactly as established in earlier Parts. Do not replace his commentary with standard/conventional Kural interpretations.

Protected examples from earlier Parts include:

- `ஊழ்` chapter heading → `Oozh`, while Kalaignar's `இயற்கை நிலை` → `natural condition`;
- Kural 543: `அந்தணர் நூற்கும்` is explained by Kalaignar as `அறவோர் நூல்களுக்கும்`, so the project translation uses `the books of the virtuous`, not an automatic `Brahmins` rendering;
- preserve his governance, citizens, treasury, justice, public-resource and working-people vocabulary;
- preserve direct images/comparisons rather than sanitizing them.

Permanent workflow:

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Proceed directly with the exact next activity after reading the mandatory files. Do not ask me to reconfirm the workflow unless the repository/source contains a genuine ambiguity that prevents safe continuation.

---
