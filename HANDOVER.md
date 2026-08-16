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
6. inspect the actual controlling source scan needed for the activity;
7. for English work additionally fresh-read:
   - `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`;
   - `works/thirukkural/translations/en/GLOSSARY.md`;
   - `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
   - `works/thirukkural/translations/en/reviews/PART_010_REVIEW.md`;
   - `works/thirukkural/translations/en/reviews/PART_010_RELEASE_REPORT.md`;
   - `works/thirukkural/AUDIT_PART_011.md`;
   - all 23 audited Part 011 Tamil page records.

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
- Kural 543's Kalaignar-directed `அறவோர் நூல்களுக்கும்` → **the books of the virtuous** rather than an automatic caste-specific conventional gloss;
- preservation of Kalaignar's governance, citizens, working-people, justice, public-resource and rational/inquiry vocabulary where the Tamil explicitly uses it.

# Established state

## Tamil

Parts **001–011 are audited / ARCHIVAL-READY continuously** through:

- overall scan **237**;
- printed page **204**;
- Kural **1010**.

Latest completed Tamil audit:

`works/thirukkural/AUDIT_PART_011.md` — **PASS / ARCHIVAL-READY**.

Part 011 final Tamil state:

- physical pages: **23 / 23**;
- scans: **215–237**;
- Part-local pages: **1–23**;
- printed pages: **182–204**;
- Kural range: **896–1010**;
- `verified`: **23 / 23**;
- `needs-review`: **0**;
- `partial`: **0**;
- `blocked`: **0**;
- unresolved/missing: **0**.

## English project translation

Parts **001–010 are fully released continuously through Kural 895**.

Part 011 English has **not started**. It is now eligible for the first-pass translation gate because the Tamil audit passed.

Released Part 010 English protections remain binding and must not be modified merely because Part 011 introduces related vocabulary:

1. Kural 813 / 822 — **women for hire**;
2. Kural 842 commentary — no unsupported **earned**;
3. Kural 849 — corrected source-grounded subject relationship;
4. Kural 850 — evidence clause stays commentary-only; retain evidence/truth framing and **“ghosts”** image;
5. Kural 867 commentary — no unsupported “and harmful to us”;
6. Kural 887 — retain *seppu* without inventing “metal”;
7. Kural 835 — **seven periods**, not “seven births”;
8. Kural 861 — retain Kalaignar's supplied interpretation;
9. Kural 869 — retain **“cowards who are afraid, and ignorant cowards”**;
10. Kural 876 — retain the nuanced enemy/friendship stance;
11. Kural 895 — retain Kural **ruler** / commentary **government** distinction.

# Part 011 controlling source

`திருக்குறள்_கலைஞர்_உரை_part_011_pages_215-237.pdf`

Supplied-file identity used for verification/audit: `file_0000000076208208aa848290e8fe125d`.

Audited source scope:

- physical pages: **23**;
- overall scans: **215–237**;
- Part-local pages: **1–23**;
- printed pages: **182–204**;
- Kural range: **896–1010**.

Incoming continuity is confirmed:

- Part 010 final page: printed **181 / Kural 895**;
- Part 011 first page: printed **182 / Kural 896**.

No Kural **1011** or later Tamil/English text has been inferred or created.

# Part 011 chapter / page map

- scan **215** / p182 — chapter 90 `பெரியாரைப் பிழையாமை`, Kural **896–900**, completing the chapter begun in Part 010;
- scans **216–217** / pp183–184 — chapter 91 `பெண்வழிச் சேறல்`, Kural **901–910**;
- scans **218–219** / pp185–186 — chapter 92 `வரைவின் மகளிர்`, Kural **911–920**;
- scans **220–221** / pp187–188 — chapter 93 `கள்ளுண்ணாமை`, Kural **921–930**;
- scans **222–223** / pp189–190 — chapter 94 `சூது`, Kural **931–940**;
- scans **224–225** / pp191–192 — chapter 95 `மருந்து`, Kural **941–950**;
- scans **226–227** / pp193–194 — chapter 96 `குடிமை`, Kural **951–960**;
- scans **228–229** / pp195–196 — chapter 97 `மானம்`, Kural **961–970**;
- scans **230–231** / pp197–198 — chapter 98 `பெருமை`, Kural **971–980**;
- scans **232–233** / pp199–200 — chapter 99 `சான்றாண்மை`, Kural **981–990**;
- scans **234–235** / pp201–202 — chapter 100 `பண்புடைமை`, Kural **991–1000**;
- scans **236–237** / pp203–204 — chapter 101 `நன்றியில் செல்வம்`, Kural **1001–1010**.

# Part 011 structural transition

Preserve the actual running-header structure:

- scans **215–225**: `பொருள் — நட்பியல்`;
- from scan **226 / printed page 193 / chapter 96 குடிமை**: `பொருள் — குடியியல்`.

`நட்பியல்` is already a released controlled English structural term: **Friendship**. Do not revise earlier released Parts merely because Part 011 later changes to `குடியியல்`.

`குடியியல்` is newly encountered as a structural label in the English workflow. During first pass, choose a source-led **provisional** English rendering based on Kalaignar's actual Part 011 context; do not treat that provisional choice as glossary-final. The later editorial/glossary gate will finalize it.

# Part 011 verified Tamil page files

All 23 use:

```yaml
status: "verified"
transcription_method: "direct visual comparison with source scan"
```

Files:

1. `pages/0215-porul-periyaaraip-pizhaiyaamai-02.md`
2. `pages/0216-porul-penvazhich-seral-01.md`
3. `pages/0217-porul-penvazhich-seral-02.md`
4. `pages/0218-porul-varaivin-magalir-01.md`
5. `pages/0219-porul-varaivin-magalir-02.md`
6. `pages/0220-porul-kallunnamai-01.md`
7. `pages/0221-porul-kallunnamai-02.md`
8. `pages/0222-porul-soothu-01.md`
9. `pages/0223-porul-soothu-02.md`
10. `pages/0224-porul-marunthu-01.md`
11. `pages/0225-porul-marunthu-02.md`
12. `pages/0226-porul-kudimai-01.md`
13. `pages/0227-porul-kudimai-02.md`
14. `pages/0228-porul-maanam-01.md`
15. `pages/0229-porul-maanam-02.md`
16. `pages/0230-porul-perumai-01.md`
17. `pages/0231-porul-perumai-02.md`
18. `pages/0232-porul-saanraanmai-01.md`
19. `pages/0233-porul-saanraanmai-02.md`
20. `pages/0234-porul-panpudaimai-01.md`
21. `pages/0235-porul-panpudaimai-02.md`
22. `pages/0236-porul-nanriyil-selvam-01.md`
23. `pages/0237-porul-nanriyil-selvam-02.md`

# Direct-verification corrections retained by the audit

Exactly four real first-pass corrections were found and remain authoritative:

1. scan **216 / Kural 904** verse: **`மனையாளை யஞ்சும்`**;
2. scan **216 / Kural 905** verse: **`இல்லாளை யஞ்சுவான்`**;
3. scan **218 / Kural 911 commentary**: **`பொருள் திரட்டுவதையே`**;
4. scan **221 / Kural 927 commentary**: **`மயங்குவதைக் கண்டு`**.

English first pass must use the corrected audited records, never the pre-verification wording.

# Source-sensitive Part 011 readings to protect in English

Do not normalize these merely because another reading/interpretation may be familiar:

- **Kural 899 commentary**: `உயர்ந்த கொள்கை உறுதி கொண்டவர்கள் சீறி எழுந்தால் அடக்குமுறை ஆட்சி நிலைகுலைந்து அழிந்து விடும்.` Preserve Kalaignar's explicit governance framing.
- **Kural 912 commentary**: `பாகுமொழிபேசும்`.
- **Kural 931 commentary**: `கெளவிக் கொண்டு போவதாகிவிடும்`; preserve the fish/hook image.
- **Kural 948 commentary**: `உடல் நோய்க்கு மட்டுமின்றிச் சமுதாய நோய்க்கும் இது பொருந்தும்.` Preserve the extension from bodily illness to social illness.
- **Kural 971** printed verse: `ஒளியொருவற் குள்ள வெறுக்கை இளியொருவற் / கஃதிறந்து வாழ்தும் எனல்.` Translate this audited source wording rather than importing a familiar Kural edition.
- **Kural 972 commentary**: `பிறப்பினால் அனைவரும் சமம். செய்யும் தொழிலில் காட்டுகிற திறமையில் மட்டுமே வேறுபாடு காண முடியும்.` Preserve Kalaignar's explicit equality formulation.
- **Kural 985** verse has no terminal period in this source.
- **Kural 1001 commentary** begins `அடங்காத ஆசையினால் வீடு கொள்ளாத அளவுக்குச் செல்வத்தைச் சேர்த்து வைத்து...`.
- **Kural 1008** verse has no terminal period in this source.

# Exact next activity

**Part 011 English project translation — first pass for all 23 aligned pages.**

Required procedure:

1. fresh-read all mandatory startup files listed above;
2. inspect the target directory `works/thirukkural/translations/en/pages/` first and continue existing Part 011 files if any rather than creating duplicates;
3. inspect representative released Part 010 English pages, especially the chapter-90 opening page, so scan 215 continues the already released chapter heading **Not Offending the Great** consistently;
4. inspect all 23 audited Part 011 Tamil pages;
5. create the 23 aligned English mirror files for scans **215–237**;
6. every new English page must carry:

```yaml
translation_type: "project_translation"
status: "draft"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

7. keep the Kural number and source-supported two-line structure;
8. keep Kural translation separate from Kalaignar commentary translation;
9. preserve one-to-one page alignment and the `நட்பியல்` → `குடியியல்` source transition;
10. retain Kalaignar's actual language, images, governance/social vocabulary and interpretive direction; do not substitute a standard Kural gloss;
11. use the already released chapter-90 English heading **Not Offending the Great** on scan 215;
12. make new chapter headings 91–101 and `குடியியல்` only **provisional first-pass choices**; do not revise released earlier pages and do not treat new wording as glossary-final during this gate;
13. protect the Part 011 source-sensitive readings listed above;
14. create exactly **23** Part 011 English records as `draft` if safely possible;
15. synchronize English `TRANSLATION_STATUS.md`, English README, work README, root README and HANDOVER after the first-pass gate;
16. stop after all 23 pages are `draft`;
17. **do not perform English direct source-check in the same activity**;
18. **do not create `PART_011_REVIEW.md` or a release report yet**;
19. **do not infer or create Kural 1011 onward**;
20. **do not alter released English Parts 001–010**.

After first pass, the exact next activity becomes **Part 011 English direct source-check — all 23 draft pages**.
