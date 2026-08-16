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
6. inspect the controlling source material required by the active gate;
7. for English work additionally fresh-read:
   - `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`;
   - `works/thirukkural/translations/en/GLOSSARY.md`;
   - `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
   - `works/thirukkural/AUDIT_PART_011.md`;
   - `works/thirukkural/translations/en/reviews/PART_011_REVIEW.md`;
   - `works/thirukkural/translations/en/reviews/PART_010_RELEASE_REPORT.md` as the latest completed release-gate precedent;
   - all 23 audited Part 011 Tamil page records;
   - all 23 current Part 011 English `editorial-reviewed` pages.

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

# Established state

## Tamil

Parts **001–011 are audited / ARCHIVAL-READY continuously** through:

- overall scan **237**;
- printed page **204**;
- Kural **1010**.

Latest Tamil audit:

`works/thirukkural/AUDIT_PART_011.md` — **PASS / ARCHIVAL-READY**.

Part 011 Tamil final state:

- physical pages: **23 / 23**;
- scans: **215–237**;
- Part-local pages: **1–23**;
- printed pages: **182–204**;
- Kural range: **896–1010**;
- chapters: **90–101**;
- `verified`: **23 / 23**;
- unresolved: **0**.

The Part 010 → Part 011 boundary passes at printed **181 → 182 / Kural 895 → 896**.

The source structural transition is:

- scans **215–225**: `பொருள் — நட்பியல்`;
- from scan **226 / printed page 193 / chapter 96 குடிமை**: `பொருள் — குடியியல்`.

## English project translation

Parts **001–010 are fully released continuously through Kural 895**.

Part **011 English first-pass, direct source-check and editorial consistency / glossary reconciliation are COMPLETE 23 / 23**.

Current Part 011 English state:

- `draft`: **0**;
- `source-checked`: **0**;
- `editorial-reviewed`: **23 / 23**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

Every Part 011 English page now carries:

```yaml
translation_type: "project_translation"
status: "editorial-reviewed"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

Part 011 editorial review artefact:

`works/thirukkural/translations/en/reviews/PART_011_REVIEW.md`

No Part 011 release report exists yet.

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

# Part 011 controlling source

`திருக்குறள்_கலைஞர்_உரை_part_011_pages_215-237.pdf`

Supplied-file identity used for verification/audit: `file_0000000076208208aa848290e8fe125d`.

Audited scope:

- physical pages: **23**;
- overall scans: **215–237**;
- Part-local pages: **1–23**;
- printed pages: **182–204**;
- Kural range: **896–1010**;
- chapters: **90–101**.

No Kural **1011** or later Tamil/English text has been inferred or created.

# Part 011 chapter / page map

- scan **215** / p182 — chapter 90 `பெரியாரைப் பிழையாமை`, Kural **896–900**;
- scans **216–217** — chapter 91 `பெண்வழிச் சேறல்`, Kural **901–910**;
- scans **218–219** — chapter 92 `வரைவின் மகளிர்`, Kural **911–920**;
- scans **220–221** — chapter 93 `கள்ளுண்ணாமை`, Kural **921–930**;
- scans **222–223** — chapter 94 `சூது`, Kural **931–940**;
- scans **224–225** — chapter 95 `மருந்து`, Kural **941–950**;
- scans **226–227** — chapter 96 `குடிமை`, Kural **951–960**;
- scans **228–229** — chapter 97 `மானம்`, Kural **961–970**;
- scans **230–231** — chapter 98 `பெருமை`, Kural **971–980**;
- scans **232–233** — chapter 99 `சான்றாண்மை`, Kural **981–990**;
- scans **234–235** — chapter 100 `பண்புடைமை`, Kural **991–1000**;
- scans **236–237** — chapter 101 `நன்றியில் செல்வம்`, Kural **1001–1010**.

# Part 011 controlled structure / headings

Scan 215 continues the already released chapter 90 heading **Not Offending the Great**.

Controlled structural terms:

- `நட்பியல்` → **Friendship**;
- `குடியியல்` → **Civic Life** from scan 226 onward.

Controlled chapter headings 91–101:

- 91 `பெண்வழிச் சேறல்` → **Following a Woman's Lead**;
- 92 `வரைவின் மகளிர்` → **Women Beyond Bounds**;
- 93 `கள்ளுண்ணாமை` → **Abstaining from Liquor**;
- 94 `சூது` → **Gambling**;
- 95 `மருந்து` → **Medicine**;
- 96 `குடிமை` → **Nobility**;
- 97 `மானம்` → **Honour**;
- 98 `பெருமை` → **Greatness**;
- 99 `சான்றாண்மை` → **Exemplary Character**;
- 100 `பண்புடைமை` → **Good Character**;
- 101 `நன்றியில் செல்வம்` → **Wealth Without Benefit**.

