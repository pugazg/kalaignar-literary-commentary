# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each. Repository `scan_page` always follows the overall **1–666** sequence and never restarts per split.

| Part | Overall scans | Current archival state |
|---|---:|---|
| 001 | 1–111 | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **Tamil ARCHIVAL-READY / CLOSED; English first-pass COMPLETE 111/111; source-check COMPLETE 111/111; glossary reconciliation COMPLETE 111/111; editorial review COMPLETE 111/111; Part-level review READY / NEXT** |
| 003 | 223–333 | not-started |
| 004 | 334–444 | not-started |
| 005 | 445–555 | not-started |
| 006 | 556–666 | not-started |

Permanent workflow policy: [`../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md`](../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md).

Mandatory per-part cadence:

source intake → Pass 1 → Pass 2A → Pass 2B → Pass 3 → Part audit → final metadata/status sync → documentation sync → Tamil archival-ready → English project-translation/review closure → final Part checkpoint → next supplied Part.

For active English page-batched iterations, the user-directed normal batch size is **33 physical pages**. Historical completed batches retain their original sizes; a final remainder may be shorter. Part-level review is a whole-Part gate.

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
- Part-level review: **READY / NEXT**;
- release-ready: **0/111**.

Editorial review is closed across ER1–ER4. The final ER4 remainder, scans **211–222 / printed 194–205**, passed **12/12** and promoted all remaining pages to `editorial-reviewed`.

ER4 made source-faithful wording improvements on scans **211, 212, 215, 218, 219, 220, 221 and 222**. The **210→211** boundary remains clean; all final-range source continuities remain intact, including genuine **221→222**, and scan **222 / printed 205** closes the pastoral/ஆயர்குடி vignette and Part 002.

No Tamil page record changed and no external/published/web English wording was imported.

## Current frontier

**Next activity: Part 002 Part-level English review across scans 112–222 as one completed Part.**

Create `translations/en/reviews/PART_002_ENGLISH_REVIEW.md`, following the Part 001 review precedent. Verify one-to-one page inventory/alignment, exact final statuses, controlled terminology/names, chapter/Kural metadata, page functions and non-body material, and accumulated continuities. Do not promote pages to `release-ready` during this gate.

If the Part-level review passes, the next gate is the **Part 002 English release report**. Do not begin Part 003 before Part 002 release and final Part closure are complete.
