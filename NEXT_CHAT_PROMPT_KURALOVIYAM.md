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
- current Part-003 English state: **99 `editorial-reviewed` + 12 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.
- remaining undrafted pages: **0**.
- glossary reconciliation: **111/111 COMPLETE / CLOSED**.
- editorial review: **IN PROGRESS — ER1 + ER2 + ER3 COMPLETE / PASS 99/111**; Part review / release: **not-started**.

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

## Glossary reconciliation — COMPLETE / CLOSED

- GR1 **223–255 / printed 206–238 — 33/33 PASS**;
- GR2 **256–288 / printed 239–271 — 33/33 PASS**;
- GR3 **289–321 / printed 272–304 — 33/33 PASS**;
- GR4 **322–333 / printed 305–316 — 12/12 PASS / FINAL REMAINDER**;
- cumulative glossary reconciliation **111/111 COMPLETE / CLOSED**;
- current English page state remains **111 source-checked / 0 draft / 0 source-limited / 0 blocked**;
- GR1+GR2 page wording changes **0**; GR3 wording changes **2 English files (scans 313–314), `Kaarmegam` → `Karmegam` only**; GR4 wording changes **2 English files (scans 327 and 331), controlled chapter-label reconciliation only**; page status changes **0**; Tamil changes **0**.

GR2 verified all 16 Chapter/Kural metadata records in its range with 0 numeric or controlled-label mismatch. It added six Part-003-first chapter controls, mapped the GR2 source-form variants to established labels, refined contextual handling of `பாவம்`, `தேன்மொழி`, and descriptive `புணர்ச்சி மகிழ்தல்`, and recorded the recurring GR2 narrative/literary names.

## Editorial review progress

- ER1 **scans 223–255 / printed 206–238 — COMPLETE / PASS 33/33**;
- ER2 **scans 256–288 / printed 239–271 — COMPLETE / PASS 33/33**;
- ER3 **scans 289–321 / printed 272–304 — COMPLETE / PASS 33/33**;
- cumulative editorial review **99/111**;
- current page state **99 editorial-reviewed + 12 source-checked**;
- ER1 wording changes were limited to scans **246, 251, 255**;
- ER2 wording changes were limited to scans **256, 258, 259, 260, 263, 264, 265, 269, 270, 273, 275, 279, 281, 285, 287**;
- ER3 wording changes were limited to scans **289, 290, 292, 295, 298, 300, 304, 305, 308, 310, 313, 315, 316, 320**; the other **19** pages were status-only promotions;
- no Tamil record changed;
- genuine **288→289** remains preserved and closes on scan 289; clean **321→322** remains clean.

## Exact next activity — Part 003 English Editorial Review ER4

Process **scans 322–333 / printed 305–316 — final 12 page-aligned records**.

Requirements:

1. fetch live `main` first and preserve newer durable work;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm English drafting, source-check and glossary reconciliation are each **111/111 COMPLETE / CLOSED**, and editorial review is **99/111**;
4. read `translations/en/TRANSLATION_GUIDE.md`, `GLOSSARY.md`, and English records **0322–0333** with matching audited Tamil wherever meaning-sensitive editorial decisions arise;
5. review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity;
6. make only source-faithful editorial improvements; do not import standard/published/web English Kural wording, another edition's terminology, or memory;
7. passing pages may move from `source-checked` to `editorial-reviewed`;
8. do not alter any Tamil page record or Tamil metadata;
9. do not begin Part-level review or release work during ER4;
10. update `TRANSLATION_STATUS.md` and audit the exact changed-file set before advancing.

If ER4 passes, editorial review becomes **111/111 COMPLETE / CLOSED** and the next activity is the **whole-Part Part-level English review — scans 223–333 / printed 206–316**. Part 004 remains blocked until Part 003 completes Part review, release report/release-ready synchronization and final Part closure. External **333→334** remains deferred until Part 004 source intake.
