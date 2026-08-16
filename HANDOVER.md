# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

Active work: `works/thirukkural/`

## Mandatory startup

Before making changes:

1. read `THIRUKKURAL_ARCHIVAL_GUIDELINES.md` completely;
2. read `LITERARY_COMMENTARY_PROCESSING_GUIDE.md` completely;
3. read this `HANDOVER.md` completely;
4. read `works/thirukkural/README.md`;
5. inspect existing target files before writing;
6. inspect the actual controlling source required by the active gate;
7. for English work additionally fresh-read:
   - `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`;
   - `works/thirukkural/translations/en/GLOSSARY.md`;
   - `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
   - `works/thirukkural/translations/en/reviews/PART_011_RELEASE_REPORT.md`;
   - `works/thirukkural/translations/en/reviews/PART_012_REVIEW.md`;
   - `works/thirukkural/AUDIT_PART_012.md`.

Repository state is authoritative.

## Source rule

The supplied Tamil scans are controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

Source PDFs are working/control sources and are not to be committed to GitHub unless the user explicitly requests that.

OCR/parsed text may assist but is never authoritative over direct inspection of the scan.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Keep these as separate gates.

Every project-created English page must identify:

```yaml
translation_type: "project_translation"
```

Released English material must not be revised merely to harmonize later vocabulary.

Permanent earlier protections remain binding, including:

- chapter 38 `ஊழ்` → **Oozh**;
- Kalaignar's `இயற்கை நிலை` → **natural condition**;
- Kural 543 `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**, not an automatic caste-specific conventional gloss;
- preservation of Kalaignar's governance, citizens, working-people, justice, public-resource and rational/inquiry vocabulary where the Tamil explicitly uses it.

# Established baseline

## Tamil

Parts **001–012 are audited / ARCHIVAL-READY continuously** through:

- overall scan **260**;
- printed page **227**;
- Kural **1115**.

Latest Tamil audit:

`works/thirukkural/AUDIT_PART_012.md` — **PASS / ARCHIVAL-READY**.

## English

Parts **001–011 are fully released continuously through Kural 1010**.

Part **012 has completed first pass, direct source-check and editorial consistency / glossary reconciliation: 23 / 23 aligned physical pages are `editorial-reviewed`**.

Part 012 editorial review:

`works/thirukkural/translations/en/reviews/PART_012_REVIEW.md`.

Released Parts 001–011 must remain untouched during Part 012 work.

# Supplied later sources

- Part 012 — `திருக்குறள்_கலைஞர்_உரை_part_012_pages_238-260.pdf` — **23 pages** — Tamil **ARCHIVAL-READY**, English **EDITORIAL REVIEW COMPLETE**;
- Part 013 — `திருக்குறள்_கலைஞர்_உரை_part_013_pages_261-282.pdf` — **22 pages** — source received, not started;
- Part 014 — `திருக்குறள்_கலைஞர்_உரை_part_014_pages_283-302.pdf` — **20 pages** — source received, not started;
- Part 015 — `திருக்குறள்_கலைஞர்_உரை_part_015_pages_303-323.pdf` — **21 pages** — source received, not started.

Do not begin Part 013 Tamil transcription while the Part 012 English workflow is active.

# Part 012 Tamil archival baseline

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_012_pages_238-260.pdf`

Supplied-file identity used during source inspection:

`file_00000000f4288211a7bbe05c015edc20`

Part 012 audit:

`works/thirukkural/AUDIT_PART_012.md` — **PASS / ARCHIVAL-READY**.

Final Tamil scope:

- physical pages: **23 / 23**;
- scans: **238–260**;
- Part-local pages: **1–23**;
- printed pages: **205–218**, two unnumbered leaves, then **221–227**;
- Kural range: **1011–1115**;
- `verified`: **23 / 23**;
- unresolved records: **0**.

Incoming boundary: printed **204 → 205 / Kural 1010 → 1011** — PASS.

Outgoing boundary context, using only the supplied Part 013 first page: printed **227 → 228 / Kural 1115 → 1116** — PASS. Chapter 112 continues. No Part 013 page record has been created.

## Part 012 source structure

1. scans **238–251** — `பொருள் — குடியியல்`, chapters 102–108, Kural **1011–1080**;
2. scan **252** — centered `இன்பம்` section-title leaf;
3. scan **253** — no independent printed body text; reverse-side show-through only;
4. scans **254–260** — `இன்பம் — களவியல்`, Kural **1081–1115**;
5. scan **260 / printed page 227** begins chapter 112 `நலம் புனைந்து உரைத்தல்`, present only through Kural **1115** in Part 012.

## Authoritative Tamil verification corrections

1. scan **239 / Kural 1018 commentary**: `அகன்றுவிட்டதாகக் கருத வேண்டும்.`
2. scan **242 / Kural 1035 commentary**: `ஊதியம் பெற்று உண்ணும் இயல்புடையவர்`
3. scan **245 / Kural 1048 commentary**: `கொலை செய்வதுபோல நேற்று...`

## Protected Part 012 source readings

Do not normalize these from another edition:

### Kural 1077 — scan 251

```text
ஈங்கை விதிரார் கயவர் கொடிறுடைக்குங்
கூன்கையர் அல்லா தவர்க்கு.
```

### Kural 1098 — scan 257

```text
அசையியற் குண்டாண்டோர் ஏஎர்யான் நோக்கப்
பசையினள் பைய நகும்.
```

Kalaignar's adjacent commentary remains the primary interpretive aid for these edition-specific readings.

# Part 012 English current state

**EDITORIAL REVIEW COMPLETE — 23 / 23 aligned physical pages are `editorial-reviewed`.**

All 23 Tamil filenames are mirrored under `works/thirukkural/translations/en/pages/`, including:

- scan 252 `0252-inbam-title.md`;
- scan 253 `0253-blank.md`.

Every Part 012 English page now uses:

```yaml
translation_type: "project_translation"
status: "editorial-reviewed"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

