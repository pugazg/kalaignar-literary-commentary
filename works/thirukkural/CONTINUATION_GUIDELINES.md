# Thirukkural Continuation Guidelines — Parts 006–010 and Later

This document supplements the repository-level `LITERARY_COMMENTARY_PROCESSING_GUIDE.md` for the continuing archival work on **திருக்குறள் — கலைஞர் உரை**.

It is intentionally source-first and workflow-specific. If any later handover conflicts with this file about the **current stopping point**, the fresher `HANDOVER.md` wins. If any handover conflicts with the preservation rules below, the preservation rules win.

## 1. Mandatory startup for every new chat

Before making changes:

1. read `LITERARY_COMMENTARY_PROCESSING_GUIDE.md` completely;
2. read repository root `HANDOVER.md` completely;
3. read `works/thirukkural/README.md`;
4. read this `works/thirukkural/CONTINUATION_GUIDELINES.md`;
5. if present, read `works/thirukkural/HANDOVER_PARTS_006_010.md`;
6. inspect the repository before creating any new page record, so existing work is continued rather than duplicated;
7. inspect the actual attached scan pages that belong to the exact batch before transcribing them.

Do not rely on the PDF filename alone for content, printed page number, chapter boundary, or Kural number.

## 2. Controlling source

> **The supplied scan is the controlling source.**

Never silently:

- modernize Tamil spelling;
- normalize sandhi, word joining or punctuation;
- correct what appears to be a typo;
- substitute a familiar or web Thirukkural text;
- reconstruct unclear letters from memory;
- replace Kalaignar's commentary with a conventional interpretation;
- transcribe reverse-side bleed-through as current-page text.

The Markdown archive records this edition. It is not a corrected or standardized edition.

## 3. Newly supplied source inventory

Direct inspection of the five supplied continuation PDFs establishes the following source boundaries:

| Part | Source filename | Local PDF pages | Overall scans | Printed pages confirmed | Kural range confirmed |
|---|---|---:|---:|---:|---:|
| 006 | `திருக்குறள்_கலைஞர்_உரை_part_006_pages_107-127.pdf` | 21 | 107–127 | 74–94, with title/blank leaves between 76 and 79 | 366–460 |
| 007 | `திருக்குறள்_கலைஞர்_உரை_part_007_pages_128-148.pdf` | 21 | 128–148 | 95–115 | 461–565 |
| 008 | `திருக்குறள்_கலைஞர்_உரை_part_008_pages_149-169.pdf` | 21 | 149–169 | 116–136 | 566–670 |
| 009 | `திருக்குறள்_கலைஞர்_உரை_part_009_pages_170-191.pdf` | 22 | 170–191 | 137–158 | 671–780 |
| 010 | `திருக்குறள்_கலைஞர்_உரை_part_010_pages_192-214.pdf` | 23 | 192–214 | 159–181 | 781–895 |

These PDFs continue directly from the previously archived Kural **365** and extend the supplied source through overall scan **214** / printed page **181** / Kural **895**.

Source receipt is not the same as archival completion. Every part must still pass transcription, direct verification and audit independently.

## 4. Overall scan numbering

Repository page numbering follows the overall supplied scan sequence, not each PDF's local page number.

Examples:

- Part 006 local page 1 = overall scan 107;
- Part 007 local page 1 = overall scan 128;
- Part 008 local page 1 = overall scan 149;
- Part 009 local page 1 = overall scan 170;
- Part 010 local page 1 = overall scan 192.

Never restart numbering at 1 inside a new PDF part.

## 5. One record per physical scan

Every physical scan gets one Markdown record, including:

- commentary pages;
- section-title leaves;
- blank reverses;
- illustrations or facsimiles if encountered;
- pages whose printed page numeral is absent.

For a commentary page, use the established front matter pattern:

```yaml
---
scan_page: 114
part: 6
part_page: 8
printed_page: "81"
work: "thirukkural"
section: "பொருள் — அரசியல் — கல்வி"
page_type: "commentary"
status: "needs-review"
language: "ta"
source_filename: "திருக்குறள்_கலைஞர்_உரை_part_006_pages_107-127.pdf"
transcription_method: "manual transcription from source scan; direct visual verification pending"
---
```

For a title or blank page, use the actual page type and set `printed_page: null` when no numeral is visible rather than inventing one.

## 6. First-pass Tamil transcription rule

New page records begin as:

```yaml
status: "needs-review"
transcription_method: "manual transcription from source scan; direct visual verification pending"
```

A first-pass record is complete enough for later checking, but it is **not** verified.

During first pass:

