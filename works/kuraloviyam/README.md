# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை source-first முறையில் பக்கவாரியாகவும் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The complete source is reported as **666 physical PDF pages**, split into six Parts of 111 pages each. Repository `scan_page` always follows the overall **1–666** sequence and never restarts per split.

| Part | Overall scans | Current archival state |
|---|---:|---|
| 001 | 1–111 | **Tamil CLOSED; English CLOSED — 107 release-ready + 4 source-limited** |
| 002 | 112–222 | **Tamil ARCHIVAL-READY / CLOSED; English RELEASE COMPLETE / CLOSED — 111/111 release-ready** |
| 003 | 223–333 | **Tamil + English CLOSED — final Part checkpoint PASS / CLOSED; 111/111 English release-ready** |
| 004 | 334–444 | **Tamil + maintained English FULLY CLOSED — 111/111 release-ready English** |
| 005 | 445–555 | **Tamil + maintained English FULLY CLOSED — 111/111 release-ready English** |
| 006 | 556–666 | **Tamil ARCHIVAL-READY / CLOSED; English Draft D1 + D2 COMPLETE / PASS 74/74 — scans 556–629; Draft D3 next** |

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

## Part 004 — FULLY CLOSED

**FINAL CHECKPOINT: PASS / CLOSED.**

Tamil is **111/111 textual + visual verified / 0 exceptions**. Maintained English is **111/111 release-ready**.

## Part 005 — FULLY CLOSED

