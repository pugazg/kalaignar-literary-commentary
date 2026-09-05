# Next Chat Prompt — குறளோவியம் archival / bilingual project

Continue directly in:

`pugazg/kalaignar-literary-commentary`

Branch: `main`

Active work: `works/kuraloviyam/`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve any newer durable state. Do not reset, repeat or reopen completed Tamil work, completed first-pass English drafting, completed English source-check, completed glossary reconciliation, or completed editorial-review batches because a copied prompt or root multi-work handover contains an older checkpoint.

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

Normal Part 001 English work uses audited Tamil repository page records. Do not reopen the Part 001 PDF unless a newly discovered source/provenance issue specifically requires it.

## Source / split identity

Complete source reported by user: **666 physical pages**, split into six 111-page Parts: 1–111, 112–222, 223–333, 334–444, 445–555, 556–666. Repository `scan_page` never restarts per split.

Part 002 has not been supplied or started.

## Part 001 Tamil state — CLOSED

Part 001 Tamil is **ARCHIVAL-READY**: scans 1–111; source intake and Passes 1/2A/2B/3 complete; Part audit PASS; final status sync PASS; **107 `verified` + 4 `partial`**; partial scans **13, 14, 15, 19**; visual fidelity **111/111 `verified`**.

Do not reconstruct the handwritten/facsimile bodies on scans 13–15 or the faint/washed-out material on scan 19.

## English project translation controls

English layer: `works/kuraloviyam/translations/en/`.

It is a **project-created translation**, not an official/publisher-issued English edition. Every English page carries `translation_type: "project_translation"`.

Permanent review cadence:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

Do not import standard Thirukkural wording, published English translations, web text, another commentator or memory.

## Completed Part 001 English gates

- first-pass drafting: **111/111 COMPLETE**;
- source-check: **111/111 COMPLETE**;
- glossary / recurring-terminology reconciliation: **111/111 COMPLETE**;
- editorial review ER1 / scans **1–15: COMPLETE**;
- ER2 / **16–30: COMPLETE**;
- ER3 / **31–45: COMPLETE**;
- ER4 / **46–60: COMPLETE**;
- ER5 / **61–75: COMPLETE**;
- ER6 / **76–90: COMPLETE**;
- ER7 / **91–105: COMPLETE**;
- ER8 / **106–111: COMPLETE**.

### Editorial-review closure state

- `editorial-reviewed`: **107**;
- `source-limited`: **4** — scans 13, 14, 15, 19;
- `source-checked`: **0**;
- `draft`: **0**;
- `release-ready`: **0**;
- editorial-review coverage: **111/111 COMPLETE**;
- ER8 required **no body-text changes** and promoted scans 106–111 by status only;
- **106→107** and **109→110→111** continuities remain intact; scan 108 is self-contained;
- scan **111** is the final supplied Part 001 physical scan;
- the **111→112** split boundary remains unverified and must not be reconstructed before Part 002 is supplied;
- no source-limited material was reconstructed;
- no standard/published/web English Kural wording was imported.

## Exact next activity

If live `main` has not advanced beyond this frontier, execute the **Part 001 Part-level English review** gate.

1. review the completed **111-page English layer as a whole** rather than repeating page-level editorial batches;
2. verify every English page record exists and maps correctly to its audited Tamil page record;
3. verify final statuses are exactly **107 `editorial-reviewed` + 4 `source-limited`**, with no `draft`, `source-checked` or `release-ready` records;
4. verify scans **13, 14, 15 and 19** preserve their source limitations and contain no reconstructed missing material;
5. verify controlled glossary terms, names, chapter labels, Kural numbering/metadata, quotations, repeated phrasing, page function and cross-page continuations at Part scale;
6. preserve the unresolved **111→112** split boundary explicitly;
7. create a durable Part-level English review artefact under `works/kuraloviyam/translations/en/reviews/` recording scope, controls, findings, limitations and PASS/FAIL result;
8. update `TRANSLATION_STATUS.md`, English/work README, `works/kuraloviyam/HANDOVER.md`, and this prompt;
9. audit the exact pre-gate base→head changed-file set;
10. if the Part-level review passes, advance only to the **Part-level English release report** gate.

Do **not** promote pages to `release-ready` during Part-level review. `release-ready` is reserved for pages included in the completed and approved release report.

Do not begin Part 002 until Part 001 English/final closure is complete and the Part 002 source is supplied.
