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

## Part 003 English — FIRST-PASS DRAFTING COMPLETE

- Draft Batch D1: **scans 223–255 / printed 206–238 — COMPLETE 33/33**;
- Draft Batch D2: **scans 256–288 / printed 239–271 — COMPLETE 33/33**;
- Draft Batch D3: **scans 289–321 / printed 272–304 — COMPLETE 33/33**;
- Draft Batch D4: **scans 322–333 / printed 305–316 — COMPLETE 12/12 / FINAL REMAINDER**;
- cumulative English drafting: **111/111 COMPLETE**;
- post-drafting state: **111 `draft` / 0 source-limited / 0 blocked**;
- source-check: **111/111 COMPLETE / CLOSED**;
- current English state: **111 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;
- glossary reconciliation: **IN PROGRESS — GR1 COMPLETE 33/111**;
- editorial review / Part review / release: **not-started**.

All 111 English pages preserve page alignment, visual/non-body descriptions, Kural block separation and source-supported cross-page continuities. The known **332→333** continuation is preserved and closed within Part 003. No Tamil archival record changed.

## Part 003 English source-check — COMPLETE / CLOSED

- SC1 **223–255 / 206–238 — COMPLETE 33/33**;
- SC2 **256–288 / 239–271 — COMPLETE 33/33**;
- SC3 **289–321 / 272–304 — COMPLETE 33/33**;
- SC4 **322–333 / 305–316 — COMPLETE 12/12 / FINAL REMAINDER**;
- cumulative source-check: **111/111 COMPLETE / CLOSED**;
- current English state: **111 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.

SC4 source-fidelity reconciliation corrected the Monday-market sense on scan **327**, restored exact page alignment across **328→329**, and recorded scan **333** side title/footer furniture as non-body material. No Tamil archival record changed. Incoming **321→322 is CLEAN**; genuine **332→333** remains preserved and closes within Part 003.

SC4 page commit: `e07a6775513bcf1619e5d1bcb6e8222f7004f0a8`.

## Part 003 English glossary reconciliation — IN PROGRESS

- GR1 **223–255 / 206–238 — COMPLETE / PASS 33/33**;
- cumulative glossary reconciliation: **33/111**;
- English pages remain **111 `source-checked`**; GR1 made **0 page wording changes and 0 status changes**.

GR1 added the Part-003-first chapter controls **Folly**, **Forbearance**, **Women of Mercenary Love**, **Hospitality**, **Abstaining from Liquor**, and **Agriculture**; mapped source variant `நலம்புனைந்துரைத்தல்` to existing **Praising Her Beauty**; and refined `ஊடல்` contextually as **lovers' quarrel / sulking**. No Tamil archival record changed.

## Current frontier

Exact next activity: **Part 003 English glossary reconciliation GR2 — scans 256–288 / printed 239–271, 33 pages**.

Use `GLOSSARY.md` and audited Tamil context to reconcile recurring names, literary/structural terms, publication names, chapter labels, citation metadata and repeated English renderings. Add glossary entries only when evidenced in the active source. This gate does **not** promote pages to `editorial-reviewed`; pages remain `source-checked` until editorial review.

If GR2 passes, cumulative glossary reconciliation becomes **66/111**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.

See `TRANSLATION_STATUS.md` for the authoritative detailed frontier.
