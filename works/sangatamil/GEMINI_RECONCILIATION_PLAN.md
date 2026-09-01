# சங்கத் தமிழ் — Gemini-assisted source reconciliation plan

This document refines the whole-volume workflow for `works/sangatamil/` after a complete Gemini transcription of the source was supplied as ten Markdown files.

The controlling source remains:

`TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

Canonical source range: **scan 1–497**.

## Why the workflow is changing

The supplied Gemini transcription is materially better at retaining old / uncommon Tamil glyph and word forms than the earlier manual transcription workflow. It is therefore valuable as a **lexical scaffold**.

It is not a facsimile or structural authority. The supplied transcription may:

- miss or alter decorative headings;
- flatten or move punctuation;
- merge or split verse/prose blocks incorrectly;
- move a sentence or continuation line upward/downward;
- omit paragraphs;
- lose illustration/blank-page boundaries;
- merge running headers / page numbers into body text;
- mis-order citation / `பொருள் விளக்கம்` blocks.

Therefore neither the existing repository text nor Gemini is allowed to overrule the scan.

> **Scan = final authority. Gemini = lexical aid. Repository = preservation layer.**

## Three-source decision rule

For every physical page, compare three layers where available:

1. **controlling scan** — wording + physical/visual organization authority;
2. **Gemini transcription** — preferred first lexical scaffold, especially for old Tamil glyphs;
3. **existing repository page** — prior archival work, useful for already-captured page boundaries/layout notes.

When they differ:

- the scan decides;
- never choose a familiar/modern spelling merely because it looks more natural;
- never choose our previous repository reading merely because it is already marked `verified`;
- never choose Gemini punctuation, heading, ordering or paragraph structure without scan support.

A previous `verified` status may be **reopened** if new evidence exposes substantive errors.

## Uploaded Gemini batches

Ten supplied Markdown files together cover the complete book in successive extraction batches. Their internal phase/page comments are navigation aids only. They must not be treated as canonical pagination or section boundaries.

The import/reconciliation process should record which Gemini file supplied the lexical scaffold when useful, but the archival page record remains controlled by the PDF scan.

## Revised execution sequence

### Stage 0 — regression pilot / workflow proof

Use an already-inspected section where both scan images and Gemini text are available.

Pilot: **scans 31–36** (`துணை நின்றாள் தோழி!`).

Goals:

- identify old-glyph / lexical errors in earlier repository transcription;
- restore scan-supported wording from Gemini + direct scan comparison;
- restore page-local ordering and meaningful structure from the scan;
- remove false headings/structure introduced by the previous transcription;
- reopen status to `needs-review` when the old `verified` claim is no longer defensible.

This pilot establishes the method before bulk use.

### Stage 1 — accelerated physical/text capture, scan 54 → 497

Continue the existing Pass 1 coverage gap, but use Gemini as the lexical scaffold.

For each scan:

1. inspect the physical scan once;
2. identify page type and visible printed page number from the scan only;
3. align the corresponding Gemini text to that physical page;
4. use Gemini wording as the starting transcription, preserving uncommon/old forms rather than silently normalizing them;
5. restore only **obvious** page-local structure visible in the scan: heading, basic line/paragraph break, illustration/blank separation;
6. if Gemini text appears displaced or a paragraph appears missing, flag it rather than inventing a repair during fast capture;
7. create/update the physical page record;
8. keep text pages at `needs-review`.

Recommended metadata:

```yaml
status: "needs-review"
visual_fidelity: "needs-review"
transcription_method: "Gemini lexical scaffold aligned to controlling source scan; textual/visual verification deferred"
```

The objective is complete **497-scan physical coverage**, not final verification.

### Stage 2 — lexical/textual reconciliation, scan 1 → 497

Perform a systematic word-level pass.

Check:

- every word against the scan;
- old Tamil glyphs / uncommon printed forms;
- omitted words and duplicated words;
- punctuation characters;
- quotation wording;
- source labels and names;
- Gemini/repository disagreements.

Use Gemini to draw attention to likely old-glyph misreads, but the scan decides every correction.

Do **not** perform layout beautification in this stage.

### Stage 3 — structural / visual-text reconstruction, scan 1 → 497

Use the scan, not Gemini, to establish:

- exact decorative headings and heading hierarchy;
- verse line breaks / stanza grouping;
- prose paragraph boundaries;
- dialogue blocks;
- punctuation placement where structure depends on it;
- centered/right-aligned continuation lines;
- ornamental separators;
- citation blocks and `பொருள் விளக்கம்` placement;
- running headers, printed page numbers and footers;
- illustration/text relationships.

Also repair Gemini failure modes such as lines moved to the previous/next block.

### Stage 4 — omission / continuity audit, scan 1 → 497

Audit physical sequence and cross-page continuity:

- every scan represented exactly once;
- no paragraph omitted because Gemini skipped it;
- no sentence duplicated because of batch overlap;
- continuations appear on the correct physical page;
- `continues_from_scan` / `continues_to_scan` recorded where useful;
- illustrations/blanks/covers/end matter preserved.

### Stage 5 — section structure audit

Confirm all decorative headings and section boundaries directly from scans. Gemini headings are hints only.

### Stage 6 — Sangam provenance audit

Verify quoted Sangam text, anthology/work name, poem number/range, poet attribution and `பொருள் விளக்கம்` directly from the printed source.

### Stage 7 — metadata / status audit

Normalize repository metadata only after the relevant gates have actually passed.

### Stage 8 — whole-volume synchronization / final audit

Synchronize indexes, section READMEs, work/root README, `HANDOVER.md`, continuation prompt, and final 497-scan completeness statement.

## Batch cadence

Normal working batch: **about 10 scans**.

Rules:

- a natural decorative section boundary may extend/shorten a batch;
- dense pages may be processed in smaller groups;
- bulk capture must not convert uncertainty into invented text;
- later verification remains page-by-page even if Gemini supplied a complete transcript.

## Status discipline

`verified` means the current archival text has passed the relevant direct scan gates. It is not permanent merely because an older workflow assigned it.

If a regression comparison reveals substantive lexical, ordering or structural errors:

1. fix source-supported errors;
2. record that the page was reopened;
3. set it to `needs-review` unless the designated verification gates are fully repeated;
4. promote again only during/after the systematic verification stages.

## Immediate execution order

1. Reconcile the demonstrated regression in scans **31–36** using Gemini for lexical recovery and the scan for structure.
2. Record the corrected exact heading and reopen affected statuses where appropriate.
3. Resume accelerated Stage 1 at **scan 54**, using the Gemini-assisted method, in ~10-scan iterations.
4. Do not restart completed physical coverage merely to satisfy the new method; systematic scans 1–497 reconciliation happens in Stages 2–4.
