# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

Active work: `works/thirukkural/`

Current active phase: **Thirukkural semantic structure / canonical physical-page provenance mapping**.

Last repository-state synchronization: **2026-08-17**.

## Mandatory startup

Before making changes:

1. read `THIRUKKURAL_ARCHIVAL_GUIDELINES.md` completely;
2. read `LITERARY_COMMENTARY_PROCESSING_GUIDE.md` completely;
3. read this `HANDOVER.md` completely;
4. read `works/thirukkural/README.md`;
5. read `works/thirukkural/structure/README.md`;
6. read `works/thirukkural/structure/CHAPTER_README_POLICY.md`;
7. read `works/thirukkural/structure/STRUCTURE_AUDIT.md`;
8. inspect the existing target files before writing;
9. for any English translation work additionally fresh-read `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`, `GLOSSARY.md`, `TRANSLATION_STATUS.md`, and the latest relevant review/release artefacts.

## Repository-state precedence

When documents disagree about current progress, use this order:

1. actual files on `main` and their page-level metadata;
2. completed Tamil audits and English review/release reports;
3. `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
4. this handover and current READMEs;
5. older continuation guides / saved prompts only for permanent procedural rules, not historical progress snapshots.

## Source rule

The supplied Tamil scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

Source PDFs are working/control sources and are not to be committed to GitHub unless the user explicitly requests that.

OCR/parsed text may assist but is never authoritative over direct inspection of the scan.

## Permanent archival / translation workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Keep these as separate gates.

Permanent English protections remain binding, including:

- `ஊழ்` → **Oozh**;
- Kalaignar's `இயற்கை நிலை` → **natural condition**;
- Kural 543 `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**;
- `இன்பம் — கற்பியல்` → **Inbam — Wedded Love**;
- `ஊடலுவகை` → **Joy of Lovers' Quarrel**;
- preservation of Kalaignar's governance, citizens, working-people, justice, public-resource and rational/inquiry vocabulary;
- no revision of released Parts merely for later stylistic harmonization.

# Completed canonical source state

## Tamil Parts 001–015

Parts **001–015 are audited / ARCHIVAL-READY continuously** through the end of the supplied Thirukkural volume:

- overall scans **1–323**;
- commentary through printed page **270**;
- Kural sequence through **1330**;
- index back matter through printed page **288**;
- scan 322 blank leaf;
- scan 323 plain back cover.

Audits exist as `works/thirukkural/AUDIT_PART_001.md` through `AUDIT_PART_015.md`.

Part 001 scan 8 remains the documented source-limited exception already covered by its audit.

## English Parts 001–015

Parts **001–015 are released continuously through the end of the supplied volume**.

Current released boundaries:

- commentary: scan **303 / printed page 270 / Kural 1330**;
- physical volume: scan **323**;
- back-matter index: scans **304–321 / printed pages 271–288**;
- scan **322** blank leaf;
- scan **323** back cover.

Part 015 release artefacts:

- Tamil audit: `works/thirukkural/AUDIT_PART_015.md` — **PASS / ARCHIVAL-READY**;
- English editorial review: `works/thirukkural/translations/en/reviews/PART_015_REVIEW.md` — **PASS**;
- English release report: `works/thirukkural/translations/en/reviews/PART_015_RELEASE_REPORT.md` — **PASS / RELEASE APPROVED**.

There is no unreleased Thirukkural transcription or English translation remaining in this supplied volume.

# Semantic structure phase

## Purpose

A human-readable literary hierarchy has been added at:

`works/thirukkural/structure/`

The hierarchy is:

**பால் → இயல் → அதிகாரம்**

Target structure:

- **3 பால்**;
- **13 இயல்**;
- **133 அதிகாரம்**;
- **1,330 குறள்**.

This layer is navigational/provenance metadata. It does **not** replace the canonical physical-page archives:

- Tamil canonical layer: `works/thirukkural/pages/`;
- released English layer: `works/thirukkural/translations/en/pages/`.

Do not move or rewrite those canonical layers merely to fit the semantic hierarchy.

## Structure policy and audit

Read:

- `works/thirukkural/structure/CHAPTER_README_POLICY.md`;
- `works/thirukkural/structure/STRUCTURE_AUDIT.md`.

The 133 chapter folders and their base README metadata exist. A previous structural audit corrected an accidental duplicate for chapter 28. During later provenance mapping, additional duplicate naming variants were discovered around chapters 11–14; chapters 11 and 12 have already been reconciled to their source-controlled active nodes. Inspect chapters 13–14 carefully before writing and do not recreate obsolete parallel folders.

## Completed exact provenance mapping

Exact canonical physical-page mapping is complete through:

- **அதிகாரம் 12**;
- **குறள் 120**.

Mapped chapters 1–12:

1. வழிபாடு
2. வான் சிறப்பு
3. நீத்தார் பெருமை
4. அறன் வலியுறுத்தல்
5. இல்வாழ்க்கை
6. வாழ்க்கைத் துணைநலம்
7. மக்கட்பேறு
8. அன்புடைமை
9. விருந்தோம்பல்
10. இனியவை கூறல்
11. செய்ந்நன்றியறிதல்
12. நடுவு நிலைமை

Each mapped chapter README records:

- பால் and இயல்;
- அதிகார number/title;
- 10-Kural range;
- exact source scan(s);
- Part and Part-page number;
- printed-page number;
- exact Kural coverage per physical page;
- canonical verified Tamil archival path;
- corresponding released English path;
- preservation statement for the canonical physical-page layers.

The mapping must be derived from actual repository records. Do not infer scan boundaries arithmetically even where the pattern appears regular.

## User-requested cadence

For this provenance phase, process **5 அதிகாரம் per iteration** when 10 cannot be handled safely. Never report a batch as complete unless all chapters in that batch were actually verified and committed.

# Exact next activity

Map **அதிகாரங்கள் 13–17 / குறள் 121–170**:

13. அடக்கம் உடைமை
14. ஒழுக்கம் உடைமை
15. பிறனில் விழையாமை
16. பொறையுடைமை
17. அழுக்காறாமை

For each chapter:

1. inspect the actual canonical Tamil page records;
2. establish exact scan boundaries and Kural coverage from those records;
3. confirm Tamil status is `verified`;
4. inspect the corresponding English page records and confirm `release-ready`;
5. record scan, Part, Part page, printed page and exact coverage in the semantic chapter README;
6. preserve existing/source-controlled folder and chapter naming;
7. reconcile any duplicate semantic node carefully if encountered;
8. do not modify canonical Tamil or released English body text.

After all five are complete, commit them to `main`, report the exact new boundary, and STOP. The expected following batch is **அதிகாரங்கள் 18–22**, subject to repository inspection.

## Important continuity rule

The semantic mapping phase is independent of the completed archival/translation release state. Do not reopen released Parts 001–015 unless a specific source-supported defect is discovered. Any such correction must be documented explicitly rather than silently changed.
