# HANDOVER — குறளோவியம்

Repository: `pugazg/kalaignar-literary-commentary`

Branch: `main`

Active work: `works/kuraloviyam/`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve any newer durable Kuraloviyam state. Do not reopen completed Part 001 Tamil passes or repeat completed English batches because an older prompt or root handover section records an earlier frontier.

For Kuraloviyam, this work-specific handover, `translations/en/TRANSLATION_STATUS.md` and `NEXT_CHAT_PROMPT_KURALOVIYAM.md` carry the current frontier. The root `HANDOVER.md` is multi-work and may contain historical Kuraloviyam text.

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
16. the Pass 2A / Pass 2B / Pass 3 records only when source-verification provenance is needed.

## Source family

- source ID: `TVA_BOK_0065733`;
- work: **குறளோவியம்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- complete source extent reported by user: **666 physical PDF pages**;
- split plan: six parts × 111 pages;
- overall ranges: 1–111, 112–222, 223–333, 334–444, 445–555, 556–666;
- repository `scan_page` never restarts per split.

## Mandatory per-part closure rule

Finish one supplied Part completely before beginning the next:

source intake → Pass 1 → Pass 2A → Pass 2B → Pass 3 → Part audit → final metadata/status synchronization → documentation synchronization → Tamil archival-ready → project-created English translation/review closure → final Part checkpoint → next Part.

## Part 001 Tamil source-dependent work — CLOSED

Controlling split used:

`TVA_BOK_0065733_குறளோவியம்_part_001_pages_1-111.pdf`

Boundary:

- overall scans **1–111**;
- main body begins scan **18 / printed 1**;
- Part 001 ends scan **111 / printed 94**.

Completed Tamil gates:

- source intake: **111/111**;
- Pass 1: **111/111**;
- Pass 2A: **111/111**;
- Pass 2B: **111/111**;
- Pass 3: **111/111**;
- Part audit: **PASS**;
- final page-status synchronization: **PASS**.

Final Tamil status:

- **107** pages `verified`;
- scans **13, 14, 15, 19** remain source-controlled `partial`;
- **111/111** pages have `visual_fidelity: "verified"`.

Do not reconstruct the partial records. Scans 13–15 contain unreadable continuous handwritten/facsimile bodies; scan 19 has a physically washed-out/faint printed region.

## Source independence after Tamil closure

For normal Part 001 English work, use the audited repository Tamil records. Do not require the Part 001 PDF again unless a newly discovered source/provenance problem specifically requires an earlier scan to be reopened.

The external 111→112 boundary check remains deferred until Part 002 is supplied.

# Part 001 English project translation

## Identity and controls

The English layer is a **project-created translation**, not an official/publisher English edition.

Authoritative English controls:

- `works/kuraloviyam/translations/en/README.md`
- `works/kuraloviyam/translations/en/TRANSLATION_GUIDE.md`
- `works/kuraloviyam/translations/en/GLOSSARY.md`
- `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`

Every English page declares:

```yaml
translation_type: "project_translation"
```

Permanent cadence:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

Do not import a standard Kural reading or published English translation. Translate only from the audited Tamil page records.

## English Batch 1 — COMPLETE

First-pass drafts now exist for **scans 1–8**:

- scans 1–3 — cover / title-publisher / edition-imprint;
- scans 4–8 / printed iii–vii — complete `முகப்புரை` / Preface.

Current English coverage:

- draft: **8 / 111**;
- source-checked: **0 / 111**;
- editorial-reviewed: **0 / 111**;
- release-ready: **0 / 111**.

The eight new pages remain `draft`; Batch 1 did not perform the later review gates.

## Current exact activity

Proceed with **Part 001 English Batch 2 — scans 9–17**, a natural boundary that closes the remaining front matter before the main body begins at scan 18.

Batch 2 composition:

- scans **9–12** — `மதிப்புரை` / **Critical Appreciation**;
- scans **13–15** — handwritten/facsimile pages: create English `source-limited` records from securely established Tamil material only; do not reconstruct handwriting;
- scan **16** — first-edition photograph/note;
- scan **17** — later-edition publication note.

Rules for Batch 2:

1. fetch live `main` first;
2. fetch each audited Tamil record for scans 9–17;
3. mirror filenames under `translations/en/pages/`;
4. safely translatable pages remain `draft`;
5. scans 13–15 use `status: "source-limited"`;
6. preserve paragraph/quotation/verse structure and source-visible limitations;
7. do not import web/memory/standard-edition Kural wording;
8. update `TRANSLATION_STATUS.md` after the batch;
9. compare batch base → head and confirm only intended English/doc files changed;
10. record the exact next frontier before advancing to scan 18.

Do not begin English source-check yet if first-pass drafting remains incomplete across Part 001.

## Part 002

Part 002 / overall scans **112–222** is **not started** and its source is not supplied.

Do not begin Part 002 until Part 001 English/final closure is complete and Part 002 source is supplied.
