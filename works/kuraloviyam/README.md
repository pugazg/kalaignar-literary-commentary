# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each. Repository `scan_page` always follows the overall **1–666** sequence and never restarts per split.

| Part | Overall scans | Current archival state |
|---|---:|---|
| 001 | 1–111 | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **Tamil ARCHIVAL-READY / CLOSED; English RELEASE COMPLETE / CLOSED — 111/111 release-ready** |
| 003 | 223–333 | **source intake + Pass 1 COMPLETE — 111/111; Pass 2A ACTIVE — 55/111 verified** |
| 004 | 334–444 | not-started |
| 005 | 445–555 | not-started |
| 006 | 556–666 | not-started |

Permanent workflow policy: [`../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md`](../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md).

Mandatory per-part cadence:

source intake → Pass 1 → Pass 2A → Pass 2B → Pass 3 → Part audit → final metadata/status sync → documentation sync → Tamil archival-ready → English project-translation/review closure → final Part checkpoint → next supplied Part.

## Part 001 — CLOSED

Tamil scans **1–111** are archival-ready. English is closed at **107 release-ready + 4 source-limited**.

## Part 002 — TAMIL + ENGLISH CLOSED

Controlling source: `TVA_BOK_0065733_குறளோவியம்_part_002_pages_112-222.pdf` — **111 physical pages; scans 112–222; printed 95–205; SHA-256 `4397caf9ba405ba65f50865c85e24461ea56bd2efa3dd589d31469877c9a4bda`.**

Tamil is **ARCHIVAL-READY / CLOSED** at **111 textual verified + 111 visual verified / 0 exceptions**.

Maintained English is **RELEASE COMPLETE / CLOSED — 111/111 `release-ready`**. Durable review and release records are under `translations/en/reviews/`.

## Part 003 — SOURCE INTAKE + PASS 1 COMPLETE / PASS 2A ACTIVE

Controlling source:

`TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf`

Confirmed intake identity:

- **111 physical pages**;
- overall scans **223–333**;
- printed pages **206–316**;
- **93,488,924 bytes**;
- SHA-256 `f07e7cdb3a6e786b0378e00bbe699a241be41c9e099c004a4faa90fa82b4239f`;
- no usable parsed text layer; rendered scan images are controlling.

Durable intake record: `SOURCE_INTAKE_PART_003.md`.

The **222→223** boundary is resolved as **clean**. The external **333→334** boundary remains deferred until Part 004 is supplied.

### Part 003 Pass 1 state

**COMPLETE — 111 / 111 scans captured, overall scans 223–333 / printed 206–316.** All records remain `needs-review` / `visual_fidelity: needs-review`; Pass 1 capture does not make them source-verified.

Completed capture:

- **P3-01: scans 223–233 / printed 206–216 — COMPLETE 11/11**;
- **P3-02: scans 234–244 / printed 217–227 — COMPLETE 11/11**;
- **P3-03: scans 245–255 / printed 228–238 — COMPLETE 11/11**;
- **P3-04: scans 256–266 / printed 239–249 — COMPLETE 11/11**;
- **P3-05: scans 267–277 / printed 250–260 — COMPLETE 11/11**;
- **P3-06: scans 278–288 / printed 261–271 — COMPLETE 11/11**;
- **P3-07: scans 289–299 / printed 272–282 — COMPLETE 11/11**;
- **P3-08: scans 300–310 / printed 283–293 — COMPLETE 11/11**;
- **P3-09: scans 311–321 / printed 294–304 — COMPLETE 11/11**;
- **P3-10: scans 322–332 / printed 305–315 — COMPLETE 11/11**;
- **final remainder: scan 333 / printed 316 — COMPLETE 1/1**.

Final Pass-1 source unit:

- scan **332 / printed 315** begins the severe-rule / famine vignette;
- scan **333 / printed 316** directly continues and closes it with Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567;
- **332→333 is a genuine continuation**;
- external **333→334 remains deferred** until Part 004 intake.

Boundary state through the Part 003 Pass-1 close: **233→234 genuine; 244→245 clean; 255→256 clean; 266→267 genuine; 277→278 clean; 288→289 genuine; 299→300 clean; 310→311 clean; 321→322 clean; 323→324 clean; 325→326 clean; 327→328 clean; 329→330 clean; 331→332 clean; 332→333 genuine**.

Durable Pass-1 record: `PART_003_PASS1_PROGRESS.md`.

### Part 003 Pass 2A state

User-directed Pass-2A cadence: **11 physical scans per normal iteration**, with a shorter final remainder if necessary.

- **Batch 1: scans 223–233 / printed 206–216 — COMPLETE 11/11**; 8 records corrected, 3 no-change; **233→234 genuine** reconfirmed.
- **Batch 2: scans 234–244 / printed 217–227 — COMPLETE 11/11**; 9 records corrected, scans **239** and **241** no-change; **244→245 CLEAN** confirmed from scan 245 witness.
- **Batch 3: scans 245–255 / printed 228–238 — COMPLETE 11/11**; 10 records corrected, scan **254** no-change; **255→256 CLEAN** confirmed from scan 256 witness.
- **Batch 4: scans 256–266 / printed 239–249 — COMPLETE 11/11**; 7 records corrected, scans **256, 258, 264, 266** no-change; **266→267 genuine continuation** reconfirmed from scan 267 witness.
- **Batch 5: scans 267–277 / printed 250–260 — COMPLETE 11/11**; 6 records corrected, scans **268, 270, 272, 274, 276** no-change; **277→278 CLEAN** reconfirmed from scan 278 witness.

Representative Batch-5 source readings restored include `தொடமுடியாமல்`, `உச்சிமுதல்`, `இடித்துரைத்துக்`, `கூடிமகிழும் நிலையில்`, the source comma in `அதாவது,`, the missing `என்பது`, plus printed quotation punctuation around Kurals 1220, 155, 1327, 133, 1267 and 476.

Current Pass-2A frontier: **55 / 111 scans verified through scan 277 / printed 260**. All records remain `needs-review` / `visual_fidelity: needs-review`; later Pass 2B, Pass 3, audit and final synchronization are still required before textual/visual `verified` status.

Durable Pass-2A record: `PASS2_TEXTUAL_VERIFICATION_PART_003.md`.

## Current frontier

**Next activity: Part 003 Pass 2A / Batch 6 — scans 278–288 / printed 261–271, 11 direct textual-verification scans.** Begin after the confirmed clean **277→278** boundary. Inspect scan **289 / printed 272** only as a continuity/boundary witness when necessary; Pass-1 mapping records **288→289 as a genuine continuation**. Compare source-visible wording, punctuation, paragraph/quotation boundaries, Kural wording/lineation and printed `அதிகாரம்` / பாடல் metadata directly against rendered scans. Keep records at `needs-review` / `visual_fidelity: needs-review`; do not normalize or import standard Kural wording.