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
14. `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_003.md`
15. `works/kuraloviyam/PART_003_AUDIT.md`
16. `works/kuraloviyam/PART_002_FINAL_STATUS_SYNC.md` as metadata-sync precedent
17. `works/kuraloviyam/PART_002_TAMIL_ARCHIVAL_READY.md`
18. `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`
19. `works/kuraloviyam/translations/en/reviews/PART_002_ENGLISH_RELEASE_REPORT.md`

## Durable state

- Part 001: **CLOSED**.
- Part 002 Tamil: **ARCHIVAL-READY / CLOSED — 111/111 textual + visual verified**.
- Part 002 English: **RELEASE COMPLETE / CLOSED — 111/111 release-ready**.
- Part 003 source intake: **PASS / COMPLETE**.
- Part 003 Pass 1: **COMPLETE — 111/111, scans 223–333 / printed 206–316**.
- Part 003 Pass 2A: **COMPLETE — 111/111, scans 223–333 / printed 206–316**.
- Part 003 Pass 2B: **COMPLETE — 111/111 independently re-read through scan 333 / printed 316**.
- Part 003 Pass 3: **COMPLETE — 111/111 through scan 333 / printed 316**.
- Part 003 audit: **PASS — 111/111**.
- Part 003 final metadata/status synchronization: **NEXT / not-started**.
- Part 003 documentation synchronization and Tamil archival-ready: **not-started**.
- English remains **blocked until Tamil closure**.

## Part 003 controlling source

`TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf`

Confirmed identity:

- local PDF pages: **111**;
- overall scans: **223–333**;
- printed pages: **206–316**;
- file size: **93,488,924 bytes**;
- SHA-256: `f07e7cdb3a6e786b0378e00bbe699a241be41c9e099c004a4faa90fa82b4239f`;
- no usable parsed text layer; rendered source scans controlled the completed verification passes.

## Part 003 audit closure

Durable audit record: `works/kuraloviyam/PART_003_AUDIT.md`.

Audit result: **PASS**.

The audit confirms:

- physical coverage: **111/111**, scans **223–333 / printed 206–316**;
- scan/local/printed-page mapping: **PASS**;
- source intake / Pass 1 / Pass 2A / Pass 2B / Pass 3: **COMPLETE — 111/111 each**;
- internal continuation and structural edge cases: **PASS**;
- non-body source material / page-furniture separation: **PASS**;
- carried `partial`, `blocked` or source-limited Tamil exceptions: **0**;
- premature Part-003 `verified` promotion: **0**;
- Tamil body-text changes during audit: **0**.

Internal **332→333 genuine continuation is closed**. External **333→334 remains deferred until Part 004 source intake** and is not a Part-003 defect.

All Part-003 page records intentionally still remain:

- `status: "needs-review"`
- `visual_fidelity: "needs-review"`

The audit did **not** promote them.

## Exact next activity — Part 003 final metadata/status synchronization

Perform the **metadata-only final status synchronization across all 111 Part-003 page records / scans 223–333 / printed 206–316**, following `works/kuraloviyam/PART_002_FINAL_STATUS_SYNC.md` as precedent.

Requirements:

1. fetch live `main` first and preserve newer durable state;
2. confirm `works/kuraloviyam/PART_003_AUDIT.md` remains **PASS** and no newer source/provenance/fidelity issue invalidates that result;
3. fetch the current Part-003 page-record inventory before writing;
4. change only these two metadata fields on eligible Part-003 records:
   - `status: "needs-review"` → `status: "verified"`
   - `visual_fidelity: "needs-review"` → `visual_fidelity: "verified"`
5. do **not** change Tamil body wording, quoted Kural wording/lineation, paragraph/dialogue structure, `page_type`, `visual_notes`, source comments, source-furniture treatment, scan number, local Part page or printed page;
6. process **all 111 records** in the metadata-only gate;
7. before documentation writes, compare the status-sync starting checkpoint to the page-status endpoint and confirm:
   - exactly **111 Part-003 page files** changed;
   - no non-page file changed in the metadata-only portion;
   - every page change is limited to the two status-value transitions above;
   - no Tamil body-text or structural change occurred;
8. create `works/kuraloviyam/PART_003_FINAL_STATUS_SYNC.md` recording the evidence base, exact starting/end checkpoints, changed-file audit and final distribution;
9. after that metadata-only gate passes, proceed to **documentation synchronization** as the next separate gate;
10. only after documentation synchronization may the separate **Tamil archival-ready checkpoint** close Part 003 Tamil;
11. English remains blocked until Tamil archival closure;
12. external **333→334 remains deferred** until Part 004 source intake.
