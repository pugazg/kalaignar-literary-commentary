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
- editorial review: **111/111 COMPLETE** — ER1 through ER8 complete;
- page statuses after ER8: **107 `editorial-reviewed` + 4 `source-limited`**;
- `source-checked`: **0**;
- `draft`: **0**;
- source-limited scans: **13, 14, 15, 19**; all were reviewed within securely established material and remain `source-limited`;
- ER1 readability refinements: scans **5 and 6**;
- ER2: **20, 21, 24 and 28**;
- ER3: **36, 42, 43 and 44**;
- ER4: **46, 50 and 60**;
- ER5: **61, 68, 73 and 74**;
- ER6: **78, 79 and 80**;
- ER7: **91, 103 and 105**;
- ER8 / scans **106–111** required **no body-text changes**; status promotion only;
- ER8 preserved **106→107** and **109→110→111** continuities; scan 108 remains self-contained;
- scan **111** is the final supplied Part 001 scan; **111→112** remains unresolved until Part 002 is supplied;
- no unreadable source material was reconstructed;
- no standard/published/web English Kural wording was imported;
- release-ready: **0**.

The exact next gate is the **Part 001 Part-level English review**. This gate reviews the completed English layer as a whole and creates a durable Part-level review artefact. It does **not** promote pages to `release-ready`; that occurs only after the later release-report gate.

See `TRANSLATION_STATUS.md` for the authoritative English frontier.

Part 002 / scans 112–222 is not supplied and must not begin until Part 001 English/final closure is complete.
