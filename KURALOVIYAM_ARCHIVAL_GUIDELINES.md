# Kuraloviyam — Archival Guidelines

This is the work-specific operating guide for `works/kuraloviyam/` in `pugazg/kalaignar-literary-commentary`.

It supplements `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`. The controlling scan and the stricter source-preservation rule always govern.

## 1. Controlling-source rule

> **The rendered source scan is the controlling source.**

The Markdown archive is a preservation layer, not a corrected or normalized edition.

Never silently:

- correct spelling, punctuation, sandhi, names or numbers because another edition differs;
- replace a printed Kural with a memorized, web or standard-edition reading;
- modernize historical forms;
- reconstruct unclear letters from context;
- treat OCR, parsed text or model memory as source authority;
- merge printed text with handwriting, library marks, bleed-through or scanner artefacts.

If a reading is uncertain, use `needs-review`, `partial` or `blocked` rather than guessing.

## 2. Source identity and split-PDF rule

The complete Kuraloviyam source is reported as **666 physical PDF pages**, manually split into **six parts of 111 pages each**.

| Part | Overall scans |
|---|---:|
| 001 | 1–111 |
| 002 | 112–222 |
| 003 | 223–333 |
| 004 | 334–444 |
| 005 | 445–555 |
| 006 | 556–666 |

Repository `scan_page` always means the **overall 1–666 physical scan number**. It never restarts inside a later split. `part_page` may record the local 1–111 position.

Do not infer a later Part's exact filename, printed-page boundary, text, illustrations or continuity until that source is supplied.

## 3. Source files are not stored in GitHub

Split PDFs are controlling working sources and are not committed unless the user explicitly changes that policy.

Archive transcription, metadata, indexes, verification/audit records and project-created translation layers in GitHub.

## 4. Image-only / no-text-layer handling

Parts 001–004 expose no usable parsed text layer in the supplied file environment.

- inspect rendered page images directly;
- OCR may be a disposable aid only, never authority;
- do not fill unclear print from language knowledge or context;
- final source verification must compare repository text against the rendered scan.

## 5. Page-aligned Tamil archive

Every physical scan must have one page record, including covers, publication matter, prefaces, facsimiles, photographs, illustrations, blank source-side pages and body pages.

Core status vocabulary:

- `not-started`
- `needs-review`
- `partial`
- `verified`
- `blocked`

Use textual `verified` only after the required direct source comparisons are complete. A genuine source-limited page may remain `partial` permanently rather than being guessed.

Meaningful visual fidelity is tracked separately through `visual_fidelity` and may be `verified` even when textual status remains `partial`, provided the source-visible organization has been directly checked.

## 6. Kuraloviyam-specific fidelity

Kuraloviyam combines prose, Kural quotations/references and substantial illustration/layout work. Preserve, when source-supported:

- section/vignette headings and hierarchy;
- prose paragraph boundaries and dialogue structure;
- quoted Kural wording and printed lineation;
- `அதிகாரம்` / chapter labels, numbers and song/Kural references exactly as printed;
- quotation marks, separators and deliberate block placement;
- running headers and printed page numbers as page furniture rather than body prose;
- captions or text directly associated with illustrations;
- illustration/text order and relationship;
- continuation across physical page boundaries;
- non-body handwriting/stamps separately from printed body text.

Do not substitute standard Thirukkural wording for what this edition actually prints. Pixel-perfect artwork recreation is not required; factual `visual_notes` are sufficient.

## 7. Mandatory per-part closure workflow

> **Finish the entire required workflow for the currently supplied Part before beginning the next Part.**

For each Part, in order:

