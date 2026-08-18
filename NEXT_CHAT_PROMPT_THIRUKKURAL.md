# Next Chat Prompt — Thirukkural Kalaignar Commentary — Completed Baseline

Copy/paste the prompt below into a new chat window when returning to this repository.

---

Continue work directly in:

`pugazg/kalaignar-literary-commentary`

Work on `main`.

The supplied **Thirukkural — Kalaignar Commentary** volume is already complete. Do **not** restart transcription, translation, semantic chapter mapping, or any old continuation batch unless current `main` proves that a regression or new source has been introduced.

## MANDATORY STARTUP

Before making any repository change, read these files completely:

1. `NEXT_CHAT_PROMPT_THIRUKKURAL.md`
2. `THIRUKKURAL_ARCHIVAL_GUIDELINES.md`
3. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
4. root `HANDOVER.md`
5. `works/thirukkural/README.md`
6. `works/thirukkural/metadata/source.md`
7. `works/thirukkural/indexes/page-map.md`
8. `works/thirukkural/structure/README.md`
9. `works/thirukkural/structure/CHAPTER_README_POLICY.md`
10. `works/thirukkural/structure/STRUCTURE_AUDIT.md`
11. `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`
12. `works/thirukkural/translations/en/TRANSLATION_STATUS.md`

Then inspect current GitHub `main`. Repository state is authoritative over stale SHAs or historical progress paragraphs.

## COMPLETED BASELINE — DO NOT RESTART

### Tamil archival layer

Parts **001–015** are audited / archival-ready through the entire supplied volume:

- scans **1–323**;
- commentary through printed page **270**;
- Kural sequence through **1330**;
- scans 304–321: `குறள் முதற்குறிப்பு அகரவரிசை`, printed pages 271–288;
- scan 322 blank;
- scan 323 back cover.

Tamil audits exist through `AUDIT_PART_015.md`.

### English project translation

Parts **001–015** are released through the end of the supplied volume.

Do not restart:

- Part 014 source-check;
- Part 015 drafting/source-check/editorial/release;
- any released earlier Part merely for stylistic harmonization.

### Semantic structure / provenance

`works/thirukkural/structure/` is complete:

- **3 பால்**;
- **13 இயல்**;
- **133 அதிகாரம்**;
- **1,330 குறள்**.

Final chapter:

- **133 — ஊடலுவகை**;
- Kurals **1321–1330**;
- scans **302–303**;
- Parts **014–015**;
- printed pages **269–270**.

`works/thirukkural/structure/STRUCTURE_AUDIT.md` records **PASS — SEMANTIC PROVENANCE MAPPING COMPLETE**.

Do not restart chapters 113–117 or any other old semantic batch.

## SOURCE / ARCHIVE RULES

The supplied scan is the controlling source.

Do not silently modernize, normalize, correct, reconstruct or replace Tamil from memory, the web or another edition.

Do not move, duplicate or rewrite:

- canonical Tamil physical pages: `works/thirukkural/pages/`;
- released English physical pages: `works/thirukkural/translations/en/pages/`.

The semantic hierarchy is navigation/provenance only.

Exact scan boundaries must come from actual verified page records, not arithmetic inference.

## IMPORTANT INBAM PROVENANCE DISCREPANCY

Semantic hierarchy:

- chapters 109–115 → `களவியல்`;
- chapters 116–133 → `கற்பியல்`.

Physical archive metadata:

- retains `களவியல்` / `Clandestine Love` through scan **277**;
- scan **278** is the first physical `கற்பியல்` / `Wedded Love` record.

This discrepancy is intentionally documented in the semantic READMEs. Do not “fix” it by rewriting canonical Tamil or released English records.

## HISTORICAL DOCUMENTS

The following are retired/historical records, not current workflow instructions:

- `works/thirukkural/CONTINUATION_GUIDELINES.md`;
- `works/thirukkural/HANDOVER_PARTS_006_010.md`;
- `works/thirukkural/NEXT_CHAT_PROMPT_PARTS_006_010.md`;
- completed Part audits and English review/release reports.

Preserve them as project provenance.

## CURRENT NEXT-ACTIVITY RULE

There is no predefined unfinished Thirukkural activity for the supplied volume.

When the user provides a new request:

1. inspect current `main` first;
2. determine whether the request is a new source intake, another literary-commentary work, or a separately defined enhancement/audit/indexing task;
3. perform only that new scope;
4. do not manufacture continuation after Kural 1330;
5. do not reopen released source-controlled text without an explicit, source-supported reason.

If a new Thirukkural PDF/source is supplied, inspect it directly before deciding whether it is a supplement, alternate edition, duplicate source, or new archival unit.

---
