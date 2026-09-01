# சங்கத் தமிழ் — Full-volume multi-pass workflow

This document is the canonical execution plan for `works/sangatamil/`.

It supersedes the earlier mixed page-by-page cadence in which transcription, textual verification, visual-fidelity verification, provenance review, section mapping and status synchronization were often performed together.

The Gemini-assisted reconciliation rules are defined in [`GEMINI_RECONCILIATION_PLAN.md`](GEMINI_RECONCILIATION_PLAN.md) and are part of this workflow.

## Governing principle

> **One activity at a time across the whole 497-scan source.**

The controlling source remains `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`.

Canonical source range: **scan 1 through scan 497**. Scan 497 is the back cover. No scan 498+ record may be invented.

The source-first fidelity rules remain unchanged: never silently normalize, modernize, reconstruct, correct from another edition, infer printed pagination, or replace source-visible Sangam wording/provenance.

## Gemini lexical scaffold rule

A complete Gemini transcription has now been supplied in ten Markdown batches. It is useful because it captures many old / uncommon Tamil glyph and word forms better than the earlier manual transcription.

Gemini is **not** a structural or final textual authority. In particular, do not trust it by itself for:

- decorative headings;
- punctuation;
- paragraph / verse grouping;
- physical page boundaries;
- sentence order across page transitions;
- illustration / blank-page placement;
- provenance / `பொருள் விளக்கம்` layout.

Decision order:

> **controlling scan → archival decision; Gemini → lexical scaffold; existing repository → prior preservation layer.**

A previous `verified` page may be reopened when new evidence exposes substantive errors.

## Current state at workflow revision

- physical page records exist through **scan 53**;
- earlier pages contain mixed levels of verification;
- a regression comparison of scans 31–36 exposed substantive lexical/structural errors in pages previously marked `verified`;
- those demonstrated regressions are being reconciled under the Gemini-assisted plan;
- **Pass 1 resumes at scan 54** after the regression pilot;
- existing verified pages are not automatically downgraded merely because Gemini exists, but all pages remain eligible for the later systematic scan-1→497 verification passes.

# Stage 0 — regression pilot

Reconcile **scans 31–36** using Gemini for lexical recovery and the controlling scan for page-local structure.

This is a targeted workflow proof, not a replacement for the later whole-volume passes.

Where substantive errors invalidate an older `verified` claim, correct the source-supported text and reopen the page to `needs-review` unless the full designated gates are repeated.

# Pass 1 — Gemini-assisted transcription / physical capture only

## Goal

Create a physical Markdown record for **every scan through 497** before beginning any new whole-volume verification activity.

Current execution range: **scan 54 → scan 497**.

## Per-page procedure

For each scan:

1. inspect the physical page once;
2. identify page type and visible printed page number from the scan only;
3. align the corresponding Gemini transcription to the physical page;
4. use Gemini wording as the lexical starting point, especially for old/uncommon printed Tamil forms;
5. preserve obvious source-visible line breaks, paragraph breaks and directly visible headings;
6. for illustration, blank, cover or other non-text pages, create a concise factual physical-page record;
7. if Gemini appears to omit/move text or the alignment is uncertain, flag it for later review rather than inventing a repair;
8. commit the page record and proceed to the next scan.

## Pass-1 status

New text-page captures should normally use:

```yaml
status: "needs-review"
visual_fidelity: "needs-review"
transcription_method: "Gemini lexical scaffold aligned to controlling source scan; textual/visual verification deferred"
```

For a non-text page, `transcription_method` may instead say `single-pass visual capture; verification intentionally deferred`.

`partial` or `blocked` may be used when the source itself prevents a usable first-pass capture.

## Explicitly deferred during Pass 1

Do **not** perform the following as part of routine Pass-1 page capture:

- second character-by-character comparison;
- textual verification gate;
- visual-fidelity verification gate;
- forensic crop/zoom work unless text is literally unreadable for basic capture;
- provenance verification;
- external-edition comparison;
- section-end investigation beyond an immediately visible decorative heading;
- full continuity audit;
- metadata/status consistency audit;
- routine updates to `page-map.md`, `section-register.md`, `source-citation-register.md`, section READMEs, work README, root README, HANDOVER or next-chat prompt after every page.

Structural metadata recorded during Pass 1 is provisional until the dedicated structure/metadata passes.

## Pass-1 completion condition

