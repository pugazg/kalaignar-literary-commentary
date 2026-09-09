# Next Chat Prompt — குறளோவியம் archival / bilingual project

Continue directly in `pugazg/kalaignar-literary-commentary`, branch `main`, active work `works/kuraloviyam/`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work. Do not reopen closed Part 001 or Part 002 unless a genuinely new source/provenance/fidelity issue appears.

## Mandatory startup

Read completely before changing anything:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this prompt
5. `works/kuraloviyam/HANDOVER.md`
6. `works/kuraloviyam/README.md`
7. `works/kuraloviyam/metadata/source.md`
8. `works/kuraloviyam/metadata/transcription-policy.md`
9. `works/kuraloviyam/indexes/page-map.md`
10. `works/kuraloviyam/SOURCE_INTAKE_PART_003.md`
11. `works/kuraloviyam/PART_003_PASS1_PROGRESS.md`
12. `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_003.md`
13. `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_003.md`
14. `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_002.md` as Pass-3 precedent
15. `works/kuraloviyam/PART_002_TAMIL_ARCHIVAL_READY.md`
16. `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`
17. `works/kuraloviyam/translations/en/reviews/PART_002_ENGLISH_RELEASE_REPORT.md`

## Durable state

- Part 001: **CLOSED**.
- Part 002 Tamil: **ARCHIVAL-READY / CLOSED — 111/111 textual + visual verified**.
- Part 002 English: **RELEASE COMPLETE / CLOSED — 111/111 release-ready**.
- Part 003 source intake: **PASS / COMPLETE**.
- Part 003 Pass 1: **COMPLETE — 111/111, scans 223–333 / printed 206–316**.
- Part 003 Pass 2A: **COMPLETE — 111/111, scans 223–333 / printed 206–316**.
- Part 003 Pass 2B: **COMPLETE — 111/111 independently re-read through scan 333 / printed 316**.
- Part 003 Pass 3: **NOT STARTED**.
- Part 003 audit and Tamil archival-ready: **not-started**.
- English remains **blocked until Tamil closure**.

## Part 003 controlling source

`TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf`

Confirmed identity:

- local PDF pages: **111**;
- overall scans: **223–333**;
- printed pages: **206–316**;
- file size: **93,488,924 bytes**;
- SHA-256: `f07e7cdb3a6e786b0378e00bbe699a241be41c9e099c004a4faa90fa82b4239f`;
- no usable parsed text layer; rendered source scans control.

All Part-003 page records intentionally remain:

- `status: "needs-review"`
- `visual_fidelity: "needs-review"`

Do not promote records during Pass 3.

## Pass 2B closure

Part 003 Pass 2B is **COMPLETE — 111/111**.

- Batches 1–9: **90/111 through scan 312**;
- Batch 10: **313–322 — 10/10**, corrections on **314, 316, 320, 322**;
- Batch 11: **323–332 — 10/10**, correction on **326**;
- final remainder: **scan 333 / printed 316 — 1/1**, with source restorations `இறுதியான` → `இறுதி யான` and `தலைமை ஏற்று` → `தலைமைபெற்று`.

The final scan independently reconfirmed Kural 567 wording/lineation and Chapter 57 — `வெருவந்த செய்யாமை` metadata. Internal **332→333 genuine continuation is closed**. External **333→334 remains deferred until Part 004 source intake**.

Durable cumulative record: `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_003.md`.

## Pass 3 rule

Pass 3 is **meaningful visual-text verification**, not another lexical reread. Follow `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_002.md` as precedent.

For each scan verify source-supported visual organization, including:

- heading hierarchy;
- Kural/quotation lineation and block placement;
- prose/quotation relationships;
- page furniture and source/non-source visual separation;
- illustration/text physical order and relationship;
- physical-page continuation;
- source-size legibility.

Exact font, colour and artwork recreation are not required. Rewrite a page record only when a directly source-supported structural correction is required. Do not mechanically rewrite no-change records. Pass 3 does **not** authorize final `verified` status.

## Exact next activity — Part 003 Pass 3 / Batch 1

Process **scans 223–232 / printed 206–215 — 10 physical scans** in one meaningful visual-text verification iteration.

Requirements:

1. fetch live `main` first;
2. resolve the supplied Part 003 PDF and freshly render/inspect scans **223–232** directly;
3. fetch current page records `0223`–`0232` before comparison;
4. verify heading hierarchy, illustration/text order, Kural/quotation block placement and lineation, prose/quotation relationships, page furniture, non-body marks and physical continuations against the scans;
5. make only direct source-supported **structural** corrections; do not repeat lexical verification or normalize settled wording;
6. inspect scan **233 / printed 216** only as the outgoing continuity/boundary witness when needed; known **232→233 is CLEAN**;
7. create `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_003.md` following the Part-002 precedent and log every structural-correction/no-change result;
8. keep all records at `needs-review` / `visual_fidelity: needs-review`;
9. synchronize README, work/root handovers, page-map and this prompt to the resulting Pass-3 frontier;
10. audit the exact changed-file set before advancing;
11. do not begin the Part audit until Pass 3 covers all 111 Part-003 scans.
