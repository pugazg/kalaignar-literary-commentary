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
  reviews/
    PART_001_ENGLISH_REVIEW.md
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
- editorial review: **111/111 COMPLETE** — ER1 through ER8 complete;
- Part-level English review: **COMPLETE — PASS**;
- durable Part-level review: `reviews/PART_001_ENGLISH_REVIEW.md`;
- Tamil↔English filename alignment confirmed: **111/111**;
- current page statuses: **107 `editorial-reviewed` + 4 `source-limited`**;
- source-limited scans: **13, 14, 15, 19**; all were independently rechecked at Part level and remain explicitly limited without reconstructed wording;
- `source-checked`: **0**;
- `draft`: **0**;
- `release-ready`: **0**;
- Part-scale controlled terminology, names, chapter labels, Kural metadata, quotation handling, page functions and known cross-page continuities: **PASS**;
- `TRANSLATION_GUIDE.md` stale frontier was corrected during Part-level review as a documentation-only control fix;
- no English page body text or page status was changed during Part-level review;
- scan **111** is the final supplied Part 001 scan; **111→112** remains unresolved until Part 002 is supplied;
- no unreadable source material was reconstructed;
- no standard/published/web English Kural wording was imported.

The exact next gate is the **Part 001 Part-level English release report**. It must use the completed Part-level review to decide release approval. Pages must not be promoted to `release-ready` before the release report is completed and approved.

See `TRANSLATION_STATUS.md` for the authoritative English frontier.

Part 002 / scans 112–222 is not supplied and must not begin until Part 001 English/final closure is complete.