# சங்கத் தமிழ் — archival / provenance guidelines

This document governs `works/sangatamil/` in `pugazg/kalaignar-literary-commentary`.

The canonical execution framework remains in [`works/sangatamil/MULTI_PASS_WORKFLOW.md`](works/sangatamil/MULTI_PASS_WORKFLOW.md), but the **current user-approved lexical policy** is recorded in [`works/sangatamil/GEMINI_TEXT_LOCK.md`](works/sangatamil/GEMINI_TEXT_LOCK.md). Where older workflow language conflicts with that file or with this document, **the Gemini text lock wins for the current correction workflow**.

## 1. Current controlling rule

The current correction workflow deliberately separates **lexical wording** from **source-supported structure**:

> **Keep the supplied words from the Gemini transcription. Correct only source-supported structure and presentation. Do not silently correct lexical words.**

Authority is therefore:

1. **Gemini transcription (`File1.md` … `File10.md`) = lexical/text-wording lock**;
2. **controlling PDF scan = physical-page and structural authority**;
3. **repository = preservation layer**.

For legitimate source body text, do **not** replace Gemini words, characters, spellings, names, quoted wording, old/uncommon forms, or lexical choices merely because the scan, another edition, memory, OCR, or a more familiar spelling appears preferable.

If a suspected correction requires changing a legitimate Gemini lexical word, leave it unchanged unless the user explicitly authorizes that lexical change.

### 1.1 Source-supported corrections that are allowed

Use the controlling scan to correct only structure/presentation such as:

- physical scan/page placement;
- printed page number and page type;
- paragraph order and paragraph boundaries;
- punctuation;
- quotation structure and quotation-block placement;
- headings and heading hierarchy;
- speaker-label placement/formatting;
- poetry/verse lineation and stanza grouping;
- spacing;
- indentation/alignment where meaningful;
- separators/rules;
- citation / provenance / `பொருள் விளக்கம்` block placement;
- continuation order across pages;
- illustration/divider/blank placement;
- running-header/footer handling.

The scan determines these structural facts. Gemini does not.

### 1.2 Non-source material must not contaminate body text

Remove from the archival body transcription material that is not part of the printed source text, including when Gemini/OCR accidentally captured it:

- library stamps and accession markings;
- handwriting-derived text or handwriting OCR garbage;
- scanner artefacts;
- bleed-through OCR garbage;
- unrelated labels/stickers;
- duplicated running headers/page numbers accidentally merged into body text;
- other clearly non-source OCR fragments.

When useful for provenance, such marks may be described factually in metadata/`visual_notes`, but they must not be silently retained as source body wording.

### 1.3 Missing-text rule

If the scan visibly contains an entire source paragraph/block that is absent from the supplied Gemini transcription, **do not silently source-transcribe new lexical content** under this lock. Record/flag the omission for follow-up unless the user explicitly authorizes lexical recovery.

## 2. Controlling source and physical boundary

Controlling source:

`TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

The source has **497 physical scans**. Scan **497** is the back cover.

Canonical controls:

- physical scan range: **1–497**;
- never create scan 498+;
- printed-page numbers must be read from the scan, not inferred by arithmetic;
- physical scan number and printed page number are different coordinate systems;
- scan defects/cropping must be documented rather than reconstructed from context.

Every physical scan has one Markdown record under:

`works/sangatamil/pages/`

Pass-1 physical coverage is complete through scan **497**.

## 3. Gemini files and split-PDF working method

The user supplied Gemini transcription in ten Markdown batches (`File1.md` … `File10.md`). These are the lexical/text-wording layer for the current correction workflow.

The user may supply the controlling PDF as split files such as:

- `TVA_BOK_0042551_சங்கத்_தமிழ்_part_001_pages_1-50.pdf` with `File1.md`;
- `TVA_BOK_0042551_சங்கத்_தமிழ்_part_002_pages_51-100.pdf` with `File2.md`;
- and corresponding later split parts / `FileN.md` files.

Use the relevant split PDF for direct page inspection and its corresponding Gemini Markdown file for lexical wording.

Gemini page comments such as `<!-- Page N of 497 -->` are navigation aids only and must not control physical scan sequencing. The PDF scan establishes physical placement.

## 4. Current correction workflow

The earlier source-based lexical Pass 2 began through scan **13**, but that mode is now discontinued. Do **not** continue character/word correction from the scan.

The current user-directed activity is a **Gemini-locked structural correction pass**.

For each physical scan:

1. fetch the current repository page record;
2. inspect the controlling scan directly;
3. align the corresponding supplied Gemini text;
4. preserve the legitimate Gemini lexical words;
5. correct only source-supported page placement, paragraph order/boundaries, punctuation, quotation structure, headings, speaker labels, poetry lineation, spacing, and related structural organization;
6. remove clearly non-source material such as library stamps, handwriting-derived/OCR garbage, scanner artefacts, and accidentally merged page furniture;
7. do not silently modernize, normalize, or source-correct lexical words;
8. if an existing repository record contains a prior source-based lexical change that conflicts with the supplied Gemini wording, restore the supplied Gemini lexical wording while preserving the source-supported structure;
9. if the scan reveals missing lexical content not present in Gemini, flag it rather than inventing/recovering words without user authorization;
10. commit the page correction and continue.

Normal working batch: **about 10 physical scans**, adjusted to a natural nearby boundary when useful.

At batch end:

- compare batch base → live head;
- confirm only intended page records changed;
- fetch live `main` again;
- record the next structural-correction frontier.

Do not merely describe the next activity when the user says **“proceed with next activity”** or equivalent. Execute the next recorded batch directly.

## 5. Verse / prose / quotation handling

The supplied Gemini words remain locked, while the scan controls their organization.

Correct from the scan:

- verse line breaks;
- stanza grouping;
- prose paragraph boundaries/order;
- dialogue grouping;
- speaker labels as structural labels;
- quotation marks/punctuation;
- quotation/citation block boundaries;
- `பொருள் விளக்கம்` block placement;
- headings and separators.

Do not substitute a web/critical-edition Sangam verse or a scan-derived alternative wording for Gemini lexical text unless the user explicitly authorizes lexical correction.

## 6. Illustration, divider, blank, handwriting and library marks

Illustration/divider/blank pages remain physical archival records.

For illustration-only pages:

- use factual visual description;
- do not identify an unlabelled real person from appearance;
- transcribe only printed source captions if present.

Handwriting, stamps, accession marks and scanner artefacts are **not body text**. If historically useful, note them factually outside the body transcription; do not allow OCR/Gemini garbage from them into the source text.

## 7. Provenance layer

Maintain ultimately:

`works/sangatamil/indexes/source-citation-register.md`

The current structural correction pass must not use external editions to rewrite Gemini lexical wording. External comparison, if later requested, must remain a separately labelled provenance/research layer.

## 8. Status and synchronization discipline

Do not automatically promote a page to `verified` merely because its structure was corrected. Later audit/status synchronization remains separate.

Broad synchronization of:

- `indexes/page-map.md`;
- `indexes/section-register.md`;
- `indexes/source-citation-register.md`;
- section READMEs;
- work/root README;
- root `HANDOVER.md`;
- next-chat prompt

should be done only at an explicit synchronization/handover activity, not after every page.

## 9. Current durable state — refreshed 2026-09-02

Pass-1 physical capture is complete through **scan 497**.

The discontinued scan-led lexical reconciliation reached **scan 13** at:

`a9b7b118a5b729c4e670b453260dc06327a011a3` — `sangatamil: Pass 2 reconcile scan 13`

The user-approved Gemini lexical lock was then recorded at:

`a4d13ade0b0c8ecccbe4609a438457d871163fdb` — `sangatamil: Lock Gemini lexical transcription policy`

From that directive onward:

> **Do not continue source-based lexical correction. Preserve Gemini words and perform source-supported structural correction only.**

### Exact next activity for a fresh chat

Fetch live `main`, read the mandatory startup documents including `works/sangatamil/GEMINI_TEXT_LOCK.md`, resolve:

- `TVA_BOK_0042551_சங்கத்_தமிழ்_part_001_pages_1-50.pdf`;
- `File1.md`;

then begin the **Gemini-locked structural correction pass from physical scan 1**, normally scans **1–10** for the first batch. Reconcile any earlier scan-1–13 source-based lexical edits back to the supplied Gemini wording where they differ, while applying only source-supported structural/punctuation/spacing corrections.