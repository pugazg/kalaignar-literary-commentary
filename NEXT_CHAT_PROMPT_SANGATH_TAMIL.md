# Next Chat Prompt — சங்கத் தமிழ் archival project

Continue the **சங்கத் தமிழ் — Kalaignar source-first archival / provenance project** directly in:

`pugazg/kalaignar-literary-commentary`

Branch: `main`

Active path: `works/sangatamil/`

Controlling source:

`TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve the newest durable state.

The last completed **source-work checkpoint** when this prompt was refreshed was:

`2b3552a1f487e6ab747a394a8fe36f80f49f2cae` — `sangatamil: Pass 1 capture scan 425`

Later commits may be documentation-only or may advance the source frontier. Do **not** reset, overwrite, repeat, or reopen later completed work merely because this prompt records an older checkpoint.

## Mandatory startup

Before any repository change, read completely:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`
5. `works/sangatamil/README.md`
6. `works/sangatamil/MULTI_PASS_WORKFLOW.md`
7. `works/sangatamil/GEMINI_RECONCILIATION_PLAN.md`
8. `works/sangatamil/metadata/source.md`
9. `works/sangatamil/metadata/transcription-policy.md`
10. `works/sangatamil/indexes/page-map.md`
11. `works/sangatamil/indexes/section-register.md`
12. `works/sangatamil/indexes/source-citation-register.md`

Then determine the actual live frontier from `main`; broad README/index snapshots are not synchronized after every Pass-1 page and must not override live page files/history.

## Attach / resolve source files in the fresh chat

Before page-level source work, attach or otherwise resolve:

1. **Required:** `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf` — controlling source, 497 physical scans.
2. **Strongly useful for the current remainder:** `File10.md` — Gemini lexical scaffold. Its supplied header covers Book Pages 414–484 corresponding to physical PDF pages 426–497.

If `File10.md` is unavailable, continue source-first from the PDF rather than guessing Gemini text from memory.

## Source authority

> **Scan = final authority. Gemini = lexical aid. Repository = preservation layer.**

Never silently modernize, normalize, correct from another edition, replace quoted Sangam text, alter printed anthology/poem/poet labels, reconstruct hidden text, or infer pagination/source content.

Gemini comment markers such as `<!-- Page N of 497 -->` are navigation aids and in the supplied batches generally track **printed book pages**, not physical scan numbers. Gemini can also omit illustration/divider pages. Drive physical sequencing only from the controlling PDF.

## Source boundary

- physical source: **497 scans**;
- scan **497**: back cover;
- canonical range: **1–497**;
- never create scan 498+;
- printed page numbers must be read from the scan.

## Canonical workflow

Use `works/sangatamil/MULTI_PASS_WORKFLOW.md` and `works/sangatamil/GEMINI_RECONCILIATION_PLAN.md`.

Pass order:

1. Pass 1 — transcription / physical capture through scan 497;
2. Pass 2 — textual verification, scan 1 → 497;
3. Pass 3 — visual-text fidelity verification, scan 1 → 497;
4. Pass 4 — physical-page / omission / continuity audit, scan 1 → 497;
5. Pass 5 — section-structure audit, scan 1 → 497;
6. Pass 6 — Sangam source / provenance audit, scan 1 → 497;
7. Pass 7 — metadata / status consistency audit, scan 1 → 497;
8. Pass 8 — whole-volume synchronization and final audit.

**Only Pass 1 is active now. Do not begin Pass 2 until all 497 scans have physical records.**

## Pass-1 rules

Normal working batch: **about 10 physical scans**.

For each scan:

- inspect the physical scan once;
- identify page type and visible printed page number from the scan;
- align Gemini as lexical scaffold where available;
- preserve directly visible decorative headings, basic line/paragraph structure, quotations/provenance/gloss blocks;
- record illustration/divider/blank pages separately rather than skipping them;
- if Gemini omits, moves or corrupts source-visible material, source wins;
- avoid prolonged forensic verification during Pass 1; leave uncertainty for later passes;
- normally use `status: needs-review` and `visual_fidelity: needs-review`;
- commit each page record and continue.

At batch end, compare the starting commit to live head and verify that only the intended page records changed.

Do not routinely update broad indexes/READMEs/HANDOVER during the page batch.

## Current durable boundary

Physical records exist through **scan 425**.

Remaining Pass-1 source range at this checkpoint: **426–497 (72 scans)**.

Recent sequence:

- scans 406–408 — `மணித்தேரில் சென்ற மகன்!`;
- scans 409–412 — `ஆயமகன் குழலூதினான்!`;
- scans 413–416 — `சொல்வேன் கேளடி தோழி!`;
- scans 417–420 — `இருவிழி மழையும் இதய மகிழ்வும்!`;
- scans 421–424 — `இன்ப விளக்கேற்ற எப்போது வருவாரோ?`;
- scan 425 — decorative divider `கைக்கிளை / ஒருதலைக் காதல்`.

## Exact next activity

Fetch live `main` and confirm whether scan 426 is still the first missing record.

If so, continue **Pass 1 only from physical scan 426**, approximately through scan 435 for the next batch.

Direct inspection at handoff established that scan **426 / printed page 414** begins numbered unit **1** under `கைக்கிளை / ஒருதலைக் காதல்`, starting:

`கற்கண்டுத் தமிழில் கவிதைகள் வடிக்கும்...`

Use `File10.md` only as lexical scaffold and the PDF scan for every physical/structural decision.

Do the repository work directly; do not merely describe a plan.
