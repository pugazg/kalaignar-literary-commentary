# சங்கத் தமிழ் — archival / provenance guidelines

This document governs `works/sangatamil/` in `pugazg/kalaignar-literary-commentary`.

It combines the source-first page workflow used for `works/thirukkural/` with the page/section/provenance discipline used in `pugazg/tolkappiyap-poonga`.

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

OCR may assist location but is never authoritative. A page becomes `verified` only after direct visual comparison with the scan.

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

When a page has meaningful visual-text structure, the following optional fields may also be used:

```yaml
visual_fidelity: "needs-review"
visual_notes: "decorative heading; verse block; source citation block"
```

After direct comparison of both text and meaningful layout, `visual_fidelity` may be promoted to `verified`.

Status vocabulary:

- `not-started`
- `partial`
- `needs-review`
- `verified`
- `blocked`

## 3. Source-integrity rule

The current supplied PDF has been independently verified as a **497-scan complete source**. `pdfinfo` reports 497 pages; scans 493–497 render directly from the mounted PDF; scan 497 is the back cover.

The earlier 150-page count came from a preview-service limit and is not a valid archival boundary.

Current source controls:

- canonical scan range: **1–497**;
- do not create scan 498+ records;
- do not infer printed-page numbers from scan arithmetic;
- if a page is cropped, damaged, shadowed or otherwise source-limited, document that defect at the page level rather than changing the global source boundary.

If cropping, damage, shadow, binding curvature or scan loss hides characters or meaningful layout, do not reconstruct the hidden material from context. Keep the page `partial` or `blocked` as appropriate.

## 4. Verse / prose fidelity

This work mixes Kalaignar's poetic rendering, narrative/explanatory prose, Sangam quotations and word glosses.

Preserve:

- each printed verse line as its own Markdown line;
- paragraph boundaries for prose;
- quotation marks and asterisks/dividers where meaningful;
- cited Sangam poem text exactly as printed here;
- the printed source label, poem number and poet attribution;
- `பொருள் விளக்கம்` as a distinct source block.

Do not substitute a web or critical-edition Sangam verse for the wording printed in this book.

### 4.1 Visual text fidelity

Text fidelity includes the **meaningful visual organization of the printed text**, not only the sequence of characters.

During transcription and final verification, preserve or explicitly document, where source-visible and meaningful:

- verse line breaks and stanza grouping;
- prose paragraph breaks;
- indentation and hanging indentation;
- centered, right-aligned or otherwise deliberately positioned headings/lines;
- decorative heading hierarchy and the exact heading text;
- isolated quotation/citation blocks;
- `பொருள் விளக்கம்` placement as a distinct visual/textual block;
- numbered or lettered lists and their grouping;
- asterisks, rules, ornamental separators and section breaks;
- bold, underline, enlarged text or other emphasis when it distinguishes structure or meaning;
- running headers, printed page numbers and footers as page furniture rather than silently merging them into body text;
- text printed inside or immediately associated with an illustration, including captions;
- continuation of a sentence, poem or paragraph across a physical page boundary.

#### Markdown representation rule

The repository does **not** need to imitate the page pixel-for-pixel or reproduce the exact font face, font size, colour, kerning or ornamental artwork.

Instead:

1. reproduce meaningful lineation and block structure faithfully with Markdown;
2. use limited HTML only when Markdown cannot preserve a meaningful alignment or grouping cleanly;
3. when exact spatial placement cannot be represented safely, preserve the text and add a concise factual `visual_notes` / HTML source comment describing the source arrangement;
4. never introduce alignment, emphasis, stanza breaks or decorative grouping that the scan does not support.

A page must **not** be marked `verified` merely because all readable characters appear correct. `verified` requires checking both:

- **textual fidelity** — wording, spelling, punctuation, line content and order; and
- **visual text fidelity** — meaningful lineation, paragraph/stanza/block structure, heading hierarchy, separators, emphasis and text/image relationship.

If visual structure is uncertain because the source is cropped or damaged, retain `needs-review`, `partial` or `blocked` even when most words are readable.

## 5. Illustrations

Illustration-only pages are archival records.

For a full-page image:

- use `page_type: "illustration"`;
- transcribe any printed caption verbatim;
- otherwise provide only a concise factual visual description;
- do not identify an unlabelled person from appearance alone;
- do not infer scene, date or literary identity unless the printed source supports it.

Where text and illustration share a page, record their relationship factually—for example, whether the illustration interrupts a verse block, sits between two text blocks, or carries a caption—without inventing narrative meaning from the artwork.

## 6. Structural section layer

The book uses decorative thematic headings rather than the numbered `மலர்` system of *தொல்காப்பியப் பூங்கா*.

Create source-order navigation nodes under:

`works/sangatamil/sections/`

Repository sequence numbers are navigation identifiers only; they must not be presented as source-authored chapter numbers.

A section README should record:

- exact printed heading;
- scan start/end;
- printed-page range where visible;
- page list and statuses;
- illustration pages;
- Sangam source citations found within the section;
- boundary confidence;
- preservation statement that the full text remains in page records.

Do not establish a section boundary merely from page count. Confirm the next decorative heading or another clear source marker.

## 7. Sangam-source provenance layer

Maintain:

`works/sangatamil/indexes/source-citation-register.md`

For each printed Sangam citation, record only source-supported facts:

- scan page;
- section;
- anthology/work name;
- poem number;
- poet attribution;
- exact page record containing the citation;
- verification status.

Do not silently correct a poem number or poet from an external edition. If a later comparison is requested, preserve the printed citation and record the comparison separately.

## 8. Gate sequence

For the Tamil source:

**source intake → page records / first-pass transcription → direct textual + visual-fidelity verification → section review → batch/part audit**.

Do not collapse first-pass transcription and direct verification into one claimed gate unless the page was actually read directly against the scan for both text and meaningful visual organization.

## 9. English layer

The repository already anticipates a separately published English *Sangatamil* source. If that English source is supplied, archive it as an independent source-controlled edition with its own pagination and wording, then create an alignment layer.

Do not overwrite it with a project translation, and do not use it to silently rewrite the Tamil archive.

If the user separately requests a project-created English translation before a published English source is supplied, follow the Thirukkural translation gates and mark it explicitly as `translation_type: "project_translation"`.

## 10. Current source and milestone

The current supplied source is complete at **497 scans**, ending with the back cover at scan 497.

Current first milestone:

1. establish source metadata and page map;
2. preserve front matter scans 1–16;
3. map the first two decorative body sections beginning at scans 17 and 20;
4. finish front-matter transcription/verification before bulk body work;
5. expand the Sangam citation register only from directly inspected pages;
6. progressively extend physical page records through scan 497 in source order.
