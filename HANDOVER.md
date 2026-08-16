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
   - `works/thirukkural/translations/en/reviews/PART_011_REVIEW.md`;
   - `works/thirukkural/translations/en/reviews/PART_011_RELEASE_REPORT.md`;
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

Latest released English artefacts:

- `works/thirukkural/translations/en/reviews/PART_011_REVIEW.md`;
- `works/thirukkural/translations/en/reviews/PART_011_RELEASE_REPORT.md` — **PASS / RELEASE APPROVED**.

Released Parts 001–011 must remain untouched during Part 012 work.

# Supplied later sources

- Part 012 — `திருக்குறள்_கலைஞர்_உரை_part_012_pages_238-260.pdf` — **23 pages** — Tamil **ARCHIVAL-READY**, English first pass complete;
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

Kalaignar's adjacent commentary is the primary interpretive aid for these edition-specific readings.

# Part 012 English current state

**FIRST PASS COMPLETE — 23 / 23 aligned physical pages are `draft`.**

All 23 Tamil filenames are mirrored under `works/thirukkural/translations/en/pages/`, including:

- scan 252 `0252-inbam-title.md`;
- scan 253 `0253-blank.md`.

Every Part 012 English page uses:

```yaml
translation_type: "project_translation"
status: "draft"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

Current Part 012 English status counts:

- `draft`: **23**;
- `source-checked`: **0**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

First-pass structural treatment:

- scans **238–251**: `Porul — Civic Life`;
- scan **252**: `Inbam` title leaf;
- scan **253**: reverse of title leaf;
- scans **254–260**: provisionally `Inbam — Clandestine Love`.

First-pass chapter renderings are provisional for chapters 102–109 and 111–112. Chapter 110 `குறிப்பறிதல்` continues the already controlled **Understanding Signs** rendering. Do not finalize new Part 012 terms in `GLOSSARY.md` during source-check.

Source-sensitive first-pass treatments that require explicit attention during source-check include:

- Kural **1062** — preserve Kalaignar's direct challenge to the one said to have created the world;
- Kural **1077** — retain this edition's unusual printed wording and Kalaignar's fist/cheek and saliva-wet-hand commentary direction;
- Kural **1098** — retain this edition's unusual printed wording and Kalaignar's affectionate soft-smile / new-radiance direction;
- Kural **1103** — preserve Kalaignar's skeptical comparison with the “world of the lotus-eyed one”;
- Kural **1115** — preserve the direct anicham-flower/stalk and broken-waist/drum explanation.

`GLOSSARY.md` was deliberately not changed during first pass.

# Exact next activity

**Part 012 English direct source-check — all 23 draft physical pages / scans 238–260.**

Required procedure:

1. fresh-read the mandatory startup and English files listed above;
2. inspect all 23 Part 012 English draft records and their 23 verified Tamil counterparts;
3. compare every English Kural against the exact Tamil Kural, preserving the source-supported two-line relationship;
4. compare every Kalaignar commentary translation against his verified Tamil commentary, correcting omissions, additions, subject drift, softened/strengthened claims, lost imagery or unsupported conventional interpretation;
5. use the controlling scan whenever a verified Tamil form or punctuation requires direct confirmation;
6. explicitly re-check the three authoritative Tamil verification corrections and protected Kural 1077 / 1098 readings;
7. preserve the title and blank physical-page alignment at scans 252–253;
8. keep `களவியல்` and newly introduced Part 012 chapter headings provisional during this gate;
9. do **not** update `GLOSSARY.md` during source-check;
10. promote only passing Part 012 English records from `draft` to `source-checked`;
11. synchronize `TRANSLATION_STATUS.md`, English README, work README, root README and this handover after the gate;
12. stop after source-check;
13. do **not** perform editorial/glossary reconciliation or release in the same activity;
14. do **not** begin Part 013 Tamil transcription;
15. do **not** alter released English Parts 001–011.

If all 23 pages pass source-check, the following separate activity will be **Part 012 English editorial consistency / glossary reconciliation**.
