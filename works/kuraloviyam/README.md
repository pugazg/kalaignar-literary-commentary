# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each. Repository `scan_page` always follows the overall **1–666** sequence and never restarts per split.

| Part | Overall scans | Current archival state |
|---|---:|---|
| 001 | 1–111 | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **source intake COMPLETE; Pass 1 COMPLETE; Pass 2A COMPLETE; Pass 2B COMPLETE; Pass 3 COMPLETE 111/111; Part audit NEXT** |
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
- `works/kuraloviyam/indexes/page-map.md`

### Completed gates

- source intake — **COMPLETE**;
- Pass 1 — **COMPLETE, 111/111**;
- Pass 2A direct textual verification — **COMPLETE, 111/111**;
- Pass 2B independent lexical-fidelity reread — **COMPLETE, 111/111**;
- Pass 3 meaningful visual-text verification — **COMPLETE, 111/111**, overall scans **112–222 / printed 95–205**.

Detailed scan-by-scan Pass 2A, Pass 2B and Pass 3 histories remain in their dedicated control logs and are authoritative for corrections made during those gates.

### Pass 3 final batch closure

Final Batch 11, scans **215–222 / printed 198–205**, closed **8/8** by direct comparison with freshly rendered source scans.

All eight page records received source-supported **structural-only** corrections:

- illustrated openings **215, 217, 219, 221** now restore physical illustration-before-prose order;
- text-only conclusions **216, 218, 220, 222** now preserve source-highlighted Kural blocks as distinct two-line blocks;
- scans **217–218** preserve the blue circular library stamp as non-body material;
- **221→222** remains a genuine physical continuation;
- scan **222 / printed 205** is the final physical scan of Part 002.

**No Tamil lexical wording changed during Pass 3 Batch 11.**

### Status discipline

All Part 002 records intentionally remain `status: "needs-review"` / `visual_fidelity: "needs-review"` even though Pass 3 is complete. Final `verified` status is not authorized until the **Part audit** and **final metadata/status synchronization** close.

## Current frontier

**Next activity: Part 002 Part audit.**

The audit must verify complete physical coverage, internal continuity, source limits, page-map/record consistency, non-body source marks, and the supplied Part boundary across scans **112–222 / printed 95–205**. Do not change Tamil wording during the audit unless a new direct source discrepancy is genuinely discovered.

Do not start final metadata/status synchronization until the Part audit passes. Do not start Part 003 before Part 002 is fully closed.
