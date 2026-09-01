# சங்கத் தமிழ் — archival / provenance guidelines

This document governs `works/sangatamil/` in `pugazg/kalaignar-literary-commentary`.

The canonical execution cadence is defined in [`works/sangatamil/MULTI_PASS_WORKFLOW.md`](works/sangatamil/MULTI_PASS_WORKFLOW.md), with Gemini-specific rules in [`works/sangatamil/GEMINI_RECONCILIATION_PLAN.md`](works/sangatamil/GEMINI_RECONCILIATION_PLAN.md).

## 1. Controlling source

> **Scan = final authority. Gemini = lexical aid. Repository = preservation layer.**

Controlling source:

`TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

Never silently modernize, normalize, correct, reconstruct or replace:

- Kalaignar's wording;
- Sangam quotations as printed in this edition;
- old/uncommon Tamil glyph forms;
- spelling, sandhi, punctuation or lineation;
- source work names, poem numbers or poet attributions;
- decorative headings;
- `பொருள் விளக்கம்` wording;
- publication/front-matter wording.

OCR/Gemini may assist lexical recovery or navigation but is never final authority. A page becomes `verified` only after the designated direct-source verification gates have passed.

## 2. Physical-page layer

Every physical scan in the supplied PDF must have exactly one archival Markdown record under:

`works/sangatamil/pages/`

Use zero-padded physical scan numbers. Record covers, title pages, annotations, blanks, handwritten facsimiles, body text, decorative dividers and illustrations; do not omit non-text pages.

Recommended front matter:

```yaml
---
scan_page: 426
printed_page: "414"
work: "sangatamil"
section: "ஒருதலைக் காதல்"
page_type: "text"
status: "needs-review"
visual_fidelity: "needs-review"
language: "ta"
source_filename: "TVA_BOK_0042551_சங்கத்_தமிழ்.pdf"
---
```

Status vocabulary:

- `not-started`
- `partial`
- `needs-review`
- `verified`
- `blocked`

During current Pass 1, newly created records should normally remain `needs-review` with `visual_fidelity: needs-review`.

## 3. Source-integrity and pagination rule

The source has been independently confirmed as **497 physical scans**. Scan **497** is the back cover.

Canonical controls:

- physical scan range: **1–497**;
- never create scan 498+;
- printed-page numbers must be read from the scan, not inferred from scan arithmetic;
- physical scan number and printed page number are different coordinate systems;
- if a page is cropped, damaged, shadowed or otherwise source-limited, document that defect at page level rather than altering the global source boundary.

The earlier 150-page count was a preview-service limitation and is retired.

If cropping, binding curvature, shadow or scan loss hides text, do not reconstruct hidden material from context. Use `partial` or `blocked` when necessary.

## 4. Gemini lexical-scaffold rule

A complete Gemini transcription was supplied in ten Markdown batches. It is useful for old/uncommon Tamil forms, but it is not a physical-page or structural authority.

Gemini may:

- corrupt or omit decorative headings;
- flatten punctuation or paragraph structure;
- move continuation lines across apparent page boundaries;
- merge quotation/provenance/gloss blocks;
- omit illustration/divider/blank pages;
- include running headers or page numbers in body text;
- misread old Tamil glyphs despite being useful as a first lexical scaffold.

### 4.1 Gemini page-marker warning

Comments such as:

`<!-- Page N of 497 -->`

must **not** be interpreted as physical scan numbers. In the supplied batches they generally identify **printed book pages** used by Gemini's extraction sequence. Illustration/divider pages can be absent from that sequence.

Therefore:

> **Drive physical sequencing from the PDF scan only.**

At the current frontier, `File10.md` is the relevant supplied scaffold. Its header describes Book Pages **414–484** corresponding to physical PDF pages **426–497**. This mapping is a navigation aid, not permission to infer page boundaries without checking the scan.

## 5. Pass-1 capture vs later fidelity gates

Pass 1 exists to obtain complete physical/text coverage quickly and safely.

For each scan during Pass 1:

1. inspect the physical scan once;
2. identify page type and visible printed page number from the scan;
3. align Gemini only as lexical scaffold where available;
4. preserve directly visible headings and obvious line/paragraph grouping;
5. preserve source-visible quotation, provenance and `பொருள் விளக்கம்` blocks without replacing their wording from another edition;
6. create a separate factual record for illustration/divider/blank/non-text pages;
7. if a Gemini/source disagreement is plainly visible, source wins immediately;
8. if resolution would require prolonged forensic work, leave the record `needs-review` for later passes rather than inventing certainty.

Recommended text-page metadata:

```yaml
status: "needs-review"
visual_fidelity: "needs-review"
transcription_method: "Gemini lexical scaffold aligned to controlling source scan; textual/visual verification deferred"
```

For a directly inspected illustration/divider page, a direct visual capture statement may be used instead.

Do **not** routinely perform during Pass 1:

- full second character-by-character verification;
- final textual verification;
- final visual-fidelity audit;
- extended crop/zoom forensic work;
- external-edition correction;
- formal provenance verification;
- section-end investigation beyond what is directly visible;
- whole-book continuity audit;
- broad metadata normalization;
- per-page synchronization of README/index/HANDOVER documents.

A directly obvious source correction during Pass 1 is allowed; that does not promote the page to `verified`.

## 6. Verse / prose fidelity

The final archive must preserve:

- each printed verse line as its own Markdown line where visually meaningful;
- prose paragraph boundaries;
- quotation marks and meaningful asterisks/dividers;
- cited Sangam text exactly as printed in this edition;
- printed source label, poem number and poet attribution;
- `பொருள் விளக்கம்` as a distinct source block;
- numbered/lettered units where printed;
- continuation across physical page boundaries.

Do not substitute a web or critical-edition Sangam verse for the wording printed in this book.

During Pass 2, verify wording/spelling/punctuation/omissions directly against the scan. During Pass 3, verify meaningful visual organization and heading hierarchy.

## 7. Illustrations and decorative dividers

Illustration-only and divider pages are archival records, not gaps.

For a full-page image/divider:

- use an appropriate `page_type` (`illustration` for illustration-only pages; `text` may be used for a textual/decorative divider where the printed wording itself is the content);
- transcribe any printed caption or divider wording verbatim;
- otherwise give a concise factual visual description;
- do not identify an unlabelled person from appearance alone;
- do not infer scene/date/literary identity unless the printed source supports it;
- keep `needs-review` during Pass 1 unless later verification gates are completed.

Where meaningful text and illustration share a page, treat it as a text-bearing page rather than discarding the text as illustration metadata.

## 8. Decorative-heading rule

Decorative headings must be read from the scan. Gemini has repeatedly corrupted or dropped them during bulk work.

Use a decorative heading provisionally as the page's `section` during Pass 1 when it is directly visible. Do not attempt a formal section-end audit at that moment.

Canonical section starts/ends, page ranges, illustration placement and boundary confidence are established in **Pass 5**.

Repository sequence numbers are navigation identifiers only and must never be presented as source-authored chapter numbers.

## 9. Sangam-source provenance layer

Maintain ultimately:

`works/sangatamil/indexes/source-citation-register.md`

During Pass 1, preserve source-visible quotation/provenance/gloss text in the page record but do not stop the bulk capture to perform systematic provenance checking.

Pass 6 will verify across scans 1–497:

- anthology/work name;
- poem number/range;
- poet attribution;
- quoted Sangam text;
- `பொருள் விளக்கம்`;
- other printed source notes.

Never silently correct a printed poem number or poet from an external edition. External comparison belongs in a separate explicitly labelled layer.

## 10. Canonical multi-pass gate sequence

The old mixed cadence is retired. The canonical order is:

1. **Pass 1 — transcription / physical capture through scan 497**;
2. **Pass 2 — textual verification, scan 1 → 497**;
3. **Pass 3 — visual-text fidelity verification, scan 1 → 497**;
4. **Pass 4 — physical-page / omission / continuity audit, scan 1 → 497**;
5. **Pass 5 — section-structure audit, scan 1 → 497**;
6. **Pass 6 — Sangam source / provenance audit, scan 1 → 497**;
7. **Pass 7 — metadata / status consistency audit, scan 1 → 497**;
8. **Pass 8 — whole-volume synchronization and final audit**.

Do not opportunistically combine later passes into routine Pass-1 capture.

## 11. Batch and repository discipline

Normal Pass-1 batch: **about 10 physical scans**, adjusted to a nearby natural source boundary or reduced for dense pages.

For every batch:

- fetch live `main` before writing;
- preserve any newer durable state;
- create/update only the intended missing physical page records;
- commit sequentially;
- after the batch, compare the starting commit against live head;
- confirm the changed-file set matches the intended scan range;
- do not treat stale README/index snapshot text as the live frontier.

This compare-after-batch step is part of archival control, not merely a convenience.

## 12. English layer

If a separately published English *Sangatamil* source is supplied, archive it as an independent source-controlled edition with its own pagination and wording, then create an alignment layer.

Do not overwrite a published English source with a project translation, and do not use it to silently rewrite the Tamil archive.

If a project-created translation is separately requested, mark it explicitly as `translation_type: "project_translation"` and use the translation gates established by the repository.

## 13. Current active milestone — refreshed 2026-09-01

Last completed source-work checkpoint before the current documentation refresh:

`2b3552a1f487e6ab747a394a8fe36f80f49f2cae` — `sangatamil: Pass 1 capture scan 425`

Physical records exist through **scan 425**.

Remaining Pass-1 range at that checkpoint: **426–497 (72 scans)**.

Scan 425 is the decorative divider introducing:

- `கைக்கிளை`
- `ஒருதலைக் காதல்`

Direct source inspection confirms scan **426 / printed page 414** begins numbered unit **1**, starting `கற்கண்டுத் தமிழில் கவிதைகள் வடிக்கும்...`.

Active milestone:

> **Complete physical capture/transcription through scan 497 before beginning Pass 2.**

Next normal batch begins at **scan 426**, approximately scans **426–435** unless live `main` has already advanced.
