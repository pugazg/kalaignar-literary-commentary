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

The English layer is explicitly a **project-created translation**, not an official/publisher edition.

Every English page declares `translation_type: "project_translation"`.

Permanent cadence:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

Translate only from audited Tamil records. Do not import standard Kural wording, published English translations, web text, another commentator or memory.

## First-pass completed batches

- **Batch 1 — scans 1–8 — COMPLETE**.
- **Batch 2 — scans 9–17 — COMPLETE**; scans 13–15 are `source-limited`.
- **Batch 3 — scans 18–27 — COMPLETE**; scan 19 is `source-limited` and preserves the audited washed-out gap.
- **Batch 4 — scans 28–37 — COMPLETE**.

Batch 4 content:

- scan 28 — Editor Saavi;
- scan 29 — Dr. Me. Sundaram;
- scan 30 — Dr. Ma. Nannan;
- scan 31 — Kalaignar's Response;
- scan 32 — `கலைஞரின் குறளோவியம்` section-title leaf;
- scan 33 — intentional blank source-side page / printed page 16;
- scans 34–37 — first four pages of the main `கலைஞரின் குறளோவியம்` sequence.

The physical continuations 34→35 and 37→38 are preserved. No source-check or editorial-review promotion has been claimed.

Current English totals:

- page records: **37/111**;
- `draft`: **33**;
- `source-limited`: **4** — scans 13–15, 19;
- source-checked: **0**;
- editorial-reviewed: **0**;
- release-ready: **0**.

## Current exact activity

Proceed with **Part 001 English Batch 5 — scans 38–47**:

1. fetch live `main` first;
2. fetch audited Tamil records for scans 38–47;
3. mirror filenames under `translations/en/pages/`;
4. translate only repository-supported Tamil wording;
5. keep ordinary verified-source English records at `draft`;
6. preserve headings, paragraphs, quotations, Kural/verse blocks, visual/source-page functions and physical continuations;
7. do not import standard Kural English wording or any external translation;
8. update `TRANSLATION_STATUS.md`, README/handover/current prompt after the batch;
9. compare the pre-batch base SHA to the new head and confirm only intended files changed;
10. record the exact next frontier before advancing to scan 48.

Do not begin source-check while Part 001 first-pass drafting remains incomplete unless a newer live workflow explicitly changes this cadence.

## Part 002

Part 002 / scans **112–222** is not started and its source is not supplied. Do not begin it until Part 001 English/final closure is complete.
