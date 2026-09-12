# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each. Repository `scan_page` always follows the overall **1–666** sequence and never restarts per split.

| Part | Overall scans | Current archival state |
|---|---:|---|
| 001 | 1–111 | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **Tamil ARCHIVAL-READY / CLOSED; English RELEASE COMPLETE / CLOSED — 111/111 release-ready** |
| 003 | 223–333 | **Tamil + English CLOSED — final Part checkpoint PASS / CLOSED; 111/111 English release-ready** |
| 004 | 334–444 | **Tamil ARCHIVAL-READY / CLOSED; English editorial review COMPLETE / CLOSED 111/111; Part-level English review next** |
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

## Part 003 — TAMIL + ENGLISH CLOSED

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

The **222→223** boundary is resolved as **clean**. The adjacent **333→334** boundary is now also **CLEAN / source-resolved** from the supplied Part 004 source.

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

**COMPLETE — 111 / 111 scans directly textually verified against rendered source scans, overall scans 223–333 / printed 206–316.**

User-directed Pass-2A cadence was **11 physical scans per normal iteration**, with a one-scan final remainder.

- **Batch 1: scans 223–233 / printed 206–216 — COMPLETE 11/11**; 8 records corrected, 3 no-change; **233→234 genuine** reconfirmed.
- **Batch 2: scans 234–244 / printed 217–227 — COMPLETE 11/11**; 9 records corrected, scans **239** and **241** no-change; **244→245 CLEAN** confirmed from scan 245 witness.
- **Batch 3: scans 245–255 / printed 228–238 — COMPLETE 11/11**; 10 records corrected, scan **254** no-change; **255→256 CLEAN** confirmed from scan 256 witness.
- **Batch 4: scans 256–266 / printed 239–249 — COMPLETE 11/11**; 7 records corrected, scans **256, 258, 264, 266** no-change; **266→267 genuine continuation** reconfirmed from scan 267 witness.
- **Batch 5: scans 267–277 / printed 250–260 — COMPLETE 11/11**; 6 records corrected, scans **268, 270, 272, 274, 276** no-change; **277→278 CLEAN** reconfirmed from scan 278 witness.
- **Batch 6: scans 278–288 / printed 261–271 — COMPLETE 11/11**; 5 records corrected, scans **278, 280, 282, 284, 286, 288** no-change; **288→289 genuine continuation** reconfirmed from scan 289 witness.
- **Batch 7: scans 289–299 / printed 272–282 — COMPLETE 11/11**; 6 records corrected, scans **290, 292, 294, 296, 298** no-change; **299→300 CLEAN** reconfirmed from scan 300 witness.
- **Batch 8: scans 300–310 / printed 283–293 — COMPLETE 11/11**; 5 records corrected, scans **301, 302, 304, 305, 306, 307** no-change; **310→311 CLEAN** reconfirmed from scan 311 witness.
- **Batch 9: scans 311–321 / printed 294–304 — COMPLETE 11/11**; 7 records corrected, scans **311, 313, 315, 319** no-change; **321→322 CLEAN** reconfirmed from scan 322 witness.
- **Batch 10: scans 322–332 / printed 305–315 — COMPLETE 11/11**; 8 records corrected, scans **324, 328, 330** no-change; genuine **332→333 continuation** reconfirmed from scan 333 witness.
- **Final remainder: scan 333 / printed 316 — COMPLETE 1/1**; Pass-2A corrections were subsequently independently rechecked during Pass 2B; Chapter 57 / Kural 567 and Part-ending continuation remain directly confirmed.

Pass-2A closure: **111 / 111 COMPLETE through scan 333 / printed 316**. The internal **332→333 genuine continuation** is closed. External **333→334 remains deferred** until Part 004 intake.

Durable Pass-2A record: `PASS2_TEXTUAL_VERIFICATION_PART_003.md`.

### Part 003 Pass 2B state

**COMPLETE — 111 / 111 independently re-read through scan 333 / printed 316.** Pass 2B followed the Part-002 independent lexical-fidelity precedent and used freshly rendered scans as authority.

