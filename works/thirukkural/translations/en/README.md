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

Latest released Part 009 artefacts:

- [`reviews/PART_009_REVIEW.md`](reviews/PART_009_REVIEW.md)
- [`reviews/PART_009_RELEASE_REPORT.md`](reviews/PART_009_RELEASE_REPORT.md)

Released Parts 001–009 must not be changed merely to harmonize later wording.

## Part 010 — EDITORIAL REVIEW COMPLETE

Part 010 Tamil audit: [`../../AUDIT_PART_010.md`](../../AUDIT_PART_010.md) — **PASS / ARCHIVAL-READY**.

Editorial review: [`reviews/PART_010_REVIEW.md`](reviews/PART_010_REVIEW.md).

Scope:

- aligned pages: **23 / 23**;
- scans **192–214**;
- printed pages **159–181**;
- Kural **781–895**;
- source section throughout: `பொருள் — நட்பியல்`;
- chapters **79–90**;
- chapter 90 `பெரியாரைப் பிழையாமை` is represented only through Kural **895** because the supplied Tamil source ends there.

Current Part 010 English state:

- `draft`: **0**;
- `source-checked`: **0**;
- `editorial-reviewed`: **23 / 23**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

Every Part 010 page now remains at the editorial-review gate:

```yaml
translation_type: "project_translation"
status: "editorial-reviewed"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

### Controlled Part 010 section / headings

`நட்பியல்` is now controlled as **Friendship**. The source itself keeps that structural label even when later chapters move into discord and enmity, so the project does not invent a broader English section title.

Controlled headings:

- 79 **Friendship**;
- 80 **Examining Friendship**;
- 81 **Long-Standing Friendship**;
- 82 **Harmful Friendship**;
- 83 **False Friendship**;
- 84 **Folly**;
- 85 **Possession of Little Understanding**;
- 86 **Discord**;
- 87 **Excellence in Enmity**;
- 88 **Discerning Enmity**;
- 89 **Internal Enmity**;
- 90 **Not Offending the Great**.

Chapter 87 was refined from the provisional **The Character of Enmity** to **Excellence in Enmity** during editorial review, restoring the force of `மாட்சி` and following Kalaignar's supplied Kural 861 explanation.

### Fidelity protections retained

All seven source-check corrections remain intact, including **women for hire** at Kural 813/822, the corrected Kural 849 subject relation, separation of Kural 850 from Kalaignar's evidence commentary, the Kural 867 and 887 removals of unsupported additions, and the Kural 842 correction.

The review also retains Kural **835** as **seven periods**, Kural **850**'s evidence/“ghosts” commentary, Kalaignar's supplied Kural **861** interpretation, Kural **869**'s repeated **“cowards who are afraid, and ignorant cowards”**, Kural **876**'s nuanced enemy/friendship position, and Kural **895**'s ruler/government distinction.

No substantive Kural or commentary body text was changed during the editorial gate. The only text-level editorial refinement was the chapter 87 heading/metadata on scans 208–209.

No Kural **896** or later English text has been created or inferred.

## Next project activity

Perform the separate **Part 010 English release gate** for all **23 editorial-reviewed pages**.

Check final page/Kural/metadata continuity and alignment, controlled terminology and protected source decisions, create `reviews/PART_010_RELEASE_REPORT.md`, and only then promote pages to `release-ready` if the gate passes.

Do not combine release with an unsupplied Tamil continuation after Kural 895.
