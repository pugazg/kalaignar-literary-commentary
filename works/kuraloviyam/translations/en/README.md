# Kuraloviyam — English project translation

This directory contains the **project-created English translation layer** for the audited Tamil archive of Kalaignar M. Karunanidhi's `குறளோவியம்`.

This is **not** an official or publisher-issued English edition.

Every English page declares:

```yaml
translation_type: "project_translation"
```

## Authority

Normal translation/review work uses the audited Tamil page records under `../../pages/`. The original Tamil scan remains the ultimate source authority if a genuinely new provenance or fidelity problem is discovered, but a Tamil-closed Part is not routinely reopened.

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
- source-limited scans: **13, 14, 15, 19**.

Durable Part 001 controls:

- `reviews/PART_001_ENGLISH_REVIEW.md`
- `reviews/PART_001_ENGLISH_RELEASE_REPORT.md`

## Part 002 Tamil readiness

Part 002 / overall scans **112–222 / printed 95–205** is now **TAMIL ARCHIVAL-READY / CLOSED**.

- source intake / Pass 1 / Pass 2A / Pass 2B / Pass 3: complete **111/111**;
- Part audit: **PASS**;
- final status sync: **PASS / CLOSED**;
- documentation sync: **COMPLETE**;
- Tamil archival-ready checkpoint: **PASS / CLOSED**;
- Tamil status: **111 verified / 0 partial / 0 needs-review**;
- visual fidelity: **111 verified / 0 needs-review**.

Durable declaration: `../../PART_002_TAMIL_ARCHIVAL_READY.md`.

## Part 002 English frontier

Part 002 English has not started:

- draft: **0/111**;
- source-check: **0/111**;
- glossary reconciliation: **0/111**;
- editorial review: **0/111**;
- Part review: not started;
- release report: not started.

Standard drafting cadence is **11 physical/page-aligned records per iteration**.

### Exact next activity

Draft **overall scans 112–122 / printed pages 95–105**, 11 English records, from the audited Tamil page files.

Use `TRANSLATION_GUIDE.md`, `GLOSSARY.md` and `TRANSLATION_STATUS.md`. The original PDF is not a routine English drafting dependency; reopen source only if a genuinely new provenance/fidelity issue appears.

After Batch 1, the next draft batch is **123–133 / printed 106–116**.