- **Batch 1: 223–232 — COMPLETE 10/10**; corrections on **223, 226**.
- **Batch 2: 233–242 — COMPLETE 10/10**; corrections on **235, 236**.
- **Batch 3: 243–252 — COMPLETE 10/10**; corrections on **249, 250, 251, 252**.
- **Batch 4: 253–262 — COMPLETE 10/10**; corrections on **253, 261**.
- **Batch 5: 263–272 — COMPLETE 10/10**; correction on **264**.
- **Batch 6: 273–282 — COMPLETE 10/10**; correction on **281**.
- **Batch 7: 283–292 — COMPLETE 10/10**; corrections on **285, 287, 288, 291**.
- **Batch 8: 293–302 — COMPLETE 10/10**; corrections on **293, 294, 295, 299, 302**.
- **Batch 9: 303–312 — COMPLETE 10/10**; corrections on **304, 305**.
- **Batch 10: 313–322 — COMPLETE 10/10**; corrections on **314, 316, 320, 322**.
- **Batch 11: 323–332 — COMPLETE 10/10**; correction on **326**.
- **Final remainder: scan 333 / printed 316 — COMPLETE 1/1**; restored source-visible `இறுதியான` → `இறுதி யான` and `தலைமை ஏற்று` → `தலைமைபெற்று`; Kural 567 lineation and Chapter 57 metadata reconfirmed.

Internal **332→333 genuine continuation is closed**. External **333→334 remains deferred** until Part 004 intake.

Those records intentionally remained `needs-review` / `visual_fidelity: needs-review` through Pass 2B and the later Pass 3/audit gates; after the audit PASS, the dedicated final metadata/status synchronization promoted all 111 records to textual and visual `verified` without changing Tamil wording or structure.

Durable Pass-2B record: `PASS2B_LEXICAL_FIDELITY_PART_003.md`. Supplemental late-batch record: `PASS2B_BATCH_010_011_CLOSURE.md`.

### Part 003 Pass 3 state

**COMPLETE — 111 / 111 meaningful visual-text verification scans through scan 333 / printed 316.** User-directed cadence was **11 physical scans per normal iteration**, with a one-scan final remainder.

- **Batch 1: scans 223–233 / printed 206–216 — COMPLETE 11/11**; structural/visual-description correction on **scan 223 only**; scans **224–233** no structural change; **233→234 genuine continuation** reconfirmed from scan 234 witness.
- **Batch 2: scans 234–244 / printed 217–227 — COMPLETE 11/11**; **no structural corrections**; scans **234–244** all no-change; **244→245 CLEAN** reconfirmed from scan 245 witness.
- **Batch 3: scans 245–255 / printed 228–238 — COMPLETE 11/11**; **no structural corrections**; scans **245–255** all no-change; **255→256 CLEAN** reconfirmed from scan 256 witness.
- **Batch 4: scans 256–266 / printed 239–249 — COMPLETE 11/11**; structural/visual-description correction on **scan 260 only**; scans **256–259, 261–266** no structural change; **266→267 genuine continuation** reconfirmed from scan 267 witness.
- **Batch 5: scans 267–277 / printed 250–260 — COMPLETE 11/11**; structural/visual-description corrections on **scans 267, 274, 277**; scans **268–273, 275–276** no structural change; **277→278 CLEAN** reconfirmed from scan 278 witness.
- **Batch 6: scans 278–288 / printed 261–271 — COMPLETE 11/11**; **no structural corrections**; scans **278–288** all no-change; **288→289 genuine continuation** reconfirmed from scan 289 witness.
- **Batch 7: scans 289–299 / printed 272–282 — COMPLETE 11/11**; structural correction on **scan 292 only** to preserve the source-displayed altered three-line Kural as a distinct set-out block; scans **289–291, 293–299** no structural change; **299→300 CLEAN** reconfirmed from scan 300 witness.
- **Batch 8: scans 300–310 / printed 283–293 — COMPLETE 11/11**; structural/visual-description corrections on **scans 302, 303**; scans **300–301, 304–310** no structural change; **310→311 CLEAN** reconfirmed from scan 311 witness.
- **Batch 9: scans 311–321 / printed 294–304 — COMPLETE 11/11**; structural/visual-description correction on **scan 311 only**; scans **312–321** no structural change; **321→322 CLEAN** reconfirmed from scan 322 witness.
- **Batch 10: scans 322–332 / printed 305–315 — COMPLETE 11/11**; structural/visual-description corrections on **scans 330 and 332**; scans **322–329, 331** no structural change; **332→333 genuine continuation** reconfirmed from scan 333 witness.
- **Final remainder: scan 333 / printed 316 — COMPLETE 1/1**; structural correction preserves highlighted Kural 567 as a distinct two-line set-out block and records side vertical title/footer furniture separately; lexical wording unchanged.
- Lexical body-text changes during Pass 3: **0**.
- Status promotions during Pass 3: **0**.

