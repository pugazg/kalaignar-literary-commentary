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
- Part 003 Pass 1: **ACTIVE — scans 223–233 / 11 of 111 captured**.

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

**222→223 is resolved CLEAN.** Scan 222 closes the pastoral / `ஆயர்குடி` vignette with Chapter 128 / Kural 1275. Scan 223 / printed 206 begins a new illustrated `பேதைமை` vignette.

**233→234 is a genuine continuation.** Scan 233 / printed 216 begins the festival / green-sari vignette; scan 234 / printed 217 was inspected only as the P3-01 boundary witness and continues the same unit.

At the far end, scan 333 / printed 316 closes the final visible Part 003 unit with Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567. The external **333→334** boundary remains deferred until Part 004 intake.

## User-directed Part 003 Pass 1 cadence

Process **11 physical scan pages per normal iteration**. These are workflow boundaries only; preserve genuine source continuations across them.

Completed:

- **P3-01: scans 223–233 / printed 206–216 — COMPLETE 11/11**.

Remaining:

- P3-02: 234–244 / printed 217–227
- P3-03: 245–255 / printed 228–238
- P3-04: 256–266 / printed 239–249
- P3-05: 267–277 / printed 250–260
- P3-06: 278–288 / printed 261–271
- P3-07: 289–299 / printed 272–282
- P3-08: 300–310 / printed 283–293
- P3-09: 311–321 / printed 294–304
- P3-10: 322–332 / printed 305–315
- final remainder: 333 / printed 316

## Exact next activity — P3-02

Process **scans 234–244 / printed 217–227 — 11 physical pages** in one iteration.

Requirements:

1. use the supplied Part 003 controlling PDF and inspect rendered scans directly;
2. begin scan 234 as the direct continuation of scan 233;
3. create page-aligned Tamil records under `works/kuraloviyam/pages/` for scans 234–244 only;
4. preserve exact visible wording, punctuation, paragraphs, dialogue, Kural blocks, chapter/Kural metadata, illustration/text relationships and non-body marks;
5. keep overall `scan_page` numbering; do not restart numbering at Part-local page 1;
6. default new records to `status: "needs-review"` and `visual_fidelity: "needs-review"` unless a genuine source limitation requires otherwise;
7. do not normalize, modernize, import standard/web Kural wording, use another edition, or guess from OCR/memory;
8. inspect scan **245 / printed 228** only as a boundary witness when needed; do not create scan 245 during P3-02;
9. after capture, update `PART_003_PASS1_PROGRESS.md`, page-map/frontier and handover as needed;
10. audit the exact changed-file set before advancing;
11. next after successful P3-02 is **P3-03 scans 245–255 / printed 228–238**.
