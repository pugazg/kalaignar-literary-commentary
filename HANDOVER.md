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

- `source-checked`: **11** — scans 1–7 and 9–12
- `source-limited`: **1** — scan 8; source-limited alignment check complete
- `draft`: **8** — scans 13–20
- `editorial-reviewed`: **0**
- `release-ready`: **0**

## Source-check completed — scans 1–7

- scans 1–5: no translation-text changes required;
- scan 6: `பேராசிரியரின் அணிந்துரை` aligned to **The Professor's Foreword**;
- scan 7: source-supported fidelity corrections restored `நிறைவேற்றி மகிழ்`, `உண்மை நிலை`, and `இனமான ஏந்தல்`.

## Scan 8 — source-limited alignment check COMPLETE

The English record was checked against the partial Tamil archival record. Securely established heading, decorative divider, signature presence, date **27/12/2007**, bleed-through description and deliberate omission of unreadable handwriting all align. No translation-text correction was required.

The page remains `source-limited`; do not reconstruct the handwritten body unless a clearer controlling source is supplied.

## Source-check completed — scans 9–12

K. Anbazhagan's `பேராசிரியரின் அணிந்துரை` / **The Professor's Foreword** is now source-checked page by page.

Files:

- `translations/en/pages/0009-aninthurai-01.md` — source-checked
- `translations/en/pages/0010-aninthurai-02.md` — source-checked
- `translations/en/pages/0011-aninthurai-03.md` — source-checked
- `translations/en/pages/0012-aninthurai-04.md` — source-checked

Source-check results:

- scan 9: `சிறப்பொவ்வா செய்தொழில் வேற்றுமையான்` was tightened from the awkward first-pass `Though distinction may differ because occupations differ` to **`Though distinctions are unequal because the work performed differs`**;
- scan 10: `தொல்லறநூல் உரைகண்ட பதின்மர்` was clarified as **`the ten commentators who wrote on this ancient work of aram`**; source form `திருவிடம்` remains **Tiruvidam** with an explicit source note;
- scan 11: no translation-text correction required;
- scan 12: no translation-text correction required.

The poem-like line structure, quotations and emphatic lines remain preserved.

Review-sensitive terms deliberately retained for the later editorial-consistency stage:

- `முப்பால்` → **Muppaal**;
- `திருவிடம்` → **Tiruvidam** because that is the verified source form;
- `ஊழ்` → **oozh** in the foreword's explicit discussion;
- `வாயுறை` → **counsel** provisionally; source-check found no basis to replace it, but final poetic nuance remains editorial work.

Do not promote scans 9–12 to `editorial-reviewed` yet.

## Scans 13–20 — still draft

Professor Ma. Nannan's **Critical Appreciation** remains `draft`.

Coverage:

- scans 13–14 — `தேவை` / **Need**;
- scan 15 — `வழிபாடு` / **Worship**;
- scans 16–17 — `பெண்வழிச் சேறல்` / **Following a Woman's Lead**;
- scans 18–19 — `ஊழ்` / **Oozh**;
- scans 19–20 — `பல்வகைச் சிறப்புகள்` / **Various Distinctive Merits**.

Review-sensitive decisions include:

- `பெண்வழிச் சேறல்` → **Following a Woman's Lead** provisionally;
- `ஊழ்` → **Oozh**, with `இயற்கை நிலை` rendered as **natural condition**;
- `பிறிது மொழிதல்` → ***pirithu mozhithal*** with a gloss;
- `அடுத்தூர்வது அஃதொப்பதில்` → provisional English on scan 19;
- `பா நலம்`, `அணி நலம்`, `அடை நலம்` → provisional literary headings.

The Kural examples on scan 20 were translated from the audited Tamil source; do not replace them with published English Kural versions.

# Next exact activity

Source-check **Part 001 scans 13–20**, Professor Ma. Nannan's `மதிப்புரை` / **Critical Appreciation**.

1. Fetch Tamil files `0013-mathippurai-01.md` through `0020-mathippurai-paa-nalam.md` and their matching English drafts.
2. Compare every heading, paragraph, numbered item, quotation, Kural citation, source-sensitive term, metadata field and page marker.
3. Preserve source paragraph structure and the argument of Nannan's assessment; do not soften, modernize or import outside interpretation.
4. Recheck especially:
   - `பெண்வழிச் சேறல்`;
   - `ஊழ்` and Nannan's `இயற்கை நிலை` explanation;
   - `பிறிது மொழிதல்`;
   - `அடுத்தூர்வது அஃதொப்பதில்`;
   - scan 20 literary headings and quoted Kurals 1101, 1098 and 17.
5. Do not substitute published English Kural translations.
6. Correct only source-supported translation issues.
7. Promote each page from `draft` to `source-checked` only after comparison.
8. Do not perform `editorial-reviewed` promotion in the same activity.
9. Once scans 13–20 are source-checked, the next activity is the full Part 001 editorial-consistency / glossary reconciliation pass, followed by review/release artefacts.

## Source authority rule

The supplied scans remain the controlling sources. The project English translation must preserve the meaning and interpretive stance of the audited Tamil source without presenting itself as an official English edition.