Durable Pass-3 record: `PASS3_VISUAL_TEXT_VERIFICATION_PART_003.md`. Supplemental Batch-9 record: `PASS3_BATCH_009.md`.

### Part 003 audit state

**PASS — all 111 records / scans 223–333 / printed 206–316.**

The audit confirms complete physical coverage and mapping, closed source intake / Pass 1 / Pass 2A / Pass 2B / Pass 3 gates, coherent internal continuations, preserved Kural/visual structure, correct non-body separation and **0 carried partial / blocked / source-limited Tamil exceptions**. No page record or Tamil body wording was changed during the audit, and no status was promoted.

Durable audit record: `PART_003_AUDIT.md`.

### Part 003 final metadata/status synchronization

**PASS / CLOSED — all 111 records / scans 223–333 / printed 206–316 are now `status: "verified"` and `visual_fidelity: "verified"`.**

The metadata-only change set was audited from `56cbca5a1eaf85f37d764969f36fb3b856061033` to clean endpoint `d76ac41ab64e01ded549942530f96e0b8db801d1`: exactly **111 Part-003 page files** changed, each with **2 additions / 2 deletions**, and no non-page file remained changed. Tamil body wording, Kural text/lineation, structure, visual notes, source comments and mapping were unchanged.

Durable final-status record: `PART_003_FINAL_STATUS_SYNC.md`.

### Part 003 documentation synchronization

**COMPLETE.** The live overview, handovers, page map, archival guideline, next-chat prompt, source metadata and transcription policy are synchronized to the closed Part-003 audit and final-status state. Historical phase statements are retained as history; the live state is **111 textual verified + 111 visual verified / 0 partial / 0 source-limited / 0 needs-review / 0 unresolved status exceptions**.

Durable documentation-sync record: `PART_003_DOCUMENTATION_SYNC.md`.

## Part 004 — TAMIL CLOSED / ENGLISH RELEASE APPROVED

- drafting — **COMPLETE / CLOSED 111/111**;
- source-check — **COMPLETE / CLOSED 111/111**;
- glossary reconciliation — **COMPLETE / CLOSED 111/111**;
- editorial review — **COMPLETE / CLOSED 111/111**;
- Part-level English review — **PASS / CLOSED**;
- English release — **APPROVED / CLOSED**;
- durable review — `translations/en/reviews/PART_004_ENGLISH_REVIEW.md`;
- durable release report — `translations/en/reviews/PART_004_ENGLISH_RELEASE_REPORT.md`;
- current page status — **111 release-ready / 0 editorial-reviewed**;
- release promotion change set — **111 English page files only, +1/-1 each, status-token-only**;
- English wording changes — **0**;
- Tamil changes — **0**;
- **333→334 CLEAN**, **366→367 genuine continuation**, **399→400 CLEAN**, **432→433 CLEAN**, **443→444 CLEAN** preserved;
- scan **444 / printed 427 remains source-open**;
- external **444→445 DEFERRED / UNRESOLVED**.

## Current frontier

**Final Part 004 closure checkpoint/documentation confirmation — NEXT.**
