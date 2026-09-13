# குறளோவியம் — Part 005 Pass 2A textual verification

Controlling source: `TVA_BOK_0065733_குறளோவியம்_part_005_pages_445-555.pdf`

This log records **Pass 2A direct textual verification only** for Part 005. It does **not** claim the independent Pass 2B lexical-fidelity re-read, Pass 3 meaningful visual-text verification, the Part audit, archival-ready status, or English readiness.

Source identity:

- overall scans: **445–555**;
- local pages: **111**;
- visible printed pages: **428–538**;
- SHA-256: `082d46dc437851b37bea24c3152c2ea41b39c425628ddaa66461866a3177c235`;
- no usable parsed text layer; rendered scans are controlling.

For every Pass 2A batch, compare directly against rendered source scans:

- every source-visible word and punctuation mark;
- paragraph and quotation boundaries relevant to textual fidelity;
- quoted Kural wording and printed lineation;
- printed `அதிகாரம்` / பாடல் metadata;
- source glosses;
- continuations across physical scan boundaries;
- separation of printed body text from illustrations, page furniture, stamps and other non-body marks.

The rendered source scan is authoritative. Do not normalize, modernize, import standard/web Kural wording, use another edition, or fill source readings from OCR/model memory.

All Part 005 page records remain `status: "needs-review"` / `visual_fidelity: "needs-review"` throughout Pass 2A. Pass 2B begins only after Pass 2A covers all 111 scans.

Established Part 005 Pass 2A cadence: **11 physical scans per normal iteration**, with the final remainder adjusted to the source endpoint. Workflow boundaries do not create textual boundaries.

## Batch 1 — overall scans 445–455 / printed pages 428–438

**Status: COMPLETE — 11 / 11 scans directly compared against rendered source.**

Incoming **444→445 GENUINE CONTINUATION** remains preserved from the already source-resolved Part 004/005 boundary; closed Part 004 was not reopened. Scan **456 / printed 439** was inspected only as the outgoing witness and reconfirms **455→456 as a genuine continuation** of the court-jester challenge vignette.

| Scan | Printed page | Result |
|---:|---:|---|
| 445 | 428 | direct textual comparison complete; no correction required; Chapter 4 / Kural 34 and source gloss confirmed |
| 446 | 429 | direct textual comparison complete; no correction required; mirror/eye-blame vignette continues into 447 |
| 447 | 430 | corrected `கேவிக் கூத்தாகத்தான்` → source-visible `கேலிக் கூத்தாகத்தான்`; Chapter 118 / Kural 1173 and both source glosses confirmed |
| 448 | 431 | direct textual comparison complete; no correction required; source page ends with `தனிகைமலை` and continues morphologically as `யுடன்` on scan 449 |
| 449 | 432 | direct textual comparison complete; no correction required; Chapter 56 / Kural 558 confirmed |
| 450 | 433 | direct textual comparison complete; no correction required; Nallamma / Ulakanathan vignette continues into 451 |
| 451 | 434 | corrected `விளக்குகள் உறுமும் ஒலிகூடக் கேட்டது!` → `விலங்கினங்கள் உறுமும் ஒலிகூடக் கேட்டது!`; corrected `கற்பையும் குறையாடிவிட்டு` → `கற்பையும் சூறையாடிவிட்டு`; final quoted sentence continues into 452 |
| 452 | 435 | direct textual comparison complete; no correction required; Chapter 7 / Kural 69 confirmed |
| 453 | 436 | direct textual comparison complete; no correction required; lovers/eyes vignette continues into 454 |
| 454 | 437 | direct textual comparison complete; no correction required; Chapter 113 / Kurals 1127 and 1129 plus both source glosses confirmed |
| 455 | 438 | direct textual comparison complete; no correction required; scan 456 witness reconfirms genuine continuation |

Batch 1 correction summary: **2 records corrected; 9 records required no textual change; 3 source-supported readings corrected in total**.

Durable correction commit:

`ac7659d900b260f0211eae9ebacf5b14d1d01528` — `kuraloviyam: Pass 2A verify Part 005 scans 445-455`

Exact compare from pre-batch `06352ed4a732fb6f1fc566ec1b0826e0ae3a0168` to correction endpoint `ac7659d900b260f0211eae9ebacf5b14d1d01528` is **ahead by 1 commit** and changes exactly **2 page files**, scans **447** and **451** only.

## Current gate

Part 005 Pass 2A: **11/111 complete**.

Next: **Batch 2 / scans 456–466 / printed 439–449**, preserving incoming **455→456 GENUINE CONTINUATION** and inspecting scan **467 / printed 450** only as the outgoing witness when required.
