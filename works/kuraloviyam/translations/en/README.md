# Kuraloviyam — English project translation

This directory contains the **project-created English translation layer** for the audited Tamil archive of Kalaignar M. Karunanidhi's `குறளோவியம்`.

This is **not** an official or publisher-issued English edition.

Every English page declares:

```yaml
translation_type: "project_translation"
```

## Authority

Normal translation/review work uses the audited Tamil page records under `../../pages/`. The original Tamil scan remains the ultimate source authority if a new provenance or fidelity problem is discovered, but a closed Tamil Part is not routinely reopened.

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
```

English pages mirror the Tamil filenames exactly.

## Workflow

**Tamil archival-ready → English draft → English source-check → glossary reconciliation → editorial review → Part-level review → release report → release-ready.**

Tamil verification status and English review status are separate.

## Part 001 — CLOSED

Part 001 Tamil / scans **1–111**: **ARCHIVAL-READY / CLOSED**.

Part 001 English is closed at **107 `release-ready` + 4 `source-limited`**; source-limited scans are **13, 14, 15, 19**.

Durable Part 001 controls:

- `reviews/PART_001_ENGLISH_REVIEW.md`
- `reviews/PART_001_ENGLISH_RELEASE_REPORT.md`

## Part 002 Tamil — ARCHIVAL-READY / CLOSED

Part 002 covers overall scans **112–222 / printed 95–205**, 111 physical pages. The Tamil layer is closed at **111 textual verified + 111 visual verified**, with zero exceptions.

Durable declaration:

`../../PART_002_TAMIL_ARCHIVAL_READY.md`

## Part 002 English — ACTIVE

First-pass drafting status: **111/111 COMPLETE**.

Source-check status: **15/111 complete**.

Completed source-check:

- **SC1: scans 112–126 / printed 95–109 — 15/15 source-checked.**

SC1 preserved the clean **111→112** Part boundary and all source-supported visual and continuation relationships. Scan 127 was inspected only as the continuation witness for scan 126 and remains `draft` for SC2. One fidelity correction was made on scan **125 / Kural 1291**, removing the unsupported draft addition “and his love” before promotion to `source-checked`.

No published/standard/web English Kural wording has been imported, and the closed Tamil layer has not been changed during English review.

## Current frontier

Proceed with **Part 002 English source-check SC2: scans 127–141 / printed 110–124**, 15 consecutive records.

Compare English against the audited Tamil page-by-page and block-by-block for omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual function and continuity. Only passing pages may move from `draft` to `source-checked`. Do not begin glossary reconciliation until source-check covers all 111 records.

See `TRANSLATION_STATUS.md` for the authoritative detailed frontier.