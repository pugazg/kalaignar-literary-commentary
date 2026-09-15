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
- Tamil Pass 1 — **COMPLETE 111/111**.

### Exact next content stage

Part 005 is **FULLY CLOSED** at `works/kuraloviyam/PART_005_FINAL_CLOSURE.md`; do not reopen it. Part 006 Pass 1 is **COMPLETE 111/111**. P6-10 / scans **655–665 / printed 638–648** is **COMPLETE 11/11**, and final scan **666 / unnumbered pictorial back cover** is **COMPLETE 1/1**. Final Pass-1 page-layer commits are `8b6a5838b0fb02b3c5a8a64e9e5cc36a532c69c6` and endpoint `6f58cc1c4a12bcf06776507a42a47225d782cc2b`; exact compare from `0935e9380db4aa406793db9a5f261354831466c7` changes exactly **12 newly added Part 006 Tamil page files** and **0 non-page files**. All **111** records remain `needs-review` / visual `needs-review`. Scans **658–665** are the complete `பொருளடக்கம்` backmatter run; scan **666** is the physical source endpoint with no external continuation. Part 006 Pass 2A is **COMPLETE / PASS 111/111**. Batch 1 / scans **556–566 / printed 539–549** changed scans **556, 560, 562, 564, 565** in commit `39a88bcbf4047df1d755bd49b7ed18efe98aeaf2`. Batch 2 / scans **567–577 / printed 550–560** changed scans **568, 570, 571, 572, 575** in commit `7d54c4c367305393429fbfad87c4ae7eef6cffec`. Batch 3 / scans **578–588 / printed 561–571** changed scans **579, 580, 584, 585, 588** in commit `b7e40436f7459425e4d9ef6e52e296df23e6e776`. Batch 4 / scans **589–599 / printed 572–582** changed scans **590, 594, 596, 598, 599** in commit `e8126d62ba9863cca5af2fde19fe271677b81e20`. Batch 5 / scans **600–610 / printed 583–593** changed scans **600, 601, 602, 604–610** across commits `1dd72f0d670fcbfb75dffdb17609ebc18457d562` and `8f540105fa3f4aadd941335ff2e3f54e30b58352`. Batch 6 / scans **611–621 / printed 594–604** changed scans **611–617, 620** in commit `97de20acdabe512f52e05aa2437689411500f57f`. Batch 7 / scans **622–632 / printed 605–615** changed scans **622, 623, 627, 628, 629, 632** in commit `54dd2781658025df576d489eb63b3c2c830e1141`. Batch 8 / scans **633–643 / printed 616–626** changed scans **634, 635, 636, 637, 638, 639, 642** with endpoint `d377e43ee74c10c72d146ab478ae84a0234e96db`; exact compare from `0eda5245a9caf5832d7bd3b85bbfb16bff91fde3` changes exactly **7 Part 006 page files / 0 non-page files**. Batch 9 / scans **644–654 / printed 627–637** changed scans **645, 646, 649, 650, 653** with endpoint `eecb22e76e33400c9e65fad45326ff222a3ec468`; exact compare from `7bc5fa1941b4f8f05af3663f6320f505130afe6a` changes exactly **5 Part 006 page files / 0 non-page files**. Batch 10 / scans **655–665 / printed 638–648** changed scans **656, 657, 658, 659, 660, 661, 665** with endpoint `a88d9e186f5956b0fa24abc49c7b7f7a50ca46b5`; exact compare from `84de610b844dd594c1b8c0d4a75737e7f472e6f4` changes exactly **7 Part 006 page files / 0 non-page files**. Final remainder scan **666** required no textual correction and confirms the physical endpoint. Part 006 Pass 2B Batch 1 / scans **556–566 / printed 539–549** is **COMPLETE 11/11**. Source-supported corrections were applied to scans **559 and 566** with endpoint `742a19e72937f243db891575b45bb96964e81215`; exact compare from `bb71d16b95c57b91441b773fe62664b3e81a1697` changes exactly **2 Part 006 page files / 0 non-page files**. Part 006 Pass 2B Batch 2 / scans **567–577 / printed 550–560** is **COMPLETE 11/11**. Source-supported corrections were applied to scans **570 and 576** with endpoint `8037c41cdfd4e06cffc12b43764f26e2de793929`; exact compare from `ecc3369787c6488417f1b3d5524862f99fbf2d77` changes exactly **2 Part 006 page files / 0 non-page files**. Part 006 Pass 2B Batch 3 / scans **578–588 / printed 561–571** is **COMPLETE 11/11**. Source-supported corrections were applied to scans **580, 582, 583, 584, 588** with endpoint `cc8cd04b40be7037dfafa234bed0364bf46c48b5`; exact compare from `9ad873d2b09927603ae029f44dfa9e2071327f09` changes exactly **5 Part 006 page files / 0 non-page files**. Part 006 Pass 2B Batch 4 / scans **589–599 / printed 572–582** is **COMPLETE 11/11**. Source-supported corrections were applied to scan **598** with endpoint `6ae5eb87bc1a77e021a3114368484e52f65d5d75`; exact compare from `1695340957368313627315636547895ae0892e36` changes exactly **1 Part 006 page file / 0 non-page files**. Part 006 Pass 2B Batch 5 / scans **600–610 / printed 583–593** is **COMPLETE 11/11**. Source-supported correction was applied to scan **608** with endpoint `c3aa962722aac34bb21c581014dfc259fbf7d129`; exact compare from `ee9e3ec3783597fba25eaaa34a5f940a316f7163` changes exactly **1 Part 006 page file / 0 non-page files**. Part 006 Pass 2B Batch 6 / scans **611–621 / printed 594–604** is **COMPLETE 11/11**. Source-supported corrections were applied to scans **614, 615, 619, 620** with endpoint `5487cd351f03e09fbb2739061309bc4a008864c8`; exact compare from `009054ef9f31c000ce239d904e27f97f7bf4ce16` changes exactly **4 Part 006 page files / 0 non-page files**. Part 006 Pass 2B Batch 7 / scans **622–632 / printed 605–615** is **COMPLETE 11/11**. Source-supported corrections were applied to scans **628 and 629** with endpoint `c387d03e97542aef082121b3435930481cabef2c`; exact compare from `5a4ee430753ac437dee6ca1be7c233c215070f8e` changes exactly **2 Part 006 page files / 0 non-page files**. Part 006 Pass 2B Batch 8 / scans **633–643 / printed 616–626** is **COMPLETE 11/11**. Source-supported corrections were applied to scans **636, 637, 638 and 639** with endpoint `2c9083549d7f5cb88d4029590a93fe87532a54c1`; exact compare from `0387f24eff065c17c45999077592179a7bdbdd24` changes exactly **4 Part 006 page files / 0 non-page files**. Part 006 Pass 2B Batch 9 / scans **644–654 / printed 627–637** is **COMPLETE 11/11**. Source-supported corrections were applied to scans **646 and 648** with endpoint `88ed6de7619947e777ae083436e09a44ed6f4df7`; exact compare from `d06c6b966b0604a80fcfcc5f24568d2734a6fff6` changes exactly **2 Part 006 page files / 0 non-page files**. Part 006 Pass 2B Batch 10 / scans **655–665 / printed 638–648** is **COMPLETE 11/11** with **no page-layer correction**; exact compare `d5c1adceda92c0e4dcd888b555bcef2dc3ae9180` → same commit is **identical / 0 commits / 0 changed files**. The final Pass-2B remainder, scan **666 / unnumbered pictorial back cover**, is **COMPLETE 1/1 / no correction**; exact compare `9ad10d1f342e3313ce308bafe578d76a4ba06a54` → same commit is **identical / 0 changed files**. Part 006 Pass 2B is therefore **COMPLETE / PASS 111/111**. Scan 666 is confirmed as `back-cover`, has no visible printed body text, and preserves **665→666 CLEAN / PHYSICAL SOURCE ENDPOINT**. Part 006 Pass 3 Batch 1 / scans **556–566 / printed 539–549** is **COMPLETE 11/11** with **0 structural/visual-description corrections** and **0 lexical/body-text changes**. Exact page-layer compare `6416c58b83d96af2dfd4683685d1672eafebc199` → same commit is **identical / 0 changed files**. Part 006 Pass 3 Batch 2 / scans **567–577 / printed 550–560** is **COMPLETE 11/11** with **0 structural/visual-description corrections** and **0 lexical/body-text changes**. Exact page-layer compare `b2c8d842938a7e56f17c9010b2cd01b2f4025e94` → same commit is **identical / 0 changed files**. Part 006 Pass 3 Batch 3 / scans **578–588 / printed 561–571** is **COMPLETE 11/11** with **0 structural/visual-description corrections** and **0 lexical/body-text changes**. Exact page-layer compare `51642b8e999a501029832cb95e0d238fd11d131f` → same commit is **identical / 0 changed files**. Part 006 Pass 3 Batch 4 / scans **589–599 / printed 572–582** is **COMPLETE 11/11** with **0 structural/visual-description corrections** and **0 lexical/body-text changes**. Exact page-layer compare `338cf9d0a20d131acdfe3ad1d422001ce820999c` → same commit is **identical / 0 changed files**. Part 006 Pass 3 Batch 5 / scans **600–610 / printed 583–593** is **COMPLETE 11/11** with **0 structural/visual-description corrections** and **0 lexical/body-text changes**. Exact page-layer compare `5f2cb18c4accc2a36d0df1582cb64dc428b60b5f` → same commit is **identical / 0 changed files**. Pass 3 Batch 6 / scans **611–621 / printed 594–604** is **COMPLETE 11/11** with one visual-continuity correction on scan **611** and **0 lexical/body-text changes**. Pass 3 Batch 7 / scans **622–632 / printed 605–615** is **COMPLETE 11/11** with one visual-description correction on scan **631** and **0 lexical/body-text changes**. Batches 8–10 / scans **633–665 / printed 616–648** are **COMPLETE 33/33** with **0 structural/visual-description corrections** and **0 lexical/body-text changes**. The final remainder, scan **666 / unnumbered pictorial back cover**, is **COMPLETE 1/1 / PASS** with **0 correction**; exact page-layer compare `c51b18d49513a78c26be806384875b0cf7ee9245` → same commit is **identical / 0 changed files**. Part 006 Pass 3 is therefore **COMPLETE / PASS 111/111**. Across Pass 3, visual-description corrections were limited to scans **611 and 631**, lexical/body-text changes were **0**, and status promotions were **0**. Scan 666 confirms **665→666 CLEAN / PHYSICAL SOURCE ENDPOINT**. The Part 006 audit is **PASS / COMPLETE** with **111/111** canonical records, **0 gaps / 0 duplicates / 0 mapping anomalies**, **102 body-prose / 8 contents-index / 1 back-cover**, and **0 blocked / partial / source-limited / unresolved internal Tamil exceptions**. Final metadata/status synchronization is **PASS / CLOSED**. Starting checkpoint `fec10c426518d8b5cb490db9bfab8b50f6d6a440` → page-layer endpoint `6cdb3cdd18cc1ccf1b1f2071055e9a1fd7782db0` is **11 commits ahead / exactly 111 Part-006 page files / +2 -2 each / 0 non-page files**. Final Part-006 distribution is **111 textual verified / 111 visual verified / 0 needs-review / 0 exceptions**. Part 006 documentation synchronization is **COMPLETE / PASS** with **0 page-layer changes**. The separate Part 006 Tamil archival-ready checkpoint is now **PASS / CLOSED**. Part 006 Tamil is **ARCHIVAL-READY / CLOSED — 111/111 textual verified + 111/111 visual verified / 0 exceptions**. The maintained frontier has moved to the project-created English workflow. Repository inventory at Tamil closure contained **0 Part-006 English page records**. The user updated the normal English cadence on 2026-09-15 to **37 physical scans**. Draft D1 is **COMPLETE / PASS 37/37** for scans **556–592 / printed 539–575**. Draft D2 is **COMPLETE / PASS 37/37** for scans **593–629 / printed 576–612**. Draft D3 is **COMPLETE / PASS 37/37** for scans **630–666 / printed 613–648 + unnumbered back cover**; exact page-layer compare `f88a79c563871669c96533c07d5d50f0f87d1e17` → `8a87fbe5cf0ee36858111f693805eb4ab64ad8b0`, **5 commits / exactly 37 new English page files / 0 non-page changes / 0 Tamil changes**. Part 006 English drafting is **COMPLETE / CLOSED 111/111**. English Source-Check SC1, SC2 and SC3 are **COMPLETE / PASS 111/111**. Exact SC3 page-layer compare: `ba1391558c55e0a2917af872b6fbc42c0af8f064` → `35f666f3ab3e904565c5c24deecbffc034133a39`, **3 commits / exactly 37 modified English page files / 0 non-page changes / 0 Tamil changes**. **19** page files received source-fidelity or page-function repairs; the other **18** changed only by status promotion. Scans **658–665** are **8/8 exact contents pages** with source index lines preserved, and scan **666** remains the pictorial back cover / physical endpoint. Part 006 English source-check is **COMPLETE / CLOSED 111/111** with **111 source-checked / 0 draft**. The exact next activity is **Part 006 English Glossary Reconciliation GR1 / scans 556–592 / printed 539–575 — 37 pages**. Glossary reconciliation must use `GLOSSARY.md` plus audited Tamil context, add or reconcile only source-evidenced controls, and make **no page-status promotion**.
