# Next Chat Prompt — சங்கத் தமிழ் archival project

Continue the **சங்கத் தமிழ் — Kalaignar archival / correction project** directly in:

`pugazg/kalaignar-literary-commentary`

Branch: `main`

Active path: `works/sangatamil/`

## LIVE MAIN IS AUTHORITATIVE

Fetch live GitHub `main` **first** and preserve the newest durable state.

The latest policy checkpoint when this prompt was refreshed was:

`a4d13ade0b0c8ecccbe4609a438457d871163fdb` — `sangatamil: Lock Gemini lexical transcription policy`

Documentation commits may follow. If live `main` is newer, preserve it. Do not reset, overwrite, repeat or reopen later completed work merely because this prompt records an older SHA.

## Mandatory startup

Before any repository change, read completely:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`
5. `works/sangatamil/GEMINI_TEXT_LOCK.md` **— current user-approved lexical override**
6. `works/sangatamil/README.md`
7. `works/sangatamil/MULTI_PASS_WORKFLOW.md`
8. `works/sangatamil/GEMINI_RECONCILIATION_PLAN.md`
9. `works/sangatamil/metadata/source.md`
10. `works/sangatamil/metadata/transcription-policy.md`
11. `works/sangatamil/indexes/page-map.md`
12. `works/sangatamil/indexes/section-register.md`
13. `works/sangatamil/indexes/source-citation-register.md`

If older documents conflict with `GEMINI_TEXT_LOCK.md`, this prompt, or the refreshed Sangath Tamil guidelines, **the current user-approved Gemini text lock wins for the present correction workflow**.

## Current user directive — MUST FOLLOW

> **Keep the supplied words from Gemini transcription. Correct only source-supported structure—page placement, paragraph order, punctuation, quotation structure, headings, speaker labels, poetry lineation, spacing—and remove non-source material such as library stamps, handwriting-derived/OCR garbage. Do not silently correct lexical words.**

This is the controlling correction rule.

### Lexical authority

The supplied Gemini Markdown files (`File1.md` … `File10.md`) are the **locked lexical/text-wording layer**.

Do **not** change legitimate Gemini:

- words;
- characters;
- spellings;
- names;
- quoted wording;
- old/uncommon forms;
- lexical choices

merely because the PDF scan, OCR, another edition, memory, or a more familiar spelling seems different.

If changing a legitimate Gemini word would be required, leave it unchanged unless the user explicitly authorizes that lexical correction.

### Structural authority

The controlling PDF scan is authoritative for:

- physical scan/page placement;
- printed page numbers;
- page type;
- paragraph order/boundaries;
- punctuation;
- quotation structure and block placement;
- headings/hierarchy;
- speaker-label placement/formatting;
- poetry/verse lineation and stanza grouping;
- spacing/indentation;
- separators/rules;
- citation / provenance / `பொருள் விளக்கம்` block placement;
- continuation order across pages;
- illustration/divider/blank placement;
- running-header/footer handling.

### Remove non-source material from body text

Remove material accidentally captured by Gemini/OCR that is not part of the printed source body, including:

- library stamps / accession marks;
- handwriting-derived OCR text;
- handwriting garbage;
- scanner artefacts;
- bleed-through OCR garbage;
- unrelated labels/stickers;
- duplicated running headers or printed page numbers merged into the body;
- other clearly non-source OCR fragments.

Such marks may be noted factually in metadata/visual notes when useful, but must not contaminate body transcription.

### Missing lexical material

If the scan shows a whole printed paragraph/block absent from Gemini, **do not silently source-transcribe new lexical wording**. Flag the omission for follow-up unless the user explicitly authorizes recovery.

## Source files for the immediate work

Controlling full source:

`TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

Canonical physical range: **1–497**; scan **497** is the back cover.

For the immediate next work, attach/resolve:

1. `TVA_BOK_0042551_சங்கத்_தமிழ்_part_001_pages_1-50.pdf`
2. `File1.md`

The next supplied pair is:

- `TVA_BOK_0042551_சங்கத்_தமிழ்_part_002_pages_51-100.pdf`
- `File2.md`

Use later split PDF + `FileN.md` pairs as they are supplied.

Gemini page-marker comments are navigation aids only and do not control physical scan numbering.

## Durable state

Pass-1 physical capture is complete through **scan 497**. Do not restart it.

A previous scan-led lexical reconciliation reached scan **13** at:

`a9b7b118a5b729c4e670b453260dc06327a011a3` — `sangatamil: Pass 2 reconcile scan 13`

That source-based lexical correction mode is now **discontinued**.

The Gemini lexical lock was recorded at:

`a4d13ade0b0c8ecccbe4609a438457d871163fdb` — `sangatamil: Lock Gemini lexical transcription policy`

Do **not** resume the old lexical Pass 2 at scan 14.

For scans **1–13**, earlier source-based lexical edits may exist. When encountered in the new correction pass, restore the corresponding supplied Gemini lexical wording where it differs, while preserving source-supported structure.

## Current activity — Gemini-locked structural correction pass

The current task is to work sequentially through the physical source while:

- preserving supplied Gemini lexical words;
- using the scan to correct structure/presentation only;
- removing clearly non-source material from body text.

Normal batch: **about 10 physical scans**.

For each scan:

1. fetch the current repository page record;
2. inspect the corresponding PDF scan directly;
3. locate the matching Gemini text;
4. keep legitimate Gemini lexical wording;
5. correct source-supported page placement, paragraph order, punctuation, quotation structure, headings, speaker labels, poetry lineation, spacing and related structure;
6. remove non-source stamps/handwriting/OCR garbage from body text;
7. do not silently correct lexical words;
8. commit sequentially and continue.

At batch end:

1. compare the batch-start SHA to live head;
2. verify only intended page records changed;
3. fetch live `main` again;
4. record the next structural-correction frontier.

## Exact next activity

Fetch live `main`, complete mandatory startup, resolve **Part 001 pages 1–50 + `File1.md`**, and begin the **Gemini-locked structural correction pass at physical scan 1**.

Process approximately **scans 1–10** as the first batch.

For those pages:

- **keep supplied Gemini words**;
- correct only scan-supported structure/punctuation/spacing;
- remove non-source material such as library stamps and handwriting/OCR garbage;
- restore Gemini wording where earlier scan-led lexical edits changed it;
- do not invent missing lexical text;
- do not start another phase in the same batch.

Then perform the normal base→head audit.

## Execution behavior

When the user says **“proceed with next activity”**, **do the repository work directly**. Do not merely describe a plan, ask again for files that are already attached/resolved, or claim that split PDFs prevent continuation. If the relevant split source is available, inspect it and execute the batch.