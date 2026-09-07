# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each. Repository `scan_page` always follows the overall **1–666** sequence and never restarts per split.

| Part | Overall scans | Current archival state |
|---|---:|---|
| 001 | 1–111 | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **Tamil ARCHIVAL-READY / CLOSED; English drafting ACTIVE 11/111** |
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

## Part 002 — TAMIL CLOSED / ENGLISH ACTIVE

Controlling source:

`TVA_BOK_0065733_குறளோவியம்_part_002_pages_112-222.pdf`

Source identity:

- local pages: **111**;
- overall scans: **112–222**;
- printed pages: **95–205**;
- file size: **93,279,161 bytes**;
- SHA-256: `4397caf9ba405ba65f50865c85e24461ea56bd2efa3dd589d31469877c9a4bda`;
- no usable parsed text layer; rendered source pages remain ultimate source authority if a genuinely new provenance/fidelity issue appears.

Durable Tamil controls:

- `works/kuraloviyam/SOURCE_INTAKE_PART_002.md`
- `works/kuraloviyam/PART_002_PASS1_PROGRESS.md`
- `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_002.md`
- `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_002.md`
- `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_002.md`
- `works/kuraloviyam/PART_002_AUDIT.md`
- `works/kuraloviyam/PART_002_FINAL_STATUS_SYNC.md`
- `works/kuraloviyam/PART_002_TAMIL_ARCHIVAL_READY.md`
- `works/kuraloviyam/indexes/page-map.md`

### Closed Tamil gates

- source intake — **COMPLETE**;
- Pass 1 — **COMPLETE, 111/111**;
- Pass 2A direct textual verification — **COMPLETE, 111/111**;
- Pass 2B independent lexical-fidelity reread — **COMPLETE, 111/111**;
- Pass 3 meaningful visual-text verification — **COMPLETE, 111/111**, overall scans **112–222 / printed 95–205**;
- Part audit — **PASS**;
- final metadata/status synchronization — **PASS / CLOSED**;
- documentation synchronization — **COMPLETE**;
- Tamil archival-ready checkpoint — **PASS / CLOSED**.

Final Part 002 Tamil distribution:

- textual `status: "verified"` — **111/111**;
- textual `partial` / source-limited — **0**;
- textual `needs-review` — **0**;
- `visual_fidelity: "verified"` — **111/111**;
- visual `needs-review` — **0**.

`PART_002_TAMIL_ARCHIVAL_READY.md` is the durable Tamil closure declaration. Part 002 Tamil should not normally be reopened; reopen source/Tamil only for a genuinely new provenance or fidelity problem.

## Maintained English workflow

Normal translation/review work uses the audited Tamil page records under `works/kuraloviyam/pages/`.

Permanent cadence:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

Part 002 first-pass drafting is now **ACTIVE: 11/111 complete**.

Completed:

- **Batch 1: scans 112–122 / printed pages 95–105 — 11/11 draft records.**

Batch 1 preserves page alignment, Kural blocks, Chapter/Kural metadata, visual-material placement and source continuations. The batch ends inside the merchant/rest-house vignette: scan **122 continues to 123**.

English controls:

- `works/kuraloviyam/translations/en/README.md`
- `works/kuraloviyam/translations/en/TRANSLATION_GUIDE.md`
- `works/kuraloviyam/translations/en/GLOSSARY.md`
- `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`

## Current frontier

**Next activity: Part 002 English first-pass draft Batch 2 — scans 123–133 / printed 106–116, 11 records.**

Do not begin source-check until first-pass drafting covers the full Part, and do not begin Part 003 before Part 002 English review/release and final Part closure are complete.
