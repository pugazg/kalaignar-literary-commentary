# சங்கத் தமிழ் — archival / provenance guidelines

This document governs `works/sangatamil/` in `pugazg/kalaignar-literary-commentary`.

It combines the source-first page discipline used for `works/thirukkural/` with the page/section/provenance discipline used in `pugazg/tolkappiyap-poonga`.

The current execution cadence is defined canonically in [`works/sangatamil/MULTI_PASS_WORKFLOW.md`](works/sangatamil/MULTI_PASS_WORKFLOW.md).

## 1. Controlling source

> **The supplied scan is the authority. Markdown is a preservation layer, not a corrected edition.**

Never silently modernize, normalize, correct, reconstruct or replace:

- Kalaignar's wording;
- Sangam quotations as printed in this edition;
- spelling, sandhi, punctuation or lineation;
- source work names, poem numbers or poet attributions;
- decorative headings;
- `பொருள் விளக்கம்` wording;
- publication/front-matter wording.

OCR may assist location but is never authoritative. A page becomes `verified` only after the required later source-verification passes have been completed.

## 2. Physical-page layer

Every scan page in the supplied PDF must eventually have one Markdown record under:

`works/sangatamil/pages/`

Use zero-padded scan numbers. Record covers, title pages, annotations, blanks, handwritten facsimiles, body text and illustrations; do not omit non-text pages.

Recommended front matter:

```yaml
---
scan_page: 20
printed_page: "5"
work: "sangatamil"
section: "யாதும் ஊரே; யாவரும் கேளிர்!"
page_type: "text"
status: "needs-review"
language: "ta"
source_filename: "TVA_BOK_0042551_சங்கத்_தமிழ்.pdf"
---
```

Meaningful visual-text fields may also be used:

```yaml
visual_fidelity: "needs-review"
visual_notes: "decorative heading; verse block; source citation block"
```

Status vocabulary:

- `not-started`
- `partial`
- `needs-review`
- `verified`
- `blocked`

During the current Pass 1 transcription/capture phase, newly created records should normally remain `needs-review`; direct textual and visual-fidelity verification are intentionally deferred to later whole-volume passes.

## 3. Source-integrity rule

The current supplied PDF has been independently verified as a **497-scan complete source**. `pdfinfo` reports 497 pages; scans 493–497 render directly from the mounted PDF; scan 497 is the back cover.

The earlier 150-page count came from a preview-service limit and is not a valid archival boundary.

Current source controls:

- canonical scan range: **1–497**;
- do not create scan 498+ records;
- do not infer printed-page numbers from scan arithmetic;
- if a page is cropped, damaged, shadowed or otherwise source-limited, document that defect at the page level rather than changing the global source boundary.

If cropping, damage, shadow, binding curvature or scan loss hides characters or meaningful layout, do not reconstruct hidden material from context. Use `partial` or `blocked` where necessary.

## 4. Verse / prose fidelity

This work mixes Kalaignar's poetic rendering, narrative/explanatory prose, Sangam quotations and word glosses.

The final archive must preserve:

- each printed verse line as its own Markdown line;
- paragraph boundaries for prose;
- quotation marks and asterisks/dividers where meaningful;
- cited Sangam poem text exactly as printed here;
- the printed source label, poem number and poet attribution;
- `பொருள் விளக்கம்` as a distinct source block.

Do not substitute a web or critical-edition Sangam verse for the wording printed in this book.

### 4.1 Pass-1 capture vs later fidelity gates

The workflow now separates capture from verification.

During **Pass 1 — transcription / physical capture only**:

- perform one source reading sufficient to create the page record;
- preserve obvious lineation, paragraph breaks and directly visible headings;
- do not spend extended time on second-pass character resolution;
- mark uncertain readings for later review;
- do not claim `verified` merely because a first-pass transcription exists.

During **Pass 2 — textual verification**, check wording, spelling, punctuation, omissions, duplications, quotations and line content directly against the scan.

During **Pass 3 — visual-text fidelity verification**, check meaningful visual organization:

- verse line breaks and stanza grouping;
- prose paragraph breaks;
- indentation and hanging indentation;
- centered, right-aligned or otherwise deliberately positioned headings/lines;
- decorative heading hierarchy and exact heading text;
- isolated quotation/citation blocks;
- `பொருள் விளக்கம்` placement as a distinct visual/textual block;
- numbered or lettered lists and their grouping;
- asterisks, rules, ornamental separators and section breaks;
- bold, underline, enlarged text or other emphasis when structurally meaningful;
- running headers, printed page numbers and footers as page furniture;
- text printed inside or immediately associated with an illustration, including captions;
- continuation of a sentence, poem or paragraph across a physical page boundary.

