# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each. Repository `scan_page` always follows the overall **1–666** sequence and never restarts per split.

| Part | Overall scans | Current archival state |
|---|---:|---|
| 001 | 1–111 | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **verification COMPLETE 111/111; Part audit PASS; final status sync PASS 111/111 verified; documentation sync COMPLETE; Tamil archival-ready checkpoint NEXT** |
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
- `works/kuraloviyam/PART_002_FINAL_STATUS_SYNC.md`
- `works/kuraloviyam/indexes/page-map.md`

### Completed gates

- source intake — **COMPLETE**;
- Pass 1 — **COMPLETE, 111/111**;
- Pass 2A direct textual verification — **COMPLETE, 111/111**;
- Pass 2B independent lexical-fidelity reread — **COMPLETE, 111/111**;
- Pass 3 meaningful visual-text verification — **COMPLETE, 111/111**, overall scans **112–222 / printed 95–205**;
- Part audit — **PASS**;
- final metadata/status synchronization — **PASS / CLOSED**;
- documentation synchronization — **COMPLETE**.

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

The audit made **no Tamil body-text changes** and deliberately made **no page-status promotions**.

### Final metadata/status synchronization — PASS

`PART_002_FINAL_STATUS_SYNC.md` records the dedicated post-audit status gate.

Final Part 002 status distribution:

- textual `status: "verified"` — **111/111**;
- textual `partial` / source-limited — **0**;
- textual `needs-review` — **0**;
- `visual_fidelity: "verified"` — **111/111**;
- visual `needs-review` — **0**.

The metadata-only comparison from audit checkpoint `6266ee60a27f2310d4a2e3e83779d0b987352eb8` to page-status endpoint `90d1b43acb01b876a1b269605079f437d5f87b53` contains exactly the **111 Part 002 page records**, each with **2 additions + 2 deletions** for the two final status fields. No Tamil body wording, page type, visual structure, source-continuation note or non-body stamp treatment changed during this gate.

### Documentation synchronization — COMPLETE

The Part 002 status result is now synchronized in:

- this README;
- `HANDOVER.md`;
- `indexes/page-map.md`;
- root `NEXT_CHAT_PROMPT_KURALOVIYAM.md`.

This documentation synchronization does not itself reopen or modify the audited Tamil page layer.

## Current frontier

**Next activity: Part 002 Tamil archival-ready checkpoint.**

The checkpoint must confirm that source intake, Pass 1, Pass 2A, Pass 2B, Pass 3, Part audit, final metadata/status synchronization and documentation synchronization are all closed; verify the final **111 verified / 111 visual-verified / 0 exceptions** disposition; record the Tamil archival-ready declaration durably; and identify the maintained Part 002 English workflow as the subsequent content stage.

Do not begin Part 003 before Part 002 completes its required Tamil and maintained English closure workflow.
