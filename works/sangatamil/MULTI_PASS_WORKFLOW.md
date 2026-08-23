# சங்கத் தமிழ் — Full-volume multi-pass workflow

This document is the canonical execution plan for `works/sangatamil/`.

It supersedes the earlier mixed page-by-page cadence in which transcription, textual verification, visual-fidelity verification, provenance review, section mapping and status synchronization were often performed together.

## Governing principle

> **One activity at a time across the whole 497-scan source.**

The controlling source remains `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`.

Canonical source range: **scan 1 through scan 497**. Scan 497 is the back cover. No scan 498+ record may be invented.

The source-first fidelity rules remain unchanged: never silently normalize, modernize, reconstruct, correct from another edition, infer printed pagination, or replace source-visible Sangam wording/provenance.

## Current state at workflow adoption

- physical page records exist through **scan 53**;
- scans through **50** include earlier work with mixed levels of verification;
- scan **51** is a transcription-only record with `needs-review`;
- scan **52** is an illustration record with `needs-review`;
- scan **53 / printed 38** is a fast transcription-only record with `needs-review`;
- **Pass 1 resumes at scan 54**;
- existing `verified` pages are not downgraded, but they remain eligible for the later systematic full-volume passes so the final audit is uniform from scan 1 to scan 497.

# Pass 1 — transcription / physical capture only

## Goal

Create a physical Markdown record for **every scan through 497** before beginning any new whole-volume verification activity.

Current execution range: **scan 54 → scan 497**.

## Per-page procedure

For each scan:

1. inspect the page once;
2. create the physical Markdown record;
3. transcribe visible literary/editorial text;
4. preserve obvious printed line breaks, paragraph breaks and directly visible headings;
5. for illustration, blank, cover or other non-text pages, create a concise factual physical-page record;
6. record a printed page number only when it is actually visible;
7. mark uncertain readings for later review instead of spending extended time resolving them;
8. commit the page record and proceed to the next scan.

## Pass-1 status

New Pass-1 captures should normally use:

```yaml
status: "needs-review"
visual_fidelity: "needs-review"
transcription_method: "fast direct transcription from source scan; verification intentionally deferred"
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

# Pass 2 — textual verification, scan 1 → 497

Perform only source-text verification:

- characters and words;
- spelling exactly as printed;
- punctuation;
- omissions and duplications;
- quotation wording;
- line content and order;
- printed labels and text content.

Correct the Markdown directly from the controlling scan. Do not turn this pass into a layout or structural audit.

Previously `verified` pages are still included in the systematic scan-1→497 sweep unless an explicit later policy records a justified exemption.

# Pass 3 — visual-text fidelity verification, scan 1 → 497

Perform only meaningful visual/text-organization review:

- headings and hierarchy;
- verse lineation;
- stanza and paragraph grouping;
- indentation;
- centered/right-aligned text;
- quote/gloss/citation blocks;
- separators and rules;
- ornaments where structurally meaningful;
- running headers, footers and printed page numbers;
- illustration/text relationship.

Exact facsimile typography is not required. Semantic visual fidelity is required.

# Pass 4 — physical-page and continuity audit, scan 1 → 497

Audit the book as a physical sequence:

- every scan represented exactly once;
- no missing or duplicate physical records;
- covers, blanks, title pages, front matter, illustrations and end matter represented;
- printed pagination read only from source;
- `continues_from_scan` / `continues_to_scan` relationships;
- sentence/paragraph/poem continuation across physical pages;
- scan anomalies, crop or damage notes.

# Pass 5 — section-structure audit, scan 1 → 497

Establish the canonical thematic structure only in this pass:

- exact decorative headings;
- section starts;
- section ends;
- page ranges;
- illustration placement;
- section navigation records / READMEs;
- boundary confidence.

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

The purpose of this separation is to keep each iteration fast, measurable and auditable while preserving eventual archival quality.

## Exact next activity

**Pass 1 only — capture scan 54, then continue sequentially toward scan 497.**

No verification or broad documentation synchronization should be mixed into routine page capture during this pass.