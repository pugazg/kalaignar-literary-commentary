# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each.

| Part | Overall scans | Supplied state | Current archival state |
|---|---:|---|---|
| 001 | 1–111 | supplied | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **supplied** — `TVA_BOK_0065733_குறளோவியம்_part_002_pages_112-222.pdf` | **intake complete; Pass 1 112–122 complete (11/111)** |
| 003 | 223–333 | not yet supplied | not-started |
| 004 | 334–444 | not yet supplied | not-started |
| 005 | 445–555 | not yet supplied | not-started |
| 006 | 556–666 | not yet supplied | not-started |

Repository `scan_page` always follows the **overall 1–666 sequence** and never restarts per split.

Use [`../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md`](../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md) for permanent policy.

## Mandatory per-part closure cadence

source intake → Pass 1 → Pass 2A → Pass 2B → Pass 3 → Part audit → final metadata/status sync → documentation sync → Tamil archival-ready → English project-translation/review closure → final Part checkpoint → next supplied Part.

Closed Parts should not routinely require their earlier PDF again; reopen an older split only for a newly discovered source/provenance problem.

# Part 001 — CLOSED

Tamil scans **1–111** are archival-ready: source intake and Passes 1/2A/2B/3 complete; Part audit and final status sync PASS; **107 `verified` + 4 `partial`**; partial scans **13, 14, 15, 19**; visual fidelity **111/111 verified**.

English Part 001 is also closed:

- drafting, source-check, glossary reconciliation and editorial review: **111/111 complete**;
- Part-level English review: **PASS**;
- release report: **APPROVED WITH EXPLICIT SOURCE LIMITATIONS**;
- final English statuses: **107 `release-ready` + 4 `source-limited`**;
- source-limited scans remain **13, 14, 15, 19**;
- no missing wording was reconstructed;
- no English body text changed during the release gate.

Durable release report:

`works/kuraloviyam/translations/en/reviews/PART_001_ENGLISH_RELEASE_REPORT.md`

# Part 002 — ACTIVE

Controlling source:

`TVA_BOK_0065733_குறளோவியம்_part_002_pages_112-222.pdf`

Source intake is **COMPLETE**:

- local pages: **111**;
- overall scans: **112–222**;
- file size: **93,279,161 bytes**;
- SHA-256: `4397caf9ba405ba65f50865c85e24461ea56bd2efa3dd589d31469877c9a4bda`;
- no usable parsed text layer; rendered source pages are controlling;
- scan **112 / printed 95** is local page 1.

Durable intake record:

`works/kuraloviyam/SOURCE_INTAKE_PART_002.md`

## Resolved split boundary

The old **111→112** open check is now resolved from the real Part 002 source:

- scan 111 closes the learned-speaker / `சொல்வன்மை` vignette;
- scan 112 starts a new illustrated love vignette;
- therefore the split is a **clean vignette boundary**.

## Standard iteration size

Part 002 uses **11 physical scans per iteration** as the standard cadence.

Planned batches:

- P2-01: **112–122** — COMPLETE
- P2-02: **123–133** — NEXT
- P2-03: **134–144**
- P2-04: **145–155**
- P2-05: **156–166**
- P2-06: **167–177**
- P2-07: **178–188**
- P2-08: **189–199**
- P2-09: **200–210**
- P2-10: **211–221**
- final remainder: **222**

Do not allow the 11-page work cadence to create artificial textual or narrative boundaries; page continuations must follow the source.

## P2-01 / Pass 1 result

**COMPLETE — scans 112–122 / printed pages 95–105.**

- 11 page-aligned Tamil records created under `works/kuraloviyam/pages/`;
- all remain `status: "needs-review"` and `visual_fidelity: "needs-review"` as required for Pass 1;
- Kural/chapter metadata captured from the source-visible edition only;
- scan 118's blue circular library stamp is recorded as non-body material;
- scan 123 / printed 106 was inspected only as a boundary witness;
- **122→123 is a real narrative continuation** of the merchant/rest-house vignette.

## Current frontier

Exact next activity: **P2-02 / Part 002 Pass 1, overall scans 123–133**.

Begin from the already confirmed continuation at scan 123. Process exactly 11 scans and inspect scan 134 only when needed as the closing boundary witness. Do not reconstruct uncertain text from OCR, context, another edition, standard Kural wording, web material or memory.
