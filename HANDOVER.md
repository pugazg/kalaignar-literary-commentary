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
7. for English work additionally read:
   - `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`;
   - `works/thirukkural/translations/en/GLOSSARY.md`;
   - `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
   - the current Part review/release artefacts and corresponding Tamil audit.

Repository state is authoritative.

## Source rule

The supplied Tamil scans are controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

Source PDFs are working/control sources and are not to be committed to GitHub unless the user explicitly requests that.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Keep these as separate gates.

# Established state

## Tamil

Parts **001–009 are audited / ARCHIVAL-READY continuously** through:

- overall scan **191**;
- printed page **158**;
- Kural **780**.

Latest Tamil audit: `works/thirukkural/AUDIT_PART_009.md`.

## English project translation

Parts **001–009 are fully released continuously** through Kural **780**.

Part 009 English completed:

- first-pass translation: **22 / 22**;
- direct source-check: **22 / 22**;
- editorial consistency / glossary reconciliation: **22 / 22**;
- release gate: **PASS**;
- final `release-ready`: **22 / 22**.

Part 009 release artefacts:

- `works/thirukkural/translations/en/reviews/PART_009_REVIEW.md`
- `works/thirukkural/translations/en/reviews/PART_009_RELEASE_REPORT.md`

Every English page must identify:

```yaml
translation_type: "project_translation"
```

Released Parts 001–009 must not be revised merely to harmonize later vocabulary.

Permanent earlier protections remain binding, including chapter 38 `ஊழ்` → **Oozh**, `இயற்கை நிலை` → **natural condition**, and Kural 543's Kalaignar-directed `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**.

# Part 009 Tamil — ARCHIVAL-READY

Controlling source: `திருக்குறள்_கலைஞர்_உரை_part_009_pages_170-191.pdf`

Final Tamil scope:

- physical pages: **22**;
- scans **170–191**;
- printed pages **137–158**;
- Kural **671–780**;
- chapters **68–78**;
- `verified`: **22 / 22**;
- audit decision: **PASS / ARCHIVAL-READY**.

Protected Tamil readings:

- Kural **717**: `கற்றறிந்தார் கல்வி விளங்கும் கசடறச் / சொற்றெரிதல் முன்னர் இழுக்கு.`
- Kural **725 commentary**: `தருக்கமென்படும் அளவைக் திறமும்`
- Kural **733 commentary**: `மளவுக்கு வளம்`
- Kural **771 commentary**: `நடுகல்லாய்ப் போனவர்கள்`.

The source-visible section sequence is:

`அமைச்சியல்` → `அரணியல்` → `கூழியல்` → `படையியல்`.

# Part 009 English — RELEASE COMPLETE

Scope:

- scans **170–191**;
- printed pages **137–158**;
- Kural **671–780**;
- chapters **68–78**;
- aligned English records: **22 / 22**;
- final status: **22 / 22 `release-ready`**.

Release report:

`works/thirukkural/translations/en/reviews/PART_009_RELEASE_REPORT.md`

Release decision: **PASS — PART 009 ENGLISH RELEASE APPROVED**.

## Released Part 009 chapter headings

- 68 `வினை செயல்வகை` → **The Method of Action**;
- 69 `தூது` → **The Envoy**;
- 70 `மன்னரைச் சேர்ந்து ஒழுகல்` → **Conduct in the Presence of Kings**;
- 71 `குறிப்பறிதல்` → **Understanding Signs**;
- 72 `அவை அறிதல்` → **Knowing the Assembly**;
- 73 `அவை அஞ்சாமை` → **Fearlessness in the Assembly**;
- 74 `நாடு` → **The Country**;
- 75 `அரண்` → **Fortress**;
- 76 `பொருள் செயல்வகை` → **The Way of Acquiring Wealth**;
- 77 `படை மாட்சி` → **Excellence of the Army**;
- 78 `படைச் செருக்கு` → **Martial Pride**.

## Released structural vocabulary through Part 009

- `அமைச்சியல்` → **Ministerial Affairs**;
- `அரணியல்` → **Fortification Affairs**;
- `கூழியல்` → **Wealth**;
- `படையியல்` → **Military Affairs**.

Do not flatten these source-visible distinctions in later work.

## Released Part 009 source-check protections

1. **Kural 680** — **“those with little support ... the trembling among their own”**; do not restore the unsupported territorial “smaller domain” wording.
2. **Kural 691** — **“kings”**; do not restore unsupported “contentious.”
3. **Kural 717** — retain the clause ending **“there is a lapse”**, grounded in the supplied edition's verified final `இழுக்கு`.
4. **Kural 725 commentary** — retain **“the skill of measure called logic”** from `தருக்கமென்படும் அளவைக் திறமும்`.
5. **Kural 733 commentary** — retain **“possesses wealth to that measure”** from `மளவுக்கு வளம்`.
6. **Kural 771 commentary** — retain **“have become memorial stones”** from `நடுகல்லாய்ப் போனவர்கள்`.
7. **Kural 773** — retain Kalaignar's explicit **great manliness / manliness** framing.

Kalaignar's institutional/public vocabulary and direct images remain protected. No substantive Kural/commentary body text was changed during the Part 009 release gate.

# Part 010 source state

Supplied source:

`திருக்குறள்_கலைஞர்_உரை_part_010_pages_192-214.pdf`

Known intake facts already established:

- physical source pages: **23**;
- expected overall scans: **192–214**;
- first page: overall scan **192** / printed page **159**;
- first chapter visible: **79. நட்பு**;
- first Kural visible: **781**;
- Part 009 → Part 010 boundary is continuous at printed page **158 → 159** / Kural **780 → 781**.

Only the first Part 010 page was previously inspected for boundary continuity. Part 010 has **not** yet been transcribed, directly verified or audited. Do not assume the ending printed page, ending Kural or chapter range without inspecting the actual supplied Part 010 scan.

# Exact next activity

Perform **Part 010 Tamil first-pass transcription**.

## Required Part 010 first-pass procedure

1. fresh-read the mandatory startup files above;
2. locate and inspect the actual supplied Part 010 PDF before writing;
3. perform source intake across all **23** physical pages and establish the actual printed-page, Kural and chapter/section ranges from the scan itself;
4. inspect `works/thirukkural/pages/` first and confirm no Part 010 page records have already been started; continue existing work rather than creating duplicates if any exist;
5. create one Tamil Markdown record for every Part 010 physical scan page, aligned to expected overall scans **192–214**;
6. transcribe source-supported Tamil exactly as printed, preserving Kural numbering, two-line verse structure, Kalaignar commentary, punctuation, chapter headings and source-visible running-header/section distinctions;
7. distinguish printed text from bleed-through, stamps, handwriting, damage or scanner artefacts;
8. use the canonical source filename `திருக்குறள்_கலைஞர்_உரை_part_010_pages_192-214.pdf` in metadata unless the actual supplied scan establishes a different source identity;
9. every first-pass Part 010 page must remain:

```yaml
status: "needs-review"
transcription_method: "manual transcription from source scan; direct visual verification pending"
```

10. update work/root status and this handover after the complete Part 010 first pass;
11. stop after first-pass transcription.

## Do not combine with Part 010 first pass

Do **not**:

- promote any Part 010 page to `verified` during first-pass transcription;
- perform the Part 010 Tamil direct visual verification gate in the same activity;
- create `AUDIT_PART_010.md`;
- call Part 010 archival-ready;
- begin Part 010 English translation;
- alter released English Parts 001–009 merely for harmonization.

If all 23 first-pass records are completed with no source-blocking issue, the next separate activity will be **Part 010 Tamil direct visual verification**.
