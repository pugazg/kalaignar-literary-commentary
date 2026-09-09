# Next Chat Prompt — குறளோவியம் archival / bilingual project

Continue directly in `pugazg/kalaignar-literary-commentary`, branch `main`, active work `works/kuraloviyam/`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work. Do not reopen closed Part 001 or Part 002 unless a genuinely new source/provenance/fidelity issue appears.

## Mandatory startup

Read completely before changing anything:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this prompt
5. `works/kuraloviyam/HANDOVER.md`
6. `works/kuraloviyam/README.md`
7. `works/kuraloviyam/metadata/source.md`
8. `works/kuraloviyam/metadata/transcription-policy.md`
9. `works/kuraloviyam/indexes/page-map.md`
10. `works/kuraloviyam/SOURCE_INTAKE_PART_003.md`
11. `works/kuraloviyam/PART_003_PASS1_PROGRESS.md`
12. `works/kuraloviyam/PART_002_TAMIL_ARCHIVAL_READY.md`
13. `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`
14. `works/kuraloviyam/translations/en/reviews/PART_002_ENGLISH_RELEASE_REPORT.md`

## Durable state

- Part 001: **CLOSED**.
- Part 002 Tamil: **ARCHIVAL-READY / CLOSED — 111/111 textual + visual verified**.
- Part 002 English: **RELEASE COMPLETE / CLOSED — 111/111 release-ready**.
- Part 003 source intake: **PASS / COMPLETE**.
- Part 003 Pass 1: **ACTIVE — scans 223–321 / 99 of 111 captured**.
- Completed Pass-1 batches: **P3-01, P3-02, P3-03, P3-04, P3-05, P3-06, P3-07, P3-08, P3-09**.

## Part 003 controlling source

`TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf`

Confirmed source identity:

- local PDF pages: **111**;
- overall scans: **223–333**;
- printed pages: **206–316**;
- file size: **93,488,924 bytes**;
- SHA-256: `f07e7cdb3a6e786b0378e00bbe699a241be41c9e099c004a4faa90fa82b4239f`;
- no usable parsed text layer; rendered scan images control.

## Boundary state

**222→223 is CLEAN.**

Through the current Part-003 frontier:

- **233→234 genuine continuation**;
- **244→245 clean**;
- **255→256 clean**;
- **266→267 genuine continuation**;
- **277→278 clean**;
- **288→289 genuine continuation**;
- **299→300 clean**;
- **310→311 clean**;
- **321→322 clean**.

P3-09 scan **321 / printed 304** closes the lovers' quarrel / interpreting-signs vignette with Chapter 110 / Kural 1097. Scan **322 / printed 305** was inspected only as the outgoing boundary witness and begins a new illustrated classroom / `வலியறிதல்` vignette; it must be the first page captured in P3-10.

At the far end, scans **332–333 / printed 315–316** form the final visible Part 003 unit. Therefore **332→333 is a genuine continuation** into the final one-scan remainder. Scan 333 closes with Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567. The external **333→334** boundary remains deferred until Part 004 intake.

## User-directed Part 003 Pass 1 cadence

Process **11 physical scan pages per normal iteration**. These are workflow boundaries only; preserve genuine source continuations across them.

Completed:

- **P3-01: 223–233 / printed 206–216 — COMPLETE 11/11**;
- **P3-02: 234–244 / printed 217–227 — COMPLETE 11/11**;
- **P3-03: 245–255 / printed 228–238 — COMPLETE 11/11**;
- **P3-04: 256–266 / printed 239–249 — COMPLETE 11/11**;
- **P3-05: 267–277 / printed 250–260 — COMPLETE 11/11**;
- **P3-06: 278–288 / printed 261–271 — COMPLETE 11/11**;
- **P3-07: 289–299 / printed 272–282 — COMPLETE 11/11**;
- **P3-08: 300–310 / printed 283–293 — COMPLETE 11/11**;
- **P3-09: 311–321 / printed 294–304 — COMPLETE 11/11**.

Remaining:

- P3-10: 322–332 / printed 305–315
- final remainder: 333 / printed 316

## P3-09 durable capture summary

- scans **311–312** — love-separation / letter-and-shame vignette; Chapter 125 / Kural 1247;
- scans **313–314** — Kaarmegam / land, labour and idleness vignette; Chapter 104 / Kural 1040;
- scans **315–316** — Seyizhai / pallor-and-separation vignette; Chapter 119 / Kural 1188;
- scans **317–318** — boastful climber / knowing one's strength vignette; Chapter 48 / Kural 474;
- scans **319–321** — lovers' quarrel / interpreting-signs vignette; Chapter 110 / Kural 1097.

Scan 318 carries a lower-margin blue library stamp excluded from body text. Scan 321 preserves printed `குறிப்பறிதல்`, Kural 1097, and its printed word glosses. All Part-003 Pass-1 records remain `status: "needs-review"` and `visual_fidelity: "needs-review"`. Do not promote them during capture.

## Exact next activity — P3-10

Process **scans 322–332 / printed 305–315 — 11 physical pages** in one iteration.

Requirements:

1. use the supplied Part 003 controlling PDF and inspect rendered scans directly;
2. begin scan 322 as the new illustrated classroom / `வலியறிதல்` vignette confirmed by the P3-09 outgoing boundary witness;
3. create page-aligned Tamil records under `works/kuraloviyam/pages/` for scans 322–332 only;
4. preserve exact visible wording, punctuation, paragraphs, dialogue, Kural blocks, chapter/Kural metadata, illustration/text relationships and non-body marks;
5. keep overall `scan_page` numbering; do not restart numbering at Part-local page 1;
6. default new records to `status: "needs-review"` and `visual_fidelity: "needs-review"` unless a genuine source limitation requires otherwise;
7. do not normalize, modernize, import standard/web Kural wording, use another edition, or guess from OCR/memory;
8. inspect scan **333 / printed 316** only as the outgoing boundary witness; do not create scan 333 during P3-10 because it belongs to the final one-scan remainder;
9. preserve the genuine **332→333** continuation;
10. after capture, synchronize `PART_003_PASS1_PROGRESS.md`, README, handovers, this prompt and page-map/frontier;
11. audit the exact changed-file set before advancing;
12. next after successful P3-10 is the **final remainder — scan 333 / printed 316**.