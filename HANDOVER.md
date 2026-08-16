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
   - the latest relevant Tamil audit, English review and English release report.

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

Parts **001–011 are fully released continuously through Kural 1010**.

Part 011 English release gate: **PASS / RELEASE APPROVED**.

Current Part 011 English state:

- `draft`: **0**;
- `source-checked`: **0**;
- `editorial-reviewed`: **0**;
- `release-ready`: **23 / 23**;
- `source-limited`: **0**;
- `blocked`: **0**.

Every Part 011 English page carries:

```yaml
translation_type: "project_translation"
status: "release-ready"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

Part 011 release artefacts:

- `works/thirukkural/translations/en/reviews/PART_011_REVIEW.md`;
- `works/thirukkural/translations/en/reviews/PART_011_RELEASE_REPORT.md` — **PASS / RELEASE APPROVED**.

# Released Part 011 controlled structure / headings

Controlled structural terms:

- `நட்பியல்` → **Friendship** through scan 225;
- `குடியியல்` → **Civic Life** from scan 226 onward.

Released chapter headings:

- 90 `பெரியாரைப் பிழையாமை` → **Not Offending the Great**;
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

# Part 011 corrections and protections now released

Tamil verification corrections remain authoritative:

1. Kural **904** verse: `மனையாளை யஞ்சும்`;
2. Kural **905** verse: `இல்லாளை யஞ்சுவான்`;
3. Kural **911** commentary: `பொருள் திரட்டுவதையே`;
4. Kural **927** commentary: `மயங்குவதைக் கண்டு`.

English direct source-check corrections remain released:

1. Kural **911** — **bring suffering**, not **bring ruin**;
2. Kural **926** — sleepers/dead in line 1 and liquor/poison in line 2;
3. Kural **953** — **truthful citizens**;
4. Kural **961** — no unsupported qualification attached to “indispensable”;
5. Kural **989** — all-seas-overturning image remains commentary-only;
6. Kural **1006** — the person who neither enjoys nor gives is **a disease upon his great wealth**.

Editorial refinement retained at release:

- Kural **939** uses **fame** in the Kural's five-item list.

Source-sensitive Part 011 protections remain released and must not be normalized later:

- Kural **899 commentary** — **“an oppressive government will be shaken and destroyed”**;
- Kural **912 commentary** — sugar-sweet sense of `பாகுமொழிபேசும்`;
- Kural **931 commentary** — fish, bait and iron-hook imagery;
- Kural **948 commentary** — **“This applies not only to bodily disease but also to social disease.”**;
- Kural **966 commentary** — **“Will some nonexistent heaven be gained?”**;
- Kural **971** — translation from this edition's unusual audited wording, not an external familiar Kural;
- Kural **972 commentary** — **“Everyone is equal by birth. Difference can be seen only in the skill they show in the work they do.”**;
- Kural **985** and **1008** — no terminal verse period, following the source;
- Kural **1001 commentary** — wealth beyond what a house can contain;
- preserve the stranger's corpse in a dark room, “Mohini spell,” mire/hell, liquor/poison, torch-under-water, gambling hook, medical triad, `kunrimani`, `kavari` deer, queens of chastity, file/tree, dirty-vessel/milk, poisonous-fruit and infected-wealth images.

The Part 011 release gate made **no substantive body-text changes**. It promoted the 23 passing English records from `editorial-reviewed` to `release-ready` after the release report passed.

# Source boundary

The currently supplied Thirukkural material ends at:

- overall scan **237**;
- printed page **204**;
- chapter 101 `நன்றியில் செல்வம்`;
- Kural **1010**.

No Kural **1011** or later Tamil/English text has been inferred or created.

# Exact next activity

There is **no further source-processing activity to begin until an actually supplied subsequent Tamil source is available**.

Do **not** assume or reconstruct Part 012.

When the user supplies the next Tamil source:

1. fresh-read the mandatory startup files;
2. inspect the actual supplied scan before creating or modifying source records;
3. verify the source identity, physical page count and whether it genuinely follows Part 011;
4. directly check the outgoing boundary after printed page **204 / Kural 1010** from that source;
5. inspect the repository to ensure that source has not already been started;
6. only then begin the next separate **Tamil source-intake / first-pass transcription** gate;
7. do not combine first-pass transcription with direct verification or audit.

Until a later controlling source is actually supplied, the Thirukkural workflow is closed through **Tamil Part 011 archival-ready and English Part 011 release-ready / Kural 1010**.