Pass 1 is complete only when **every physical scan 1–497 has a Markdown record**. Existing earlier records count toward coverage; the active creation gap begins after scan 53.

# Pass 2 — lexical / textual reconciliation, scan 1 → 497

Perform only source-text verification:

- characters and words;
- old Tamil glyph / uncommon printed word forms;
- spelling exactly as printed;
- punctuation;
- omissions and duplications;
- quotation wording;
- line content and order;
- printed labels and names;
- Gemini/repository disagreements.

Gemini is a comparison aid; the controlling scan decides every correction.

Do not turn this pass into a layout audit.

Previously `verified` pages are included in the systematic scan-1→497 sweep unless an explicit later policy records a justified exemption.

# Pass 3 — structural / visual-text fidelity verification, scan 1 → 497

Use the scan—not Gemini—to establish meaningful visual organization:

- exact headings and hierarchy;
- verse lineation;
- stanza and paragraph grouping;
- dialogue blocks;
- indentation;
- centered/right-aligned text;
- quote/gloss/citation blocks;
- separators and rules;
- ornaments where structurally meaningful;
- running headers, footers and printed page numbers;
- illustration/text relationship;
- correction of text blocks or continuation lines that Gemini moved upward/downward.

Exact facsimile typography is not required. Semantic visual fidelity is required.

# Pass 4 — physical-page / omission / continuity audit, scan 1 → 497

Audit the book as a physical sequence:

- every scan represented exactly once;
- no missing or duplicate physical page records;
- no paragraph omitted by Gemini alignment;
- no duplicated text from extraction-batch overlap;
- covers, blanks, title pages, front matter, illustrations and end matter represented;
- printed pagination read only from source;
- `continues_from_scan` / `continues_to_scan` relationships;
- sentence/paragraph/poem continuation across physical pages;
- scan anomalies, crop or damage notes.

# Pass 5 — section-structure audit, scan 1 → 497

Establish the canonical thematic structure only in this pass:

- exact decorative headings from the scan;
- section starts;
- section ends;
- page ranges;
- illustration placement;
- section navigation records / READMEs;
- boundary confidence.

Gemini headings are hints only.

Repository sequence numbers remain navigation identifiers, not printed chapter numbers.

# Pass 6 — Sangam source / provenance audit, scan 1 → 497

Review printed Sangam-source material as a separate whole-volume activity:

- anthology/work name;
- poem number or range;
- poet attribution;
- quoted Sangam text;
- `பொருள் விளக்கம்`;
- other printed source notes.

Preserve what this book prints. External editions may be compared only in a separate explicitly labelled layer and must never silently overwrite the archival source record.

Finalize `indexes/source-citation-register.md` during this pass.

# Pass 7 — metadata / status consistency audit, scan 1 → 497

Check every physical page record for consistent metadata:

- `scan_page`;
- `printed_page`;
- `work`;
- `section`;
- `page_type`;
- `status`;
- `visual_fidelity` where applicable;
- continuation fields;
- `transcription_method`;
- source filename;
- filename/path consistency.

Promote statuses only when the relevant earlier gates have actually passed.

# Pass 8 — whole-volume synchronization and final audit

After Passes 1–7 are complete, synchronize and audit:

- `indexes/page-map.md`;
- `indexes/section-register.md`;
- `indexes/source-citation-register.md`;
- all section READMEs;
- `works/sangatamil/README.md`;
- repository root `README.md`;
- root `HANDOVER.md`;
- `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`;
- final 497-scan completeness and archival-readiness state.

# Execution discipline

During an active pass, do not opportunistically begin another pass because an issue is noticed. Record or leave the relevant item for its designated pass unless the source is so unreadable that the current activity cannot proceed safely.

The Stage-0 regression pilot is the explicit exception adopted to validate the new Gemini-assisted method before bulk capture resumes.

The purpose of this separation is to keep each iteration fast, measurable and auditable while preserving eventual archival quality.

## Batch cadence

Default: **about 10 scans per iteration**, adjusted to a nearby natural section boundary or reduced for unusually dense pages.

## Exact next activity

1. Finish the scans **31–36** Gemini-assisted regression pilot and reopen/correct any invalid legacy `verified` records.
2. Then resume **Pass 1 only at scan 54**, continuing sequentially toward scan 497 using the Gemini lexical scaffold + controlling scan alignment.
