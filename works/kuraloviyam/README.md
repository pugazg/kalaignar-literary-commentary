# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each. Repository `scan_page` always follows the overall **1–666** sequence and never restarts per split.

| Part | Overall scans | Current archival state |
|---|---:|---|
| 001 | 1–111 | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **source intake COMPLETE; Pass 1 COMPLETE; Pass 2A COMPLETE; Pass 2B COMPLETE; Pass 3 COMPLETE 111/111; Part audit PASS; final metadata/status sync NEXT** |
| 003 | 223–333 | not-started |
| 004 | 334–444 | not-started |
| 005 | 445–555 | not-started |
| 006 | 556–666 | not-started |

Permanent workflow policy: [`../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md`](../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md).

Mandatory per-part cadence:

source intake → Pass 1 → Pass 2A → Pass 2B → Pass 3 → Part audit → final metadata/status sync → documentation sync → Tamil archival-ready → English project-translation/review closure → final Part checkpoint → next supplied Part.

## Part 001 — CLOSED

Tamil scans **1–111** are archival-ready: **107 `verified` + 4 `partial`**; visual fidelity **111/111 verified**. English Part 001 is closed: **107 `release-ready` + 4 `source-limited`**; limited scans are **13, 14, 15, 19**.

Durable English release report:

`works/kuraloviyam/translations/en/reviews/PART_001_ENGLISH_RELEASE_REPORT.md`

## Part 002 — ACTIVE

Controlling source:

`TVA_BOK_0065733_குறளோவியம்_part_002_pages_112-222.pdf`

Source identity:

- local pages: **111**;
- overall scans: **112–222**;
- printed pages: **95–205**;
- file size: **93,279,161 bytes**;
- SHA-256: `4397caf9ba405ba65f50865c85e24461ea56bd2efa3dd589d31469877c9a4bda`;
- no usable parsed text layer; rendered source pages control.

Durable controls:

- `works/kuraloviyam/SOURCE_INTAKE_PART_002.md`
- `works/kuraloviyam/PART_002_PASS1_PROGRESS.md`
- `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_002.md`
- `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_002.md`
- `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_002.md`
- `works/kuraloviyam/PART_002_AUDIT.md`
- `works/kuraloviyam/indexes/page-map.md`

### Completed gates

- source intake — **COMPLETE**;
- Pass 1 — **COMPLETE, 111/111**;
- Pass 2A direct textual verification — **COMPLETE, 111/111**;
- Pass 2B independent lexical-fidelity reread — **COMPLETE, 111/111**;
- Pass 3 meaningful visual-text verification — **COMPLETE, 111/111**, overall scans **112–222 / printed 95–205**;
- Part audit — **PASS**.

Detailed scan-by-scan Pass 2A, Pass 2B and Pass 3 histories remain in their dedicated control logs and are authoritative for corrections made during those gates.

### Part audit — PASS

`PART_002_AUDIT.md` records the full-Part closure audit across **111/111 scans**.

The audit confirms:

- continuous physical coverage **112–222 / local 1–111 / printed 95–205**;
- one durable page-aligned record per physical scan as recorded by the Pass 1 and page-map controls;
- all source-verification gates through Pass 3 closed **111/111**;
- illustration-only continuations **176→177→178** and **202→203→204** remain coherent;
- **221→222** is a genuine continuation and scan **222 / printed 205** is the supplied Part 002 endpoint;
- identified library stamps remain separated from body text, including scans **117–118** and **217–218**;
- no carried blocked/source-limited/partial Tamil condition requires an audit HOLD.

The audit made **no Tamil body-text changes** and **no page-status promotions**.

### Status discipline

All Part 002 records intentionally remain `status: "needs-review"` / `visual_fidelity: "needs-review"` after the audit. The audit authorizes the next gate, but final status promotion is performed only by the separate **final metadata/status synchronization**.

## Current frontier

**Next activity: Part 002 final metadata/status synchronization across all 111 records, scans 112–222 / printed 95–205.**

This gate must synchronize final textual and visual status metadata from the completed source intake, Pass 1, Pass 2A, Pass 2B, Pass 3 and Part-audit evidence without changing Tamil body wording.

Do not declare Part 002 Tamil archival-ready until final status synchronization and the subsequent documentation synchronization close. Do not start Part 003 before Part 002 is fully closed.
