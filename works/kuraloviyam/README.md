# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each. Repository `scan_page` always follows the overall **1–666** sequence and never restarts per split.

| Part | Overall scans | Current archival state |
|---|---:|---|
| 001 | 1–111 | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **source intake complete; Pass 1 COMPLETE 111/111; Pass 2A COMPLETE 111/111; Pass 2B COMPLETE 111/111; Pass 3 ACTIVE 62/111** |
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

### Pass 1 — COMPLETE

All **111 / 111** Part 002 physical scans are represented by page-aligned Tamil records, overall scans **112–222 / printed 95–205**. All remain `status: "needs-review"` / `visual_fidelity: "needs-review"` until later verification gates close.

### Pass 2A — COMPLETE

Pass 2A completed in 11 source-verification batches covering all **111/111** scans, overall **112–222 / printed 95–205**. Full scan-by-scan correction history is maintained in `PASS2_TEXTUAL_VERIFICATION_PART_002.md`.

### Pass 2B — COMPLETE

Pass 2B completed an independent fresh-source lexical reread across all **111/111** Part 002 scans. Full results are maintained in `PASS2B_LEXICAL_FIDELITY_PART_002.md`. Pass 2B completion is **not** final verification; all Part 002 records remain `needs-review` / `visual_fidelity: needs-review` until Pass 3, the Part audit and final synchronization close.

### Pass 3 — ACTIVE

Batch 1, scans **112–121 / printed 95–104**, COMPLETE 10/10. Structural-only corrections: **112, 114, 116, 117, 119, 120, 121**. No Tamil lexical wording changed.

Batch 2, scans **122–131 / printed 105–114**, COMPLETE 10/10. Structural-only corrections: **124, 126, 128, 130**. No Tamil lexical wording changed.

Batch 3, scans **132–141 / printed 115–124**, COMPLETE 10/10. Structural-only corrections: **132, 134, 136, 138, 140**. No Tamil lexical wording changed.

Batch 4, scans **142–152 / printed 125–135**, COMPLETE 11/11. Structural-only corrections: **142, 144, 145, 146, 147, 148, 149, 150, 151, 152**. Illustrated openings restore illustration-before-prose order; highlighted Kural blocks and scan 149 lower monument are structurally separated. No Tamil lexical wording changed.

Batch 5, scans **153–163 / printed 136–146**, COMPLETE 11/11. Structural-only corrections: **153, 154, 155, 156, 158, 160, 162**. Illustrated pages restore illustration-before-prose order; scan 155 separates its lower monument; scan 160's visual description was corrected to the source-visible fallen-warrior/jackal elephant scene. No Tamil lexical wording changed.

Batch 6, scans **164–173 / printed 147–156**, COMPLETE 10/10. Structural-only corrections: **164, 166, 168, 170, 171, 172**. Illustrated openings **164, 166, 168, 170, 172** now restore illustration-before-prose order; scan **171** separately represents the small centred Valluvar-monument illustration below Kural 580 / Chapter 58 metadata. Scans **165, 167, 169, 173** required no page-record correction. **No Tamil lexical wording changed in Pass 3 Batch 6.**

Pass 3 coverage: **62 / 111 scans**, overall scans **112–173 / printed 95–156**. Remaining Pass 3: **49 scans**.

Full Pass 3 results are maintained in `PASS3_VISUAL_TEXT_VERIFICATION_PART_002.md`.

All Part 002 records intentionally remain `status: "needs-review"` / `visual_fidelity: "needs-review"` until the later Part audit and final metadata/status synchronization.

## Current frontier

Exact next activity: **Part 002 Pass 3 meaningful visual-text verification — Batch 7, overall scans 174–183 / printed pages 157–166**.

Pass 3 must directly verify headings/hierarchy, quoted-Kural lineation and block placement, paragraph/quotation relationships, page furniture, illustration/text relationships, non-body stamps/marks and physical continuations against freshly rendered source scans. Page records should be rewritten only for directly source-supported structural corrections; otherwise record the no-change result in the Pass 3 control log.

Do not normalize source wording, do not substitute standard/published/web Kural text, and do not begin Part 003 before Part 002 is fully closed.