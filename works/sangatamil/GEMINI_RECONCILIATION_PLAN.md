# சங்கத் தமிழ் — Gemini-assisted source reconciliation plan

This document refines the whole-volume workflow for `works/sangatamil/` after a complete Gemini transcription of the source was supplied as ten Markdown files.

Controlling source:

`TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

Canonical physical range: **scan 1–497**.

## Governing rule

> **Scan = final authority. Gemini = lexical aid. Repository = preservation layer.**

Gemini is materially useful for lexical recovery, especially old/uncommon Tamil glyph and word forms, but it is not a facsimile or structural authority.

Gemini may:

- miss/corrupt decorative headings;
- flatten or move punctuation;
- merge/split verse or prose incorrectly;
- move continuation lines;
- omit paragraphs;
- omit illustration/divider/blank pages;
- merge running headers/page numbers into body text;
- mis-order citation / `பொருள் விளக்கம்` blocks.

Neither Gemini nor an existing repository record may overrule the scan.

## Three-source decision rule

Where available compare:

1. **controlling scan** — wording + physical/visual organization authority;
2. **Gemini transcription** — lexical scaffold;
3. **existing repository page** — prior preservation layer.

When they differ, the scan decides. Do not choose a modern/familiar spelling merely because it looks natural. A prior `verified` page may be reopened when later source evidence shows substantive errors.

## Gemini pagination warning

The ten Gemini Markdown batches use internal comments such as:

`<!-- Page N of 497 -->`

These comments are navigation aids and generally refer to **printed book pages** in the supplied extraction, not physical PDF scan numbers. Gemini often omits illustration/divider pages from that marker sequence.

Therefore:

- never increment physical scan numbers from Gemini markers;
- never infer printed pages from scan arithmetic;
- align every page from the controlling PDF.

## Current relevant Gemini batch

At the refreshed handoff frontier, `File10.md` is the relevant lexical scaffold.

Its supplied header states:

- Book Pages **414–484**;
- corresponding physical PDF pages **426–497**.

This is useful navigation only. The scan still decides all physical page boundaries, illustrations/dividers, headings and printed pagination.

## Current source-work checkpoint — refreshed 2026-09-01

`2b3552a1f487e6ab747a394a8fe36f80f49f2cae` — `sangatamil: Pass 1 capture scan 425`

Physical records exist through **scan 425**.

Scan 425 is the decorative divider:

- `கைக்கிளை`
- `ஒருதலைக் காதல்`

Direct source inspection confirms scan **426 / printed page 414** begins numbered unit **1** with `கற்கண்டுத் தமிழில் கவிதைகள் வடிக்கும்...`.

Remaining physical Pass-1 range at the checkpoint: **426–497 (72 scans)**.

## Stage 0 — regression pilot

The scans 31–36 regression pilot established the method: Gemini can improve lexical recovery but source-visible structure/headings must come from the scan. The pilot is historical workflow proof and must not be restarted merely because this document is reread.

## Stage 1 / Pass 1 — accelerated physical/text capture

Active now.

Goal: one physical page record for every scan through 497.

For each scan:

1. inspect the physical scan once;
2. identify page type and visible printed page number from the scan;
3. align Gemini text to that physical page;
4. use Gemini as the lexical starting point;
5. preserve directly visible heading/basic lineation/paragraph grouping;
6. create separate illustration/divider/blank records;
7. correct a plainly visible Gemini error from the source when obvious;
8. if the issue requires prolonged forensic resolution, defer it rather than inventing text;
9. normally keep `needs-review` / `visual_fidelity: needs-review`;
10. commit and continue.

Recommended text metadata:

```yaml
status: "needs-review"
visual_fidelity: "needs-review"
transcription_method: "Gemini lexical scaffold aligned to controlling source scan; textual/visual verification deferred"
```

Normal batch: **about 10 physical scans**.

At batch end, compare base → head and verify that only intended page records changed.

## Stage 2 / Pass 2 — lexical/textual reconciliation, scan 1 → 497

Systematically verify:

- every word against scan;
- old/uncommon forms;
- omissions/duplications;
- punctuation;
- quotation wording;
- labels/names;
- Gemini/repository disagreements.

Do not turn this into a layout pass.

## Stage 3 / Pass 3 — structural / visual-text reconstruction, scan 1 → 497

Establish from scan:

- exact decorative headings/hierarchy;
- verse line breaks/stanzas;
- prose paragraph boundaries;
- dialogue blocks;
- alignment/indentation;
- separators;
- citation and `பொருள் விளக்கம்` placement;
- running headers/footers/printed page numbers;
- illustration/text relationships;
- displaced continuation lines.

## Stage 4 / Pass 4 — omission / continuity audit, scan 1 → 497

Audit:

- every physical scan represented once;
- no paragraph omitted by Gemini;
- no duplicate from extraction-batch overlap;
- continuations on correct page;
- illustration/divider/blank/cover/end matter preserved;
- continuation metadata where useful.

## Stage 5 / Pass 5 — section structure audit

Confirm decorative headings and canonical section boundaries directly from scans. Gemini headings are hints only.

## Stage 6 / Pass 6 — Sangam provenance audit

Verify quoted Sangam text, work/anthology, poem number/range, poet attribution, `பொருள் விளக்கம்` and printed source notes directly from this source.

## Stage 7 / Pass 7 — metadata / status audit

Normalize metadata only after the relevant source gates pass.

## Stage 8 / Pass 8 — whole-volume synchronization / final audit

Synchronize indexes, section READMEs, work/root README, handover, continuation prompt and final 497-scan completeness state.

## Immediate execution order

1. Fetch live `main` and preserve any source work newer than the checkpoint above.
2. Find the first missing physical scan.
3. If it is still **426**, continue Pass 1 with approximately **scans 426–435** using the controlling PDF + `File10.md` scaffold.
4. Verify the changed-file set after the batch.
5. Continue in ~10-scan Pass-1 batches until scan 497.
6. Do not start Pass 2 before physical coverage is complete.
