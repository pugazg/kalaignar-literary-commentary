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

# Established released baseline

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

Released Parts 001–011 must remain untouched during the Part 012 first-pass gate.

# Supplied later sources

- Part 012 — `திருக்குறள்_கலைஞர்_உரை_part_012_pages_238-260.pdf` — **23 pages** — Tamil **ARCHIVAL-READY**;
- Part 013 — `திருக்குறள்_கலைஞர்_உரை_part_013_pages_261-282.pdf` — **22 pages** — source received, not started;
- Part 014 — `திருக்குறள்_கலைஞர்_உரை_part_014_pages_283-302.pdf` — **20 pages** — source received, not started;
- Part 015 — `திருக்குறள்_கலைஞர்_உரை_part_015_pages_303-323.pdf` — **21 pages** — source received, not started.

Do not begin Part 013 Tamil transcription while Part 012 English first pass is active.

# Part 012 Tamil archival baseline

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_012_pages_238-260.pdf`

Supplied-file identity used during source inspection:

`file_00000000f4288211a7bbe05c015edc20`

Part 012 audit:

`works/thirukkural/AUDIT_PART_012.md` — **PASS / ARCHIVAL-READY**.

Final Tamil scope:

- physical pages: **23 / 23**;
- overall scans: **238–260**;
- Part-local pages: **1–23**;
- printed pages: **205–218**, then two unnumbered leaves, then **221–227**;
- Kural range: **1011–1115**;
- `verified`: **23 / 23**;
- unresolved records: **0**.

Part 011 → Part 012 incoming boundary:

- printed page **204 → 205**;
- Kural **1010 → 1011**;
- **PASS / continuous**.

Part 012 → Part 013 outgoing boundary context was checked from the supplied Part 013 first page only:

- printed page **227 → 228**;
- Kural **1115 → 1116**;
- chapter 112 continues;
- **PASS / continuous**.

No Part 013 Tamil record has been created.

# Part 012 source structure

The audited structure is:

1. scans **238–251** — `பொருள் — குடியியல்`, chapters 102–108, Kural **1011–1080**;
2. scan **252** — centered section-title leaf `இன்பம்`;
3. scan **253** — no independent printed body text; reverse-side show-through only;
4. scans **254–260** — `இன்பம் — களவியல்`, Kural **1081–1115**;
5. scan **260 / printed page 227** begins chapter 112 `நலம் புனைந்து உரைத்தல்`; Part 012 contains only Kural **1111–1115** of that chapter.

The English first-pass layer must preserve the same physical alignment, including scans 252 and 253.

# Part 012 Tamil direct-verification corrections

These three corrections are authoritative and must be the basis for English translation:

1. scan **239 / Kural 1018 commentary**:
   `அகன்றுவிட்டதாகக் கருத வேண்டும்.`
2. scan **242 / Kural 1035 commentary**:
   `ஊதியம் பெற்று உண்ணும் இயல்புடையவர்`
3. scan **245 / Kural 1048 commentary**:
   `கொலை செய்வதுபோல நேற்று...`

# Part 012 protected source-sensitive readings

Do not normalize these from another edition or memory.

## Kural 1077 — scan 251

```text
ஈங்கை விதிரார் கயவர் கொடிறுடைக்குங்
கூன்கையர் அல்லா தவர்க்கு.
```

## Kural 1098 — scan 257

```text
அசையியற் குண்டாண்டோர் ஏஎர்யான் நோக்கப்
பசையினள் பைய நகும்.
```

Translate these edition-specific readings using Kalaignar's adjacent commentary as the primary interpretive aid. Do not substitute a familiar conventional Kural wording.

# Part 012 English current state

**NOT STARTED — eligible for first pass.**

Expected aligned English physical pages: **23**.

Expected English filename set mirrors the Tamil Part 012 filenames:

- `0238-porul-naanudaimai-01.md`
- `0239-porul-naanudaimai-02.md`
- `0240-porul-kudiseyal-vagai-01.md`
- `0241-porul-kudiseyal-vagai-02.md`
- `0242-porul-uzhavu-01.md`
- `0243-porul-uzhavu-02.md`
- `0244-porul-nalkuravu-01.md`
- `0245-porul-nalkuravu-02.md`
- `0246-porul-iravu-01.md`
- `0247-porul-iravu-02.md`
- `0248-porul-iravachcham-01.md`
- `0249-porul-iravachcham-02.md`
- `0250-porul-kayamai-01.md`
- `0251-porul-kayamai-02.md`
- `0252-inbam-title.md`
- `0253-blank.md`
- `0254-inbam-thagai-ananguruththal-01.md`
- `0255-inbam-thagai-ananguruththal-02.md`
- `0256-inbam-kuripparithal-01.md`
- `0257-inbam-kuripparithal-02.md`
- `0258-inbam-punarchchi-magizhthal-01.md`
- `0259-inbam-punarchchi-magizhthal-02.md`
- `0260-inbam-nalam-punaindhuraiththal-01.md`

# Exact next activity

**Part 012 English project translation — first pass for all 23 aligned physical pages / scans 238–260.**

Required procedure:

1. fresh-read all mandatory English startup files listed above;
2. inspect the target English directory first and continue existing Part 012 files if any rather than creating duplicates;
3. use `AUDIT_PART_012.md` and the 23 verified Tamil records as the working basis; the Tamil scan remains ultimate authority;
4. mirror all 23 Tamil filenames under `works/thirukkural/translations/en/pages/`;
5. every new Part 012 English record must use:
   ```yaml
   translation_type: "project_translation"
   status: "draft"
   source_tamil_status: "verified"
   translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
   ```
6. preserve Kural number and the source-supported two-line English verse structure on commentary pages;
7. keep the Kural translation separate from Kalaignar commentary translation;
8. preserve one-to-one physical alignment for scan 252 (`இன்பம்` title leaf) and scan 253 (blank/reverse-show-through leaf), using the established English treatment for non-body physical pages;
9. preserve the structural transition from `பொருள் — குடியியல்` to `இன்பம் — களவியல்`;
10. determine new English structural/chapter headings provisionally from the Tamil main-body context and existing glossary conventions; do not finalize new glossary controls in the first-pass gate unless prior project practice clearly requires it;
11. protect the Kural 1077 and Kural 1098 edition-specific readings and Kalaignar's commentary direction;
12. translate Kalaignar's actual wording/images rather than importing another commentator or standard English Kural;
13. create all **23 / 23** aligned records as `draft` if safely possible;
14. synchronize English `TRANSLATION_STATUS.md`, English README, work README, root README and this `HANDOVER.md` after first pass;
15. stop after first pass;
16. **do not perform direct source-check in the same activity**;
17. **do not perform editorial/glossary review or release in the same activity**;
18. **do not begin Part 013 Tamil transcription**;
19. **do not alter released English Parts 001–011**.

If all 23 first-pass records are safely created, the following exact activity will be **Part 012 English direct source-check**.
