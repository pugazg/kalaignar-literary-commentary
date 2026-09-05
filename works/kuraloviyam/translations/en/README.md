# Kuraloviyam — English project translation

This directory contains the **project-created English translation layer** for the audited Tamil archive of Kalaignar M. Karunanidhi's `குறளோவியம்`.

This is **not** an official or publisher-issued English edition.

Every English page declares:

```yaml
translation_type: "project_translation"
```

## Authority

Normal translation/review work uses the audited Tamil page records under `../../pages/`. The original Tamil scan remains the ultimate source authority if a new provenance or fidelity problem is discovered, but a closed Part is not routinely reopened.

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
    PART_001_ENGLISH_RELEASE_REPORT.md
```

English pages mirror the Tamil filenames exactly.

## Workflow

**Tamil archival-ready → English draft → English source-check → glossary reconciliation → editorial review → Part-level review → release report → release-ready.**

Tamil verification status and English review status are separate.

## Part 001 source limitations

Part 001 has four intentional source-limited pages:

- scans 13–15 — unreadable continuous handwritten/facsimile bodies;
- scan 19 — physically washed-out/faint printed region.

The English layer preserves those limits and does not reconstruct unavailable wording.

## Part 001 final state

Part 001 Tamil / scans **1–111**: **ARCHIVAL-READY / CLOSED**.

Part 001 English:

- page-aligned first-pass translation: **111/111 COMPLETE**;
- source-check: **111/111 COMPLETE**;
- glossary / recurring-terminology reconciliation: **111/111 COMPLETE**;
- editorial review: **111/111 COMPLETE**;
- Part-level English review: **PASS**;
- release report: **APPROVED WITH EXPLICIT SOURCE LIMITATIONS**;
- final page statuses: **107 `release-ready` + 4 `source-limited`**;
- source-limited scans: **13, 14, 15, 19**;
- `editorial-reviewed`: **0**;
- `source-checked`: **0**;
- `draft`: **0**;
- no English body text changed at the release gate;
- no source-limited material was reconstructed;
- no standard/published/web English Kural wording was imported.

Durable Part 001 controls:

- `reviews/PART_001_ENGLISH_REVIEW.md`
- `reviews/PART_001_ENGLISH_RELEASE_REPORT.md`

The **111→112** external split boundary was deliberately left unresolved until Part 002 became available.

## Current frontier

Part 002 has now been supplied as `TVA_BOK_0065733_குறளோவியம்_part_002_pages_112-222.pdf` and covers overall scans **112–222**.

The standard Part 002 working cadence is **11 physical scans per iteration**. The first source-first iteration is **112–122**, beginning with an explicit 111→112 boundary check.

See `TRANSLATION_STATUS.md` for the authoritative English frontier.