1. **Source intake** — confirm actual local page count, overall scan range, source identity and visible boundaries.
2. **Pass 1: physical capture / transcription** — create the complete page-aligned Tamil record set.
3. **Pass 2A: direct textual verification** — compare wording, punctuation, paragraph boundaries, Kural text and metadata against the rendered scan.
4. **Pass 2B: independent lexical-fidelity re-read** — after Pass 2A covers the whole Part, re-read every source-visible printed word independently; this is not normalization.
5. **Pass 3: meaningful visual-text verification** — verify headings, lineation, block relationships, page furniture, illustration/text relationships and physical continuations.
6. **Part audit** — verify complete physical coverage, internal continuity, source limits and the supplied Part boundary.
7. **Final metadata/status synchronization** — assign final textual/visual statuses without changing Tamil body wording.
8. **Documentation synchronization** — update work overview, page map/current frontier, audit/closure record, handover and next-chat prompt.
9. **Tamil archival-ready checkpoint** — declare the Part closed only when the above gates pass.
10. **Project-created English workflow, when maintained** — translate only from audited Tamil records, perform required review/status synchronization, and record a closed English checkpoint.
11. **Final Part closure** — only then may the next Part begin, and only when that next Part's source is supplied.

A page is not finally source-verified merely because Pass 2A completed. Pass 2B and Pass 3 must also close before final verification metadata is assigned.

## 8. Closed-Part source independence

After a Part reaches its closed checkpoint, repository records become the durable working layer for normal subsequent work.

Do **not** routinely require an older split PDF again while processing later Parts. Reopen an earlier Part source only when a newly discovered source/provenance/fidelity problem specifically requires an earlier scan to be checked.

The cross-Part boundary itself is checked only when the adjacent Part source becomes available; do not infer the missing side of a boundary.

## 9. Batch discipline

Default source-dependent work may use smaller batches when no user override exists. **Part 004 Pass 1 and Pass 2A used 11 physical scans per normal iteration. For Part 004 Pass 3, the user-directed cadence from Batch 7 onward was 30 physical scans per normal iteration. For active Part 005 Pass 3, Batches 1–3 used 11 scans, Batches 4–5 used 12 scans, and the user-directed cadence from Batch 6 onward is 25 physical scans per normal iteration**, with a shorter final remainder when fewer than 25 scans remain.

For every source-dependent batch:

1. fetch live `main`;
2. resolve the exact split PDF;
3. inspect source images directly;
4. fetch existing target records before writing;
5. transcribe/correct only source-supported visible material;
6. preserve overall scan numbering;
7. commit sequentially;
8. inspect the changed-file set;
9. record the exact next frontier.

### Mandatory frontier-control synchronization

A completed batch is not operationally closed until the live frontier controls agree.

Before stopping after **every completed Kuraloviyam batch**:

1. update the relevant Pass/gate log;
2. update the current Part progress/frontier tracker (for Part 004, `works/kuraloviyam/PART_004_PASS1_PROGRESS.md`);
3. update `works/kuraloviyam/HANDOVER.md` to the same durable phase, coverage and exact next activity;
4. update `NEXT_CHAT_PROMPT_KURALOVIYAM.md` to the same durable phase, coverage and exact next activity;
5. fetch live `main` again and verify that the tracker, work handover and next-chat prompt all point to the same next frontier.

Do not leave the handover or next-chat prompt at an older batch merely because the detailed Pass log is current.

At every **phase transition** (for example Pass 1 → Pass 2A, Pass 2A → Pass 2B, Pass 2B → Pass 3, Pass 3 → Part audit, audit → final synchronization), also update:

- root `HANDOVER.md`;
- `works/kuraloviyam/README.md` when the overview/status changes;
- `works/kuraloviyam/indexes/page-map.md` when the mapped/status frontier changes.

The end-of-Part documentation-synchronization gate remains a final consistency/closure audit. It is **not** the first time handover and next-chat controls are refreshed.

A workflow batch boundary never implies a narrative, quotation or Kural boundary. Inspect the first scan of the following batch only as a boundary witness when needed.

Pass 2B is performed only after Pass 2A reaches the end of the supplied Part so it functions as an independent second read.

## 10. English layers

If a published English Kuraloviyam source is supplied later, archive it separately as a source-controlled edition. Never mix it with a project-created translation.

