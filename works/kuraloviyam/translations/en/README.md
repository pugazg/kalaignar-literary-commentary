# Kuraloviyam — English project translation

This directory contains the **project-created English translation layer** for the audited Tamil archive of Kalaignar M. Karunanidhi's `குறளோவியம்`.

This is **not** an official or publisher-issued English edition.

Every English page declares:

```yaml
translation_type: "project_translation"
```

## Authority

Normal translation/review work uses the audited Tamil page records under `../../pages/`. The original Tamil scan remains the ultimate source authority if a new provenance or fidelity problem is discovered, but the closed Part 001 PDF is not routinely reopened for English review.

Do not import standard Thirukkural wording, a published English Kural translation, another commentator, web text or memory.

## Structure

```text
translations/en/
  README.md
  TRANSLATION_GUIDE.md
  GLOSSARY.md
  TRANSLATION_STATUS.md
  pages/
  reviews/          # created when review/release artefacts are actually needed
```

English pages mirror the Tamil filenames exactly.

## Workflow

**Tamil archival-ready → English draft → English source-check → glossary reconciliation → editorial review → Part-level review → release report → release-ready.**

Tamil verification status and English review status are separate.

## Part 001 source limitations

Part 001 Tamil has four intentional source-limited pages:

- scans 13–15 — unreadable continuous handwritten/facsimile bodies;
- scan 19 — physically washed-out/faint printed region.

The English layer preserves those limits and does not reconstruct unavailable wording.

## Current state

Part 001 Tamil / scans **1–111**: **ARCHIVAL-READY / CLOSED**.

Part 001 English:

- page-aligned first-pass translation: **111/111 COMPLETE**;
- source-check: **111/111 COMPLETE**;
- glossary / recurring-terminology reconciliation: **111/111 COMPLETE**;
- editorial review: **105/111 scans reviewed at the gate** — ER1 scans 1–15, ER2 scans 16–30, ER3 scans 31–45, ER4 scans 46–60, ER5 scans 61–75, ER6 scans 76–90 and ER7 scans 91–105 COMPLETE;
- page statuses after ER7: **101 `editorial-reviewed` + 6 `source-checked` + 4 `source-limited`**;
- `draft`: **0**;
- source-limited scans: **13, 14, 15, 19**; all have been reviewed within securely established material for the editorial batches that include them and remain `source-limited`;
- ER1 readability refinements: scans **5 and 6**;
- ER2 readability refinements: scans **20, 21, 24 and 28**;
- ER3 readability refinements: scans **36, 42, 43 and 44**;
- ER4 readability refinements: scans **46, 50 and 60**;
- ER5 readability refinements: scans **61, 68, 73 and 74**;
- ER6 readability refinements: scans **78, 79 and 80**;
- ER7 readability refinements: scans **91, 103 and 105**; all other ER7 pages required status promotion only;
- ER7 preserved the **91→92, 93→94, 95→96, 97→98, 99→100→101, 102→103 and 104→105** continuities; **105→106** was boundary-checked and scan 106 begins a new vignette;
- no unreadable source material was reconstructed;
- no standard/published/web English Kural wording was imported;
- release-ready: **0**.

The exact next gate is **editorial consistency review ER8 — scans 106–111**, the final six-scan editorial remainder. Passing pages may move from `source-checked` to `editorial-reviewed`.

See `TRANSLATION_STATUS.md` for the authoritative English frontier.

Part 002 / scans 112–222 is not supplied and must not begin until Part 001 English/final closure is complete.
