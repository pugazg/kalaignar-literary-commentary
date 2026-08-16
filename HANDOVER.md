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
7. if English work later becomes active, fresh-read `TRANSLATION_GUIDE.md`, `GLOSSARY.md`, `TRANSLATION_STATUS.md`, and the latest review/release artefacts.

Repository state is authoritative.

## Source rule

The supplied Tamil scans are controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

Source PDFs are working/control sources and are not to be committed to GitHub unless the user explicitly requests that.

OCR/parsed text may assist but is never authoritative over direct inspection of the scan.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Keep these as separate gates.

Every project-created English page must identify `translation_type: "project_translation"`.

Released English material must not be revised merely to harmonize later vocabulary. Permanent earlier protections remain binding, including:

- chapter 38 `ஊழ்` → **Oozh**;
- Kalaignar's `இயற்கை நிலை` → **natural condition**;
- Kural 543 `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**;
- preservation of Kalaignar's governance, citizens, working-people, justice, public-resource and rational/inquiry vocabulary where the Tamil explicitly uses it.

# Established released baseline

## Tamil

Parts **001–011 are audited / ARCHIVAL-READY continuously** through overall scan **237 / printed page 204 / Kural 1010**.

Latest completed Tamil audit: `works/thirukkural/AUDIT_PART_011.md` — **PASS / ARCHIVAL-READY**.

## English

Parts **001–011 are fully released continuously through Kural 1010**.

Latest English release artefacts:

- `works/thirukkural/translations/en/reviews/PART_011_REVIEW.md`;
- `works/thirukkural/translations/en/reviews/PART_011_RELEASE_REPORT.md` — **PASS / RELEASE APPROVED**.

All released Part 011 corrections/protections recorded in those artefacts remain binding.

# Supplied later sources

- Part 012 — `திருக்குறள்_கலைஞர்_உரை_part_012_pages_238-260.pdf` — **23 pages**;
- Part 013 — `திருக்குறள்_கலைஞர்_உரை_part_013_pages_261-282.pdf` — **22 pages**;
- Part 014 — `திருக்குறள்_கலைஞர்_உரை_part_014_pages_283-302.pdf` — **20 pages**;
- Part 015 — `திருக்குறள்_கலைஞர்_உரை_part_015_pages_303-323.pdf` — **21 pages**.

Part **012** has completed Tamil first pass and direct visual verification. Parts **013–015 remain received but not started**.

# Part 012 controlling source

`திருக்குறள்_கலைஞர்_உரை_part_012_pages_238-260.pdf`

Supplied-file identity used for direct inspection: `file_00000000f4288211a7bbe05c015edc20`.

## Verified source scope

- physical pages: **23 / 23**;
- overall scans: **238–260**;
- Part-local pages: **1–23**;
- printed pages: **205–218**, then two unnumbered section leaves, then **221–227**;
- Kural range physically present: **1011–1115**;
- `verified`: **23 / 23**;
- `needs-review`: **0**;
- `partial`: **0**;
- `blocked`: **0**;
- audit: **not started**.

Every Part 012 page now uses:

```yaml
status: "verified"
transcription_method: "direct visual comparison with source scan"
```

The Part 011 → Part 012 boundary is source-supported and continuous at printed **204 → 205 / Kural 1010 → 1011**.

The supplied Part 013 first page was inspected only for outgoing-boundary context. It is printed page **228** and carries Kural **1116–1120**, confirming continuation after Part 012. **No Part 013 page record has been created.**

# Part 012 source-visible structure — directly verified

1. scans **238–251** — `பொருள் — குடியியல்`, chapters 102–108, Kural **1011–1080**;
2. scan **252** — centered section-title leaf `இன்பம்`;
3. scan **253** — no independent printed body text; reverse-side show-through only;
4. scans **254–260** — `இன்பம் — களவியல்`, Kural **1081–1115**;
5. scan **260 / printed page 227** begins chapter 112 `நலம் புனைந்து உரைத்தல்`; only Kural **1111–1115** of that chapter are present in Part 012.

# Part 012 direct-verification corrections

Exactly three real first-pass corrections were required and are now authoritative:

1. scan **239 / Kural 1018 commentary**
   - first pass: `அகன்றுவிடத்தான் வேண்டும்.`
   - verified: `அகன்றுவிட்டதாகக் கருத வேண்டும்.`
2. scan **242 / Kural 1035 commentary**
   - first pass: `ஊதியம் பெற்று உண்பும் இயல்புடையவர்`
   - verified: `ஊதியம் பெற்று உண்ணும் இயல்புடையவர்`
3. scan **245 / Kural 1048 commentary**
   - first pass: `கொலை செய்வதுபோல் நேற்று...`
   - verified: `கொலை செய்வதுபோல நேற்று...`

# Part 012 protected source-sensitive readings

These were explicitly re-read from the scan during verification and must not be normalized from a familiar edition:

- scan **251 / Kural 1077**:
  ```text
  ஈங்கை விதிரார் கயவர் கொடிறுடைக்குங்
  கூன்கையர் அல்லா தவர்க்கு.
  ```
- scan **257 / Kural 1098**:
  ```text
  அசையியற் குண்டாண்டோர் ஏஎர்யான் நோக்கப்
  பசையினள் பைய நகும்.
  ```

# Part 012 current gate state

**Tamil direct visual verification: COMPLETE — 23 / 23 verified.**

Part 012 is **not yet ARCHIVAL-READY** because the part audit is a separate mandatory gate.

No `AUDIT_PART_012.md` has been created yet.

Part 012 English has **not** started and remains ineligible until the Tamil audit passes.

# Exact next activity

**Part 012 Tamil audit / archival-ready gate.**

Required audit procedure:

1. fresh-read the mandatory startup files;
2. inspect the Part 012 verified page records and controlling scan as needed;
3. confirm all **23 / 23** expected physical page records exist;
4. confirm overall scans **238–260** and Part-local pages **1–23** are continuous;
5. confirm printed-page progression **205–218 → two unnumbered leaves → 221–227** is source-supported;
6. confirm Kural continuity **1011–1115** with no gap or duplication;
7. confirm chapter/section transitions, including `பொருள் — குடியியல்` → `இன்பம்` title/blank leaves → `இன்பம் — களவியல்`;
8. confirm the incoming boundary printed **204 → 205 / Kural 1010 → 1011**;
9. confirm the outgoing boundary context at printed **227 → 228 / Kural 1115 → 1116** using the supplied Part 013 first page without starting Part 013 transcription;
10. confirm all **23** records are `verified`, with no unresolved `needs-review`, `partial` or `blocked` records;
11. document the three verification corrections and the protected Kural 1077 / 1098 readings;
12. create `works/thirukkural/AUDIT_PART_012.md` with an explicit PASS/FAIL and archival-ready decision;
13. synchronize repository status documents after the audit decision;
14. stop after the Tamil audit gate.

Do **not** begin Part 012 English during the audit activity. Do **not** begin Part 013 transcription. Do **not** alter released English Parts 001–011.

If the audit passes, the following separate activity will be **Part 012 English project translation — first pass**, with aligned English pages created as `draft` only.
