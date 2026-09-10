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

## Workflow

**Tamil archival-ready → English draft → English source-check → glossary reconciliation → editorial review → Part-level review → release report → release-ready.**

The user-directed normal iteration size is **33 physical scan pages** for page-batched work. Historical completed batches retain their recorded sizes; a final remainder may be shorter. Part-level review and release report are whole-Part gates.

## Part 001 — CLOSED

Part 001 English is closed at **107 `release-ready` + 4 `source-limited`**; source-limited scans are **13, 14, 15, 19**.

## Part 002 — TAMIL + ENGLISH CLOSED

Part 002 covers scans **112–222 / printed 95–205**, 111 physical pages.

- Tamil: **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**;
- English first-pass drafting: **111/111 COMPLETE**;
- source-check: **111/111 COMPLETE / CLOSED**;
- glossary reconciliation: **111/111 COMPLETE / CLOSED**;
- editorial review: **111/111 COMPLETE / CLOSED**;
- Part-level review: **PASS / CLOSED**;
- release report: **APPROVED / CLOSED**;
- release-ready: **111/111 COMPLETE / CLOSED**.

Durable Part-level records:

- `reviews/PART_002_ENGLISH_REVIEW.md`
- `reviews/PART_002_ENGLISH_RELEASE_REPORT.md`

No Tamil archival record changed and no publisher/standard/web English wording was imported. The previously deferred **222→223** boundary was subsequently resolved as **CLEAN** during Part 003 source intake.

## Part 003 Tamil — ARCHIVAL-READY / CLOSED

Part 003 covers scans **223–333 / printed 206–316**, 111 physical pages. Tamil is closed at **111 textual verified + 111 visual verified / 0 exceptions**.

Durable Tamil closure: `../../PART_003_TAMIL_ARCHIVAL_READY.md`.

Incoming **222→223 is CLEAN**. Internal **332→333** is a genuine continuation closed within Part 003. External **333→334** remains deferred until Part 004 source intake.

## Part 003 English — FIRST-PASS DRAFTING ACTIVE

- Draft Batch D1: **scans 223–255 / printed 206–238 — COMPLETE 33/33**;
- Draft Batch D2: **scans 256–288 / printed 239–271 — COMPLETE 33/33**;
- Draft Batch D3: **scans 289–321 / printed 272–304 — COMPLETE 33/33**;
- cumulative English drafting: **99/111**;
- completed-range state: **99 `draft` / 0 source-limited / 0 blocked**;
- remaining undrafted pages: **12**;
- source-check / glossary reconciliation / editorial review / Part review / release: **not-started**.

D1–D3 preserve page alignment, visual-material descriptions, Kural block separation and source-supported cross-page continuities. No Tamil archival record changed. D3 preserved the genuine incoming **288→289** continuation and closes at a **CLEAN 321→322** boundary.

## Current frontier

Exact next activity: **Part 003 English first-pass Draft Batch D4 / final remainder — scans 322–333 / printed 305–316, 12 pages**.

Keep each newly created record at `status: "draft"` with `source_tamil_status: "verified"`. Preserve the genuine **332→333** continuation. Do not infer external **333→334**; that remains deferred until Part 004 source intake.

If D4 closes, first-pass drafting becomes **111/111 COMPLETE** and the next gate is **Part 003 English source-check**, starting with scans **223–255 / printed 206–238** at the current 33-page cadence.

Part 004 remains blocked until the Part-003 maintained English workflow and final Part closure checkpoint are complete.

See `TRANSLATION_STATUS.md` for the authoritative detailed frontier.