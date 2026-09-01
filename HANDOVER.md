# HANDOVER — Kalaignar Literary Commentary Archive

Last refreshed for the active Sangath Tamil work: **2026-09-01**.

## Repository

`pugazg/kalaignar-literary-commentary`

Branch: `main`

Current active work: `works/sangatamil/`

Completed benchmark retained: `works/thirukkural/`

## Live-main rule

**Fetch live `main` first and treat it as authoritative.**

The last completed **source-work** checkpoint before this documentation refresh was:

`2b3552a1f487e6ab747a394a8fe36f80f49f2cae` — `sangatamil: Pass 1 capture scan 425`

Documentation-only commits may follow that checkpoint. If live `main` has advanced, preserve the newer durable state. Do not reset, overwrite, repeat, or reopen later completed work merely because this handover records an older checkpoint.

## Mandatory startup — active சங்கத் தமிழ் work

Before making any repository change, read completely:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`
5. `works/sangatamil/README.md`
6. `works/sangatamil/MULTI_PASS_WORKFLOW.md`
7. `works/sangatamil/GEMINI_RECONCILIATION_PLAN.md`
8. `works/sangatamil/metadata/source.md`
9. `works/sangatamil/metadata/transcription-policy.md`
10. `works/sangatamil/indexes/page-map.md`
11. `works/sangatamil/indexes/section-register.md`
12. `works/sangatamil/indexes/source-citation-register.md`

Then fetch the current page frontier from live `main` and inspect the actual controlling scan before writing.

Some README/index snapshots are intentionally not synchronized after every Pass-1 page. **The live page files and live branch history control the frontier.**

# Permanent source / fidelity rule

> **Scan = final authority. Gemini = lexical aid. Repository = preservation layer.**

Never silently modernize, normalize, correct from another edition, replace quotations, alter printed anthology/poem/poet labels, reconstruct unclear source, invent pagination, or infer missing source content.

A first-pass record is not `verified`. Newly captured Pass-1 pages normally remain:

```yaml
status: "needs-review"
visual_fidelity: "needs-review"
```

# Active source — சங்கத் தமிழ்

- source: `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`
- author: **கலைஞர் மு. கருணாநிதி**
- physical PDF extent: **497 scans**
- scan **497**: back cover
- canonical physical range: **1–497**
- never create scan 498+
- printed pagination must be read from the scan, never inferred from scan arithmetic

The earlier 150-page figure was a preview-service limitation and is retired.

## Fresh-chat source requirement

For page-level work in a new chat, attach or otherwise resolve the controlling PDF again before source-dependent verification/transcription.

A complete Gemini transcription was supplied in ten Markdown files. For the current remaining range, **`File10.md` is the relevant lexical scaffold**: its supplied header describes Book Pages **414–484** corresponding to physical PDF pages **426–497**. Gemini page comments are navigation aids only; illustration/divider pages may be skipped or flattened, so the PDF scan remains the physical-page authority.

If `File10.md` is unavailable in the fresh chat, do not invent from memory. Either attach it or continue source-first from the PDF without Gemini assistance.

# Canonical workflow

The active execution plan is `works/sangatamil/MULTI_PASS_WORKFLOW.md` with the Gemini refinements in `works/sangatamil/GEMINI_RECONCILIATION_PLAN.md`.

Pass order:

1. **Pass 1 — transcription / physical capture through scan 497**;
2. **Pass 2 — textual verification, scan 1 → 497**;
3. **Pass 3 — visual-text fidelity verification, scan 1 → 497**;
4. **Pass 4 — physical-page / omission / continuity audit, scan 1 → 497**;
5. **Pass 5 — section-structure audit, scan 1 → 497**;
6. **Pass 6 — Sangam source / provenance audit, scan 1 → 497**;
7. **Pass 7 — metadata / status consistency audit, scan 1 → 497**;
8. **Pass 8 — whole-volume synchronization and final audit**.

**Only Pass 1 is active now. Do not start Pass 2 before scan 497 has a physical record.**

# Pass 1 operating discipline

Normal batch: **about 10 physical scans**, adjusted only for a nearby natural section boundary or unusually dense pages.

For each physical scan:

- inspect the scan once;
- identify page type and visible printed page number from the scan;
- align Gemini only as a lexical scaffold where available;
- preserve directly visible headings, basic lineation/paragraphs and source blocks;
- create illustration/divider/blank records rather than skipping them;
- leave unresolved readings for later passes rather than doing prolonged forensic work;
- normally keep `status: needs-review` and `visual_fidelity: needs-review`;
- commit and continue.

Important learned alignment rule: Gemini markers such as `<!-- Page N of 497 -->` usually refer to the **printed book page** in these supplied batches, not the physical scan number. They must never drive physical sequencing. The physical scan does.

At the end of each batch, compare the batch base to live head and confirm that only the intended page files were added/changed.

# Current physical boundary

Physical page records now exist through **scan 425**.

Remaining Pass-1 physical scans: **426–497 (72 scans)**.

Recent durable sequence:

- scans **406–408** — `மணித்தேரில் சென்ற மகன்!`;
- scans **409–412** — `ஆயமகன் குழலூதினான்!`;
- scans **413–416** — `சொல்வேன் கேளடி தோழி!`;
- scans **417–420** — `இருவிழி மழையும் இதய மகிழ்வும்!`;
- scans **421–424** — `இன்ப விளக்கேற்ற எப்போது வருவாரோ?`;
- scan **425** — full-page decorative divider introducing **`கைக்கிளை / ஒருதலைக் காதல்`**, no printed page number.

Scan 425 is preserved at:

`works/sangatamil/pages/0425-kaikkilai-oruthalaik-kaadhal-divider.md`

# Exact next activity

**Resume Pass 1 at physical scan 426.**

Direct source inspection shows:

- physical scan **426**;
- printed page **414**;
- under the `கைக்கிளை / ஒருதலைக் காதல்` division;
- numbered unit **1** begins with `கற்கண்டுத் தமிழில் கவிதைகள் வடிக்கும்...`.

Process approximately **scans 426–435** as the next Pass-1 batch, adjusting only if a nearby natural source boundary makes a slightly shorter/longer batch cleaner. Use the controlling scan for physical boundaries/headings and `File10.md` only as lexical scaffold.

Do not update broad indexes or start later passes during this routine batch.

# Completed Thirukkural baseline — DO NOT RESTART

`works/thirukkural/` remains complete:

- Tamil Parts **001–015** archival-ready through scan **323**;
- commentary through printed page **270 / Kural 1330**;
- English project translation Parts **001–015** released;
- semantic provenance complete for **3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள்**;
- final structure audit PASS.
