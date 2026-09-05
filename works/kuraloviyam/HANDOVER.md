# HANDOVER — குறளோவியம்

Repository: `pugazg/kalaignar-literary-commentary`

Branch: `main`

Active work: `works/kuraloviyam/`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve any newer durable Kuraloviyam state. Do not reopen completed Part 001 Tamil passes, first-pass English drafting, or completed English source-check because an older prompt or root handover records an earlier frontier.

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

The current user-directed normal iteration size is **15 consecutive physical scan pages**; a final Part remainder may be shorter.

## First-pass drafting — COMPLETE

All **111/111** English page records exist.

## Source-check — COMPLETE

All **111/111 physical scans** have been source-reviewed.

- SC1 / 1–15 — COMPLETE;
- SC2 / 16–30 — COMPLETE;
- SC3 / 31–45 — COMPLETE;
- SC4 / 46–60 — COMPLETE;
- SC5 / 61–75 — COMPLETE;
- SC6 / 76–90 — COMPLETE;
- SC7 / 91–105 — COMPLETE;
- SC8 / 106–111 — COMPLETE, final 6-page remainder.

SC8 recorded four fidelity-adjustment groups affecting five records:

- scan **107**: `சே` is now source-faithful **“Tch”**, replacing unsupported **“Hey”**;
- scan **108**: removed unsupported **“care”** from `உப்பிட்டு வளர்த்த பெற்றோர்` and retained the source's salt/feeding image;
- scans **109–110**: repaired the physical continuation across `காலையில் / மலரும் அவர் கண்கள்` and removed unsupported **“palm-leaf”** from `ஏடுகள்`;
- scan **111**: corrected the `ஏவலை ... விரைந்து கேட்கும்` sense in prose and Kural 648 to **“swiftly heeds the bidding”** rather than the weaker/incorrect listen/hear rendering.

Final source-check state:

- English page records: **111/111**;
- `source-checked`: **107**;
- `source-limited`: **4** — scans 13, 14, 15, 19; all four reviewed within available evidence;
- `draft`: **0**;
- editorial-reviewed: **0**;
- release-ready: **0**;
- unreadable source material reconstructed: **none**;
- external/standard Kural English imported: **none**.

## Current exact activity

Proceed with **Part 001 glossary / recurring-terminology reconciliation GR1 — scans 1–15**:

1. fetch live `main` first;
2. process exactly **15 consecutive scans** under the current cadence;
3. fetch the matching English and audited Tamil records as needed;
4. compare recurring names, controlled literary terms, publication/work names, chapter labels and repeated English renderings against `translations/en/GLOSSARY.md` and their Tamil context;
5. add or refine glossary entries only where Part 001 evidence supports them;
6. do not mechanically force one English equivalent where context requires a different rendering;
7. do not import standard Thirukkural terminology, web text, published translations, another commentator or memory;
8. this gate does **not** itself promote `source-checked` pages to `editorial-reviewed`; scans 13–15 remain `source-limited`;
9. record terminology corrections transparently in affected English pages and `GLOSSARY.md`;
10. update `TRANSLATION_STATUS.md`, work README/handover/current prompt, then audit the exact changed-file set before advancing to GR2.

Do not begin Part 002 until Part 001 English/final closure is complete and Part 002 source is supplied.