`GLOSSARY.md` now records these as controlled main-body decisions.

# Tamil verification corrections that remain authoritative

1. scan **216 / Kural 904** verse: `மனையாளை யஞ்சும்`;
2. scan **216 / Kural 905** verse: `இல்லாளை யஞ்சுவான்`;
3. scan **218 / Kural 911 commentary**: `பொருள் திரட்டுவதையே`;
4. scan **221 / Kural 927 commentary**: `மயங்குவதைக் கண்டு`.

# Part 011 English source-check corrections retained

1. **Kural 911** — **bring suffering**, not **bring ruin**.
2. **Kural 926** — sleepers/dead in line 1 and liquor/poison in line 2.
3. **Kural 953** — **truthful citizens**, following Kalaignar's `வாய்மையுள்ள குடிமக்கள்`.
4. **Kural 961** — no unsupported **to one's distinction** attached to “indispensable.”
5. **Kural 989** — all-seas-overturning image remains in commentary only, not the Kural.
6. **Kural 1006** — the person who neither enjoys nor gives is **a disease upon his great wealth**.

# Part 011 editorial refinement

The editorial gate made one additional source-led body-text refinement:

- **Kural 939**: **honour** → **fame** in the Kural's five-item list, matching Kalaignar's adjacent `புகழும்` explanation and the project's existing `புகழ்` control.

No other substantive Kural or Kalaignar-commentary body text was changed during editorial review.

# Source-sensitive Part 011 protections after editorial review

Do not normalize or weaken these at release:

- **Kural 899 commentary** — retain **“an oppressive government will be shaken and destroyed”** for `அடக்குமுறை ஆட்சி`;
- **Kural 912 commentary** — retain the sugar-sweet sense of `பாகுமொழிபேசும்`;
- **Kural 931 commentary** — retain fish, bait and iron-hook imagery;
- **Kural 948 commentary** — retain **“This applies not only to bodily disease but also to social disease.”**;
- **Kural 966 commentary** — retain Kalaignar's rationalist **“Will some nonexistent heaven be gained?”** question;
- **Kural 971** — retain translation from this edition's unusual audited printed wording; do not substitute a familiar external Kural;
- **Kural 972 commentary** — retain **“Everyone is equal by birth. Difference can be seen only in the skill they show in the work they do.”**;
- **Kural 985** verse — no terminal period, following source punctuation;
- **Kural 1001 commentary** — retain wealth accumulated beyond what a house can contain;
- **Kural 1008** verse — no terminal period, following source punctuation;
- retain the stranger's corpse in a dark room, “Mohini spell,” mire called hell, liquor/poison comparison, torch under water, gambling hook, medical triad, `kunrimani`, `kavari` deer, queens of chastity, file/tree image, dirty-vessel/milk image, poisonous fruit, and the miser as a disease infecting wealth.

# Exact next activity

**Part 011 English release gate — all 23 `editorial-reviewed` pages.**

Required procedure:

1. fresh-read the mandatory startup files listed above;
2. inspect all 23 Part 011 English `editorial-reviewed` pages and their aligned audited Tamil records;
3. confirm one-to-one English/Tamil filename and `source_tamil_file` alignment for scans **215–237**;
4. confirm printed-page continuity **182–204** and Kural continuity **896–1010**;
5. confirm `translation_type: "project_translation"`, `source_tamil_status: "verified"`, common translation basis, and `status: "editorial-reviewed"` on all 23 before promotion;
6. confirm the controlled `Friendship → Civic Life` source transition and chapter headings 90–101;
7. confirm all six source-check corrections, the Kural 939 editorial refinement, and all source-sensitive protections above;
8. confirm no Kural 1011 or later material has been inferred;
9. create `works/thirukkural/translations/en/reviews/PART_011_RELEASE_REPORT.md` only if the gate passes;
10. if the gate passes, promote all 23 Part 011 English pages from `editorial-reviewed` to `release-ready`;
11. synchronize `TRANSLATION_STATUS.md`, English README, work README, root README and HANDOVER;
12. stop after the release gate;
13. **do not begin any later Tamil source activity in the same gate**;
14. **do not alter released English Parts 001–010 merely to harmonize wording**;
15. **do not infer or create Kural 1011 onward**.

After a successful release gate, English Parts **001–011** will be released continuously through Kural **1010**. The next activity must then be determined only from an actually supplied subsequent Tamil source; do not assume or reconstruct Part 012.
