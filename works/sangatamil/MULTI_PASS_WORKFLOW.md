# சங்கத் தமிழ் — Full-volume multi-pass workflow

This document is the canonical execution plan for `works/sangatamil/`.

It supersedes the earlier mixed page-by-page cadence in which transcription, textual verification, visual-fidelity verification, provenance review, section mapping and status synchronization were performed together.

Gemini-assisted rules are defined in [`GEMINI_RECONCILIATION_PLAN.md`](GEMINI_RECONCILIATION_PLAN.md).

## Governing principle

> **One activity at a time across the whole 497-scan source.**

Controlling source: `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

Canonical physical range: **scan 1 through scan 497**. Scan 497 is the back cover. Never create scan 498+.

Source-first fidelity is permanent: never silently normalize, modernize, reconstruct, correct from another edition, infer printed pagination, or replace source-visible Sangam wording/provenance.

## Gemini lexical-scaffold rule

A complete Gemini transcription was supplied in ten Markdown batches. Gemini is useful for lexical recovery, especially old/uncommon Tamil forms, but is not a structural or physical-page authority.

Do not trust Gemini alone for:

- decorative headings;
- punctuation;
- paragraph/verse grouping;
- physical page boundaries;
- sentence order across page transitions;
- illustration/divider/blank placement;
- provenance / `பொருள் விளக்கம்` layout.

Decision order:

> **controlling scan → archival decision; Gemini → lexical scaffold; existing repository → prior preservation layer.**

Gemini comments such as `<!-- Page N of 497 -->` generally track printed book pages in the supplied batches, not physical scan numbers. Illustration/divider pages may be absent from the Gemini sequence.

At the current frontier, `File10.md` is the relevant scaffold; its supplied header covers Book Pages **414–484** corresponding to physical PDF pages **426–497**. This is navigation help only; the scan still establishes every physical boundary.

## Current durable state — refreshed 2026-09-01

Last completed source-work checkpoint before documentation refresh:

`2b3552a1f487e6ab747a394a8fe36f80f49f2cae` — `sangatamil: Pass 1 capture scan 425`

Physical page records exist through **scan 425**.

Remaining Pass-1 physical range: **426–497 (72 scans)**.

Scan 425 is a decorative divider introducing **`கைக்கிளை / ஒருதலைக் காதல்`**.

Direct source inspection confirms scan **426 / printed page 414** begins numbered unit **1** with `கற்கண்டுத் தமிழில் கவிதைகள் வடிக்கும்...`.

Fetch live `main` before every continuation; if the frontier has advanced, preserve the newer state.

# Pass 1 — Gemini-assisted transcription / physical capture

## Goal

Create a physical Markdown record for every scan through **497** before beginning any later whole-volume verification pass.

## Per-page procedure

For each physical scan:

1. inspect the physical page once;
2. identify page type and visible printed page number from the scan only;
3. align corresponding Gemini text where available;
4. use Gemini wording as the lexical starting point, especially for old/uncommon Tamil forms;
5. preserve directly visible decorative headings and obvious line/paragraph grouping;
6. preserve source-visible quotation/provenance/gloss blocks;
7. create factual records for illustration/divider/blank/cover pages rather than skipping them;
8. when Gemini and source visibly disagree, source wins;
9. if resolution would require prolonged forensic work, leave it for a later pass rather than inventing certainty;
10. commit and proceed.

## Pass-1 status

New text-page captures normally use:

```yaml
status: "needs-review"
visual_fidelity: "needs-review"
transcription_method: "Gemini lexical scaffold aligned to controlling source scan; textual/visual verification deferred"
```

For a non-text or decorative page, use an appropriate direct visual-capture description.

`partial` or `blocked` may be used when the source itself prevents usable first-pass capture.

## Explicitly deferred during Pass 1

Do not routinely perform:

- a second full character-by-character comparison;
- final textual verification;
- final visual-fidelity verification;
- extended crop/zoom forensic work;
- provenance verification;
- external-edition comparison;
- formal section-end investigation;
- whole-book continuity audit;
- metadata/status normalization;
- per-page updates to page-map, section-register, source-citation-register, section READMEs, work README, root README, HANDOVER or next-chat prompt.

A plainly visible source correction during Pass 1 is allowed; it does not make the page `verified`.

## Batch cadence

Default working batch: **about 10 physical scans**, adjusted only to a nearby natural source boundary or reduced for unusually dense pages.

At batch end:

1. compare the starting commit to live head;
2. confirm the intended scan files are the only changed source records;
3. fetch live `main` again;
4. record the next missing physical scan.

## Pass-1 completion condition

Pass 1 is complete only when every physical scan **1–497** has one archival record.

Do not start Pass 2 early.

# Pass 2 — lexical / textual reconciliation, scan 1 → 497

Check only source text:

- characters and words;
- old/uncommon printed forms;
- spelling exactly as printed;
- punctuation;
- omissions/duplications;
- quotation wording;
- line content/order;
- printed labels and names;
- Gemini/repository disagreements.

The controlling scan decides every correction.

# Pass 3 — structural / visual-text fidelity verification, scan 1 → 497

Use the scan to establish meaningful visual organization:

- exact headings/hierarchy;
- verse lineation and stanza grouping;
- prose paragraphs and dialogue blocks;
- indentation/alignment;
- citation and `பொருள் விளக்கம்` blocks;
- separators/rules;
- running headers, footers and printed page numbers;
- illustration/text relationships;
- displaced continuation lines.

Exact facsimile typography is not required; meaningful structural fidelity is.

# Pass 4 — physical-page / omission / continuity audit, scan 1 → 497

Audit:

- every scan represented exactly once;
- no missing/duplicate physical records;
- no Gemini omission or extraction-batch duplication;
- covers, blanks, dividers, illustrations and end matter preserved;
- printed pagination sourced only from scan;
- continuation relationships and cross-page sentence/poem flow;
- scan anomalies/crop/damage notes.

# Pass 5 — section-structure audit, scan 1 → 497

Establish canonical thematic structure:

- exact decorative headings;
- section starts/ends;
- page ranges;
- illustration placement;
- section navigation records/READMEs;
- boundary confidence.

Repository sequence numbers remain navigation identifiers, not printed chapter numbers.

# Pass 6 — Sangam source / provenance audit, scan 1 → 497

Verify printed source material:

- anthology/work name;
- poem number/range;
- poet attribution;
- quoted Sangam text;
- `பொருள் விளக்கம்`;
- other printed source notes.

Preserve what this edition prints. External comparison must be separately labelled.

Finalize `indexes/source-citation-register.md` in this pass.

# Pass 7 — metadata / status consistency audit, scan 1 → 497

Check every record for consistent:

- `scan_page`;
- `printed_page`;
- `work`;
- `section`;
- `page_type`;
- `status`;
- `visual_fidelity`;
- continuation fields;
- `transcription_method`;
- source filename;
- filename/path consistency.

Promote statuses only after relevant gates pass.

# Pass 8 — whole-volume synchronization and final audit

Synchronize only after Passes 1–7:

- `indexes/page-map.md`;
- `indexes/section-register.md`;
- `indexes/source-citation-register.md`;
- section READMEs;
- `works/sangatamil/README.md`;
- root `README.md`;
- root `HANDOVER.md`;
- `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`;
- final 497-scan completeness/readiness state.

# Exact next activity

Fetch live `main` and find the first missing physical record.

At this handoff checkpoint it is **scan 426**. If still missing, process approximately **scans 426–435** as the next Pass-1 batch using the controlling PDF + `File10.md` lexical scaffold, then verify the changed-file set.
