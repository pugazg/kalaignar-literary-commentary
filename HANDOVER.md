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
7. for English work additionally fresh-read:
   - `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`;
   - `works/thirukkural/translations/en/GLOSSARY.md`;
   - `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
   - the latest relevant editorial review and release report.

Repository state is authoritative.

## Source rule

The supplied Tamil scans are controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

Source PDFs are working/control sources and are not to be committed to GitHub unless the user explicitly requests that.

OCR/parsed text may assist but is never authoritative over direct inspection of the scan.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Keep these as separate gates.

Every project-created English page must identify:

```yaml
translation_type: "project_translation"
```

Released English material must not be revised merely to harmonize later vocabulary.

Permanent earlier protections remain binding, including:

- chapter 38 `ஊழ்` → **Oozh**;
- Kalaignar's `இயற்கை நிலை` → **natural condition**;
- Kural 543's Kalaignar-directed `அறவோர் நூல்களுக்கும்` → **the books of the virtuous** rather than an automatic caste-specific conventional gloss;
- preservation of Kalaignar's governance, citizens, working-people, justice, public-resource and rational/inquiry vocabulary where the Tamil explicitly uses it.

# Established state

## Tamil

Parts **001–010 are audited / ARCHIVAL-READY continuously** through:

- overall scan **214**;
- printed page **181**;
- Kural **895**.

Latest Tamil audit:

`works/thirukkural/AUDIT_PART_010.md` — **PASS / ARCHIVAL-READY**.

## English project translation

Parts **001–010 are fully released continuously through the supplied Kural 895**.

Part 010 English:

- first pass: **COMPLETE 23 / 23**;
- direct source-check: **COMPLETE 23 / 23**;
- editorial consistency / glossary reconciliation: **COMPLETE 23 / 23**;
- release gate: **PASS / COMPLETE 23 / 23**;
- final status: **23 / 23 `release-ready`**.

Part 010 editorial review:

`works/thirukkural/translations/en/reviews/PART_010_REVIEW.md`

Part 010 release report:

`works/thirukkural/translations/en/reviews/PART_010_RELEASE_REPORT.md` — **PASS / RELEASE APPROVED**.

# Part 010 source boundary

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_010_pages_192-214.pdf`

Audited/released scope:

- physical pages: **23**;
- overall scans: **192–214**;
- Part-local pages: **1–23**;
- printed pages: **159–181**;
- Kural range present: **781–895**;
- source structural section throughout: `பொருள் — நட்பியல்`;
- chapters visible: **79–90**;
- chapters **79–89** complete;
- chapter 90 `பெரியாரைப் பிழையாமை` present only through Kural **895**;
- Tamil `verified`: **23 / 23**;
- English `release-ready`: **23 / 23**.

Part 009 → Part 010 continuity passed at printed page **158 → 159** / Kural **780 → 781**.

The supplied Part 010 source physically ends at printed page **181 / Kural 895**. No Kural **896** or later Tamil or English text has been inferred or created.

# Released Part 010 English terminology

Structural term:

- `நட்பியல்` → **Friendship**.

Do not expand the section into an invented “Friendship and Enmity” label. The supplied source itself continues to print `நட்பியல்` through this unit.

Released main-body chapter headings:

- 79 `நட்பு` → **Friendship**;
- 80 `நட்பாராய்தல்` → **Examining Friendship**;
- 81 `பழைமை` → **Long-Standing Friendship**;
- 82 `தீ நட்பு` → **Harmful Friendship**;
- 83 `கூடா நட்பு` → **False Friendship**;
- 84 `பேதைமை` → **Folly**;
- 85 `புல்லறிவாண்மை` → **Possession of Little Understanding**;
- 86 `இகல்` → **Discord**;
- 87 `பகை மாட்சி` → **Excellence in Enmity**;
- 88 `பகைத்திறம் தெரிதல்` → **Discerning Enmity**;
- 89 `உட்பகை` → **Internal Enmity**;
- 90 `பெரியாரைப் பிழையாமை` → **Not Offending the Great**.

Chapter 87 was deliberately refined during editorial review from provisional **The Character of Enmity** to **Excellence in Enmity**, preserving the force of `மாட்சி` and following Kalaignar's Kural 861 commentary.

# Part 010 released source-check protections

All seven Part 010 source-check corrections are released and must not be silently reverted:

1. **Kural 813** — **women for hire**, not the unsupported first-pass “women who sell intimacy.”
2. **Kural 822** — **women for hire** in the Kural; Kalaignar's fuller explanation stays in the separate commentary.
3. **Kural 842 commentary** — no unsupported **earned**.
4. **Kural 849** — corrected subject relationship using Kalaignar's adjacent commentary as the permitted interpretive aid.
5. **Kural 850** — the evidence clause remains in Kalaignar's commentary and is not inserted into the Kural.
6. **Kural 867 commentary** — no unsupported added phrase **and harmful to us**.
7. **Kural 887** — no unsupported **metal** for `செப்பு`; commentary retains *seppu*.

Released source-sensitive protections also include:

- **Kural 835** — Kalaignar's `ஏழு காலத்திலும்` → **seven periods**; do not import “seven births.”
- **Kural 850 commentary** — retain evidence/truth framing and quoted **“ghosts”** image.
- **Kural 861** — retain Kalaignar's supplied interpretation: leaving the weak and preferring to fight the strong is praised as `பகைமாட்சி`; do not replace it with a familiar external interpretation.
- **Kural 869 commentary** — retain **“cowards who are afraid, and ignorant cowards”**. The repetition is directly source-confirmed.
- **Kural 876** — retain the nuanced position of neither becoming too close to the enemy in friendship nor separating completely while maintaining hostility when danger arises.
- **Kural 895** — retain the distinction between the Kural's **ruler** and Kalaignar commentary's institutional **government** framing.

# Current stopping point

The project has completed every workflow gate for all Thirukkural material currently supplied, through Kural **895**.

There is **no active next transcription or translation gate because the next controlling Tamil source has not been supplied**.

Do not guess that the next file is “Part 011,” do not invent a filename, and do not create Kural 896 onward from memory or another edition.

# Exact next activity when a new Thirukkural source is supplied

1. inspect the actual newly supplied scan before creating or modifying archival records;
2. identify its true printed-page, Kural and chapter starting point from the scan itself rather than its filename;
3. verify whether it continues the existing boundary at printed page **181 → 182** / Kural **895 → 896**;
4. inspect the repository first and continue existing work if the source has already been started rather than creating duplicates;
5. only if the source genuinely continues the book, begin the separate **Tamil first-pass transcription** gate for the new supplied pages;
6. preserve the source's exact historical spelling, punctuation, wording, names, numbers, repetition, unusual grammar and typographical forms;
7. stop after that gate and continue the permanent workflow one gate at a time.

Until a new controlling Tamil source is supplied, the correct project state is **waiting for source**.
