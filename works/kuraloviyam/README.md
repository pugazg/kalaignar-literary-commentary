# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each. Repository `scan_page` always follows the overall **1–666** sequence and never restarts per split.

| Part | Overall scans | Current archival state |
|---|---:|---|
| 001 | 1–111 | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **source intake complete; Pass 1 COMPLETE 111/111; Pass 2A COMPLETE 111/111; Pass 2B NEXT** |
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
- `works/kuraloviyam/indexes/page-map.md`

### Pass 1 — COMPLETE

All **111 / 111** Part 002 physical scans are represented by page-aligned Tamil records, overall scans **112–222 / printed 95–205**. All remain `status: "needs-review"` / `visual_fidelity: "needs-review"` until later verification gates close.

### Pass 2A — COMPLETE

Completed source-verification batches:

| Batch | Overall scans | Printed pages | State |
|---:|---:|---:|---|
| 1 | 112–121 | 95–104 | COMPLETE |
| 2 | 122–131 | 105–114 | COMPLETE |
| 3 | 132–141 | 115–124 | COMPLETE |
| 4 | 142–152 | 125–135 | COMPLETE |
| 5 | 153–163 | 136–146 | COMPLETE |
| 6 | 164–173 | 147–156 | COMPLETE |
| 7 | 174–183 | 157–166 | COMPLETE |
| 8 | 184–194 | 167–177 | COMPLETE |
| 9 | 195–204 | 178–187 | COMPLETE |
| 10 | 205–214 | 188–197 | COMPLETE |
| 11 | 215–222 | 198–205 | COMPLETE |

Pass 2A coverage: **111 / 111 scans**, overall scans **112–222 / printed 95–205**. Remaining Pass 2A: **0**.

Batch 10 directly verified scans **205–214**. Source-supported corrections were required on scans **206, 207, 208, 209, 210, 211, 213, 214**; scans **205 and 212** required no textual correction. Important restorations include `காதலுற்று`, `தணியாமல்`, `கணக்குப் பார்ப்பதும்`, `பயன்படாத நாட்களேயாகும்`, `போய்விட்டீர்கள்`, `அவனைத் தேடித்தான்`, `முத்து விரிசைகள்`, `கவலையைப்`, `காதலனின்`, and `மாரியெனப்`.

Batch 11 directly verified scans **215–222** and completed Pass 2A. Source-supported corrections were required on scans **215, 216, 217, 218, 219, 220, 222**; scan **221** required no textual correction. Important restorations include `தழையாகிச்`, `அக்கணமில்லை`, `நம் காளை சுழல்காற்றாய்ப்`, `என்னத்தான்`, `அதைச் சமைத்தேன்`, `காரிருள்`, `சாவுக்கு விடை கொடுத்தனுப்பி`, `எழுத்தாணியைக்`, `கொலு மண்டபத்தில்`, `பத்தாண்டுகட்கு`, `தலைமையேற்றபோது`, `இளமைக் காலந்தொட்டு`, `அவர் தான்மட்டும்`, and `மகிழ்ச்சியடைகிறான்`. Scan **218** carries a blue circular library stamp; **221→222** is a genuine continuation; scan **222 / printed 205** closes the pastoral / ஆயர்குடி vignette and is the final physical scan of Part 002.

Full scan-by-scan correction history is maintained in `PASS2_TEXTUAL_VERIFICATION_PART_002.md`.

Pass 2A is **not** final verification. All Part 002 records remain `needs-review` / `visual_fidelity: needs-review`. Final `verified` is unavailable until Pass 2B, Pass 3, the Part audit and final synchronization close.

## Current frontier

Exact next activity: **Part 002 Pass 2B independent lexical-fidelity re-read — overall scans 112–121 / printed pages 95–104**.

Pass 2B must be an independent source re-read rather than a mechanical confirmation of Pass 2A. Re-render/read the controlling scans directly and compare every source-visible word, punctuation mark, paragraph/quotation boundary, Kural lineation and printed `அதிகாரம்` / பாடல் metadata. Record and correct only newly source-supported discrepancies.

Do not normalize source wording, do not substitute standard/published/web Kural text, and do not begin Part 003 before Part 002 is fully closed.
