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

Every usable scan page must eventually have one Markdown record under:

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

Status vocabulary:

- `not-started`
- `partial`
- `needs-review`
- `verified`
- `blocked`

## 3. Source-integrity rule

The currently supplied attachment is usable only as the explicitly documented source fragment in `metadata/source.md`.

Do not create scan records beyond the verified usable attachment boundary. If a later complete PDF is supplied, inspect it independently, confirm continuity and then extend the archive.

Never infer missing pages from printed-page arithmetic.

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

## 5. Illustrations

Illustration-only pages are archival records.

For a full-page image:

- use `page_type: "illustration"`;
- transcribe any printed caption verbatim;
- otherwise provide only a concise factual visual description;
- do not identify an unlabelled person from appearance alone;
- do not infer scene, date or literary identity unless the printed source supports it.

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

**source intake → page records / first-pass transcription → direct visual verification → section review → source-fragment/part audit**.

Do not collapse first-pass transcription and direct verification into one claimed gate unless the page was actually read directly against the scan.

## 9. English layer

The repository already anticipates a separately published English *Sangatamil* source. If that English source is supplied, archive it as an independent source-controlled edition with its own pagination and wording, then create an alignment layer.

Do not overwrite it with a project translation, and do not use it to silently rewrite the Tamil archive.

If the user separately requests a project-created English translation before a published English source is supplied, follow the Thirukkural translation gates and mark it explicitly as `translation_type: "project_translation"`.

## 10. Current source fragment

The present attached source fragment exposes scans **1–150**. It is not to be declared the complete book. See `works/sangatamil/metadata/source.md` for the source-integrity warning.

Current first milestone:

1. establish source metadata and page map;
2. preserve front matter scans 1–16;
3. map the first two decorative body sections beginning at scans 17 and 20;
4. finish front-matter transcription/verification before bulk body work;
5. expand the Sangam citation register only from directly inspected pages.
