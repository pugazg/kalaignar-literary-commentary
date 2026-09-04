# Next Chat Prompt — குறளோவியம் archival / bilingual project

Continue directly in:

`pugazg/kalaignar-literary-commentary`

Branch: `main`

Active work: `works/kuraloviyam/`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve any newer durable state. Do not reset, repeat or reopen completed Tamil work or completed English batches because a copied prompt or the root multi-work handover contains an older checkpoint.

## Mandatory startup

Read completely before any Kuraloviyam change:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this `NEXT_CHAT_PROMPT_KURALOVIYAM.md`
5. `works/kuraloviyam/HANDOVER.md`
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

Normal Part 001 English work uses the audited Tamil repository page records. Do not reopen the Part 001 PDF unless a newly discovered source/provenance issue specifically requires it.

## Source / split identity

Complete source reported by user: **666 physical pages**, split into six 111-page Parts.

- Part 001: 1–111
- Part 002: 112–222
- Part 003: 223–333
- Part 004: 334–444
- Part 005: 445–555
- Part 006: 556–666

Repository `scan_page` never restarts per split.

Part 002 has not been supplied or started.

## Part 001 Tamil state — CLOSED

Part 001 Tamil is **ARCHIVAL-READY**:

- source intake: 111/111;
- Pass 1: 111/111;
- Pass 2A: 111/111;
- Pass 2B: 111/111;
- Pass 3: 111/111;
- Part audit: PASS;
- final status sync: PASS;
- Tamil statuses: **107 `verified` + 4 `partial`**;
- partial scans: **13, 14, 15, 19**;
- visual fidelity: **111/111 `verified`**.

Do not reconstruct the handwritten/facsimile bodies on scans 13–15 or the faint/washed-out material on scan 19.

## Mandatory per-part closure rule

Finish one supplied Part completely before the next:

Tamil source intake → Pass 1 → Pass 2A → Pass 2B → Pass 3 → Part audit → final status/documentation sync → Tamil archival-ready → English translation/review closure → final Part checkpoint → next supplied Part.

## English project translation controls

English layer:

`works/kuraloviyam/translations/en/`

It is a **project-created translation**, not an official/publisher-issued English edition.

Every English page declares:

```yaml
translation_type: "project_translation"
```

Permanent cadence:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

Do not import standard Thirukkural wording, published English Kural translations, web text, another commentator or memory.

## English first-pass progress

### Batch 1 — COMPLETE — scans 1–8

- scans 1–3 — cover/publication matter;
- scans 4–8 — complete Preface;
- all eight: `draft`.

### Batch 2 — COMPLETE — scans 9–17

- scans 9–12 — `மதிப்புரை` / **Critical Appreciation** — `draft`;
- scans 13–15 — handwritten/facsimile prefaces — `source-limited`;
- scan 16 — first-edition photograph / commemorative note — `draft`;
- scan 17 — Sixth Edition Publisher's Note — `draft`.

Current English totals:

- page records created: **17/111**;
- `draft`: **14**;
- `source-limited`: **3**;
- source-checked: **0**;
- editorial-reviewed: **0**;
- release-ready: **0**.

Do not redo Batches 1–2 merely for stylistic harmonization. Later review gates are the proper place for deliberate refinement.

## Exact next activity

If live `main` has not advanced beyond this frontier, execute **Part 001 English Batch 3 — scans 18–27**.

1. fetch the audited Tamil page records for scans 18–27;
2. create matching English files under `works/kuraloviyam/translations/en/pages/`;
3. scan 18 begins the main body / published-speech excerpts at printed page 1;
4. scan **19** is audited Tamil `partial`: create an English `source-limited` record that translates only repository-preserved Tamil wording and explicitly preserves the washed-out gap;
5. ordinary pages whose Tamil source status is `verified` remain English `draft`;
6. preserve paragraph, quotation, verse, speaker/attribution and physical continuation structure as appropriate;
7. do not import a standard Kural reading or external English wording;
8. update `translations/en/TRANSLATION_STATUS.md` after the batch;
9. audit the changed-file set from the pre-batch live SHA to the new head;
10. record the exact next English frontier before advancing to scan 28.

Do not begin English source-check while Part 001 first-pass drafting remains incomplete unless a newer live workflow explicitly changes that cadence.

Do not begin Part 002 until Part 001 English/final closure is complete and the Part 002 source is supplied.
