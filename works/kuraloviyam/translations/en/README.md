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
- editorial review: **60/111 scans reviewed at the gate** — ER1 scans 1–15, ER2 scans 16–30, ER3 scans 31–45 and ER4 scans 46–60 COMPLETE;
- page statuses after ER4: **56 `editorial-reviewed` + 51 `source-checked` + 4 `source-limited`**;
- `draft`: **0**;
- source-limited scans: **13, 14, 15, 19**; all have been reviewed within securely established material for the editorial batches that include them and remain `source-limited`;
- ER1 made two source-faithful readability refinements on scans **5 and 6**;
- ER2 made four source-faithful readability refinements on scans **20, 21, 24 and 28**;
- ER3 made four source-faithful readability refinements on scans **36, 42, 43 and 44**;
- ER4 made three source-faithful readability refinements on scans **46, 50 and 60**; all other ER4 pages required status promotion only;
- ER4 preserved the **50→51**, **56→57** and **58→59** continuations and boundary-checked **60→61** without processing scan 61;
- no unreadable source material was reconstructed;
- no standard/published/web English Kural wording was imported;
- release-ready: **0**.

The exact next gate is **editorial consistency review ER5 — scans 61–75**, exactly 15 consecutive scans. Passing pages may move from `source-checked` to `editorial-reviewed`.

See `TRANSLATION_STATUS.md` for the authoritative English frontier.

Part 002 / scans 112–222 is not supplied and must not begin until Part 001 English/final closure is complete.