A project-created English translation may be produced only from audited Tamil records and must declare:

```yaml
translation_type: "project_translation"
```

English translation must not silently alter or repair a source-limited Tamil reading. Where the Tamil archive explicitly marks unavailable/uncertain source text, the English layer must preserve that limitation rather than inventing a translation.

## 11. Current frontier

### Part 001 — overall scans 1–111

**Tamil + maintained English: CLOSED.**

English final state: **107 `release-ready` + 4 `source-limited`**.

### Part 002 — overall scans 112–222

**Tamil + maintained English: CLOSED.**

- Tamil: **111/111 textual verified + 111/111 visual verified / 0 exceptions**;
- English: **111/111 `release-ready`**;
- final Part checkpoint: **PASS / CLOSED**.

### Part 003 — overall scans 223–333

Controlling source: `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf`.

- Tamil source intake / Pass 1 / Pass 2A / Pass 2B / Pass 3 / audit / final metadata-status sync / documentation sync: **COMPLETE / PASS**;
- Tamil archival-ready checkpoint: **PASS / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**;
- incoming **222→223: CLEAN**; internal **332→333** genuine continuation closes within the Part; adjacent **333→334: CLEAN / source-resolved at Part 004 intake**;
- project-created English drafting: **111/111 COMPLETE / CLOSED**;
- English source-check: **111/111 COMPLETE / CLOSED**;
- English glossary reconciliation: **COMPLETE / CLOSED — 111/111**;
- English editorial review: **COMPLETE / CLOSED — 111/111**; Part-level English review: **PASS / CLOSED**; English release: **APPROVED / CLOSED — 111/111 release-ready**; final Part checkpoint: **PASS / CLOSED**.

### Part 004 — overall scans 334–444

**Tamil + maintained English: CLOSED.**

- Tamil — **111/111 textual verified + 111/111 visual verified / 0 exceptions**;
- English — **111/111 release-ready**;
- final Part checkpoint — **PASS / CLOSED**;
- durable final checkpoint — `works/kuraloviyam/PART_004_FINAL_CLOSURE.md`.

### Part 005 — overall scans 445–555

