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
- final source-check statuses: **107 `source-checked` + 4 `source-limited`**;
- `draft`: **0**;
- source-limited scans: **13, 14, 15, 19**, all reviewed within available evidence;
- glossary / recurring-terminology reconciliation: **30/111 scans complete** — GR1 scans 1–15 and GR2 scans 16–30;
- GR2 reconciled `பதிப்புரை` as **Publisher's Note**, retained context-aware `உரை` and `புதுக் கவிதை` renderings, standardized scan 17's three structural Book labels, and standardized **Puratchi Kavignar Bharathidasan** across scans 19 and 30;
- the user-confirmed lexical clarification `பதவுரை` → **word-by-word explanation** was also applied to the glossary and the existing English occurrences on scans 4–5;
- no standard/published/web English Kural translation wording was imported;
- editorial-reviewed: **0**;
- release-ready: **0**.

The exact next gate is **glossary reconciliation GR3 — scans 31–45**, exactly 15 consecutive scans. This gate checks controlled names/terms and recurring English renderings; it does not itself promote pages to `editorial-reviewed`.

See `TRANSLATION_STATUS.md` for the authoritative English frontier.

Part 002 / scans 112–222 is not supplied and must not begin until Part 001 English/final closure is complete.