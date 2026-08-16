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
   - all 23 audited Part 011 Tamil pages;
   - all 23 current Part 011 English draft pages.

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

Part 011 Tamil final state:

- physical pages: **23 / 23**;
- scans: **215–237**;
- Part-local pages: **1–23**;
- printed pages: **182–204**;
- Kural range: **896–1010**;
- `verified`: **23 / 23**;
- unresolved: **0**.

## English project translation

Parts **001–010 are fully released continuously through Kural 895**.

Part **011 English first-pass translation is COMPLETE 23 / 23**.

Current Part 011 English state:

- `draft`: **23 / 23**;
- `source-checked`: **0**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

All Part 011 English pages use:

```yaml
translation_type: "project_translation"
status: "draft"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

No Part 011 source-check has yet been performed. No Part 011 review or release report exists.

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

Audited source scope:

- physical pages: **23**;
- overall scans: **215–237**;
- Part-local pages: **1–23**;
- printed pages: **182–204**;
- Kural range: **896–1010**.

Incoming continuity:

- Part 010 final page: printed **181 / Kural 895**;
- Part 011 first page: printed **182 / Kural 896**.

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

# Part 011 structural transition

The actual source transition is preserved in the English draft:

- scans **215–225**: `பொருள் — நட்பியல்` → `Porul — Friendship`;
- from scan **226 / printed page 193 / chapter 96 குடிமை**: `பொருள் — குடியியல்` → provisional `Porul — Civic Life`.

`நட்பியல்` → **Friendship** is already released and controlled.

`குடியியல்` → **Civic Life** is only a **first-pass provisional** choice. Do not add it to `GLOSSARY.md` or treat it as final during the source-check gate. The later editorial/glossary gate must finalize it.

# Part 011 English draft files

1. `translations/en/pages/0215-porul-periyaaraip-pizhaiyaamai-02.md`
2. `translations/en/pages/0216-porul-penvazhich-seral-01.md`
3. `translations/en/pages/0217-porul-penvazhich-seral-02.md`
4. `translations/en/pages/0218-porul-varaivin-magalir-01.md`
5. `translations/en/pages/0219-porul-varaivin-magalir-02.md`
6. `translations/en/pages/0220-porul-kallunnamai-01.md`
7. `translations/en/pages/0221-porul-kallunnamai-02.md`
8. `translations/en/pages/0222-porul-soothu-01.md`
9. `translations/en/pages/0223-porul-soothu-02.md`
10. `translations/en/pages/0224-porul-marunthu-01.md`
11. `translations/en/pages/0225-porul-marunthu-02.md`
12. `translations/en/pages/0226-porul-kudimai-01.md`
13. `translations/en/pages/0227-porul-kudimai-02.md`
14. `translations/en/pages/0228-porul-maanam-01.md`
15. `translations/en/pages/0229-porul-maanam-02.md`
16. `translations/en/pages/0230-porul-perumai-01.md`
17. `translations/en/pages/0231-porul-perumai-02.md`
18. `translations/en/pages/0232-porul-saanraanmai-01.md`
19. `translations/en/pages/0233-porul-saanraanmai-02.md`
20. `translations/en/pages/0234-porul-panpudaimai-01.md`
21. `translations/en/pages/0235-porul-panpudaimai-02.md`
22. `translations/en/pages/0236-porul-nanriyil-selvam-01.md`
23. `translations/en/pages/0237-porul-nanriyil-selvam-02.md`

# Part 011 first-pass headings

Chapter 90 continues the already released **Not Offending the Great**.

The following new headings are provisional until editorial/glossary reconciliation:

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

Do not revise released earlier pages merely to harmonize these provisional choices.

# Direct-verification corrections used by the English draft

The audited Tamil corrections remain the translation basis:

1. scan **216 / Kural 904** verse: `மனையாளை யஞ்சும்`;
2. scan **216 / Kural 905** verse: `இல்லாளை யஞ்சுவான்`;
3. scan **218 / Kural 911 commentary**: `பொருள் திரட்டுவதையே`;
4. scan **221 / Kural 927 commentary**: `மயங்குவதைக் கண்டு`.

# Source-sensitive Part 011 draft protections

The first pass deliberately preserves:

- **Kural 899 commentary** — `அடக்குமுறை ஆட்சி` → draft **“an oppressive government will be shaken and destroyed”**;
- **Kural 912 commentary** — `பாகுமொழிபேசும்` represented through sugar-sweet speech rather than a generic moral paraphrase;
- **Kural 931 commentary** — fish, bait and iron-hook image retained;
- **Kural 948 commentary** — **“This applies not only to bodily disease but also to social disease.”**;
- **Kural 971** — draft translated from the unusual audited printed wording, not an external familiar Kural;
- **Kural 972 commentary** — **“Everyone is equal by birth. Difference can be seen only in the skill they show in the work they do.”**;
- **Kural 985** verse — no terminal period in the draft, following the audited source punctuation;
- **Kural 1001 commentary** — keeps the image of wealth accumulated beyond what a house can contain;
- **Kural 1008** verse — no terminal period in the draft;
- **Kural 966 commentary** — Kalaignar's rationalist question retained as **“Will some nonexistent heaven be gained?”**;
- source images including the stranger's corpse in a dark room, “Mohini spell,” mire called hell, liquor/poison comparison, torch under water, gambling hook, the medical triad, `kunrimani`, `kavari` deer, queens of chastity, file/tree image, dirty-vessel/milk image, poisonous fruit, and the miser as a disease infecting wealth.

These are first-pass translations, not source-checked decisions. The next gate must compare them against the audited Tamil and correct any omission, unsupported addition, subject drift, lost image or interpretive drift.

# Exact next activity

**Part 011 English direct source-check — all 23 draft pages.**

Required procedure:

1. fresh-read all mandatory startup files;
2. inspect all 23 current Part 011 English draft pages;
3. inspect all 23 audited Part 011 Tamil pages;
4. compare each English Kural against the audited Tamil Kural for:
   - number;
   - two-line structure;
   - lexical/semantic meaning;
   - subject/object relationship;
   - unsupported additions;
   - missing source material;
5. compare each Kalaignar commentary translation paragraph-by-paragraph for:
   - omissions;
   - additions;
   - weakened or intensified claims;
   - lost social/governance vocabulary;
   - lost imagery or rhetorical questions;
   - conventional interpretation imported in place of Kalaignar's explanation;
6. protect the source-sensitive readings listed above;
7. correct only what the audited Tamil basis requires;
8. for each passing page change only the English status to:

```yaml
status: "source-checked"
```

9. complete all **23 / 23** pages in this source-check gate if safely possible;
10. synchronize `TRANSLATION_STATUS.md`, English README, work README, root README and HANDOVER;
11. stop after source-check;
12. **do not finalize `குடியியல்` → Civic Life or chapter headings 91–101 during source-check**;
13. **do not update `GLOSSARY.md` in this gate unless a source-check correction merely restores an already controlled earlier term**;
14. **do not create `PART_011_REVIEW.md` or a release report**;
15. **do not promote any Part 011 page to `editorial-reviewed` or `release-ready`**;
16. **do not alter released English Parts 001–010**;
17. **do not infer Kural 1011 onward**.

After source-check, the exact next activity becomes **Part 011 English editorial consistency / glossary reconciliation** for all 23 `source-checked` pages.
