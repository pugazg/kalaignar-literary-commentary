# HANDOVER — குறளோவியம்

Repository: `pugazg/kalaignar-literary-commentary`

Branch: `main`

Active work: `works/kuraloviyam/`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve any newer durable Kuraloviyam state. Do not reopen completed Part 001 Tamil passes or repeat completed English batches because an older prompt or root handover contains an earlier frontier.

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

## Source family

- source ID: `TVA_BOK_0065733`;
- work: **குறளோவியம்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- complete extent reported by user: **666 physical PDF pages**;
- split plan: six parts × 111 pages;
- Part ranges: 1–111, 112–222, 223–333, 334–444, 445–555, 556–666;
- repository `scan_page` never restarts per split.

## Mandatory per-part closure rule

Finish one supplied Part completely before beginning the next:

source intake → Pass 1 → Pass 2A → Pass 2B → Pass 3 → Part audit → final metadata/status sync → documentation sync → Tamil archival-ready → English translation/review closure → final Part checkpoint → next supplied Part.

## Part 001 Tamil source-dependent work — CLOSED

Controlling split used:

`TVA_BOK_0065733_குறளோவியம்_part_001_pages_1-111.pdf`

- overall scans: **1–111**;
- main body begins: scan **18 / printed 1**;
- Part ends: scan **111 / printed 94**;
- source intake: **111/111**;
- Pass 1: **111/111**;
- Pass 2A: **111/111**;
- Pass 2B: **111/111**;
- Pass 3: **111/111**;
- Part audit: **PASS**;
- final status sync: **PASS**;
- final Tamil statuses: **107 `verified` + 4 `partial`**;
- visual fidelity: **111/111 `verified`**.

Permanent source-limited Tamil records:

- scans **13–15** — unreadable continuous handwritten/facsimile bodies;
- scan **19** — physically washed-out/faint printed region.

Do not reconstruct them.

For normal Part 001 English work, use the audited repository Tamil records. The Part 001 PDF is not routinely required again unless a newly discovered source/provenance issue specifically requires a recheck.

The 111→112 boundary check remains deferred until Part 002 is supplied.

# Part 001 English project translation

The English layer is explicitly a **project-created translation**, not an official/publisher edition.

Authoritative controls:

- `translations/en/README.md`
- `translations/en/TRANSLATION_GUIDE.md`
- `translations/en/GLOSSARY.md`
- `translations/en/TRANSLATION_STATUS.md`

Every English page declares:

```yaml
translation_type: "project_translation"
```

Permanent cadence:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

Translate only from the audited Tamil repository records. Do not import standard Kural wording, published English translations, web text, another commentator or memory.

## English Batch 1 — COMPLETE

First-pass records exist for scans **1–8**:

- scans 1–3 — cover/publication matter;
- scans 4–8 — complete Preface.

All eight remain `draft`.

## English Batch 2 — COMPLETE

First-pass records now also exist for scans **9–17**:

- scans **9–12** — `மதிப்புரை` / **Critical Appreciation** — `draft`;
- scans **13–15** — source-limited handwritten/facsimile records — `source-limited`;
- scan **16** — first-edition photograph/note — `draft`;
- scan **17** — Sixth Edition Publisher's Note — `draft`.

Current English totals:

- page records created: **17/111**;
- `draft`: **14**;
- `source-limited`: **3**;
- source-checked: **0**;
- editorial-reviewed: **0**;
- release-ready: **0**.

Batches 1–2 are first-pass translation only; do not promote them to later review states yet.

## Current exact activity

Proceed with **Part 001 English Batch 3 — scans 18–27**.

Rules:

1. fetch live `main` first;
2. fetch the audited Tamil records for scans 18–27;
3. mirror filenames under `translations/en/pages/`;
4. translate only repository-supported Tamil wording;
5. scan **19** must use `status: "source-limited"` and may translate only the Tamil text actually preserved in the audited partial record;
6. ordinary verified-source pages remain `draft`;
7. preserve paragraph, quotation, verse and cross-page continuation structure in clear English;
8. update `TRANSLATION_STATUS.md` after the batch;
9. compare the pre-batch base SHA to the new head and confirm only intended English/documentation files changed;
10. record the exact next drafting frontier before advancing to scan 28.

Do not begin English source-check while Part 001 first-pass drafting remains incomplete unless a newer live workflow explicitly changes the cadence.

## Part 002

Part 002 / overall scans **112–222** is **not started** and its source is not supplied.

Do not begin Part 002 until Part 001 English/final closure is complete and Part 002 source is supplied.
