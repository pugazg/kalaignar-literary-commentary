# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each. Repository `scan_page` always follows the overall **1–666** sequence and never restarts per split.

| Part | Overall scans | Current archival state |
|---|---:|---|
| 001 | 1–111 | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **Tamil ARCHIVAL-READY / CLOSED; English RELEASE COMPLETE / CLOSED — 111/111 release-ready** |
| 003 | 223–333 | **source intake PASS / COMPLETE; Tamil Pass 1 ACTIVE — 11/111 captured** |
| 004 | 334–444 | not-started |
| 005 | 445–555 | not-started |
| 006 | 556–666 | not-started |

Permanent workflow policy: [`../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md`](../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md).

Mandatory per-part cadence:

source intake → Pass 1 → Pass 2A → Pass 2B → Pass 3 → Part audit → final metadata/status sync → documentation sync → Tamil archival-ready → English project-translation/review closure → final Part checkpoint → next supplied Part.

Current user-directed Part 003 Pass 1 page-batched iteration size is **11 physical pages**. Historical completed batches retain their original sizes; a final remainder may be shorter. Workflow boundaries never create artificial source boundaries.

## Part 001 — CLOSED

Tamil scans **1–111** are archival-ready. English is closed at **107 release-ready + 4 source-limited**.

## Part 002 — TAMIL + ENGLISH CLOSED

Controlling source: `TVA_BOK_0065733_குறளோவியம்_part_002_pages_112-222.pdf` — **111 physical pages; scans 112–222; printed 95–205; SHA-256 `4397caf9ba405ba65f50865c85e24461ea56bd2efa3dd589d31469877c9a4bda`.**

Tamil is **ARCHIVAL-READY / CLOSED** at **111 textual verified + 111 visual verified / 0 exceptions**.

Maintained English is **RELEASE COMPLETE / CLOSED — 111/111 `release-ready`**. Durable review and release records are under `translations/en/reviews/`.

## Part 003 — SOURCE INTAKE COMPLETE / TAMIL ACTIVE

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

The previously deferred **222→223** boundary is resolved as **clean**: scan 222 closes the pastoral / `ஆயர்குடி` vignette with Chapter 128 / Kural 1275, while scan 223 / printed 206 begins a new illustrated `பேதைமை` vignette. Scan 224 / printed 207 closes that new unit with Chapter 84 / Kurals 838, 839.

At the far end, scan **333 / printed 316** closes the final visible Part 003 unit with Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567. The external **333→334** boundary remains deferred until Part 004 is supplied.

### Part 003 Pass 1 state

**P3-01 scans 223–233 / printed 206–216 — COMPLETE, 11/11.** All records remain `needs-review` / `visual_fidelity: needs-review` as required for Pass 1.

Captured units:

- 223–224 — `பேதைமை`; Chapter 84 / Kurals 838, 839;
- 225–226 — `தும்மல்` / lovers; Chapters 121, 132, 126 / Kurals 1203, 1318, 1253;
- 227–228 — Valluvar / land / patience and slander; Chapter 16 / Kural 151 and Chapter 19 / Kural 189;
- 229–230 — Maragatham / medicine / love-sickness; Chapter 125 / Kural 1241;
- 231–232 — courtesan / `வரைவின் மகளிர்`; Chapter 92 / Kural 913;
- 233 — festival / green-sari vignette begins and continues directly to scan 234.

**233→234 is a genuine continuation.** Scan 234 / printed 217 was inspected only as the next-batch boundary witness.

### Remaining 11-page Pass 1 cadence

- P3-02: **234–244 / printed 217–227**;
- P3-03: **245–255 / printed 228–238**;
- P3-04: **256–266 / printed 239–249**;
- P3-05: **267–277 / printed 250–260**;
- P3-06: **278–288 / printed 261–271**;
- P3-07: **289–299 / printed 272–282**;
- P3-08: **300–310 / printed 283–293**;
- P3-09: **311–321 / printed 294–304**;
- P3-10: **322–332 / printed 305–315**;
- final remainder: **333 / printed 316**.

Durable progress record: `PART_003_PASS1_PROGRESS.md`.

## Current frontier

**Next activity: Part 003 Pass 1 / P3-02 — scans 234–244 / printed 217–227, 11 page-aligned Tamil records.** Begin by preserving the genuine **233→234** continuation. Use scan 245 / printed 228 only as a boundary witness when needed. Pass 1 records remain `needs-review` / `visual_fidelity: needs-review`; do not normalize or import standard Kural wording.