Current Part 012 English status counts:

- `draft`: **0**;
- `source-checked`: **0**;
- `editorial-reviewed`: **23**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

## Part 012 editorial decisions

The editorial consistency / glossary-reconciliation gate passed for all 23 physical pages.

No substantive Kural or Kalaignar-commentary body text was changed during the editorial gate. The source-checked English wording was retained because it passed readability and project-consistency review without requiring stylistic intervention.

Controlled structure:

- scans **238–251**: `Porul — Civic Life`;
- scan **252**: standalone `Inbam` title leaf;
- scan **253**: blank/reverse-show-through leaf;
- scans **254–260**: `Inbam — Clandestine Love`.

`களவியல்` → **Clandestine Love** is now the controlled Part 012 structural rendering.

Controlled main-body chapter headings:

- 102 `நாணுடைமை` → **Modesty**;
- 103 `குடிசெயல் வகை` → **Working for the Community**;
- 104 `உழவு` → **Agriculture**;
- 105 `நல்குரவு` → **Poverty**;
- 106 `இரவு` → **Begging**;
- 107 `இரவச்சம்` → **Dread of Begging**;
- 108 `கயமை` → **Baseness**;
- 109 `தகை அணங்குறுத்தல்` → **The Torment of Beauty**;
- 110 `குறிப்பறிதல்` → **Understanding Signs**;
- 111 `புணர்ச்சி மகிழ்தல்` → **Delight in Union**;
- 112 `நலம் புனைந்து உரைத்தல்` → **Praising Her Beauty**.

Chapter 103 is deliberately source-led by Kalaignar's repeated `குடிமக்கள்`, welfare, protection and advancement vocabulary. Do not replace it with a purely family/clan-maintenance heading from another interpretation.

Chapter 110 deliberately reuses the existing controlled **Understanding Signs** heading without a project-added parenthetical disambiguator.

Chapter 112 is controlled only for the heading and Kural **1111–1115** supplied in Part 012. Do not infer its continuation.

`GLOSSARY.md` is reconciled in this editorial gate with the Part 012 structural, chapter and recurring-term controls.

Protected English treatments remain binding:

- Kural **1018** — moral conduct itself is treated as having withdrawn in shame;
- Kural **1035** — works, **earns wages and eats**;
- Kural **1048** — poverty tormented him **as though killing him**;
- Kural **1062** — Kalaignar's direct challenge to the one said to have created this world;
- Kural **1077** — unusual supplied wording plus fist/cheek and **saliva-wet hand** commentary direction;
- Kural **1098** — unusual supplied wording plus affectionate soft smile / new radiance direction;
- Kural **1103** — skeptical comparison with the **world of the lotus-eyed one**;
- Kural **1115** — anicham-flower stalk, broken waist and absent auspicious-drum explanation.

# Exact next activity

**Part 012 English release gate — all 23 `editorial-reviewed` physical pages / scans 238–260.**

Required procedure:

1. fresh-read the mandatory startup and English files listed above;
2. inspect all 23 Part 012 `editorial-reviewed` English records and their verified Tamil counterparts as a single release unit;
3. verify one-to-one filename and `source_tamil_file` alignment;
4. verify scan continuity **238–260** and Part-local physical-page continuity **1–23**;
5. verify printed-page progression **205–218 → two unnumbered leaves → 221–227**;
6. verify Kural continuity **1011–1115** and the explicit stop midway through chapter 112;
7. verify the physical `Inbam` title leaf at scan 252 and blank reverse leaf at scan 253 remain aligned and are not collapsed;
8. verify the controlled structural sequence **Civic Life → Inbam → Clandestine Love** and chapter headings **102–112**;
9. confirm all authoritative Tamil corrections and protected source-sensitive English treatments listed above remain intact;
10. confirm every page carries `translation_type: "project_translation"`, `source_tamil_status: "verified"`, and the common translation basis;
11. create `works/thirukkural/translations/en/reviews/PART_012_RELEASE_REPORT.md` only if the release gate passes;
12. promote all 23 Part 012 English records from `editorial-reviewed` to `release-ready` only if the release gate passes;
13. synchronize `TRANSLATION_STATUS.md`, English README, work README, root README and this handover after release;
14. stop after the Part 012 release gate;
15. do **not** begin Part 013 Tamil transcription during this activity;
16. do **not** alter released English Parts 001–011.

If the release gate passes, English Parts **001–012** will then be released continuously through Kural **1115**. Only after that closed gate should the next activity be determined from the supplied Part 013 source.
