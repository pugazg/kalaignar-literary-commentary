# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

Active work: `works/thirukkural/`

Current active phase: **Thirukkural semantic structure / canonical physical-page provenance mapping**.

Last repository-state synchronization: **2026-08-18**.

## Mandatory startup

Before making any repository change, read these files completely:

1. `NEXT_CHAT_PROMPT_THIRUKKURAL.md`
2. `THIRUKKURAL_ARCHIVAL_GUIDELINES.md`
3. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
4. root `HANDOVER.md`
5. `works/thirukkural/README.md`
6. `works/thirukkural/structure/README.md`
7. `works/thirukkural/structure/CHAPTER_README_POLICY.md`
8. `works/thirukkural/structure/STRUCTURE_AUDIT.md`
9. `works/thirukkural/translations/en/TRANSLATION_STATUS.md`
10. the audit for the source Part used by the next batch — currently `works/thirukkural/AUDIT_PART_013.md`.

Then inspect current GitHub `main`. Repository state is authoritative over stale SHAs or historical progress paragraphs.

## Repository-state precedence

When documents disagree about current progress, use this order:

1. actual files on `main` and their page-level metadata;
2. completed Tamil audits and English review/release reports;
3. `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
4. this handover and current semantic READMEs;
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

- Section / பால்;
- Chapter group / இயல்;
- `Status: mapped`;
- deterministic 10-Kural range;
- exact source scan(s);
- source Part and Part-local-page number;
- printed-page number;
- exact Kural coverage per physical page;
- canonical `verified` Tamil archival path;
- corresponding `release-ready` English path with `source_tamil_status: verified`;
- source-sensitive notes where warranted;
- preservation statement that the semantic layer does not replace, move, duplicate or rewrite the canonical physical-page layers.

Never infer page boundaries arithmetically merely because earlier chapters occupy two pages. Inspect the actual repository records first.

## Current exact mapping boundary

Exact canonical physical-page provenance mapping is complete through:

- **அதிகாரம் 112 — நலம் புனைந்துரைத்தல்**;
- **குறள் 1120**;
- **scan 261**;
- **Part 013 local page 1**;
- **printed page 228**.

Therefore chapters **1–112 / Kurals 1–1120** are semantically mapped.

Chapter 112 itself crosses a source-Part boundary:

- scan 260 / Part 012 local page 23 / printed page 227 / Kurals 1111–1115;
- scan 261 / Part 013 local page 1 / printed page 228 / Kurals 1116–1120.

The Part 012 → Part 013 transition is continuous at Kural **1115 → 1116**.

## Interrupted 113–117 attempt — important current state

A continuation attempt for chapters **113–117 / Kurals 1121–1170** was started on 2026-08-18 and then explicitly stopped by the user before the provenance gate was completed.

What was established during that attempt:

- mandatory startup/guideline reading had been completed;
- live `main` had not advanced beyond the existing coordination-document state;
- `AUDIT_PART_013.md` and the live semantic hierarchy confirm the correct chapter sequence and the **களவியல் → கற்பியல்** transition at chapter 116;
- exploratory source-record lookup began.

What was **not** completed:

- the ten Tamil physical-page records for chapters 113–117 were not all fetched and verified as a complete gate;
- the ten corresponding English release records were not all verified as a complete gate;
- the five semantic chapter README skeletons were not all read and updated;
- no semantic README for chapters 113–117 was changed;
- no canonical Tamil or released English body record was changed.

Before this handover update, live `main` was still at commit `27bd6512fd243cbb4ddf0ebd614ce7666adc234f`, whose commit message was `Update Thirukkural continuation prompt for chapters 113-117`. That confirms that the interrupted attempt produced **no chapter-mapping commit**.

Therefore the authoritative semantic completion boundary remains **chapter 112 / Kural 1120**.

Treat all partial lookups from the interrupted attempt as exploratory only. A future session must repeat/complete the live provenance verification before writing chapters 113–117.

## Current Inbam hierarchy and next structural transition

The live semantic tree and Part 013 audit establish the following source-controlled hierarchy:

### `03-இன்பத்துப்பால்/01-களவியல்`

- 109. `தகையணங்குறுத்தல்`
- 110. `குறிப்பறிதல்`
- 111. `புணர்ச்சி மகிழ்தல்`
- 112. `நலம் புனைந்துரைத்தல்`
- 113. `காதற் சிறப்புரைத்தல்`
- 114. `நாணுத் துறவுரைத்தல்`
- 115. `அலர் அறிவுறுத்தல்`

### `03-இன்பத்துப்பால்/02-கற்பியல்`

- 116. `பிரிவு ஆற்றாமை`
- 117. `படர்மெலிந்து இரங்கல்`
- subsequent chapters continue under `கற்பியல்`.

**Critical transition:** chapter **115** closes `களவியல்`; chapter **116 / Kural 1151** begins `கற்பியல்`.

Do not misclassify chapter 116 as `களவியல்`, and do not move chapter 115 into `கற்பியல்`.

## Exact live semantic folder spellings for the next batch

Preserve these existing folder names exactly:

- `works/thirukkural/structure/03-இன்பத்துப்பால்/01-களவியல்/113-காதற்சிறப்புரைத்தல்/`
- `works/thirukkural/structure/03-இன்பத்துப்பால்/01-களவியல்/114-நாணுத்துறவுரைத்தல்/`
- `works/thirukkural/structure/03-இன்பத்துப்பால்/01-களவியல்/115-அலரறிவுறுத்தல்/`
- `works/thirukkural/structure/03-இன்பத்துப்பால்/02-கற்பியல்/116-பிரிவாற்றாமை/`
- `works/thirukkural/structure/03-இன்பத்துப்பால்/02-கற்பியல்/117-படர்மெலிந்திரங்கல்/`

The source audit may display chapter titles with spaces while folder slugs omit them. The live semantic folder spelling is repository-controlled; do not create normalized duplicates.

## Source-sensitive protections

All source-sensitive corrections already recorded in canonical page files, audits or completed semantic READMEs remain protected. Do not normalize or revert them during semantic mapping.

Important examples from prior batches include:

- Kural 771 commentary: `நடுகல்லாய்ப் போனவர்கள்`;
- Kural 899 commentary source wording preserved as directly verified;
- Kural 911 commentary: `பொருள் திரட்டுவதையே`;
- Kural 912 source-sensitive form: `பாகுமொழிபேசும்`;
- Kural 927 commentary source wording preserved as directly verified;
- Kural 931 commentary: `கெளவிக் கொண்டு போவதாகிவிடும்`;
- Kural 948 commentary: `உடல் நோய்க்கு மட்டுமின்றிச் சமுதாய நோய்க்கும் இது பொருந்தும்.`;
- Kural 971 printed verse and Kural 972 commentary as preserved in the completed chapter 98 README;
- Kural 985 and Kural 1008 printed punctuation as preserved in their completed READMEs;
- Kural 1018 corrected commentary ending `அகன்றுவிட்டதாகக் கருத வேண்டும்.`;
- Kural 1035: `ஊதியம் பெற்று உண்ணும் இயல்புடையவர்`;
- Kural 1048: `கொலை செய்வதுபோல நேற்று...`;
- Kural 1077 source-sensitive printed verse as recorded in Part 012 audit / source records.

These examples are not an exhaustive replacement for inspecting the source records of the active batch.

## Duplicate/source-controlled naming rule

Preserve the exact existing semantic folder spelling on `main`. Do not create a normalized duplicate merely because a title can be written another way.

Earlier duplicate-folder issues were already reconciled. Always inspect the live semantic directory before writing.

## User-requested cadence

Process **5 அதிகாரம் per iteration** when 10 cannot be processed safely.

Never report a batch as complete unless every chapter in that batch has been actually verified and written to `main`.

The GitHub Contents API may create one linear commit per README update. That is acceptable; report the final commit boundary accurately rather than claiming a single multi-file commit when one was not created.

# Exact next activity

Restart the next **5 அதிகாரங்கள்: 113–117 / குறள் 1121–1170** from the provenance-verification gate. Do **not** resume as though the interrupted attempt had completed any source-page verification.

Source-controlled chapter sequence from `AUDIT_PART_013.md`:

113. `காதற் சிறப்புரைத்தல்` — Kurals 1121–1130 — `களவியல்`
114. `நாணுத் துறவுரைத்தல்` — Kurals 1131–1140 — `களவியல்`
115. `அலர் அறிவுறுத்தல்` — Kurals 1141–1150 — final `களவியல்` chapter
116. `பிரிவு ஆற்றாமை` — Kurals 1151–1160 — begins `கற்பியல்`
117. `படர்மெலிந்து இரங்கல்` — Kurals 1161–1170 — `கற்பியல்`

Working scan expectation from the continuous Part 013 sequence is scans **262–271**, immediately after the verified chapter-112 boundary at scan 261. **Do not treat the individual chapter/page split as established until the canonical Tamil page records are fetched and inspected.** Verify the exact scan, Part-local-page, printed-page and Kural coverage for all ten pages before writing any semantic README.

For the next batch:

1. fetch current live `main` HEAD first;
2. fetch and inspect all ten canonical Tamil page records covering the 113–117 sequence; confirm `status: verified` and exact page-level provenance;
3. fetch all ten corresponding English page records; confirm `status: release-ready` and `source_tamil_status: verified`;
4. fetch all five existing semantic chapter README skeletons / paths from the live tree;
5. only after Gates 2–4 are complete, update the five semantic chapter READMEs sequentially;
6. preserve exact source-controlled wording, punctuation, chapter titles and existing folder spellings;
7. record the `களவியல் → கற்பியல்` transition at chapter 116 where appropriate;
8. do not alter canonical Tamil or released English body text;
9. do not update root handover/audit/status documents during the ordinary batch unless instructions change;
10. read back all five written READMEs and fetch live `main` HEAD;
11. report the exact new mapping boundary and STOP.

If the expected two-page-per-chapter pattern is confirmed by the live page records, the final boundary after chapter 117 should be around scan 271 / Part 013 local page 11 / printed page 238. This is an **expected boundary only until verified from the canonical records**.

## Continuity rule

The semantic mapping phase is independent of the completed archival/translation release state. Do not reopen released Parts 001–015 merely to support navigation. If a genuine source-supported defect is discovered, document it explicitly rather than silently changing released material.
