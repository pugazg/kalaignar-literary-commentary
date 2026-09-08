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
- Part 003 Pass 1: **0/111 page records captured; READY / NEXT**.

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

**222→223 is resolved CLEAN.** Scan 222 closes the pastoral / `ஆயர்குடி` vignette with Chapter 128 / Kural 1275. Scan 223 / printed 206 begins a new illustrated `பேதைமை` vignette, and scan 224 / printed 207 closes it with Chapter 84 / Kurals 838, 839.

At the far end, scan 333 / printed 316 closes the final visible Part 003 unit with Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567. The external **333→334** boundary remains deferred until Part 004 intake.

## User-directed cadence

Process **33 physical scan pages per normal Part 003 Pass 1 iteration**. These are workflow boundaries only; preserve genuine source continuations across them.

- P3-01: 223–255 / printed 206–238
- P3-02: 256–288 / printed 239–271
- P3-03: 289–321 / printed 272–304
- final remainder: 322–333 / printed 305–316

## Exact next activity — P3-01

Process **scans 223–255 / printed 206–238 — 33 physical pages** in one iteration.

Requirements:

1. use the supplied Part 003 controlling PDF and inspect rendered scans directly;
2. create page-aligned Tamil records under `works/kuraloviyam/pages/` for scans 223–255 only;
3. preserve exact visible wording, punctuation, paragraphs, dialogue, Kural blocks, chapter/Kural metadata, illustration/text relationships and non-body marks;
4. keep overall `scan_page` numbering; do not restart numbering at Part-local page 1;
5. default new records to `status: "needs-review"` and `visual_fidelity: "needs-review"` unless a genuine source limitation requires otherwise;
6. do not normalize, modernize, import standard/web Kural wording, use another edition, or guess from OCR/memory;
7. inspect scan **256 / printed 239** only as a boundary witness when needed; do not create scan 256 during P3-01;
8. after capture, update `PART_003_PASS1_PROGRESS.md`, page-map/frontier and handover as needed;
9. audit the exact changed-file set before advancing;
10. next after successful P3-01 is **P3-02 scans 256–288 / printed 239–271**.