- preserve Kural number exactly;
- preserve the two printed Kural lines;
- preserve Kalaignar commentary wording and paragraph boundaries;
- preserve source-specific joining, spelling and punctuation;
- reproduce headings only when visibly present on that page;
- do not infer missing printed numerals on section-title/blank leaves;
- describe blank/bleed-through pages factually rather than fabricating text.

## 7. Dedicated verification stage

Do not mix direct visual verification into the first-pass activity unless the current handover explicitly changes the workflow.

After **all physical pages in one supplied PDF part** have first-pass records:

1. compare each record directly with its scan;
2. correct only source-supported differences;
3. change `status` to `verified` only after comparison;
4. change `transcription_method` to `direct visual comparison with source scan`;
5. leave genuinely unresolved material `needs-review`, `partial` or `blocked` rather than guessing.

Verification is character-level/source-level review, not editorial modernization.

## 8. Part audit gate

Create `AUDIT_PART_00X.md` only after the full part has completed direct verification.

The audit must check at minimum:

- one record per physical scan;
- overall/local scan mapping;
- printed-page continuity and any deliberate gaps/title leaves;
- Kural continuity;
- chapter and section boundaries;
- unresolved pages;
- status integrity;
- source filename consistency;
- known source-sensitive wording.

Only a passed audit may declare the Tamil part **ARCHIVAL-READY**.

## 9. English translation gate

English is a separate **project-created translation** layer.

Never start English merely because the PDF has been supplied or first-pass Tamil exists.

Required order for each part:

**Tamil first pass → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release report.**

Do not collapse stages.

English must follow the released `TRANSLATION_GUIDE.md` and `GLOSSARY.md`, retain Kalaignar's language and interpretation, and keep Kural translation separate from commentary translation.

## 10. Part 006 structural transition

Part 006 is structurally important:

- scan 107 / printed 74 completes chapter 37 `அவா அறுத்தல்`, Kural 366–370;
- scans 108–109 / printed 75–76 contain chapter 38 `ஊழ்`, Kural 371–380;
- scan 110 is the `பொருள்` section-title leaf;
- scan 111 is its blank reverse, with only reverse-side bleed-through;
- scan 112 / printed 79 begins `பொருள் — அரசியல் — இறைமாட்சி`, Kural 381–385.

The visible printed pagination therefore jumps from 76 to 79 because the title and blank leaves have no printed numeral. Do not invent printed pages 77–78 for scans 110–111.

## 11. `ஊழ்` source-sensitive warning

In the Part 006 source, Kalaignar's commentary repeatedly explains `ஊழ்` using **`இயற்கை நிலை`**.

Preserve that Tamil exactly. Later English review must not automatically substitute a conventional fate/destiny interpretation when Kalaignar's own explanation differs.

## 12. Batch discipline

The current workflow normally advances in explicit bounded batches.

- Default first-pass batch target: **up to 7 scans**, unless the current handover specifies another scope.
- Never silently extend beyond the exact batch defined in `HANDOVER.md`.
- After each batch, synchronize the current-status documents before stopping.
- Do not begin the next supplied PDF part until the current part's first-pass stage is complete unless the user explicitly changes the plan.

## 13. Files that must stay synchronized

After each material processing batch, update as applicable:

- `works/thirukkural/README.md`;
- repository root `README.md`;
- root `HANDOVER.md`;
- `works/thirukkural/indexes/page-map.md` when page records are added;
- `works/thirukkural/metadata/source.md` when source-part inventory or authoritative source boundaries change;
- English status files only when English-stage state changes.

A dedicated new-chat handover may also be refreshed, but root `HANDOVER.md` remains the live state pointer.

## 14. Stop conditions

Stop and document the issue instead of guessing if:

- source sequence does not match the expected continuation;
- a Kural number is missing or duplicated unexpectedly;
- a printed page number conflicts with the scan sequence;
- a page is too damaged or unclear for safe transcription;
- a filename/path already exists with materially different content;
- English interpretation would require importing an external commentary.

## 15. Current continuation checkpoint

As of the handover created with this guide:

- Parts 001–005 Tamil: archival-ready;
- Parts 001–005 English project translation: released through Kural 365;
- Parts 006–010 source: received and boundary-inspected through Kural 895;
- Part 006 first-pass Tamil: scans 107–113 completed as `needs-review`;
- Part 006 direct verification: not started;
- Part 006 audit: not started;
- Parts 007–010 transcription: not started.

For the exact next scan batch, always read the fresher `HANDOVER.md` and `HANDOVER_PARTS_006_010.md` before acting.
