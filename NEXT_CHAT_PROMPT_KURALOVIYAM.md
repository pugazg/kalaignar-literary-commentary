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
- Part 003 English first-pass drafting: **111/111 COMPLETE / CLOSED**.
- Draft Batch D1: **scans 223–255 / printed 206–238 — COMPLETE 33/33**.
- Draft Batch D2: **scans 256–288 / printed 239–271 — COMPLETE 33/33**.
- Draft Batch D3: **scans 289–321 / printed 272–304 — COMPLETE 33/33**.
- Draft Batch D4: **scans 322–333 / printed 305–316 — COMPLETE 12/12 / FINAL REMAINDER**.
- Part 003 English source-check SC1: **COMPLETE 33/33 — scans 223–255 / printed 206–238**.
- Part 003 English source-check SC2: **COMPLETE 33/33 — scans 256–288 / printed 239–271**.
- Part 003 English source-check SC3: **COMPLETE 33/33 — scans 289–321 / printed 272–304**.
- Part 003 English source-check SC4: **COMPLETE 12/12 — scans 322–333 / printed 305–316 / FINAL REMAINDER**.
- cumulative source-check: **111/111 COMPLETE / CLOSED**.
- current Part-003 English state: **111 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.
- remaining undrafted pages: **0**.
- glossary reconciliation: **NEXT / not-started**.
- editorial review / Part review / release: **not-started**.

D4 page commit: `f43d41d57622abdda7a9de63effe39697362629e`; its 12 page records were reconciled into live main with the drafting-completion controls. No Tamil files changed.

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

The Tamil archive is closed. For normal English work, the **audited Tamil page records under `works/kuraloviyam/pages/` are the working authority**. Reopen the scan only if a genuinely new provenance/fidelity issue appears.

Do not import a standard Thirukkural text, a published English Kural translation, another commentator's wording, web text, or remembered Kural wording.

## Boundary state relevant to the English layer

- incoming **222→223 — CLEAN**;
- D1 endpoint **255→256 — CLEAN**;
- D2 endpoint **288→289 — genuine continuation**, preserved and closed on scan 289;
- D3 endpoint **321→322 — CLEAN**;
- internal **332→333 — genuine continuation / closed within Part 003**;
- external **333→334 — deferred until Part 004 source intake**.

## English workflow

Permanent order:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

Current user-directed normal page-batch size: **33 physical scans**; a final remainder may be shorter.

For source-check:

- compare every English page against the audited Tamil record paragraph-by-paragraph / block-by-block;
- check omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual/non-body page function and cross-page continuities;
- make only source-fidelity corrections needed for a passing source-check;
- only a passing page may move from `status: "draft"` to `status: "source-checked"`;
- preserve `source_tamil_status: "verified"`;
- do not import standard/published/web English Kural wording;
- do not use source-check for stylistic rewriting unrelated to fidelity.

## Source-check results through SC4 — COMPLETE / CLOSED

- SC1 **223–255 / 206–238 — 33/33 source-checked**;
- SC2 **256–288 / 239–271 — 33/33 source-checked**;
- SC3 **289–321 / 272–304 — 33/33 source-checked**;
- SC4 **322–333 / 305–316 — 12/12 source-checked / FINAL REMAINDER**;
- cumulative source-check **111/111 COMPLETE / CLOSED**;
- current English state **111 source-checked / 0 draft / 0 source-limited / 0 blocked**.

SC4 source-fidelity corrections were limited to scan **327** (Monday-market sense), scans **328→329** (exact physical-page continuation), and scan **333** (side title/footer page furniture). The page-only gate changed exactly 12 English records and no Tamil record. Incoming **321→322 is CLEAN**; **332→333** remains a genuine continuation closed on scan 333.

SC4 page commit: `e07a6775513bcf1619e5d1bcb6e8222f7004f0a8`.

## Glossary reconciliation results through GR2 — COMPLETE / PASS

- GR1 **223–255 / printed 206–238 — 33/33 PASS**;
- GR2 **256–288 / printed 239–271 — 33/33 PASS**;
- cumulative glossary reconciliation **66/111**;
- current English page state remains **111 source-checked / 0 draft / 0 source-limited / 0 blocked**;
- GR1+GR2 page wording changes **0**; page status changes **0**; Tamil changes **0**.

GR2 verified all 16 Chapter/Kural metadata records in its range with 0 numeric or controlled-label mismatch. It added six Part-003-first chapter controls, mapped the GR2 source-form variants to established labels, refined contextual handling of `பாவம்`, `தேன்மொழி`, and descriptive `புணர்ச்சி மகிழ்தல்`, and recorded the recurring GR2 narrative/literary names.

## Exact next activity — Part 003 English Glossary Reconciliation GR3

Process **scans 289–321 / printed 272–304 — 33 page-aligned records**.

Requirements:

1. fetch live `main` first and preserve newer durable work;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm `translations/en/TRANSLATION_STATUS.md` records source-check **111/111 COMPLETE / CLOSED** and glossary reconciliation **66/111**;
4. read `translations/en/GLOSSARY.md` and English records **0289–0321** with their matching audited Tamil records;
5. reconcile recurring names, work/section names, controlled literary terms, publication names, chapter labels, citation metadata and repeated English renderings against the glossary and audited Tamil context;
6. update `GLOSSARY.md` only for terms actually evidenced in Part 003;
7. do not mechanically force one English rendering where context requires a different one;
8. do not import standard/published/web English Kural wording, another edition's terminology, or memory;
9. this gate does **not** promote `source-checked` pages to `editorial-reviewed`;
10. do not alter any Tamil page record or Tamil metadata;
11. do not begin editorial review during GR3;
12. update `translations/en/TRANSLATION_STATUS.md` and audit the exact changed-file set before advancing.

If GR3 passes, cumulative glossary reconciliation becomes **99/111**. GR4 is then the final **12-page remainder scans 322–333 / printed 305–316**. Part 004 remains blocked until Part 003 completes glossary reconciliation, editorial review, Part review, release report/release-ready synchronization and final Part closure. External **333→334** remains deferred until Part 004 source intake.
