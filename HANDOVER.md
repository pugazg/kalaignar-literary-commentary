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

Current status:

- `source-checked`: **7** — scans 1–7
- `source-limited`: **1** — scan 8
- `draft`: **12** — scans 9–20
- `editorial-reviewed`: **0**
- `release-ready`: **0**

## Source-check completed — scans 1–7

Each English page was compared with its audited Tamil archival page.

- scans 1–5: no translation-text changes required; promoted to `source-checked`.
- scan 6: contents entry `பேராசிரியரின் அணிந்துரை` changed from `Professor's Foreword` to **`The Professor's Foreword`**; page promoted to `source-checked`.
- scan 7 / Kalaignar's Preface: promoted to `source-checked` after source-supported fidelity corrections:
  - `நிறைவேற்றி மகிழ்` → **“Having fulfilled that desire, to my joy”**;
  - `உண்மை நிலை` → **“the fact”**, replacing the weaker first-pass “the factual possibility”;
  - `இனமான ஏந்தல்` → **“standard-bearer of the dignity of our people.”**
- Kalaignar's distinction remains: `கடவுள் வாழ்த்து` → **Invocation to God**; `வழிபாடு` → **Worship**.

Do not editorially promote these pages yet; source-check and editorial review are separate stages.

## Scan 8 — source-limited

`works/thirukkural/translations/en/pages/0008-handwritten-note.md` remains `source-limited` because the Tamil archival record is itself partial. The continuous handwriting must not be reconstructed.

## Scans 9–12 — still draft

The four pages of K. Anbazhagan's `பேராசிரியரின் அணிந்துரை` / **The Professor's Foreword** remain `draft`. Review-sensitive terms include **Muppaal**, **Tiruvidam**, **oozh**, and provisional `வாயுறை` → `counsel`.

## Scans 13–20 — still draft

Professor Ma. Nannan's **Critical Appreciation** remains `draft`. Review-sensitive decisions include:

- `பெண்வழிச் சேறல்` → **Following a Woman's Lead** provisionally;
- `ஊழ்` → **Oozh**, with `இயற்கை நிலை` rendered as **natural condition**;
- `பிறிது மொழிதல்` → ***pirithu mozhithal*** with a gloss;
- `அடுத்தூர்வது அஃதொப்பதில்` → provisional English on scan 19;
- `பா நலம்`, `அணி நலம்`, `அடை நலம்` → provisional literary headings.

The Kural examples on scan 20 were translated from the audited Tamil source; do not replace them with published English Kural versions.

# Next exact activity

Review **Part 001 scan 8** as a source-limited English alignment check.

1. Fetch Tamil `pages/0008-handwritten-note.md` and English `translations/en/pages/0008-handwritten-note.md`.
2. Compare only securely established source elements: heading, visible date, signature/facsimile description, decorative/page-condition notes.
3. Confirm that the continuous handwritten body remains untranslated and unreconstructed.
4. Correct any English mismatch only if supported by the partial Tamil archival record.
5. Keep English status **`source-limited`**; do not promote it to `source-checked` or `editorial-reviewed` merely because the alignment check is complete.
6. Record the completed source-limited alignment check in translation status/handover.
7. Then the next source-check batch is scans **9–12**.