**SOURCE INTAKE: PASS / COMPLETE. PASS 1: COMPLETE 111/111. PASS 2A: COMPLETE / PASS 111/111. PASS 2B: COMPLETE / PASS 111/111. PASS 3: COMPLETE / PASS 111/111. PART AUDIT: PASS / COMPLETE. FINAL STATUS SYNC: PASS / CLOSED. DOCUMENTATION SYNC: COMPLETE / PASS. TAMIL ARCHIVAL-READY: PASS / CLOSED. ENGLISH DRAFTING: COMPLETE / CLOSED 111/111. ENGLISH SOURCE-CHECK: COMPLETE / CLOSED 111/111. ENGLISH GLOSSARY RECONCILIATION: COMPLETE / CLOSED 111/111. ENGLISH EDITORIAL REVIEW: COMPLETE / CLOSED 111/111. PART-LEVEL ENGLISH REVIEW: PASS / CLOSED. ENGLISH RELEASE: APPROVED / CLOSED 111/111 RELEASE-READY. FINAL PART CLOSURE: PASS / CLOSED.**

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
- cumulative Tamil Pass-1 capture — **111/111 COMPLETE**;
- current captured records — **111 `needs-review` / visual `needs-review`**;
- final Pass-1 exact compare — **12 page files only / scans 544–555**;
- **555→556 CLEAN**;
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
- Batch-1 corrections — **2 page records / 3 source-supported readings**;
- Batch-2 corrections — **5 page records / 6 source-supported readings**;
- Batch-3 corrections — **7 page records / 10 source-supported readings**;
- Batch-3 correction commit — `b6ce17d55759f05f80af760ac9d3d2cd0ec96bac` — **7 page files only**;
- Batch-4 corrections — **6 page records / 8 source-supported readings**;
- Batch-4 correction commit — `4902fd9fef350947103be839135a1c7d3a7c4d6e` — **6 page files only**;
- Batch-5 corrections — **3 page records / 4 source-supported readings**;
- Batch-5 correction commit — `5d9478576f4296e34338447145c518686cd925af` — **3 page files only**;
- Batch-6 corrections — **2 page records / 2 source-supported readings**;
- Batch-6 correction commit — `fe14f3a9e284bd91b03ddaa927eb4d4595e86d30` — **2 page files only**;
- Batch-7 corrections — **2 page records / 3 source-supported readings**;
- Batch-7 correction commit — `7c87cc0b41de0141062d1847fae8e8fc73fc40b1` — **2 page files only**;
- Batch-8 corrections — **9 page records / 18 source-supported readings**;
- Batch-8 correction commit — `ba6e0ba0b7b438476bbafb846212e05c080f6028` — **9 page files only**;
- Batch-9 corrections — **1 page record / 1 source-supported reading**;
- Batch-9 correction commit — `b3216bbb18464744a06e79232d973f46575c1145` — **1 page file only / scan 534**;
- Batch-10 corrections — **6 page records / 15 source-supported textual-or-punctuation readings**;
- Batch-10 correction commit — `5be125724c549d4b1c82020ab5fb5bf0e01fc4b8` — **6 page files only / scans 544, 545, 546, 549, 551, 552**;
- **555→556 CLEAN** remains source-resolved;
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
- Batch-1 Pass-2B correction — **1 page record / 1 source-supported lexical reading**;
- Batch-1 Pass-2B correction commit — `8391075c43b72ec3e5973db080ba742e5e899c4b` — **1 page file only / scan 453**;
- **455→456 GENUINE CONTINUATION**;
- Batch-2 Pass-2B corrections — **3 page records / 4 source-supported lexical-or-spacing readings**;
- Batch-2 Pass-2B correction commit — `665a2691e0e1cdfcff740adb48a65783976b8adf` — **3 page files only / scans 457, 463, 465**;
- **466→467 GENUINE CONTINUATION**;
- Batch-3 Pass-2B corrections — **2 page records / 2 source-visible joining readings**;
- Batch-3 Pass-2B correction commit — `c7228edbf258e2d15b3949df61fe364e9cada5e4` — **2 page files only / scans 469, 477**;
- **477→478 CLEAN**;
- Batch-4 Pass-2B corrections — **4 page records / 9 source-supported lexical-or-spacing/punctuation readings**;
- Batch-4 Pass-2B correction commit — `81456d09f7745a0834c3edc2170281945b91f478` — **4 page files only / scans 482, 485, 486, 488**;
- **488→489 CLEAN**;
- Batch-5 Pass-2B corrections — **5 page records / 9 source-supported lexical-or-spacing/punctuation readings**;
- Batch-5 Pass-2B correction commit — `2c0b3b4ddff95c18c9312dbdffbc4ef2d41c2767` — **5 page files only / scans 490, 492, 494, 496, 497**;
- **499→500 GENUINE CONTINUATION**;
- Batch-6 Pass-2B corrections — **3 page records / 6 source-supported lexical-or-spacing readings**;
- Batch-6 Pass-2B correction commit — `2cdd3c70ef34e61496d51e7996a2ade8d039e433` — **3 page files only / scans 500, 506, 510**;
- **510→511 CLEAN**;
- Batch-7 Pass-2B corrections — **3 page records / 7 source-supported lexical-or-spacing readings**;
- Batch-7 Pass-2B correction commit — `ff38ae5c02ec44026482f8db9702d76e8eb424b1` — **3 page files only / scans 511, 512, 519**;
- **521→522 CLEAN**;
- Batch-8 Pass-2B corrections — **7 page records / 12 source-supported lexical-or-spacing/punctuation readings**;
- Batch-8 Pass-2B correction commit — `4af1b155dad0a81c5bd7fe68cd64569801a3718f` — **7 page files only / scans 522, 523, 527, 528, 529, 530, 532**;
- **532→533 CLEAN**;
- Batch-9 Pass-2B corrections — **3 page records / 3 source-supported lexical-or-spacing readings**;
- Batch-9 Pass-2B correction commit — `909260dc502bb4ddeaa0defd5cb25692adf38653` — **3 page files only / scans 534, 538, 541**;
- **543→544 GENUINE CONTINUATION**;
- Batch-10 Pass-2B corrections — **3 page records / 3 source-supported lexical-or-punctuation readings**;
- Batch-10 Pass-2B correction commit — `892d3273ddf04f6b1a0364d0b77e9e4eb58d0c93` — **3 page files only / scans 544, 545, 549**;
- Pass 2B — **COMPLETE / PASS 111/111**;
- cumulative Pass-2B corrections — **34 page records / 56 source-supported readings**;
- **555→556 CLEAN / source-resolved**;
- Pass 2B log — `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_005.md`;
- Pass 3 Batch 1 — **445–455 / printed 428–438 — COMPLETE 11/11**;
- Pass 3 Batch 2 — **456–466 / printed 439–449 — COMPLETE 11/11**;
- Pass 3 Batch 3 — **467–477 / printed 450–460 — COMPLETE 11/11**;
- Pass 3 Batch 4 — **478–489 / printed 461–472 — COMPLETE 12/12**;
- Pass 3 Batch 5 — **490–501 / printed 473–484 — COMPLETE 12/12**;
- Pass 3 Batch 6 — **502–526 / printed 485–509 — COMPLETE 25/25**;
- Pass 3 Batch 7 / final remainder — **527–555 / printed 510–538 — COMPLETE 29/29**;
- final-iteration user override — **all remaining 29 pages processed in one iteration**;
- Pass-3 structural/visual corrections — **6 pages / scans 472, 474, 481, 501, 531, 537**;
- Pass-3 lexical/body-text changes — **0**;
- Batch-7 Pass-3 page correction commit — `558256c0624f32b3aee9479aebb70a734eab3118` — **2 page files only / scans 531, 537**;
- **455→456 GENUINE CONTINUATION** preserved;
- **466→467 GENUINE CONTINUATION** preserved;
- **477→478 CLEAN** preserved;
- **489→490 GENUINE CONTINUATION** preserved;
- **501→502 GENUINE CONTINUATION** preserved;
- **526→527 CLEAN** preserved;
- **555→556 CLEAN / source-resolved** preserved;
- Pass 3 — **COMPLETE / PASS 111/111**;
- Pass 3 log — `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_005.md`;
- durable Pass-1 progress — `works/kuraloviyam/PART_005_PASS1_PROGRESS.md`;
- durable Pass-2A log — `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_005.md`.

### Part 006 — overall scans 556–666

**SOURCE INTAKE: PASS / COMPLETE.**

- source endpoint — **scan 666**;
- Tamil capture — **NOT STARTED / waiting behind Part 005**.

### Exact next content stage

Part 005 is **FULLY CLOSED** at `works/kuraloviyam/PART_005_FINAL_CLOSURE.md`; do not reopen it. Part 006 Pass 1 P6-01 / scans **556–566 / printed 539–549** is **COMPLETE 11/11** at endpoint `952363e891c08a58ca78d85de95307810aafeaa6`; exact compare from `3e152243b89d68a01229d4e648875f3e6df9510c` changes exactly **11 newly added Part 006 Tamil page files** and **0 non-page files**. All 11 remain `needs-review` / visual `needs-review`. Incoming **555→556 CLEAN / source-resolved** is preserved; outgoing **566→567 GENUINE CONTINUATION** is directly source-checked. The active frontier is now **P6-02 — scans 567–577 / printed 550–560 — 11 scans**. Use rendered Part 006 source pixels as controlling authority, preserve physical-page boundaries/page functions/visuals, and do not import web/canonical Kural wording or external commentary.
