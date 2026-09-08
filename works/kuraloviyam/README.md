# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each. Repository `scan_page` always follows the overall **1–666** sequence and never restarts per split.

| Part | Overall scans | Current archival state |
|---|---:|---|
| 001 | 1–111 | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **Tamil ARCHIVAL-READY / CLOSED; English first-pass COMPLETE 111/111; source-check ACTIVE 15/111** |
| 003 | 223–333 | not-started |
| 004 | 334–444 | not-started |
| 005 | 445–555 | not-started |
| 006 | 556–666 | not-started |

Permanent workflow policy: [`../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md`](../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md).

Mandatory per-part cadence:

source intake → Pass 1 → Pass 2A → Pass 2B → Pass 3 → Part audit → final metadata/status sync → documentation sync → Tamil archival-ready → English project-translation/review closure → final Part checkpoint → next supplied Part.

## Part 001 — CLOSED

Tamil scans **1–111** are archival-ready: **107 `verified` + 4 `partial`**; visual fidelity **111/111 verified**. English Part 001 is closed: **107 `release-ready` + 4 `source-limited`**; limited scans are **13, 14, 15, 19**.

## Part 002 — TAMIL CLOSED / ENGLISH ACTIVE

Controlling source: `TVA_BOK_0065733_குறளோவியம்_part_002_pages_112-222.pdf`.

Source identity: **111 physical pages; overall scans 112–222; printed pages 95–205; SHA-256 `4397caf9ba405ba65f50865c85e24461ea56bd2efa3dd589d31469877c9a4bda`.**

Part 002 Tamil is **ARCHIVAL-READY / CLOSED** at **111 textual verified + 111 visual verified / 0 exceptions**. Durable declaration: `works/kuraloviyam/PART_002_TAMIL_ARCHIVAL_READY.md`.

## Maintained English workflow

Normal translation/review work uses the audited Tamil page records under `works/kuraloviyam/pages/`.

Permanent cadence:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

Part 002 first-pass drafting is **COMPLETE: 111/111**.

Part 002 source-check is **ACTIVE: 15/111 complete**.

Completed source-check:

- **SC1: scans 112–126 / printed 95–109 — 15/15 source-checked.**

SC1 compared each English record against the audited Tamil layer paragraph-by-paragraph / block-by-block and preserved the clean **111→112** boundary. Scan **127** was used only as a continuation witness for scan 126 and remains `draft` for SC2. A single fidelity correction was required on **scan 125 / Kural 1291**, where the unsupported draft words “and his love” were removed before promotion.

No Tamil page record was changed during English source-check, and no published/standard/web English Kural wording was imported.

English controls:

- `works/kuraloviyam/translations/en/README.md`
- `works/kuraloviyam/translations/en/TRANSLATION_GUIDE.md`
- `works/kuraloviyam/translations/en/GLOSSARY.md`
- `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`

## Current frontier

**Next activity: Part 002 English source-check SC2 — scans 127–141 / printed 110–124, 15 records.**

Scan 127 directly continues and closes the Gandhi vignette from source-checked scan 126. Compare each English page against its audited Tamil record paragraph-by-paragraph / block-by-block. Check omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual function and continuation relationships. Only passing records may move from `draft` to `source-checked`. Do not begin glossary reconciliation until source-check covers all 111 Part 002 records. Do not begin Part 003 before Part 002 English review/release and final Part closure are complete.