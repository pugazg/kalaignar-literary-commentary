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

Part 010 Tamil first-pass transcription is now **COMPLETE 23 / 23**, but direct visual verification has not begun. All Part 010 records remain `needs-review`.

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

## Released structural vocabulary through Part 009

- `அமைச்சியல்` → **Ministerial Affairs**;
- `அரணியல்` → **Fortification Affairs**;
- `கூழியல்` → **Wealth**;
- `படையியல்` → **Military Affairs**.

## Released Part 009 source-check protections

1. **Kural 680** — **“those with little support ... the trembling among their own”**; do not restore the unsupported territorial “smaller domain” wording.
2. **Kural 691** — **“kings”**; do not restore unsupported “contentious.”
3. **Kural 717** — retain the clause ending **“there is a lapse”**, grounded in the supplied edition's verified final `இழுக்கு`.
4. **Kural 725 commentary** — retain **“the skill of measure called logic”** from `தருக்கமென்படும் அளவைக் திறமும்`.
5. **Kural 733 commentary** — retain **“possesses wealth to that measure”** from `மளவுக்கு வளம்`.
6. **Kural 771 commentary** — retain **“have become memorial stones”** from `நடுகல்லாய்ப் போனவர்கள்`.
7. **Kural 773** — retain Kalaignar's explicit **great manliness / manliness** framing.

Kalaignar's institutional/public vocabulary and direct images remain protected. No substantive Kural/commentary body text was changed during the Part 009 release gate.

# Part 010 Tamil — FIRST PASS COMPLETE / VERIFICATION PENDING

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_010_pages_192-214.pdf`

The actual supplied scan was inspected across all **23** physical pages before first-pass creation.

Source intake established:

- physical pages: **23**;
- overall scans: **192–214**;
- Part-local pages: **1–23**;
- printed pages: **159–181**;
- Kural range present: **781–895**;
- source section throughout: `பொருள் — நட்பியல்`;
- chapters visible: **79–90**;
- chapter 90 `பெரியாரைப் பிழையாமை` begins on scan **214 / printed page 181**, and this supplied part contains only Kural **891–895** of that chapter.

Part 009 → Part 010 continuity is established at printed page **158 → 159** / Kural **780 → 781**.

Do not infer the continuation after Kural 895 without the next controlling source scan.

## Part 010 chapter / page map

- scans **192–193** / pp. **159–160** — `79. நட்பு` — Kural **781–790**;
- scans **194–195** / pp. **161–162** — `80. நட்பாராய்தல்` — **791–800**;
- scans **196–197** / pp. **163–164** — `81. பழைமை` — **801–810**;
- scans **198–199** / pp. **165–166** — `82. தீ நட்பு` — **811–820**;
- scans **200–201** / pp. **167–168** — `83. கூடா நட்பு` — **821–830**;
- scans **202–203** / pp. **169–170** — `84. பேதைமை` — **831–840**;
- scans **204–205** / pp. **171–172** — `85. புல்லறிவாண்மை` — **841–850**;
- scans **206–207** / pp. **173–174** — `86. இகல்` — **851–860**;
- scans **208–209** / pp. **175–176** — `87. பகை மாட்சி` — **861–870**;
- scans **210–211** / pp. **177–178** — `88. பகைத்திறம் தெரிதல்` — **871–880**;
- scans **212–213** / pp. **179–180** — `89. உட்பகை` — **881–890**;
- scan **214** / p. **181** — `90. பெரியாரைப் பிழையாமை` — **891–895** in this supplied part.

## Part 010 first-pass files

All **23 / 23** aligned Tamil records now exist:

- `0192-porul-natpu-01.md`
- `0193-porul-natpu-02.md`
- `0194-porul-natpaaraaythal-01.md`
- `0195-porul-natpaaraaythal-02.md`
- `0196-porul-pazhaimai-01.md`
- `0197-porul-pazhaimai-02.md`
- `0198-porul-thee-natpu-01.md`
- `0199-porul-thee-natpu-02.md`
- `0200-porul-koodaa-natpu-01.md`
- `0201-porul-koodaa-natpu-02.md`
- `0202-porul-pethaimai-01.md`
- `0203-porul-pethaimai-02.md`
- `0204-porul-pullarivaanmai-01.md`
- `0205-porul-pullarivaanmai-02.md`
- `0206-porul-igal-01.md`
- `0207-porul-igal-02.md`
- `0208-porul-pagai-maatchi-01.md`
- `0209-porul-pagai-maatchi-02.md`
- `0210-porul-pagaithiram-therithal-01.md`
- `0211-porul-pagaithiram-therithal-02.md`
- `0212-porul-utpagai-01.md`
- `0213-porul-utpagai-02.md`
- `0214-porul-periyaaraip-pizhaiyaamai-01.md`.

Every Part 010 first-pass page currently uses:

```yaml
status: "needs-review"
transcription_method: "manual transcription from source scan; direct visual verification pending"
```

Current Part 010 Tamil state:

- `needs-review`: **23 / 23**;
- `verified`: **0**;
- `partial`: **0**;
- `blocked`: **0**.

No direct visual verification status has been claimed. No `AUDIT_PART_010.md` exists. Part 010 is **not archival-ready**. Part 010 English has not begun.

## Verification attention point

During direct visual verification, inspect every line without importing a familiar Kural from memory. In particular, give fresh attention to scan **209 / Kural 869 commentary**, whose first-pass wording must be checked directly from the page image rather than stylistically repaired from context.

# Exact next activity

Perform the separate **Part 010 Tamil direct visual verification** for all **23 `needs-review` pages**, scans **192–214 / printed pages 159–181 / Kural 781–895**.

## Required verification procedure

1. fresh-read the mandatory startup files above;
2. inspect all 23 existing Part 010 Tamil records and confirm they begin at `status: "needs-review"`;
3. inspect the controlling Part 010 scan directly, page by page;
4. compare each Kural letter-for-letter with the scan, including source-supported joins, spacing and the printed two-line structure;
5. compare every Kalaignar commentary paragraph directly with the scan, including punctuation and paragraph boundaries;
6. verify chapter headings and the running-header hierarchy `பொருள் — நட்பியல் — <chapter>`;
7. verify `scan_page`, `part: 10`, `part_page`, `printed_page`, `section`, `page_type`, `language`, canonical `source_filename`, source marker and other metadata;
8. distinguish current-page printed text from reverse-side bleed-through or scan artefacts;
9. document every real first-pass correction found during direct comparison;
10. promote only pages that pass direct comparison to:

```yaml
status: "verified"
transcription_method: "direct visual comparison with source scan"
```

11. synchronize `works/thirukkural/README.md`, root `README.md`, and this handover after verification;
12. stop at the end of direct visual verification.

## Do not combine with verification

Do **not**:

- create `AUDIT_PART_010.md` during this activity;
- call Part 010 archival-ready merely because all pages verify;
- begin Part 010 English translation;
- alter released English Parts 001–009 merely for harmonization;
- infer or transcribe Kural 896 onward without the next controlling source.

If all 23 pages pass verification with no unresolved blocker, the next separate activity will be **Part 010 Tamil audit / archival-ready gate**.