The repository does **not** need to imitate the page pixel-for-pixel or reproduce exact font face, font size, colour, kerning or ornamental artwork.

Use Markdown for meaningful structure and limited HTML only when needed for alignment/grouping. Never introduce structure unsupported by the scan.

A page may be promoted to `verified` only when the required textual and visual-fidelity gates have actually passed.

## 5. Illustrations

Illustration-only pages are archival records.

For a full-page image:

- use `page_type: "illustration"`;
- transcribe any printed caption verbatim;
- otherwise provide only a concise factual visual description;
- do not identify an unlabelled person from appearance alone;
- do not infer scene, date or literary identity unless the printed source supports it.

During Pass 1, illustration records may remain `needs-review`; later visual-fidelity and physical-page audit passes confirm them systematically.

Where text and illustration share a page, record the relationship factually without inventing narrative meaning from the artwork.

## 6. Structural section layer

The book uses decorative thematic headings rather than the numbered `மலர்` system of *தொல்காப்பியப் பூங்கா*.

Create source-order navigation nodes under:

`works/sangatamil/sections/`

Repository sequence numbers are navigation identifiers only; they must not be presented as source-authored chapter numbers.

During Pass 1, an immediately visible decorative heading may be captured as source text and used provisionally in page metadata, but **do not perform section-end investigation or routine section-README synchronization**.

Canonical section starts, ends, page ranges, illustration placement and boundary confidence are established in **Pass 5 — section-structure audit, scan 1 → 497**.

A finalized section README should record:

- exact printed heading;
- scan start/end;
- printed-page range where visible;
- page list and statuses;
- illustration pages;
- Sangam source citations found within the section;
- boundary confidence;
- preservation statement that the full text remains in page records.

## 7. Sangam-source provenance layer

Maintain:

`works/sangatamil/indexes/source-citation-register.md`

Existing verified citations remain valid historical/source-checked records. During Pass 1, do not interrupt transcription to perform provenance verification or routine citation-register updates.

The systematic whole-volume provenance pass is **Pass 6 — Sangam source / provenance audit, scan 1 → 497**.

For each printed Sangam citation, ultimately record only source-supported facts:

- scan page;
- section;
- anthology/work name;
- poem number;
- poet attribution;
- exact page record containing the citation;
- verification status.

Do not silently correct a poem number or poet from an external edition. If a later comparison is requested, preserve the printed citation and record the comparison separately.

## 8. Canonical multi-pass gate sequence

The old mixed cadence is retired for this work. The canonical order is now:

1. **Pass 1 — transcription / physical capture only, through scan 497**;
2. **Pass 2 — textual verification, scan 1 → 497**;
3. **Pass 3 — visual-text fidelity verification, scan 1 → 497**;
4. **Pass 4 — physical-page and continuity audit, scan 1 → 497**;
5. **Pass 5 — section-structure audit, scan 1 → 497**;
6. **Pass 6 — Sangam source / provenance audit, scan 1 → 497**;
7. **Pass 7 — metadata / status consistency audit, scan 1 → 497**;
8. **Pass 8 — whole-volume synchronization and final audit**.

Do not opportunistically combine later passes into routine Pass-1 page capture.

See [`works/sangatamil/MULTI_PASS_WORKFLOW.md`](works/sangatamil/MULTI_PASS_WORKFLOW.md) for the exact per-pass rules.

## 9. English layer

The repository already anticipates a separately published English *Sangatamil* source. If that English source is supplied, archive it as an independent source-controlled edition with its own pagination and wording, then create an alignment layer.

Do not overwrite it with a project translation, and do not use it to silently rewrite the Tamil archive.

If the user separately requests a project-created English translation before a published English source is supplied, follow the Thirukkural translation gates and mark it explicitly as `translation_type: "project_translation"`.

## 10. Current source and active milestone

The supplied source is complete at **497 scans**, ending with the back cover at scan 497.

At adoption of the multi-pass workflow:

- physical page records exist through **scan 53**;
- scan 50 was completed under the earlier verified-page cadence;
- scans 51–53 are first-pass / `needs-review` records;
- **Pass 1 resumes at scan 54**.

The active milestone is now singular:

> **Complete physical capture/transcription through scan 497 before beginning the next whole-volume activity.**

Do not update broad status documents after every page during Pass 1. The next routine page activity is **scan 54 transcription/capture only**.