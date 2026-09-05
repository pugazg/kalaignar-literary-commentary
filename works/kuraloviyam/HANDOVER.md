# HANDOVER — குறளோவியம்

Repository: `pugazg/kalaignar-literary-commentary`

Branch: `main`

Active work: `works/kuraloviyam/`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve any newer durable Kuraloviyam state. Do not reopen completed Part 001 Tamil passes, first-pass English drafting, or completed English source-check batches because an older prompt or root handover records an earlier frontier.

For Kuraloviyam, this work-specific handover, `translations/en/TRANSLATION_STATUS.md`, and `NEXT_CHAT_PROMPT_KURALOVIYAM.md` carry the current frontier.

## Mandatory startup

Read completely before Kuraloviyam changes:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. `NEXT_CHAT_PROMPT_KURALOVIYAM.md`
5. this `works/kuraloviyam/HANDOVER.md`
6. `works/kuraloviyam/README.md`
7. `works/kuraloviyam/PART_001_AUDIT.md`
8. `works/kuraloviyam/PART_001_FINAL_STATUS_SYNC.md`
9. `works/kuraloviyam/metadata/source.md`
10. `works/kuraloviyam/metadata/transcription-policy.md`
11. `works/kuraloviyam/indexes/page-map.md`
12. `works/kuraloviyam/translations/en/README.md`
13. `works/kuraloviyam/translations/en/TRANSLATION_GUIDE.md`
14. `works/kuraloviyam/translations/en/GLOSSARY.md`
15. `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`

## Source family / per-part rule

- source ID: `TVA_BOK_0065733`;
- complete extent reported by user: **666 physical pages**;
- split ranges: 1–111, 112–222, 223–333, 334–444, 445–555, 556–666;
- repository `scan_page` never restarts per split.

Finish each supplied Part completely before beginning the next:

source intake → Pass 1 → Pass 2A → Pass 2B → Pass 3 → Part audit → final metadata/status sync → documentation sync → Tamil archival-ready → English translation/review closure → final Part checkpoint → next supplied Part.

## Part 001 Tamil — CLOSED

Part 001 scans **1–111** are Tamil archival-ready. Source intake and Passes 1/2A/2B/3 are complete; audit and final status sync are PASS. Tamil statuses are **107 `verified` + 4 `partial`**; partial scans are **13, 14, 15, 19**; visual fidelity is **111/111 `verified`**.

Do not reconstruct the unreadable handwritten bodies on scans 13–15 or the washed-out/faint printed region on scan 19. Normal English review uses the audited Tamil repository records; do not routinely reopen the Part 001 PDF.

The 111→112 boundary check remains deferred until Part 002 is supplied.

# Part 001 English project translation

The English layer is a **project-created translation**, not an official/publisher edition. Every English page declares `translation_type: "project_translation"`.

Permanent review cadence:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

Review only from audited Tamil records. Do not import standard Kural wording, published English translations, web text, another commentator or memory.

The current user-directed normal iteration size is **15 consecutive physical scan pages**.

## First-pass drafting — COMPLETE

All **111/111** English page records exist. The permanent source-limited English pages are scans **13, 14, 15, 19** unless better Tamil source evidence is supplied later.

## Source-check progress

### SC1 — scans 1–15 — COMPLETE

- scans **1–12**: PASS and `source-checked`;
- scans **13–15**: PASS within securely established source limits and remain `source-limited`.

### SC2 — scans 16–30 — COMPLETE

- scans **16–18, 20–30**: PASS and `source-checked`;
- scan **19**: PASS within source limits and remains `source-limited`;
- corrected `மிகப் பலர் அல்லர்` to **“not very many”** from the earlier meaning-reversing **“not very few.”**

### SC3 — scans 31–45 — COMPLETE

- all fifteen pages PASS and are `source-checked`;
- six fidelity adjustments affected seven records; full detail is retained in `translations/en/TRANSLATION_STATUS.md`.

### SC4 — scans 46–60 — COMPLETE

- all fifteen Tamil↔English page pairs reviewed and PASS;
- scans **46–60** promoted to `source-checked`;
- three fidelity adjustments:
  - scan **47**: unsupported **“Fool!”** removed for Tamil `அடே!`; now neutral **“Why!”**;
  - scan **53**: unsupported **“temple”** removed from `கூட கோபுரம்`; now **“lofty towers rising to touch the clouds”**;
  - scan **55**: `மெய்மறந்து` refined from **“lost in himself”** to **“forgetting himself”**;
- no external/standard Kural English imported.

Current English totals:

- page records: **111/111**;
- source-check coverage: **60/111**;
- `source-checked`: **56**;
- `draft`: **51**;
- `source-limited`: **4** — scans 13–15, 19; all four have been reviewed within available evidence;
- editorial-reviewed: **0**;
- release-ready: **0**.

## Current exact activity

Proceed with **Part 001 English source-check SC5 — scans 61–75**:

1. fetch live `main` first;
2. fetch audited Tamil and matching English records for scans **61–75**;
3. process exactly **15 consecutive scans**;
4. compare paragraph-by-paragraph / block-by-block for omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual/page function and physical continuations;
5. promote each record from `draft` to `source-checked` only after it passes;
6. do not import standard Kural English wording or any external translation;
7. record source-check corrections transparently in affected English records and `TRANSLATION_STATUS.md`;
8. update README/handover/current prompt after SC5;
9. compare the pre-batch base SHA to the new head and confirm only intended files changed before advancing to scan 76.

Do not begin glossary reconciliation or editorial review until Part 001 source-check is complete.

## Part 002

Part 002 / scans **112–222** is not started and its source is not supplied. Do not begin it until Part 001 English/final closure is complete.
