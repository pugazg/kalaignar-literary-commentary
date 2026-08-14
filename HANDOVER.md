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
- `source-limited`: **1** — scan 8; source-limited alignment check complete
- `draft`: **12** — scans 9–20
- `editorial-reviewed`: **0**
- `release-ready`: **0**

## Source-check completed — scans 1–7

- scans 1–5: no translation-text changes required; promoted to `source-checked`.
- scan 6: `பேராசிரியரின் அணிந்துரை` aligned to **The Professor's Foreword**.
- scan 7 / Kalaignar's Preface: source-supported fidelity corrections restored the sense of `நிறைவேற்றி மகிழ்`, `உண்மை நிலை`, and `இனமான ஏந்தல்`.
- Kalaignar's distinction remains: `கடவுள் வாழ்த்து` → **Invocation to God**; `வழிபாடு` → **Worship**.

Do not editorially promote these pages yet; source-check and editorial review are separate stages.

## Scan 8 — source-limited alignment check COMPLETE

Tamil source:

`works/thirukkural/pages/0008-handwritten-note.md`

English record:

`works/thirukkural/translations/en/pages/0008-handwritten-note.md`

The English record was compared only against source elements securely established by the partial Tamil archival record.

Confirmed alignment:

- heading `முகவுரையின் ஒரு முன்னுரை!` → **An Introduction to the Preface!**;
- decorative divider presence;
- Kalaignar's signature presence;
- date **27/12/2007**;
- reverse-side bleed-through explicitly excluded from current-page handwriting;
- continuous handwritten body remains untranslated and unreconstructed.

**No translation-text correction was required.**

The English record remains `status: "source-limited"` because the controlling Tamil archival record remains `partial`. Do not promote it to `source-checked`, `editorial-reviewed`, or `release-ready` unless the review framework explicitly preserves its source limitation. Do not reconstruct the handwriting unless a clearer controlling source is supplied.

## Scans 9–12 — still draft

The four pages of K. Anbazhagan's `பேராசிரியரின் அணிந்துரை` / **The Professor's Foreword** remain `draft`.

Review-sensitive terms already identified:

- `முப்பால்` → **Muppaal** provisionally;
- `திருவிடம்` → **Tiruvidam** because that is the verified Tamil source form;
- `ஊழ்` → **oozh** in the foreword's explicit discussion;
- `வாயுறை` → **counsel** provisionally.

## Scans 13–20 — still draft

Professor Ma. Nannan's **Critical Appreciation** remains `draft`. Review-sensitive decisions include:

- `பெண்வழிச் சேறல்` → **Following a Woman's Lead** provisionally;
- `ஊழ்` → **Oozh**, with `இயற்கை நிலை` rendered as **natural condition**;
- `பிறிது மொழிதல்` → ***pirithu mozhithal*** with a gloss;
- `அடுத்தூர்வது அஃதொப்பதில்` → provisional English on scan 19;
- `பா நலம்`, `அணி நலம்`, `அடை நலம்` → provisional literary headings.

The Kural examples on scan 20 were translated from the audited Tamil source; do not replace them with published English Kural versions.

# Next exact activity

Source-check **Part 001 scans 9–12**, K. Anbazhagan's `பேராசிரியரின் அணிந்துரை` / **The Professor's Foreword**.

1. Fetch Tamil files `0009-aninthurai-01.md` through `0012-aninthurai-04.md` and their matching English drafts.
2. Compare every poetic line, quotation, emphasized line, name, source-sensitive term, metadata field and page marker.
3. Preserve the poem-like line structure as closely as natural English allows.
4. Resolve **Muppaal**, **Tiruvidam**, **oozh**, `வாயுறை` and any other meaning-sensitive wording only from the audited Tamil source and controlled project glossary; do not import outside commentary or existing English translations.
5. Correct only source-supported translation issues.
6. Promote each page from `draft` to `source-checked` only after comparison is complete.
7. Do not perform `editorial-reviewed` promotion in the same activity.
8. After scans 9–12, the next source-check batch is scans **13–20**.

## Source authority rule

The supplied scans remain the controlling sources. The project English translation must preserve the meaning and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
