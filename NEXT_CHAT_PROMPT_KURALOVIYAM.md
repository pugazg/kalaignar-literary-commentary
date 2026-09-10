# Next Chat Prompt — குறளோவியம் archival / bilingual project

Continue directly in `pugazg/kalaignar-literary-commentary`, branch `main`, active work `works/kuraloviyam/`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work. Do not reopen closed Part 001, Part 002, or the closed Part 003 Tamil layer unless a genuinely new source/provenance/fidelity issue appears.

## Mandatory startup

Read completely before changing anything:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this prompt
5. `works/kuraloviyam/HANDOVER.md`
6. `works/kuraloviyam/README.md`
7. `works/kuraloviyam/PART_003_AUDIT.md`
8. `works/kuraloviyam/PART_003_FINAL_STATUS_SYNC.md`
9. `works/kuraloviyam/PART_003_DOCUMENTATION_SYNC.md`
10. `works/kuraloviyam/PART_003_TAMIL_ARCHIVAL_READY.md`
11. `works/kuraloviyam/translations/en/README.md`
12. `works/kuraloviyam/translations/en/TRANSLATION_GUIDE.md`
13. `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`
14. `works/kuraloviyam/translations/en/GLOSSARY.md`
15. `works/kuraloviyam/translations/en/reviews/PART_002_ENGLISH_RELEASE_REPORT.md` as the preceding closed English-Part precedent

## Durable state

- Part 001: **CLOSED** — Tamil archival-ready; English **107 release-ready + 4 source-limited**.
- Part 002 Tamil: **ARCHIVAL-READY / CLOSED — 111/111 textual + visual verified**.
- Part 002 English: **RELEASE COMPLETE / CLOSED — 111/111 release-ready**.
- Part 003 Tamil: **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**.
- Part 003 English first-pass drafting: **33/111 COMPLETE**.
- Part 003 English Draft Batch D1: **scans 223–255 / printed 206–238 — COMPLETE 33/33**.
- completed Part-003 English range: **33 `draft` / 0 source-limited / 0 blocked**.
- remaining undrafted Part-003 English pages: **78**.
- Part 003 English source-check / glossary reconciliation / editorial review / Part review / release: **not-started**.

## Part 003 Tamil authority

Controlling Tamil source:

`TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf`

Confirmed identity:

- local PDF pages: **111**;
- overall scans: **223–333**;
- printed pages: **206–316**;
- file size: **93,488,924 bytes**;
- SHA-256: `f07e7cdb3a6e786b0378e00bbe699a241be41c9e099c004a4faa90fa82b4239f`;
- no usable parsed text layer.

The Tamil archive is already closed. For normal English work, the **audited Tamil page records under `works/kuraloviyam/pages/` are the working authority**. Reopen the scan only if a genuinely new provenance/fidelity issue appears.

Do not import a standard Thirukkural text, a published English Kural translation, another commentator's wording, web text, or remembered Kural wording.

## Boundary state relevant to the English layer

- incoming **222→223 — CLEAN**;
- Draft Batch D1 endpoint **255→256 — CLEAN**; scan 256 begins a new illustrated vignette;
- internal **332→333 — genuine continuation / closed within Part 003**;
- external **333→334 — deferred until Part 004 source intake**.

## English workflow

Permanent order:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

Current user-directed normal page-batch size: **33 physical scans**.

Every new first-pass English page must:

- mirror the Tamil filename under `works/kuraloviyam/translations/en/pages/`;
- carry `translation_type: "project_translation"`;
- carry `status: "draft"`;
- carry `source_tamil_status: "verified"`;
- use `translation_basis: "audited Tamil archival record; controlling scan remains ultimate source authority"`;
- preserve page alignment, meaningful paragraph/dialogue order, Kural block separation, visual/non-body descriptions, and source-supported cross-page continuity;
- translate the exact Kural wording preserved in the audited Tamil record rather than substituting a familiar published rendering.

## Exact next activity — Part 003 English Draft Batch D2

Process **scans 256–288 / printed 239–271 — 33 page-aligned records** as the second English first-pass drafting batch.

Requirements:

1. fetch live `main` first and preserve newer durable work;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm `translations/en/TRANSLATION_STATUS.md` records Draft Batch D1 as **COMPLETE 33/33 through scan 255 / printed 238**;
4. read audited Tamil records **0256–0288** completely and translate only from those records;
5. create English counterparts for exactly **33 scans, 256–288 / printed 239–271**;
6. keep every page at `status: "draft"` and `source_tamil_status: "verified"`;
7. preserve illustrations/non-body page function and every source-supported continuation across the batch;
8. do not alter any Tamil page record or Tamil metadata;
9. do not perform source-check, glossary reconciliation or editorial promotion during this drafting gate;
10. update `translations/en/TRANSLATION_STATUS.md` after the batch;
11. audit the exact changed-file set before advancing.

If D2 passes, cumulative first-pass drafting becomes **66/111**. The next drafting batch will be **D3: scans 289–321 / printed 272–304 — 33 pages**.

Part 004 remains blocked until Part 003 completes the maintained English workflow and final Part closure checkpoint.