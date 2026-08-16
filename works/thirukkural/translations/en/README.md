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

## Parts 001–011 — RELEASE COMPLETE THROUGH KURAL 1010

- Part 001: 19 `release-ready` + scan 8 `source-limited`;
- Part 002: **21/21 `release-ready`**;
- Part 003: **21/21 `release-ready`**, through Kural 145;
- Part 004: **22/22 `release-ready`**, through Kural 255;
- Part 005: **22/22 `release-ready`**, through Kural 365;
- Part 006: **21/21 `release-ready`**, through Kural 460;
- Part 007: **21/21 `release-ready`**, through Kural 565;
- Part 008: **21/21 `release-ready`**, through Kural 670;
- Part 009: **22/22 `release-ready`**, through Kural 780;
- Part 010: **23/23 `release-ready`**, through Kural 895;
- Part 011: **23/23 `release-ready`**, through Kural **1010**.

Latest released artefacts:

- Part 011 Tamil audit: [`../../AUDIT_PART_011.md`](../../AUDIT_PART_011.md) — **PASS / ARCHIVAL-READY**;
- Part 011 editorial review: [`reviews/PART_011_REVIEW.md`](reviews/PART_011_REVIEW.md);
- Part 011 release report: [`reviews/PART_011_RELEASE_REPORT.md`](reviews/PART_011_RELEASE_REPORT.md) — **PASS / RELEASE APPROVED**.

Released Parts 001–011 must not be changed merely to harmonize later wording.

## Part 012 — ENGLISH SOURCE-CHECK COMPLETE

Tamil audit: [`../../AUDIT_PART_012.md`](../../AUDIT_PART_012.md) — **PASS / ARCHIVAL-READY**.

The complete Part 012 English layer has now passed both first-pass translation and the separate direct source-check for:

- physical pages: **23 / 23**;
- scans **238–260**;
- printed pages **205–218**, two unnumbered physical leaves, then **221–227**;
- Kural **1011–1115**;
- English `draft`: **0**;
- `source-checked`: **23 / 23**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**.

Every Part 012 English record now carries:

```yaml
translation_type: "project_translation"
status: "source-checked"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

The source structure and physical alignment remain preserved:

- scans **238–251**: `Porul — Civic Life`;
- scan **252**: standalone `Inbam` title leaf;
- scan **253**: blank/reverse-show-through leaf;
- scans **254–260**: provisionally `Inbam — Clandestine Love`.

Every Kural translation and Kalaignar commentary paragraph was compared against the corresponding verified Tamil record. The controlling scan was re-inspected at source-sensitive points. No source-fidelity body-text correction was required during this gate; all 23 passing records changed only from `draft` to `source-checked`.

The source-check explicitly retained the verified Tamil corrections at Kural **1018**, **1035** and **1048**, the edition-specific Kural **1077** and **1098** readings, Kalaignar's challenge to the supposed creator at Kural **1062**, his skeptical `lotus-eyed one` comparison at Kural **1103**, and the anicham-stalk / broken-waist / auspicious-drum explanation at Kural **1115**.

New Part 012 structural/chapter renderings are still **provisional**. `GLOSSARY.md` was deliberately not changed during source-check. The established `குடியியல்` → **Civic Life** and `குறிப்பறிதல்` → **Understanding Signs** controls remain in use.

Parts **013–015** Tamil sources are received but remain not started.

## Next project activity

Perform **Part 012 English editorial consistency / glossary reconciliation** for all **23 source-checked physical pages / scans 238–260**.

Review readability and consistency while preserving the source-checked meaning. Reconcile `களவியல்` and chapter headings **102–112** against the supplied main body and existing project vocabulary, update `GLOSSARY.md` where the editorial decisions require it, create `reviews/PART_012_REVIEW.md`, and promote pages to `editorial-reviewed` only if that separate gate passes.

Do not combine the editorial gate with release. Do not begin Part 013 Tamil transcription. Do not alter released English Parts 001–011.
