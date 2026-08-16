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

Part **011 Tamil first-pass transcription is COMPLETE 23 / 23**, but it is **not yet verified or archival-ready**.

Part 011 current Tamil status:

- `needs-review`: **23 / 23**;
- `verified`: **0**;
- `partial`: **0**;
- `blocked`: **0**.

## English project translation

Parts **001–010 are fully released continuously through the supplied Kural 895**.

Part 011 English has **not started** and must not start until Part 011 Tamil direct verification and the separate Part 011 Tamil audit are complete.

Part 010 editorial review:

`works/thirukkural/translations/en/reviews/PART_010_REVIEW.md`

Part 010 release report:

`works/thirukkural/translations/en/reviews/PART_010_RELEASE_REPORT.md` — **PASS / RELEASE APPROVED**.

# Part 011 controlling source

`திருக்குறள்_கலைஞர்_உரை_part_011_pages_215-237.pdf`

Current supplied-file identity: `file_0000000076208208aa848290e8fe125d`.

The actual scan was inspected directly before transcription.

Source scope:

- physical pages: **23**;
- overall scans: **215–237**;
- Part-local pages: **1–23**;
- printed pages: **182–204**;
- Kural range present: **896–1010**.

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

Preserve the actual running-header structure. Do not flatten it:

- scans **215–225**: `பொருள் — நட்பியல்`;
- scan **226 / printed page 193 / chapter 96 குடிமை** onward: `பொருள் — குடியியல்`.

The first-pass page metadata already reflects this transition.

# Part 011 first-pass page files

All are currently `status: "needs-review"` with:

```yaml
transcription_method: "manual transcription from source scan; direct visual verification pending"
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

# Source-sensitive Part 011 material to protect during verification

Do not normalize these merely because another reading may be familiar. Verify them directly against the supplied scan:

- **Kural 899 commentary** explicitly uses Kalaignar's governance language: `உயர்ந்த கொள்கை உறுதி கொண்டவர்கள் சீறி எழுந்தால் அடக்குமுறை ஆட்சி நிலைகுலைந்து அழிந்து விடும்.`
- **Kural 948 commentary** explicitly extends its diagnostic method beyond bodily illness: `உடல் நோய்க்கு மட்டுமின்றிச் சமுதாய நோய்க்கும் இது பொருந்தும்.`
- **Kural 972 commentary** explicitly says: `பிறப்பினால் அனைவரும் சமம். செய்யும் தொழிலில் காட்டுகிற திறமையில் மட்டுமே வேறுபாடு காண முடியும்.`
- scan **218 / Kural 911 commentary** first pass preserves the source-looking form `பொருள் திரட்டுவதைமே`; verify rather than silently regularize it.
- scan **218 / Kural 912 commentary** first pass preserves `பாகுமொழிபேசும்`; verify directly.
- scan **222 / Kural 931 commentary** contains the fish/hook image and the first pass has `கெளவிக் கொண்டு போவதாகிவிடும்`; verify directly.
- scan **230 / Kural 971** preserves the printed split/orthography `ஒளியொருவற் குள்ள வெறுக்கை இளியொருவற் / கஃதிறந்து வாழ்தும் எனல்.`
- scan **232 / Kural 985** is currently transcribed without a terminal period in the verse because the scan appears that way; verify.
- scan **236 / Kural 1001 commentary** begins in first pass `அடங்காத ஆசையினால் வீடு கொள்ளாத அளவுக்குச் செல்வத்தைச் சேர்த்து வைத்து...`; verify directly.
- scan **237 / Kural 1008** is currently transcribed without a terminal period in the verse because the scan appears that way; verify.

# Released Part 010 English protections remain binding

Do not modify released Part 010 merely because Part 011 introduces related vocabulary.

Protected released decisions include:

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

# Exact next activity

**Part 011 Tamil direct visual verification — all 23 pages.**

Required procedure:

1. fresh-read the mandatory startup files above;
2. inspect all 23 Part 011 Tamil records already in `works/thirukkural/pages/`;
3. inspect all 23 controlling source page images, scans **215–237**;
4. compare line-by-line:
   - Kural text letter-for-letter;
   - two-line verse structure;
   - joins / spacing supported by the edition;
   - punctuation;
   - chapter headings;
   - running-header structural section;
   - Kalaignar commentary wording and paragraph boundary;
   - scan / Part-local / printed-page metadata;
5. correct the first-pass record only where the scan clearly requires it;
6. document every real correction found;
7. for each passing page set:

```yaml
status: "verified"
transcription_method: "direct visual comparison with source scan"
```

8. finish all **23 / 23** pages in this verification gate if safely possible;
9. stop after verification;
10. **do not create `AUDIT_PART_011.md` during this activity**;
11. **do not begin Part 011 English translation**;
12. after verification, the exact next activity becomes the separate **Part 011 Tamil audit / archival-ready gate**.
