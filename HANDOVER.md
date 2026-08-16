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
5. inspect the actual attached source pages for the activity being performed;
6. inspect the existing target Markdown files before updating them.

The repository state is authoritative for workflow status. Do not rely on conversational summaries when they conflict with GitHub.

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil.

The source PDFs are working/control sources and are **not to be uploaded into this GitHub repository** unless the user explicitly changes that instruction.

OCR or parsed text may assist but is never authoritative. Direct scan inspection controls transcription and verification.

## English fidelity rule

The English layer is a **project-created translation**, not an official/publisher English edition.

It must retain Kalaignar's language, examples, images, political/social vocabulary, emphases and interpretive direction. Do not substitute another commentator's reading or familiar standard English Kural wording.

Permanent protected examples include:

- chapter 38 `ஊழ்` → **Oozh**, with Kalaignar's `இயற்கை நிலை` → **natural condition**;
- Kural 543: Kalaignar explains `அந்தணர் நூற்கும்` as `அறவோர் நூல்களுக்கும்`; retain the English sense **the books of the virtuous**, not an automatic caste-specific “Brahmin(s)” rendering;
- preserve his governance, citizens, treasury, revenue, justice, public-resource and working-people language when it occurs;
- preserve direct source-supported comparisons rather than sanitizing them.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

These are separate gates. Do not collapse them.

# Established completed state

## Tamil

Parts **001–007 are audited / ARCHIVAL-READY** through:

- overall scan **148**;
- printed page **115**;
- Kural **565**.

## English project translation

Parts **001–007 are fully released** through Kural **565**.

Released Parts 001–007 must not be revised merely because later Parts introduce similar terminology. Any project-wide change must be deliberate, source-supported and documented.

# Part 008 Tamil — ACTIVE

Controlling source supplied in the conversation:

`திருக்குறள்_கலைஞர்_உரை_part_008_pages_149-169.pdf`

A duplicate attachment display name may include `(2)`; identify the source by its content, not filename decoration.

Physical scope:

- **21 pages**;
- overall scans **149–169**;
- printed pages **116–136**;
- Kural **566–670**.

First-pass transcription:

- **21 / 21 complete**.

Verification state at handover:

- `verified`: **14 / 21** — scans **149–162 / Kural 566–635**;
- `needs-review`: **7 / 21** — scans **163–169 / Kural 636–670**;
- `partial`: **0**;
- `blocked`: **0**.

Part 008 audit: **not started**.

Part 008 English translation: **not started**.

## Completed Part 008 verification history

### Batch 1 — scans 149–155 / Kural 566–600

Completed.

One source-supported first-pass correction was required on scan 153 / Kural 589 commentary:

- `ஒத்திருந் தால்` → `ஒத்திருந்தால்`.

### Batch 2 — scans 156–162 / Kural 601–635

Completed.

All seven pages matched the scan; no textual correction was required.

Scan **162 / printed page 129** directly confirms the running-header structural transition:

`பொருள் — அரசியல்` → **`பொருள் — அமைச்சியல் — அமைச்சு`**.

Preserve this transition exactly.

# Exact next activity

Perform **Part 008 Tamil direct visual verification — Batch 3 only**, for overall scans **163–169 / printed pages 130–136 / Kural 636–670**.

The source pages have already been identified as:

- scan 163 / printed 130 — completes chapter 64 `அமைச்சு`, Kural 636–640;
- scans 164–165 / printed 131–132 — chapter 65 `சொல்வன்மை`, Kural 641–650;
- scans 166–167 / printed 133–134 — chapter 66 `வினைத் தூய்மை`, Kural 651–660;
- scans 168–169 / printed 135–136 — chapter 67 `வினைத்திட்பம்`, Kural 661–670.

Important: in the previous chat, source images for these seven pages were inspected and scan 163's existing Markdown was fetched, but **no Batch 3 page was promoted or edited before this handover request**. Therefore the repository status of 14 verified / 7 needs-review is the correct starting point.

## Batch 3 required procedure

For each of scans 163–169:

1. inspect the controlling scan image directly;
2. fetch the corresponding `works/thirukkural/pages/....md` file;
3. compare Kural wording letter-by-letter, including joins, spacing, punctuation and two-line structure;
4. compare chapter heading / running header and all Kalaignar commentary;
5. correct only differences directly supported by the scan;
6. if the page passes, change:
   - `status: "needs-review"` → `status: "verified"`;
   - `transcription_method` → `"direct visual comparison with source scan"`;
7. document every actual correction;
8. after all seven pages, synchronize root README, `works/thirukkural/README.md`, and this handover.

Stop after scan 169.

## Do not do during Batch 3

Do **not**:

- create `AUDIT_PART_008.md` in the same activity;
- declare Part 008 `ARCHIVAL-READY` merely because verification becomes 21/21;
- begin Part 008 English translation;
- begin Part 009 Tamil transcription;
- alter released English Parts 001–007.

If all seven pages pass, Part 008 should be recorded as **21/21 verified**, and the next separate activity should be the **Part 008 Tamil audit / archival-ready decision**.

# After Part 008 verification

The intended sequence is:

1. Part 008 Tamil audit / archival-ready decision;
2. Part 008 English first-pass translation;
3. Part 008 English source-check;
4. Part 008 English editorial consistency / glossary reconciliation review;
5. Part 008 English release gate;
6. only then proceed to Part 009 Tamil work unless the user explicitly changes the order.

Part 009 source has been supplied/received in the broader project context, but **Part 009 transcription is not active and must not be started during the current Part 008 verification activity**.
