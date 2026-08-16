# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

Active work:

`works/thirukkural/`

## Mandatory startup in a new chat

Before making any change:

1. read `THIRUKKURAL_ARCHIVAL_GUIDELINES.md` completely;
2. read `LITERARY_COMMENTARY_PROCESSING_GUIDE.md` completely;
3. read this `HANDOVER.md` completely;
4. read `works/thirukkural/README.md`;
5. for English work, additionally read:
   - `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`;
   - `works/thirukkural/translations/en/GLOSSARY.md`;
   - `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
   - `works/thirukkural/translations/en/reviews/PART_007_REVIEW.md`;
   - `works/thirukkural/translations/en/reviews/PART_007_RELEASE_REPORT.md`;
6. inspect the existing target files before creating or updating anything.

The repository state is authoritative for workflow status. Do not rely on conversational summaries when they conflict with GitHub.

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil.

The source PDFs are working/control sources and are **not to be uploaded into this GitHub repository** unless the user explicitly changes that instruction.

OCR or parsed text may assist but is never authoritative. Direct scan inspection controls Tamil transcription and verification.

## English identity and fidelity rule

The English layer is a **project-created translation**, not an official/publisher English edition.

Every aligned English page must identify:

```yaml
translation_type: "project_translation"
```

The audited Tamil Markdown page is the working translation basis; the Tamil scan remains the ultimate source authority.

The English must retain Kalaignar's language, examples, images, political/social vocabulary, emphases and interpretive direction. Do not substitute another commentator's reading or familiar standard English Kural wording.

Permanent protected examples include:

- chapter 38 `ஊழ்` → **Oozh**, with Kalaignar's `இயற்கை நிலை` → **natural condition**;
- Kural 543: Kalaignar explains `அந்தணர் நூற்கும்` as `அறவோர் நூல்களுக்கும்`; retain the English sense **the books of the virtuous**, not an automatic caste-specific “Brahmin(s)” rendering;
- preserve his governance, citizens, treasury, revenue, justice, public-resource and working-people language when it occurs;
- preserve direct source-supported comparisons rather than sanitizing them;
- preserve rational/inquiry framing when Kalaignar explicitly uses it.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

These are separate gates. Do not collapse them.

# Established completed state

## Tamil

Parts **001–008 are audited / ARCHIVAL-READY** through:

- overall scan **169**;
- printed page **136**;
- Kural **670**.

Part 008 audit record:

`works/thirukkural/AUDIT_PART_008.md`

## English project translation

Parts **001–007 are fully released** through Kural **565**.

Released Parts 001–007 must not be revised merely because Part 008 introduces similar terminology. Any project-wide change must be deliberate, source-supported and documented.

# Part 008 Tamil — COMPLETE / ARCHIVAL-READY

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_008_pages_149-169.pdf`

Duplicate attachment display names may include a parenthesized suffix such as `(2)` or `(3)`; identify the source by its content, not filename decoration.

Physical scope:

- **21 pages**;
- overall scans **149–169**;
- printed pages **116–136**;
- Kural **566–670**.

Tamil state:

- first-pass transcription: **21 / 21 complete**;
- direct visual verification: **21 / 21 verified**;
- `needs-review`: **0**;
- `partial`: **0**;
- `blocked`: **0**;
- Tamil audit: **PASS / ARCHIVAL-READY**.

## Part 008 chapter coverage

- chapter 57 `வெருவந்த செய்யாமை` — Kural 566–570 in this part, completing the chapter;
- chapter 58 `கண்ணோட்டம்` — 571–580;
- chapter 59 `ஒற்றாடல்` — 581–590;
- chapter 60 `ஊக்கம் உடைமை` — 591–600;
- chapter 61 `மடி இன்மை` — 601–610;
- chapter 62 `ஆள்வினை உடைமை` — 611–620;
- chapter 63 `இடுக்கண் அழியாமை` — 621–630;
- chapter 64 `அமைச்சு` — 631–640;
- chapter 65 `சொல்வன்மை` — 641–650;
- chapter 66 `வினைத் தூய்மை` — 651–660;
- chapter 67 `வினைத்திட்பம்` — 661–670.

## Part 008 structural transition

Scan **162 / printed page 129 / Kural 631** directly confirms:

`பொருள் — அரசியல்` → **`பொருள் — அமைச்சியல் — அமைச்சு`**.

Preserve this distinction in the English structural metadata/headings according to the established translation conventions.

## Part 008 verification corrections retained by the audit

1. scan **153 / Kural 589 commentary**:
   - `ஒத்திருந் தால்` → `ஒத்திருந்தால்`;
2. scan **164 / Kural 643 commentary**:
   - `கேட்டோரைத் கவரும்` → `கேட்டோரைக் கவரும்`;
3. scan **166 / Kural 651 text**:
   - `ஆக்கம் தரூஉம்` → `ஆக்கந் தரூஉம்`;
4. scan **166 / Kural 653 text**:
   - `ஆஅதும் என்னு மவர்` → `ஆஅது மென்னு மவர்`.

The audit also confirmed that the scan-152 verification commit title suggested a wording correction but its patch changed only verification metadata; no Tamil text changed there.

# Part 008 English — NOT STARTED

No aligned English Part 008 page exists yet.

# Exact next activity

Perform **Part 008 English project translation — first pass only** for all aligned pages corresponding to scans **149–169 / printed pages 116–136 / Kural 566–670**.

## Required procedure

1. read the English translation guide, glossary, translation status, Part 007 review and Part 007 release report before writing;
2. use the audited Tamil Part 008 Markdown pages as the working translation basis;
3. mirror the Tamil filenames under `works/thirukkural/translations/en/pages/`;
4. identify every page as `translation_type: "project_translation"`;
5. set first-pass English pages to `status: "draft"`;
6. preserve Kural numbers and the two-line verse structure;
7. keep Kural translation and Kalaignar commentary translation visibly separate;
8. retain Kalaignar's own interpretation and vocabulary rather than importing conventional or external translations;
9. preserve the `அரசியல்` → `அமைச்சியல்` structural transition through the project's established English heading conventions;
10. after all 21 aligned English pages are drafted, synchronize the English translation status, work README, root README and this handover;
11. stop at the end of the English first-pass gate.

## Do not do in the Part 008 English first-pass activity

Do **not**:

- promote draft pages to `source-checked`;
- perform the English editorial review;
- create the Part 008 English release report;
- declare Part 008 English release-ready;
- begin Part 009 Tamil transcription;
- alter released English Parts 001–007.

# After Part 008 English first pass

The intended sequence is:

1. Part 008 English source-check against the audited Tamil pages;
2. Part 008 English editorial consistency / glossary reconciliation review;
3. Part 008 English release gate;
4. only then proceed to Part 009 Tamil work unless the user explicitly changes the order.

Part 009 source has been supplied/received, but **Part 009 transcription is not active**.