- source intake — **PASS / COMPLETE**;
- P5-01 — **445–455 / printed 428–438 — COMPLETE 11/11**;
- P5-02 — **456–466 / printed 439–449 — COMPLETE 11/11**;
- P5-03 — **467–477 / printed 450–460 — COMPLETE 11/11**;
- P5-04 — **478–488 / printed 461–471 — COMPLETE 11/11**;
- P5-05 — **489–499 / printed 472–482 — COMPLETE 11/11**;
- P5-06 — **500–510 / printed 483–493 — COMPLETE 11/11**;
- P5-07 — **511–521 / printed 494–504 — COMPLETE 11/11**;
- P5-08 — **522–532 / printed 505–515 — COMPLETE 11/11**;
- P5-09 — **533–543 / printed 516–526 — COMPLETE 11/11**;
- P5-10 / final remainder — **544–555 / printed 527–538 — COMPLETE 12/12**;
- cumulative Pass 1 — **111/111 COMPLETE**;
- current captured records — **111 needs-review / visual needs-review**;
- durable Pass-1 progress — `PART_005_PASS1_PROGRESS.md`;
- Pass 2A Batch 1 — **445–455 / printed 428–438 — COMPLETE 11/11**;
- Pass 2A Batch 2 — **456–466 / printed 439–449 — COMPLETE 11/11**;
- Pass 2A Batch 3 — **467–477 / printed 450–460 — COMPLETE 11/11**;
- Pass 2A Batch 4 — **478–488 / printed 461–471 — COMPLETE 11/11**;
- Pass 2A Batch 5 — **489–499 / printed 472–482 — COMPLETE 11/11**;
- Pass 2A Batch 6 — **500–510 / printed 483–493 — COMPLETE 11/11**;
- Pass 2A Batch 7 — **511–521 / printed 494–504 — COMPLETE 11/11**;
- Pass 2A Batch 8 — **522–532 / printed 505–515 — COMPLETE 11/11**;
- Pass 2A Batch 9 — **533–543 / printed 516–526 — COMPLETE 11/11**;
- Pass 2A Batch 10 / final remainder — **544–555 / printed 527–538 — COMPLETE 12/12**;
- cumulative Pass 2A — **111/111 COMPLETE / PASS**;
- Batch-3 corrections — **7 page records / 10 source-supported readings**;
- Batch-3 correction commit — `b6ce17d55759f05f80af760ac9d3d2cd0ec96bac`;
- Batch-4 corrections — **6 page records / 8 source-supported readings**;
- Batch-4 correction commit — `4902fd9fef350947103be839135a1c7d3a7c4d6e`;
- durable Pass-2A log — `PASS2_TEXTUAL_VERIFICATION_PART_005.md`;
- Batch-5 corrections — **3 page records / 4 source-supported readings**;
- Batch-5 correction commit — `5d9478576f4296e34338447145c518686cd925af`;
- Batch-6 corrections — **2 page records / 2 source-supported readings**;
- Batch-6 correction commit — `fe14f3a9e284bd91b03ddaa927eb4d4595e86d30`;
- Batch-7 corrections — **2 page records / 3 source-supported readings**;
- Batch-7 correction commit — `7c87cc0b41de0141062d1847fae8e8fc73fc40b1`;
- Batch-8 corrections — **9 page records / 18 source-supported readings**;
- Batch-8 correction commit — `ba6e0ba0b7b438476bbafb846212e05c080f6028`;
- Batch-9 corrections — **1 page record / 1 source-supported reading**;
- Batch-9 correction commit — `b3216bbb18464744a06e79232d973f46575c1145`;
- Batch-10 corrections — **6 page records / 15 textual-or-punctuation readings**;
- Batch-10 correction commit — `5be125724c549d4b1c82020ab5fb5bf0e01fc4b8`;
- Pass 2B Batch 1 — **445–455 / printed 428–438 — COMPLETE 11/11**;
- Pass 2B Batch 2 — **456–466 / printed 439–449 — COMPLETE 11/11**;
- Pass 2B Batch 3 — **467–477 / printed 450–460 — COMPLETE 11/11**;
- Pass 2B Batch 4 — **478–488 / printed 461–471 — COMPLETE 11/11**;
- Pass 2B Batch 5 — **489–499 / printed 472–482 — COMPLETE 11/11**;
- Pass 2B Batch 6 — **500–510 / printed 483–493 — COMPLETE 11/11**;
- Pass 2B Batch 7 — **511–521 / printed 494–504 — COMPLETE 11/11**;
- Pass 2B Batch 8 — **522–532 / printed 505–515 — COMPLETE 11/11**;
- Pass 2B Batch 9 — **533–543 / printed 516–526 — COMPLETE 11/11**;
- Pass 2B Batch 10 / final remainder — **544–555 / printed 527–538 — COMPLETE 12/12**;
- cumulative Pass 2B — **111/111 COMPLETE / PASS**;
- Batch-1 Pass-2B correction — **1 page record / 1 lexical reading**;
- Batch-1 Pass-2B correction commit — `8391075c43b72ec3e5973db080ba742e5e899c4b`;
- Pass 2B log — `PASS2B_LEXICAL_FIDELITY_PART_005.md`;
- **455→456 GENUINE CONTINUATION**;
- Batch-2 Pass-2B corrections — **3 page records / 4 lexical-or-spacing readings**;
- Batch-2 Pass-2B correction commit — `665a2691e0e1cdfcff740adb48a65783976b8adf`;
- **466→467 GENUINE CONTINUATION**;
- Batch-3 Pass-2B corrections — **2 page records / 2 source-visible joining readings**;
- Batch-3 Pass-2B correction commit — `c7228edbf258e2d15b3949df61fe364e9cada5e4`;
- **477→478 CLEAN**;
- Batch-4 Pass-2B corrections — **4 page records / 9 lexical-or-spacing/punctuation readings**;
- Batch-4 Pass-2B correction commit — `81456d09f7745a0834c3edc2170281945b91f478`;
- **488→489 CLEAN**;
- Batch-5 Pass-2B corrections — **5 page records / 9 lexical-or-spacing/punctuation readings**;
- Batch-5 Pass-2B correction commit — `2c0b3b4ddff95c18c9312dbdffbc4ef2d41c2767`;
- **499→500 GENUINE CONTINUATION**;
- Batch-6 Pass-2B corrections — **3 page records / 6 lexical-or-spacing readings**;
- Batch-6 Pass-2B correction commit — `2cdd3c70ef34e61496d51e7996a2ade8d039e433`;
- **510→511 CLEAN**;
- Batch-7 Pass-2B corrections — **3 page records / 7 lexical-or-spacing readings**;
- Batch-7 Pass-2B correction commit — `ff38ae5c02ec44026482f8db9702d76e8eb424b1`;
- **521→522 CLEAN**;
- Batch-8 Pass-2B corrections — **7 page records / 12 lexical-or-spacing/punctuation readings**;
- Batch-8 Pass-2B correction commit — `4af1b155dad0a81c5bd7fe68cd64569801a3718f`;
- **532→533 CLEAN**;
- Batch-9 Pass-2B corrections — **3 page records / 3 lexical-or-spacing readings**;
- Batch-9 Pass-2B correction commit — `909260dc502bb4ddeaa0defd5cb25692adf38653`;
- **543→544 GENUINE CONTINUATION**;
- Batch-10 Pass-2B corrections — **3 page records / 3 lexical-or-punctuation readings**;
- Batch-10 Pass-2B correction commit — `892d3273ddf04f6b1a0364d0b77e9e4eb58d0c93`;
- Pass 2B — **COMPLETE / PASS 111/111**;
- cumulative Pass-2B corrections — **34 page records / 56 source-supported readings**;
- **555→556 CLEAN** remains source-resolved;
- Pass 3 Batch 1 — **445–455 / printed 428–438 — COMPLETE 11/11**;
- Pass 3 Batch 2 — **456–466 / printed 439–449 — COMPLETE 11/11**;
- Pass 3 Batch 3 — **467–477 / printed 450–460 — COMPLETE 11/11**;
- Pass 3 Batch 4 — **478–489 / printed 461–472 — COMPLETE 12/12**;
- Pass 3 Batch 5 — **490–501 / printed 473–484 — COMPLETE 12/12**;
- Pass 3 Batch 6 — **502–526 / printed 485–509 — COMPLETE 25/25**;
- Pass 3 Batch 7 / final remainder — **527–555 / printed 510–538 — COMPLETE 29/29**;
- Pass 3 — **COMPLETE / PASS 111/111**;
- final-iteration user override — **all remaining 29 pages processed in one iteration**;
- Pass-3 structural/visual corrections — **6 pages / scans 472, 474, 481, 501, 531, 537**;
- Pass-3 lexical/body-text changes — **0**;
- Batch-7 Pass-3 page correction commit — `558256c0624f32b3aee9479aebb70a734eab3118`;
- **455→456 GENUINE CONTINUATION** preserved;
- **466→467 GENUINE CONTINUATION** preserved;
- **477→478 CLEAN** preserved;
- **489→490 GENUINE CONTINUATION** preserved;
- **501→502 GENUINE CONTINUATION** preserved;
- **526→527 CLEAN** preserved;
- **555→556 CLEAN / source-resolved** preserved;
- Part 005 audit — **PASS / COMPLETE**;
- audit coverage/mapping — **111/111 canonical records; 0 gaps / 0 duplicates / 0 anomalies**;
- final metadata/status synchronization — **PASS / CLOSED**;
- final textual status — **111/111 verified**;
- final visual fidelity — **111/111 verified**;
- final status exceptions — **0**;
- metadata-only promotion diff — **111 page files only / each +2,-2 / 0 non-page files**;
- documentation synchronization — **COMPLETE / PASS**;
- documentation-only sync page-record changes — **0**;
- durable documentation-sync record — `PART_005_DOCUMENTATION_SYNC.md`;
- Tamil archival-ready checkpoint — **PASS / CLOSED**;
- Tamil final state — **111/111 textual verified + 111/111 visual verified / 0 exceptions**;
- durable Tamil archival-ready record — `PART_005_TAMIL_ARCHIVAL_READY.md`;
- English Draft D1 — **445–477 / printed 428–460 — COMPLETE 33/33**;
- English Draft D2 — **478–510 / printed 461–493 — COMPLETE 33/33**;
- English Draft D3 — **511–543 / printed 494–526 — COMPLETE 33/33**;
- English Draft D4 final remainder — **544–555 / printed 527–538 — COMPLETE 12/12**;
- Part-005 English first-pass drafting — **COMPLETE / CLOSED 111/111**;
- English drafting — **COMPLETE / CLOSED 111/111**;
- English source-check SC1 — **445–477 / printed 428–460 — COMPLETE / PASS 33/33**;
- English source-check SC2 — **478–510 / printed 461–493 — COMPLETE / PASS 33/33**;
- English source-check SC3 — **511–543 / printed 494–526 — COMPLETE / PASS 33/33**;
- English source-check SC4 final remainder — **544–555 / printed 527–538 — COMPLETE / PASS 12/12**;
- English source-check — **COMPLETE / CLOSED 111/111**;
- English glossary reconciliation GR1 — **445–477 / printed 428–460 — COMPLETE / PASS 33/33**;
- English glossary reconciliation GR2 — **478–510 / printed 461–493 — COMPLETE / PASS 33/33**;
- English glossary reconciliation GR3 — **511–543 / printed 494–526 — COMPLETE / PASS 33/33**;
- English glossary reconciliation GR4 final remainder — **544–555 / printed 527–538 — COMPLETE / PASS 12/12**;
- cumulative glossary reconciliation — **111/111 COMPLETE / CLOSED**;
- GR1 exact change set — **GLOSSARY.md + English scan 445 only / 0 Tamil changes / 0 status changes**;
- GR2 exact change set — **GLOSSARY.md + English scans 479, 480, 494, 510 / 0 Tamil changes / 0 status changes**;
- GR3 exact change set — **GLOSSARY.md + English scans 519, 521, 532, 534, 540, 542 / 0 Tamil changes / 0 status changes**;
- GR4 exact change set — **GLOSSARY.md + English scans 551, 553, 554, 555 / 0 Tamil changes / 0 status changes**;
- English editorial review ER1 — **445–477 / printed 428–460 — COMPLETE / PASS 33/33**;
- ER1 exact change set — **33 English page files / 33 status promotions / 9 wording-refinement pages / 0 Tamil changes**;
- English editorial review ER2 — **478–510 / printed 461–493 — COMPLETE / PASS 33/33**;
- ER2 exact change set — **33 English page files / 33 status promotions / 12 wording-refinement pages / 0 Tamil changes**;
- English editorial review ER3 — **511–543 / printed 494–526 — COMPLETE / PASS 33/33**;
- ER3 exact change set — **33 English page files / 33 status promotions / 19 wording-refinement pages / 0 Tamil changes**;
- English editorial review ER4 — **544–555 / printed 527–538 — COMPLETE / PASS 12/12 / FINAL REMAINDER**;
- ER4 exact change set — **12 English page files / 12 status promotions / 6 wording-refinement pages / 0 Tamil changes**;
- English editorial review — **COMPLETE / CLOSED 111/111**;
- Part-level English review — **PASS / CLOSED**;
- review record — `translations/en/reviews/PART_005_ENGLISH_REVIEW.md`;
- review audit — **111/111 aligned English pages / 111 editorial-reviewed / 54 metadata pages / 55 Kural citations / 53 visual-material pages / 0 page-layer changes**;
- English release — **APPROVED / CLOSED — 111/111 release-ready**;
- release report — `translations/en/reviews/PART_005_ENGLISH_RELEASE_REPORT.md`;
- release promotion base — `af50dbf8b6ab54e456d87b10cfdcd094e6d3a516`;
- release promotion endpoint — `3d35d4c67f17f77b8ff5de036a8a3989ec088a78`;
- release promotion audit — **19 commits / exactly 111 English page files / +1,-1 each / 0 non-page files / status-token-only**;
- current English state — **0 source-checked / 0 draft / 0 editorial-reviewed / 111 release-ready / 0 source-limited / 0 blocked**;
- final Part-005 checkpoint — **PASS / CLOSED**;
- durable final closure — `PART_005_FINAL_CLOSURE.md`;
- Part 005 — **TAMIL + MAINTAINED ENGLISH FULLY CLOSED**.
- SC4 source-fidelity corrections — **4 pages / scans 549, 550, 553, 555**;
- SC4 page-layer audit — **12 modified English page records / 0 Tamil changes / 0 control-file changes**;
- **555→556 CLEAN**.

