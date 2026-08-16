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

## Part 012 — TAMIL ARCHIVAL-READY / ENGLISH FIRST PASS ELIGIBLE

Tamil audit: [`../../AUDIT_PART_012.md`](../../AUDIT_PART_012.md) — **PASS / ARCHIVAL-READY**.

Audited Tamil scope:

- physical pages: **23 / 23**;
- scans **238–260**;
- printed pages **205–218**, two unnumbered leaves, then **221–227**;
- Kural **1011–1115**;
- Tamil `verified`: **23 / 23**;
- unresolved Tamil records: **0**.

The Part 012 source structure is:

- scans **238–251**: `பொருள் — குடியியல்`;
- scan **252**: `இன்பம்` section-title leaf;
- scan **253**: blank/reverse-show-through leaf;
- scans **254–260**: `இன்பம் — களவியல்`.

The incoming boundary is continuous at printed page **204 → 205 / Kural 1010 → 1011**. The supplied Part 013 first page confirms the outgoing continuation at printed page **227 → 228 / Kural 1115 → 1116**, but Part 013 transcription remains not started.

Part 012 Tamil verification produced three authoritative commentary corrections:

1. Kural **1018** — `அகன்றுவிட்டதாகக் கருத வேண்டும்.`
2. Kural **1035** — `ஊதியம் பெற்று உண்ணும் இயல்புடையவர்`
3. Kural **1048** — `கொலை செய்வதுபோல நேற்று...`

Protected source-specific verse readings for Part 012 English work:

- Kural **1077**: `ஈங்கை விதிரார் கயவர் கொடிறுடைக்குங் / கூன்கையர் அல்லா தவர்க்கு.`
- Kural **1098**: `அசையியற் குண்டாண்டோர் ஏஎர்யான் நோக்கப் / பசையினள் பைய நகும்.`

No Part 012 English page exists yet.

## Next project activity

Perform **Part 012 English project translation — first pass** for all **23 aligned physical pages / scans 238–260**.

Before writing, fresh-read `TRANSLATION_GUIDE.md`, `GLOSSARY.md`, `TRANSLATION_STATUS.md`, the Part 012 Tamil audit, and the latest Part 011 English review/release artefacts. Inspect the target English directory and continue any existing Part 012 work rather than duplicating it.

Every new Part 012 English page must use:

```yaml
translation_type: "project_translation"
status: "draft"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

Mirror all 23 Tamil filenames and preserve physical alignment, including scan 252's `இன்பம்` title leaf and scan 253's blank/reverse-show-through leaf. Preserve the structural transition and Kalaignar's actual commentary direction. Treat Kural 1077 and 1098 as source-protected readings; do not replace them with familiar external versions.

Stop after the first-pass gate. Do not source-check, editorial-review or release Part 012 English in the same activity. Do not begin Part 013 Tamil transcription. Do not alter released English Parts 001–011.
