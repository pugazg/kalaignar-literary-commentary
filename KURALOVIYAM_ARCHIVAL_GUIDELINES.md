# Kuraloviyam — Archival Guidelines

This document is the work-specific operating guide for `works/kuraloviyam/` in `pugazg/kalaignar-literary-commentary`.

It supplements `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`. The controlling scan and the stricter source-preservation rule always govern.

## 1. Controlling-source rule

> **The rendered source scan is the controlling source.**

The Markdown archive is a preservation layer, not a corrected or normalized edition.

Never silently:

- correct spelling, punctuation, sandhi, names or numbers because another edition differs;
- replace a printed Kural with a memorized, web or standard-edition reading;
- modernize historical forms;
- reconstruct unclear letters from context;
- treat OCR, parsed text or model memory as source authority;
- merge printed text with handwriting, library marks, bleed-through or scanner artefacts.

If a reading is uncertain, use `needs-review`, `partial` or `blocked` rather than guessing.

## 2. Source identity and split-PDF rule

The user reports the complete Kuraloviyam source as **666 physical PDF pages**, split manually into **six equal parts of 111 pages each** because the original PDF is larger than the chat upload limit.

Canonical overall scan mapping:

| Part | Overall scans |
|---|---:|
| 001 | 1–111 |
| 002 | 112–222 |
| 003 | 223–333 |
| 004 | 334–444 |
| 005 | 445–555 |
| 006 | 556–666 |

Repository `scan_page` always means the **overall 1–666 physical scan number**. It never restarts at 1 for a later split file.

`part_page` may record the local 1–111 position inside the supplied split.

Do not infer a later part's exact filename until that file is supplied.

## 3. Source files are not stored in GitHub

The split PDFs are working/control sources and are not committed to this repository unless the user explicitly changes that policy.

Archive transcription, metadata, indexes, audit/review artefacts and later translation layers in GitHub.

## 4. Image-only / no-text-layer handling

Part 001 has no usable parsed text layer in the supplied file environment. Therefore:

- page images must be inspected directly;
- OCR may be used only as a disposable aid if explicitly needed, never as authority;
- unclear small print must not be silently filled from language knowledge;
- final verification must compare the Markdown against the rendered scan.

## 5. Page-aligned Tamil archive

Every physical scan page must eventually have one Markdown record, including covers, publication matter, prefaces, handwritten facsimiles, photographs, illustrations and body pages.

Recommended front matter:

```yaml
---
scan_page: 1
part: 1
part_page: 1
printed_page: null
work: "kuraloviyam"
section: "front-matter"
page_type: "cover"
status: "needs-review"
language: "ta"
source_filename: "TVA_BOK_0065733_குறளோவியம்_part_001_pages_1-111.pdf"
transcription_method: "manual visual transcription from rendered source scan"
---
```

Tamil status vocabulary:

- `not-started`
- `needs-review`
- `partial`
- `verified`
- `blocked`

Use `verified` only after the required direct source comparison and meaningful visual-text fidelity gate are complete.

## 6. Kuraloviyam-specific fidelity

Kuraloviyam combines prose, Kural quotations/references and substantial illustration/layout work. Preserve, when source-supported:

- section or vignette headings;
- prose paragraph boundaries and dialogue structure;
- quoted Kural text and its printed lineation;
- `அதிகாரம்` / chapter labels, numbers and Kural/song-number references exactly as printed;
- quotation marks, separators and deliberate block placement;
- running headers and printed page numbers as page furniture rather than body prose;
- captions or text directly associated with illustrations;
- continuation across physical page boundaries.

Do not substitute standard Thirukkural wording for what this edition actually prints.

Illustrations should receive factual `visual_notes`; pixel-perfect artwork recreation is not required.

## 7. Part-based multi-pass workflow

Because the 666-page source is supplied as six 111-page parts, each part is processed through explicit gates. Do not collapse the gates merely to move faster.

For each part:

1. **Source intake** — confirm the actual local page count, overall scan range, visible printed-page boundaries and source identity.
2. **Pass 1: physical capture / transcription** — create all 111 page records, normally in batches of about 10 physical scans; new records remain `needs-review` unless source-limited.
3. **Pass 2: textual verification** — compare wording, punctuation, paragraph boundaries, Kural text and metadata directly with the scan.
4. **Pass 3: meaningful visual-text verification** — verify headings, lineation, block relationships, page furniture and illustration/text relationships.
5. **Part audit** — check 111/111 physical coverage, continuity, statuses, boundary to the adjacent part and unresolved source limitations.
6. Only after the Tamil part is archival-ready may any project-created English translation for that part begin.

Part 001 source intake is the first gate. Later parts must not be treated as inspected merely because their overall ranges are known.

## 8. Batch discipline

Normal Pass-1 batch: **about 10 physical scans**, adjusted slightly for a natural front-matter or vignette boundary when useful.

For every batch:

1. fetch live `main`;
2. resolve the exact split PDF;
3. inspect the source images directly;
4. fetch existing target records before writing;
5. transcribe only source-supported visible text;
6. record factual visual notes for non-text/illustration material;
7. preserve overall scan numbering;
8. commit sequentially;
9. inspect the changed-file set and record the next frontier.

## 9. English layers

If a published English Kuraloviyam source is later supplied, archive it as a separate source-controlled edition. Do not mix it with a project-created translation.

A project-created English translation may be added only from audited Tamil records and must declare:

```yaml
translation_type: "project_translation"
```

## 10. Current frontier

Part 001 (`overall scans 1–111`) has been supplied. Initial source intake establishes front matter through scan 17, main body beginning at scan 18 / printed page 1, and Part 001 ending at scan 111 / printed page 94.

The next activity after intake is **Pass 1 physical capture/transcription for scans 1–10**.