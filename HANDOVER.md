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
   - the latest relevant editorial review and release report.

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

Parts **001–010 are audited / ARCHIVAL-READY continuously** through:

- overall scan **214**;
- printed page **181**;
- Kural **895**.

Latest completed Tamil audit:

`works/thirukkural/AUDIT_PART_010.md` — **PASS / ARCHIVAL-READY**.

Part **011 Tamil first-pass transcription and direct visual verification are COMPLETE 23 / 23**.

Part 011 current Tamil status:

- `verified`: **23 / 23**;
- `needs-review`: **0**;
- `partial`: **0**;
- `blocked`: **0**.

Part 011 is **not yet ARCHIVAL-READY** because its separate audit has not been performed and `AUDIT_PART_011.md` does not yet exist.

## English project translation

Parts **001–010 are fully released continuously through Kural 895**.

Part 011 English has **not started** and must not start until the separate Part 011 Tamil audit passes.

Released Part 010 English protections remain binding, including:

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

Supplied-file identity used for verification: `file_0000000076208208aa848290e8fe125d`.

Verified source scope:

- physical pages: **23**;
- overall scans: **215–237**;
- Part-local pages: **1–23**;
- printed pages: **182–204**;
- Kural range: **896–1010**.

Incoming continuity is directly confirmed:

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

All Part 011 page metadata now reflects the source-supported structure and each record uses:

```yaml
status: "verified"
transcription_method: "direct visual comparison with source scan"
```

# Direct-verification corrections

Exactly four real first-pass corrections were found and applied:

1. scan **216 / Kural 904** verse: `மனையாளை அஞ்சும்` → **`மனையாளை யஞ்சும்`**;
2. scan **216 / Kural 905** verse: `இல்லாளை அஞ்சுவான்` → **`இல்லாளை யஞ்சுவான்`**;
3. scan **218 / Kural 911 commentary**: `பொருள் திரட்டுவதைமே` → **`பொருள் திரட்டுவதையே`**;
4. scan **221 / Kural 927 commentary**: `மயங்குவதைப் கண்டு` → **`மயங்குவதைக் கண்டு`**.

No other substantive first-pass body-text correction was required.

# Source-sensitive Part 011 readings confirmed

Do not normalize these in later gates:

- **Kural 899 commentary**: `உயர்ந்த கொள்கை உறுதி கொண்டவர்கள் சீறி எழுந்தால் அடக்குமுறை ஆட்சி நிலைகுலைந்து அழிந்து விடும்.`
- **Kural 912 commentary**: `பாகுமொழிபேசும்`.
- **Kural 931 commentary**: `கெளவிக் கொண்டு போவதாகிவிடும்`.
- **Kural 948 commentary**: `உடல் நோய்க்கு மட்டுமின்றிச் சமுதாய நோய்க்கும் இது பொருந்தும்.`
- **Kural 971** printed verse: `ஒளியொருவற் குள்ள வெறுக்கை இளியொருவற் / கஃதிறந்து வாழ்தும் எனல்.`
- **Kural 972 commentary**: `பிறப்பினால் அனைவரும் சமம். செய்யும் தொழிலில் காட்டுகிற திறமையில் மட்டுமே வேறுபாடு காண முடியும்.`
- **Kural 985** verse has no terminal period in this source.
- **Kural 1001 commentary** begins `அடங்காத ஆசையினால் வீடு கொள்ளாத அளவுக்குச் செல்வத்தைச் சேர்த்து வைத்து...`.
- **Kural 1008** verse has no terminal period in this source.

# Exact next activity

**Part 011 Tamil audit / archival-ready gate.**

Required procedure:

1. fresh-read the mandatory startup files;
2. inspect all 23 verified Part 011 Tamil records;
3. confirm physical-page coverage **23 / 23** and continuous scans **215–237**;
4. confirm Part-local pages **1–23** and printed pages **182–204**;
5. confirm continuous Kural range **896–1010** and chapter coverage **90–101**;
6. confirm the Part 010 → Part 011 boundary at printed **181 → 182 / Kural 895 → 896**;
7. confirm the `பொருள் — நட்பியல்` → `பொருள் — குடியியல்` transition at scan **226 / p193**;
8. confirm all 23 statuses are `verified` and there are no unresolved `needs-review`, `partial` or `blocked` records;
9. confirm the four direct-verification corrections and source-sensitive readings above remain intact;
10. create `works/thirukkural/AUDIT_PART_011.md` and make an explicit **ARCHIVAL-READY** or non-ready decision based only on the repository/source evidence;
11. synchronize README/status/handover documents as appropriate;
12. stop after the Tamil audit gate.

Do **not** begin Part 011 English translation in the same activity. If the audit passes, the following activity becomes Part 011 English project translation — first pass.
