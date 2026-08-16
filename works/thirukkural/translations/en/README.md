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

The English should retain the source author's language, images, emphases and interpretive direction as closely as clear English allows. Kalaignar's commentary must remain Kalaignar's commentary: a familiar conventional interpretation must never replace what he actually says merely because it sounds more standard in English.

Permanent workflow:

**English first pass (`draft`) → direct source-check → editorial consistency / glossary reconciliation → release gate.**

## Parts 001–009 — RELEASE COMPLETE

- Part 001: 19 `release-ready` + scan 8 `source-limited`;
- Part 002: **21/21 `release-ready`**;
- Part 003: **21/21 `release-ready`**, through Kural 145;
- Part 004: **22/22 `release-ready`**, through Kural 255;
- Part 005: **22/22 `release-ready`**, through Kural 365;
- Part 006: **21/21 `release-ready`**, through Kural 460;
- Part 007: **21/21 `release-ready`**, through Kural 565;
- Part 008: **21/21 `release-ready`**, through Kural 670;
- Part 009: **22/22 `release-ready`**, through Kural 780.

Latest released review artefacts:

- [`reviews/PART_009_REVIEW.md`](reviews/PART_009_REVIEW.md)
- [`reviews/PART_009_RELEASE_REPORT.md`](reviews/PART_009_RELEASE_REPORT.md)

Released Parts 001–009 must not be changed merely to harmonize later wording.

## Part 010 — ENGLISH SOURCE-CHECK COMPLETE

Part 010 Tamil audit: [`../../AUDIT_PART_010.md`](../../AUDIT_PART_010.md) — **PASS / ARCHIVAL-READY**.

English scope:

- aligned pages: **23 / 23**;
- scans **192–214**;
- printed pages **159–181**;
- Kural **781–895**;
- source section throughout: `பொருள் — நட்பியல்`;
- chapters **79–90**;
- chapter 90 `பெரியாரைப் பிழையாமை` is represented only through Kural **895** because the supplied Tamil source ends there.

Current Part 010 English state:

- `draft`: **0**;
- `source-checked`: **23 / 23**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

Every Part 010 page now remains at the source-check gate:

```yaml
translation_type: "project_translation"
status: "source-checked"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

### Source-check corrections retained

The complete direct comparison against the 23 verified Tamil pages produced seven source-fidelity corrections/refinements across six English records:

- Kural **813**: **women for hire**, removing the added first-pass “sell intimacy” wording;
- Kural **822**: **women for hire**, keeping Kalaignar's fuller virtue/appearance explanation in the commentary rather than expanding the Kural line;
- Kural **842 commentary**: removed unsupported **earned**;
- Kural **849**: corrected the subject relationship using Kalaignar's commentary as the permitted interpretive aid;
- Kural **850**: removed commentary-only evidence language from the Kural while retaining Kalaignar's evidence/truth argument in the commentary;
- Kural **867 commentary**: removed the unsupported added phrase “and harmful to us”;
- Kural **887**: removed the unsupported material qualifier “metal” from `செப்பு`, retaining *seppu* in the commentary.

### Source-sensitive protections

The source-check deliberately retains:

- Kural **835** as **seven periods**, without importing “seven births”;
- Kalaignar's supplied Kural **861** interpretation about leaving the weak and preferring to fight the strong;
- scan **209 / Kural 869 commentary** as **“cowards who are afraid, and ignorant cowards”**, preserving the verified repetition;
- Kural **876**'s nuanced enemy/friendship stance during danger;
- Kural **895**'s distinction between the Kural's ruler and Kalaignar commentary's government framing;
- the Kural **850** “ghosts” image and Kalaignar's evidence/truth framing.

No Kural **896** or later English text has been created or inferred.

### Provisional section / headings

`நட்பியல்` → **Friendship** and the current chapter headings 79–90 remain **provisional**. They have not been added as final controls to `GLOSSARY.md`; that belongs to the separate editorial consistency / glossary-reconciliation gate.

## Next project activity

Perform **Part 010 English editorial consistency / glossary reconciliation** for all **23 source-checked pages**.

Finalize the source-supported section rendering and chapter headings, update `GLOSSARY.md`, review recurring terminology and readability without weakening the source-check corrections, create `reviews/PART_010_REVIEW.md`, and promote only passing pages to `editorial-reviewed`.

Do not combine that activity with the release gate. Do not create `PART_010_RELEASE_REPORT.md`, promote pages to `release-ready`, alter released Parts 001–009 merely for harmonization, or infer Kural 896 onward.
