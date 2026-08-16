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
   - all 23 current Part 011 English `source-checked` pages.

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
- `verified`: **23 / 23**;
- unresolved: **0**.

The Part 010 → Part 011 boundary passes at printed **181 → 182 / Kural 895 → 896**.

The source structural transition is:

- scans **215–225**: `பொருள் — நட்பியல்`;
- from scan **226 / printed page 193 / chapter 96 குடிமை**: `பொருள் — குடியியல்`.

## English project translation

Parts **001–010 are fully released continuously through Kural 895**.

Part **011 English first-pass and direct source-check are COMPLETE 23 / 23**.

Current Part 011 English state:

- `draft`: **0**;
- `source-checked`: **23 / 23**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

Every Part 011 English page now carries:

```yaml
translation_type: "project_translation"
status: "source-checked"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

No `PART_011_REVIEW.md` or Part 011 release report exists yet.

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

# Part 011 English structural / heading state

Scan 215 continues the already released chapter 90 heading **Not Offending the Great**.

`நட்பியல்` → **Friendship** is already released and controlled.

`குடியியல்` → **Civic Life** remains **provisional** after source-check. Do not treat it as glossary-final until the next editorial/glossary gate.

Current chapter headings 91–101 also remain provisional:

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

# Tamil verification corrections that remain authoritative

The audited Tamil basis retains these four corrections:

1. scan **216 / Kural 904** verse: `மனையாளை யஞ்சும்`;
2. scan **216 / Kural 905** verse: `இல்லாளை யஞ்சுவான்`;
3. scan **218 / Kural 911 commentary**: `பொருள் திரட்டுவதையே`;
4. scan **221 / Kural 927 commentary**: `மயங்குவதைக் கண்டு`.

# Part 011 English source-check corrections

Six substantive source-fidelity corrections/refinements were made during direct source-check:

1. **Kural 911** — **bring ruin** → **bring suffering**, following Kalaignar's `துன்பமே வந்து சேரும்` explanation.
2. **Kural 926** — restored the source's two-line relationship: sleepers/dead in line 1 and liquor/poison in line 2.
3. **Kural 953** — **true nobility** → **truthful citizens**, following Kalaignar's explicit `வாய்மையுள்ள குடிமக்கள்` interpretation.
4. **Kural 961** — removed unsupported **to one's distinction** from “indispensable”; the Kural now says to abandon even an indispensable act if it diminishes one's distinction.
5. **Kural 989** — removed the commentary-only image of all the seas overturning from the Kural; the image remains in Kalaignar's commentary.
6. **Kural 1006** — corrected the subject relationship so the person who neither enjoys nor gives is **a disease upon his great wealth**.

No other substantive first-pass English change was required.

# Source-sensitive Part 011 protections after source-check

Do not normalize these in editorial review:

- **Kural 899 commentary** — retain **“an oppressive government will be shaken and destroyed”** for `அடக்குமுறை ஆட்சி`;
- **Kural 912 commentary** — retain the sugar-sweet sense of `பாகுமொழிபேசும்`;
- **Kural 931 commentary** — retain the fish, bait and iron-hook image;
- **Kural 948 commentary** — retain **“This applies not only to bodily disease but also to social disease.”**;
- **Kural 966 commentary** — retain Kalaignar's rationalist **“Will some nonexistent heaven be gained?”** question;
- **Kural 971** — retain translation from this edition's unusual audited printed wording; do not substitute a familiar external Kural;
- **Kural 972 commentary** — retain **“Everyone is equal by birth. Difference can be seen only in the skill they show in the work they do.”**;
- **Kural 985** verse — no terminal period, following source punctuation;
- **Kural 1001 commentary** — retain the image of wealth accumulated beyond what a house can contain;
- **Kural 1008** verse — no terminal period, following source punctuation;
- retain source images including the stranger's corpse in a dark room, “Mohini spell,” mire called hell, liquor/poison comparison, torch under water, gambling hook, medical triad, `kunrimani`, `kavari` deer, queens of chastity, file/tree image, dirty-vessel/milk image, poisonous fruit, and the miser as a disease infecting wealth.

# Exact next activity

**Part 011 English editorial consistency / glossary reconciliation — all 23 `source-checked` pages.**

Required procedure:

1. fresh-read all mandatory startup files listed above;
2. inspect all 23 Part 011 English `source-checked` pages and the audited Tamil basis;
3. review readability, recurring terminology, punctuation, names, social/gender specificity and heading consistency without weakening or normalizing Kalaignar's wording;
4. deliberately finalize `குடியியல்` using the actual Part 011 main-body context;
5. deliberately finalize chapter headings **91–101**;
6. preserve all six English source-check corrections and all protected source-sensitive treatments above;
7. update `works/thirukkural/translations/en/GLOSSARY.md` with the controlled Part 011 structural/chapter decisions;
8. create `works/thirukkural/translations/en/reviews/PART_011_REVIEW.md` documenting the editorial decisions and any editorial-only changes;
9. promote passing Part 011 pages only to:

```yaml
status: "editorial-reviewed"
```

10. synchronize `TRANSLATION_STATUS.md`, English README, work README, root README and HANDOVER;
11. stop after editorial review;
12. **do not create `PART_011_RELEASE_REPORT.md` in the same activity**;
13. **do not promote pages to `release-ready` in the same activity**;
14. **do not alter released English Parts 001–010 merely to harmonize later vocabulary**;
15. **do not infer or create Kural 1011 onward**.

After editorial review, the exact next activity becomes the separate **Part 011 English release gate**.
