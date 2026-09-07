# English Translation Status — Kuraloviyam

## Translation identity

- type: **project-created English translation**
- official/publisher English source supplied: **no**
- working basis: audited Tamil archival records under `works/kuraloviyam/pages/`
- original Tamil scan: ultimate source authority only if a genuinely new provenance/fidelity issue requires reopening it

## English workflow

Permanent cadence:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**

`source-limited` is retained wherever the audited Tamil source itself is incomplete.

## Part 001 — CLOSED

Tamil scans **1–111** are archival-ready: **107 verified + 4 partial**, visual **111/111 verified**.

English gates are all closed:

- first-pass drafting: **111/111 COMPLETE**;
- source-check SC1–SC8: **111/111 COMPLETE**;
- glossary reconciliation GR1–GR8: **111/111 COMPLETE**;
- editorial review ER1–ER8: **111/111 COMPLETE**;
- Part-level English review: **PASS**;
- release report: **APPROVED WITH EXPLICIT SOURCE LIMITATIONS**;
- final English: **107 release-ready + 4 source-limited** — scans **13, 14, 15, 19**.

Durable reviews:

- `reviews/PART_001_ENGLISH_REVIEW.md`
- `reviews/PART_001_ENGLISH_RELEASE_REPORT.md`

## Part 002 Tamil readiness — CLOSED

Controlling Tamil source identity:

- source: `TVA_BOK_0065733_குறளோவியம்_part_002_pages_112-222.pdf`;
- overall scans: **112–222**;
- printed pages: **95–205**;
- physical/local pages: **111 / 1–111**;
- SHA-256: `4397caf9ba405ba65f50865c85e24461ea56bd2efa3dd589d31469877c9a4bda`.

Tamil gates:

- source intake — **COMPLETE**;
- Pass 1 — **COMPLETE 111/111**;
- Pass 2A — **COMPLETE 111/111**;
- Pass 2B — **COMPLETE 111/111**;
- Pass 3 — **COMPLETE 111/111**;
- Part audit — **PASS**;
- final status sync — **PASS / CLOSED**;
- documentation sync — **COMPLETE**;
- Tamil archival-ready checkpoint — **PASS / CLOSED**.

Final Part 002 Tamil state:

- textual verified: **111**;
- partial/source-limited: **0**;
- needs-review: **0**;
- visual verified: **111**;
- visual needs-review: **0**.

Durable Tamil declaration: `../../PART_002_TAMIL_ARCHIVAL_READY.md`.

The **111→112** split boundary is already resolved by the closed Tamil archival workflow. Do not repeat source intake or Tamil verification simply because English drafting is underway.

## Part 002 English gates

- first-pass drafting: **11/111 — ACTIVE**;
- source-check: **0/111**;
- glossary reconciliation: **0/111**;
- editorial review: **0/111**;
- Part-level English review: not started;
- release report: not started;
- release-ready: **0/111**.

### First-pass drafting batches

- **Batch 1: scans 112–122 / printed 95–105 — COMPLETE, 11/11 draft records.**

Batch 1 preserves the audited Tamil page alignment, visual-material placement, Kural block lineation, Chapter/Kural metadata and cross-page continuations. No published/standard/web English Kural wording was imported, and no Tamil archival record was changed.

Notable batch boundaries retained:

- 112→113 love / lovers' quarrel vignette;
- 114→115 sculptor/painter vignette;
- 117→118 Valluvar/student/hunter/deer continuation;
- 119→120 husband/wife continuation;
- 121→122 merchant/rest-house continuation, which continues beyond the batch to scan 123.

## Current frontier

Proceed with **Part 002 English first-pass draft Batch 2: overall scans 123–133 / printed 106–116**, 11 records.

Requirements:

1. translate only from the audited Tamil page records;
2. mirror filenames exactly under `pages/`;
3. use `translation_type: "project_translation"` and `status: "draft"`;
4. preserve source-supported Kural/chapter, visual and continuation relationships;
5. do not import published/standard/web English Kural wording;
6. do not change Tamil archival records;
7. update this status and audit the exact changed-file set after the batch.

Next draft batch after Batch 2: **134–144 / printed 117–127**, 11 records.

Part 003 remains blocked until Part 002 English workflow and final Part closure are complete.
