# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

Active work: `works/thirukkural/`

Current active phase: **Thirukkural semantic structure / canonical physical-page provenance mapping**.

Last repository-state synchronization: **2026-08-17**.

## Mandatory startup

Before making any repository change, read these files completely:

1. `THIRUKKURAL_ARCHIVAL_GUIDELINES.md`
2. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
3. root `HANDOVER.md`
4. `works/thirukkural/README.md`
5. `works/thirukkural/structure/README.md`
6. `works/thirukkural/structure/CHAPTER_README_POLICY.md`
7. `works/thirukkural/structure/STRUCTURE_AUDIT.md`
8. `works/thirukkural/translations/en/TRANSLATION_STATUS.md`

Then inspect current GitHub `main`. Repository state is authoritative over stale SHAs or historical progress paragraphs.

## Repository-state precedence

When documents disagree about current progress, use this order:

1. actual files on `main` and their page-level metadata;
2. completed Tamil audits and English review/release reports;
3. `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
4. this handover and current READMEs;
5. older continuation guides / saved prompts only for permanent procedural rules, not stale progress snapshots.

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
- scan 323 back cover.

Audits exist as `works/thirukkural/AUDIT_PART_001.md` through `AUDIT_PART_015.md`.

## English Parts 001–015

Parts **001–015 are RELEASED continuously through the end of the supplied volume**.

Current released boundaries:

- commentary: scan **303 / printed page 270 / Kural 1330**;
- physical volume: scan **323**;
- back-matter index: scans **304–321 / printed pages 271–288**;
- scan **322** blank leaf;
- scan **323** back cover.

There is no unreleased Thirukkural transcription or English translation remaining in this supplied volume.

# Semantic structure phase

## Purpose

A non-destructive literary hierarchy exists at:

`works/thirukkural/structure/`

Hierarchy:

**பால் → இயல் → அதிகாரம்**

Target structure:

- **3 பால்**;
- **13 இயல்**;
- **133 அதிகாரம்**;
- **1,330 குறள்**.

This is a navigation/provenance layer only. It does **not** replace the canonical physical-page archives:

- Tamil canonical layer: `works/thirukkural/pages/`;
- released English layer: `works/thirukkural/translations/en/pages/`.

Do not move, duplicate or rewrite those physical-page layers merely to fit the semantic hierarchy.

## Provenance README requirements

For every mapped chapter, the semantic chapter README must record:

- பால் and இயல்;
- அதிகார number/title;
- deterministic 10-Kural range;
- exact source scan(s);
- source Part and Part-local-page number;
- printed-page number;
- exact Kural coverage per physical page;
- canonical `verified` Tamil archival path;
- corresponding `release-ready` English path;
- preservation statement that the semantic layer does not replace the canonical physical-page layers.

Never infer page boundaries arithmetically merely because earlier chapters occupy two pages. Inspect the actual repository records first.

## Current exact mapping boundary

Exact canonical physical-page provenance mapping is complete through:

- **அதிகாரம் 77 — படைமாட்சி**;
- **குறள் 770**;
- **scan 189**;
- **Part 009 local page 20**;
- **printed page 156**.

Therefore chapters **1–77 / Kurals 1–770** are mapped.

The most recently completed batch was **அதிகாரங்கள் 73–77 / குறள் 721–770**:

- 73. `அவையஞ்சாமை` — scans 180–181 / Part 009 pp.11–12 / printed 147–148 / Kurals 721–730 — `அமைச்சியல்`;
- 74. `நாடு` — scans 182–183 / Part 009 pp.13–14 / printed 149–150 / Kurals 731–740 — starts `அரணியல்`;
- 75. `அரண்` — scans 184–185 / Part 009 pp.15–16 / printed 151–152 / Kurals 741–750 — `அரணியல்`;
- 76. `பொருள் செயல்வகை` — scans 186–187 / Part 009 pp.17–18 / printed 153–154 / Kurals 751–760 — starts `கூழியல்`;
- 77. `படைமாட்சி` — scans 188–189 / Part 009 pp.19–20 / printed 155–156 / Kurals 761–770 — starts `படையியல்`.

All ten underlying Tamil records in that batch were confirmed `verified`; all ten corresponding English records were confirmed `release-ready` with `source_tamil_status: verified`.

### Source-sensitive protections already encountered during semantic mapping

Do not normalize or silently rewrite these already source-checked readings when following provenance links:

- scan 179 / Kural 717 source reading preserved exactly;
- scan 180 / Kural 725 commentary: `தருக்கமென்படும் அளவைக் திறமும்`;
- scan 182 / Kural 733 commentary: `மளவுக்கு வளம்`;
- scan 190 / Kural 771 commentary must preserve verified `நடுகல்லாய்ப் போனவர்கள்` when chapter 78 is mapped.

### Important structural transitions already mapped

The semantic mapping has preserved source-visible hierarchy changes rather than flattening them, including:

- `அறத்துப்பால் → பொருட்பால்`;
- `அரசியல் → அமைச்சியல்` at chapter 64;
- `அமைச்சியல் → அரணியல்` at chapter 74;
- `அரணியல் → கூழியல்` at chapter 76;
- `கூழியல் → படையியல்` at chapter 77.

## Duplicate/source-controlled naming rule

Preserve the exact existing semantic folder spelling on `main`. Do not create a normalized duplicate merely because a title can be written another way.

Earlier duplicate-folder issues around chapters 11–14 and chapter 28 were already reconciled. Later batches also confirmed several source-controlled spellings that differ from obvious normalized forms. Always inspect the live semantic directory before writing.

## User-requested cadence

Process **5 அதிகாரம் per iteration** when 10 cannot be processed safely.

Never report a batch as complete unless every chapter in that batch has been actually verified and written to `main`.

The GitHub Contents API may create one linear commit per README update. That is acceptable; report the final commit boundary accurately rather than claiming a single multi-file commit when one was not created.

# Exact next activity

Map the next **5 அதிகாரங்கள்: 78–82 / குறள் 771–820**:

78. படைச் செருக்கு
79. நட்பு
80. நட்பாராய்தல்
81. பழைமை
82. தீ நட்பு

The expected source-backed physical ranges, which must still be confirmed from the individual live records before writing, are:

- **78. படைச் செருக்கு** — scans 190–191 / Part 009 pp.21–22 / printed 157–158 / Kurals 771–780 / `படையியல்`;
- **79. நட்பு** — scans 192–193 / Part 010 pp.1–2 / printed 159–160 / Kurals 781–790 / begins `நட்பியல்`;
- **80. நட்பாராய்தல்** — scans 194–195 / Part 010 pp.3–4 / printed 161–162 / Kurals 791–800;
- **81. பழைமை** — scans 196–197 / Part 010 pp.5–6 / printed 163–164 / Kurals 801–810;
- **82. தீ நட்பு** — scans 198–199 / Part 010 pp.7–8 / printed 165–166 / Kurals 811–820.

This batch contains two important source-supported boundaries:

1. **Part 009 → Part 010**: scan 191 / printed 158 / Kural 780 → scan 192 / printed 159 / Kural 781;
2. **படையியல் → நட்பியல்**: chapter 78 closes `படையியல்`; chapter 79 `நட்பு` starts `நட்பியல்`.

For each chapter:

1. inspect the actual canonical Tamil page records first;
2. establish exact physical scan boundaries and Kural coverage from those records, not arithmetic assumptions;
3. confirm each Tamil record is `verified`;
4. inspect the corresponding English physical-page record and confirm `release-ready` with `source_tamil_status: verified`;
5. record source scan, Part, Part page, printed page and exact Kural coverage;
6. update only the correct semantic chapter README;
7. preserve source-controlled chapter naming and existing folder spelling;
8. document structural/Part transitions where source-supported;
9. preserve the scan-190/Kural-771 verified source correction exactly;
10. do not alter canonical Tamil or released English body text.

After all five are genuinely verified and updated, report the new exact mapping boundary and STOP. The following batch should be **அதிகாரங்கள் 83–87 / குறள் 821–870**, subject to repository inspection.

## Continuity rule

The semantic mapping phase is independent of the completed archival/translation release state. Do not reopen released Parts 001–015 merely to support navigation. If a genuine source-supported defect is discovered, document it explicitly rather than silently changing released material.