## Part 006 — TAMIL ARCHIVAL-READY / ENGLISH DRAFT NEXT

- source intake — **PASS / COMPLETE**;
- scans — **556–666**;
- source family physically complete — **YES**;
- Pass 1 — **COMPLETE 111/111**;
- P6-01 through P6-09 — **556–654 / printed 539–637 — COMPLETE**;
- P6-10 — **655–665 / printed 638–648 — COMPLETE 11/11**;
- final remainder — **666 / unnumbered pictorial back cover — COMPLETE 1/1**;
- final page endpoint — `6f58cc1c4a12bcf06776507a42a47225d782cc2b`;
- exact final Pass-1 compare from `0935e9380db4aa406793db9a5f261354831466c7` — **2 commits / exactly 12 newly added Part 006 Tamil page files / 0 non-page changes**;
- scans **658–665** — complete `பொருளடக்கம்` backmatter run;
- scan **666** — physical source endpoint / no external continuation;
- all **111** records remain `needs-review` / visual `needs-review`;
- Pass 2A Batch 1 — **556–566 / printed 539–549 — COMPLETE 11/11**;
- Pass 2A Batch 2 — **567–577 / printed 550–560 — COMPLETE 11/11**;
- Pass 2A Batch 3 — **578–588 / printed 561–571 — COMPLETE 11/11**;
- Pass 2A Batch 4 — **589–599 / printed 572–582 — COMPLETE 11/11**;
- Pass 2A Batch 5 — **600–610 / printed 583–593 — COMPLETE 11/11**;
- Pass 2A Batch 6 — **611–621 / printed 594–604 — COMPLETE 11/11**;
- Pass 2A Batch 7 — **622–632 / printed 605–615 — COMPLETE 11/11**;
- Pass 2A Batch 8 — **633–643 / printed 616–626 — COMPLETE 11/11**;
- Pass 2A Batch 9 — **644–654 / printed 627–637 — COMPLETE 11/11**;
- Pass 2A Batch 10 — **655–665 / printed 638–648 — COMPLETE 11/11**;
- final Pass-2A remainder — **666 / unnumbered pictorial back cover — COMPLETE 1/1 / no textual correction**;
- Batch 10 correction endpoint — `a88d9e186f5956b0fa24abc49c7b7f7a50ca46b5`;
- exact Batch 10 compare from `84de610b844dd594c1b8c0d4a75737e7f472e6f4` — **exactly 7 page files / scans 656, 657, 658, 659, 660, 661, 665 / 0 non-page changes**;
- Pass 2A — **COMPLETE / PASS 111/111**;
- Pass 2B Batch 1 — **556–566 / printed 539–549 — COMPLETE 11/11**;
- Pass 2B Batch 2 — **567–577 / printed 550–560 — COMPLETE 11/11**;
- Pass 2B Batch 3 — **578–588 / printed 561–571 — COMPLETE 11/11**;
- Pass 2B Batch 4 — **589–599 / printed 572–582 — COMPLETE 11/11**;
- Pass 2B Batch 5 — **600–610 / printed 583–593 — COMPLETE 11/11**;
- Pass 2B Batch 6 — **611–621 / printed 594–604 — COMPLETE 11/11**;
- Pass 2B Batch 7 — **622–632 / printed 605–615 — COMPLETE 11/11**;
- Pass 2B Batch 8 — **633–643 / printed 616–626 — COMPLETE 11/11**;
- Pass 2B Batch 9 — **644–654 / printed 627–637 — COMPLETE 11/11**;
- Pass 2B Batch 10 — **655–665 / printed 638–648 — COMPLETE 11/11**;
- Pass 2B final remainder — **666 / unnumbered pictorial back cover — COMPLETE 1/1 / no correction**;
- final-remainder exact compare — `9ad10d1f342e3313ce308bafe578d76a4ba06a54` → same commit — **identical / 0 changed files**;
- Pass 2B — **COMPLETE / PASS 111/111**;
- source endpoint — **665→666 CLEAN / PHYSICAL SOURCE ENDPOINT**;
- Pass 3 Batch 1 — **556–566 / printed 539–549 — COMPLETE 11/11**;
- Pass 3 Batch 2 — **567–577 / printed 550–560 — COMPLETE 11/11**;
- Pass 3 Batch 3 — **578–588 / printed 561–571 — COMPLETE 11/11**;
- Pass 3 Batch 4 — **589–599 / printed 572–582 — COMPLETE 11/11**;
- Pass 3 Batch 5 — **600–610 / printed 583–593 — COMPLETE 11/11**;
- Pass 3 Batch 6 — **611–621 / printed 594–604 — COMPLETE 11/11**;
- Pass 3 Batch 7 — **622–632 / printed 605–615 — COMPLETE 11/11**;
- Pass 3 Batch 8 — **633–643 / printed 616–626 — COMPLETE 11/11**;
- Pass 3 Batch 9 — **644–654 / printed 627–637 — COMPLETE 11/11**;
- Pass 3 Batch 10 — **655–665 / printed 638–648 — COMPLETE 11/11**;
- Pass 3 final remainder — **666 / unnumbered pictorial back cover — COMPLETE 1/1 / PASS**;
- final-remainder structural/visual corrections — **0**;
- final-remainder lexical/body-text changes — **0**;
- final-remainder page-layer compare — `c51b18d49513a78c26be806384875b0cf7ee9245` → same commit — **identical / 0 changed files**;
- Pass 3 structural/visual corrections overall — **2 page records / scans 611 and 631**;
- Pass 3 lexical/body-text changes overall — **0**;
- Pass 3 — **COMPLETE / PASS 111/111**;
- Part 006 audit — **PASS / COMPLETE**;
- audit record — `PART_006_AUDIT.md`;
- direct header audit — **111/111 canonical records / 0 gaps / 0 duplicates / 0 mapping anomalies**;
- page functions — **102 body-prose / 8 contents-index / 1 back-cover**;
- final metadata/status synchronization — **PASS / CLOSED**;
- status-sync record — `PART_006_FINAL_STATUS_SYNC.md`;
- status-sync base — `fec10c426518d8b5cb490db9bfab8b50f6d6a440`;
- page-layer endpoint — `6cdb3cdd18cc1ccf1b1f2071055e9a1fd7782db0`;
- exact status-sync compare — **11 commits / exactly 111 Part-006 page files / 2 additions + 2 deletions each / 0 non-page files**;
- final Tamil textual status — **111 verified / 0 needs-review / 0 exceptions**;
- final visual fidelity — **111 verified / 0 needs-review / 0 exceptions**;
- documentation synchronization — **COMPLETE / PASS**;
- documentation-sync record — `PART_006_DOCUMENTATION_SYNC.md`;
- documentation-only page-layer changes — **0**;
- Tamil archival-ready checkpoint — **PASS / CLOSED**;
- archival-ready record — `PART_006_TAMIL_ARCHIVAL_READY.md`;
- Part 006 Tamil — **ARCHIVAL-READY / CLOSED — 111/111 textual verified + 111/111 visual verified / 0 exceptions**;
- Part-006 English inventory at Tamil closure — **0/111 page records**;
- current English batch cadence — **37 physical scans**;
- English Draft D1 — **COMPLETE / PASS 37/37**;
- D1 range — **scans 556–592 / printed 539–575**;
- D1 page-layer base — `411fc0fdad71c2b94ef5c17f68dece42e744089d`;
- D1 page-layer endpoint — `8ca4baeb33a8a45d13df372dc97acc705c1398e3`;
- D1 exact compare — **6 commits / exactly 37 new English page files / 0 non-page changes / 0 Tamil changes**;
- current English status after D1 — **37 draft / 74 not yet drafted / 0 source-checked / 0 blocked**;
- English Draft D2 — **COMPLETE / PASS 37/37**;
- D2 range — **scans 593–629 / printed 576–612**;
- D2 page-layer base — `7961c8869685814e213b0a6e891b5da878b0c126`;
- D2 page-layer endpoint — `9c09dfe256eb72e75beccc4ff6ba0d8c87e922da`;
- D2 exact compare — **6 commits / exactly 37 new English page files / 0 non-page changes / 0 Tamil changes**;
- current English status — **74 draft / 37 not yet drafted / 0 source-checked / 0 blocked**;
- exact next stage — **Part 006 English Draft D3 / scans 630–666 — 37 physical scans**.

## Current frontier

**Part 006 English Draft D3 — scans 630–666 — 37 physical scans.**
