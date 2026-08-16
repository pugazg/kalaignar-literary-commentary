# Thirukkural — Kalaignar's Commentary — English project translation

This directory contains the **project-created English translation layer** for the archived Tamil source `திருக்குறள் — கலைஞர் உரை`.

This is **not an official or publisher-issued English edition**. Every English page carries `translation_type: "project_translation"`.

Authority order:

1. supplied Tamil scan;
2. verified/audited Tamil archival page;
3. `TRANSLATION_GUIDE.md` and `GLOSSARY.md`;
4. project translation/review notes.

Do not import a published English Thirukkural translation, another Tamil edition, another commentator or web text.

## Translation fidelity

The English should retain Kalaignar's language, images, emphases, social vocabulary and interpretive direction as closely as clear English allows. A familiar conventional interpretation must never replace what he actually says merely because it sounds more standard in English.

Permanent workflow:

**English first pass (`draft`) → direct source-check → editorial consistency / glossary reconciliation → release gate.**

## Parts 001–010 — RELEASE COMPLETE THROUGH KURAL 895

- Part 001: 19 `release-ready` + scan 8 `source-limited`;
- Part 002: **21/21 `release-ready`**;
- Part 003: **21/21 `release-ready`**, through Kural 145;
- Part 004: **22/22 `release-ready`**, through Kural 255;
- Part 005: **22/22 `release-ready`**, through Kural 365;
- Part 006: **21/21 `release-ready`**, through Kural 460;
- Part 007: **21/21 `release-ready`**, through Kural 565;
- Part 008: **21/21 `release-ready`**, through Kural 670;
- Part 009: **22/22 `release-ready`**, through Kural 780;
- Part 010: **23/23 `release-ready`**, through Kural **895**.

Latest released artefacts:

- Part 010 Tamil audit: [`../../AUDIT_PART_010.md`](../../AUDIT_PART_010.md) — **PASS / ARCHIVAL-READY**;
- Part 010 editorial review: [`reviews/PART_010_REVIEW.md`](reviews/PART_010_REVIEW.md);
- Part 010 release report: [`reviews/PART_010_RELEASE_REPORT.md`](reviews/PART_010_RELEASE_REPORT.md) — **PASS / RELEASE APPROVED**.

Released Parts 001–010 must not be changed merely to harmonize later wording.

Released Part 010 structural vocabulary includes `நட்பியல்` → **Friendship**, and chapter 90 `பெரியாரைப் பிழையாமை` → **Not Offending the Great**.

## Part 011 Tamil basis — ARCHIVAL-READY

Tamil audit: [`../../AUDIT_PART_011.md`](../../AUDIT_PART_011.md) — **PASS / ARCHIVAL-READY**.

Part 011 Tamil scope:

- **23 / 23** verified pages;
- scans **215–237**;
- printed pages **182–204**;
- Kural **896–1010**;
- chapters **90–101**;
- no unresolved Tamil record.

## Part 011 English — DIRECT SOURCE-CHECK COMPLETE

All **23 / 23** page-aligned English records for scans **215–237 / printed pages 182–204 / Kural 896–1010** are now `source-checked`.

Current state:

- `draft`: **0**;
- `source-checked`: **23 / 23**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

Every Part 011 page carries:

```yaml
translation_type: "project_translation"
status: "source-checked"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

The source structural transition remains visible:

- scans **215–225** use the already controlled `நட்பியல்` → **Friendship**;
- from scan **226 / printed page 193 / chapter 96 குடிமை**, the current source-checked text retains provisional `குடியியல்` → **Civic Life**.

Scan 215 continues the released chapter 90 heading **Not Offending the Great**.

Current chapter headings 91–101 remain provisional until editorial/glossary reconciliation:

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

`GLOSSARY.md` was deliberately **not** changed during source-check.

### Source-check corrections

Six substantive source-fidelity corrections/refinements were made:

1. Kural **911**: **bring ruin** → **bring suffering**;
2. Kural **926**: restored sleepers/dead to the first line and liquor/poison to the second;
3. Kural **953**: **true nobility** → **truthful citizens**, following Kalaignar's `வாய்மையுள்ள குடிமக்கள்`;
4. Kural **961**: removed unsupported **to one's distinction** from “indispensable”;
5. Kural **989**: removed the commentary-only all-seas-overturning image from the Kural itself, while retaining it in Kalaignar's commentary;
6. Kural **1006**: corrected the subject so the miser is **a disease upon his great wealth**, not the wealth a disease to him.

No other substantive first-pass change was required.

### Source-sensitive treatments retained

The source-check retains Kalaignar's **oppressive government** framing at Kural 899, `பாகுமொழிபேசும்` as sugar-sweet speech at 912, the fish/bait/iron-hook image at 931, the **social disease** extension at 948, the rationalist **“nonexistent heaven”** question at 966, the unusual audited Kural 971 basis, the explicit equality formulation at 972, the source punctuation at 985 and 1008, and the house-filling wealth image at 1001.

No Kural **1011** or later English text has been created or inferred.

## Next project activity

Perform **Part 011 English editorial consistency / glossary reconciliation** for all **23 `source-checked` pages**.

Finalize `குடியியல்` and chapter headings **91–101**, update `GLOSSARY.md`, create `reviews/PART_011_REVIEW.md`, reconcile recurring terminology/readability without weakening Kalaignar's language, and promote passing pages only to `editorial-reviewed`.

Do **not** perform the release gate in the same activity and do not modify released Parts 001–010 merely to harmonize later wording.
