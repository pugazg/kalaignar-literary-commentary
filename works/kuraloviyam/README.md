# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each. Repository `scan_page` always follows the overall **1–666** sequence and never restarts per split.

| Part | Overall scans | Current archival state |
|---|---:|---|
| 001 | 1–111 | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **Tamil ARCHIVAL-READY / CLOSED; English first-pass, source-check, glossary reconciliation and editorial review COMPLETE 111/111; Part-level English review PASS; release report READY / NEXT** |
| 003 | 223–333 | not-started |
| 004 | 334–444 | not-started |
| 005 | 445–555 | not-started |
| 006 | 556–666 | not-started |

Permanent workflow policy: [`../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md`](../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md).

Mandatory per-part cadence:

source intake → Pass 1 → Pass 2A → Pass 2B → Pass 3 → Part audit → final metadata/status sync → documentation sync → Tamil archival-ready → English project-translation/review closure → final Part checkpoint → next supplied Part.

For active English page-batched iterations, the user-directed normal batch size is **33 physical pages**. Historical completed batches retain their original sizes; a final remainder may be shorter. Part-level review and release report are whole-Part gates.

## Part 001 — CLOSED

Tamil scans **1–111** are archival-ready. English is closed at **107 release-ready + 4 source-limited**.

## Part 002 — TAMIL CLOSED / ENGLISH ACTIVE

Controlling source: `TVA_BOK_0065733_குறளோவியம்_part_002_pages_112-222.pdf` — **111 physical pages; scans 112–222; printed 95–205; SHA-256 `4397caf9ba405ba65f50865c85e24461ea56bd2efa3dd589d31469877c9a4bda`.**

Tamil is **ARCHIVAL-READY / CLOSED** at **111 textual verified + 111 visual verified / 0 exceptions**.

## Maintained English workflow

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

- first-pass drafting: **111/111 COMPLETE**;
- source-check: **111/111 COMPLETE / CLOSED**;
- glossary reconciliation: **111/111 COMPLETE / CLOSED**;
- editorial review: **111/111 COMPLETE / CLOSED**;
- Part-level review: **PASS / CLOSED**;
- release report: **READY / NEXT**;
- release-ready: **0/111**.

Durable Part-level review: `translations/en/reviews/PART_002_ENGLISH_REVIEW.md`.

The whole-Part review passed one-to-one Tamil/English inventory and filename alignment, exact pre-release statuses, controlled terminology/names, chapter/Kural metadata, visual/non-body functions and continuity through final **221→222**. No English page wording or status changed at that gate.

The internal Part ending at scan **222** is closed. The external **222→223** boundary remains explicitly deferred until Part 003 source intake; no unsupported boundary is inferred.

No Tamil page record changed and no external/published/web English wording was imported.

## Current frontier

**Next activity: Part 002 English release report.**

Create `translations/en/reviews/PART_002_ENGLISH_RELEASE_REPORT.md`, following the Part 001 release-report precedent. Use the Part 002 review PASS as the authoritative prior gate. If release is approved, promote all **111** Part 002 English pages from `editorial-reviewed` to `release-ready` without wording changes.

Do not begin Part 003 before the Part 002 release report, page-status promotion and final Part closure are complete.
