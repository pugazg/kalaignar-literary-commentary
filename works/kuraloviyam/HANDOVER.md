# HANDOVER — குறளோவியம்

Repository: `pugazg/kalaignar-literary-commentary`

Branch: `main`

Active work: `works/kuraloviyam/`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve any newer durable Kuraloviyam state. Do not reopen completed Part 001 Tamil passes or repeat completed English batches because an older prompt or root handover records an earlier frontier.

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

Controlling split used: `TVA_BOK_0065733_குறளோவியம்_part_001_pages_1-111.pdf`.

- scans **1–111**;
- main body begins scan **18 / printed 1**;
- Part ends scan **111 / printed 94**;
- source intake / Pass 1 / Pass 2A / Pass 2B / Pass 3: complete;
- Part audit: **PASS**;
- final status sync: **PASS**;
- Tamil statuses: **107 `verified` + 4 `partial`**;
- partial scans: **13, 14, 15, 19**;
- visual fidelity: **111/111 `verified`**.

Do not reconstruct the unreadable handwritten bodies on scans 13–15 or the washed-out/faint printed region on scan 19. Normal Part 001 English work uses the audited Tamil repository records; do not routinely reopen the Part 001 PDF.

The 111→112 boundary check remains deferred until Part 002 is supplied.

# Part 001 English project translation

The English layer is explicitly a **project-created translation**, not an official/publisher edition. Every English page declares `translation_type: "project_translation"`.

Permanent review cadence:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

Translate only from audited Tamil records. Do not import standard Kural wording, published English translations, web text, another commentator or memory.

## Drafting batch rule

Beginning with **Batch 7**, the current user-directed drafting cadence is **15 consecutive physical scan pages per iteration**. Batches 5–6 remain historical 11-page batches. The final remainder of a Part may be shorter. Do not vary a normal batch to reach a literary boundary; preserve quotations, Kural blocks, narrative and physical continuations exactly as the audited Tamil records require.

## First-pass completed batches

- **Batch 1 — scans 1–8 — COMPLETE**.
- **Batch 2 — scans 9–17 — COMPLETE**; scans 13–15 are `source-limited`.
- **Batch 3 — scans 18–27 — COMPLETE**; scan 19 is `source-limited`.
- **Batch 4 — scans 28–37 — COMPLETE**.
- **Batch 5 — scans 38–48 — COMPLETE** — 11 pages.
- **Batch 6 — scans 49–59 — COMPLETE** — 11 pages.
- **Batch 7 — scans 60–74 — COMPLETE** — 15 pages.
- **Batch 8 — scans 75–89 — COMPLETE** — 15 pages.
- **Batch 9 — scans 90–104 — COMPLETE** — 15 pages; all new records are `draft`.

Batch 9 covers printed pages **73–87**: continuation of the love-sickness sequence; deceptive appearance and judgment by deeds; announcement-drum / eyes vignette; young poet and prospective bride; flower/eye separation and reunion; Urkkavalan's delayed tiger hunt; the two-night waiting / heart-led reunion narrative; and the opening of Villavan's battlefield-call episode. No external or standard English Kural wording was imported.

The physical continuation **104→105** remains intentionally open.

Current English totals:

- page records: **104/111**;
- `draft`: **100**;
- `source-limited`: **4** — scans 13–15, 19;
- source-checked: **0**;
- editorial-reviewed: **0**;
- release-ready: **0**.

## Current exact activity

Proceed with the **final Part 001 first-pass drafting Batch 10 — scans 105–111**:

1. fetch live `main` first;
2. fetch audited Tamil records for scans **105–111**;
3. process the final **7 consecutive scans**; this shorter batch is allowed because it is the Part remainder;
4. mirror filenames under `translations/en/pages/`;
5. translate only repository-supported Tamil wording;
6. keep ordinary verified-source English records at `draft`;
7. preserve headings, paragraphs, quotations, Kural/verse blocks, visual/source-page functions and the Part-ending structure;
8. preserve the source-supported **104→105** continuation without backfilling scan 104 from external knowledge;
9. do not import standard Kural English wording or any external translation;
10. update `TRANSLATION_STATUS.md`, README/handover/current prompt after the batch;
11. compare the pre-batch base SHA to the new head and confirm only intended files changed;
12. confirm **111/111 English page records** before beginning English source-check.

Do not begin source-check until the final drafting remainder is complete and audited.

## Part 002

Part 002 / scans **112–222** is not started and its source is not supplied. Do not begin it until Part 001 English/final closure is complete.
