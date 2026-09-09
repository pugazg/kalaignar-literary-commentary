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
12. `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_002.md` as Pass-2A precedent
13. `works/kuraloviyam/PART_002_TAMIL_ARCHIVAL_READY.md`
14. `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`
15. `works/kuraloviyam/translations/en/reviews/PART_002_ENGLISH_RELEASE_REPORT.md`

## Durable state

- Part 001: **CLOSED**.
- Part 002 Tamil: **ARCHIVAL-READY / CLOSED — 111/111 textual + visual verified**.
- Part 002 English: **RELEASE COMPLETE / CLOSED — 111/111 release-ready**.
- Part 003 source intake: **PASS / COMPLETE**.
- Part 003 Pass 1: **COMPLETE — scans 223–333 / 111 of 111 captured**.
- Part 003 Pass 2A: **NEXT / not-started**.
- Part 003 Pass 2B, Pass 3, audit and Tamil archival-ready: **not-started**.
- English remains **blocked until Tamil closure**.

## Part 003 controlling source

`TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf`

Confirmed source identity:

- local PDF pages: **111**;
- overall scans: **223–333**;
- printed pages: **206–316**;
- file size: **93,488,924 bytes**;
- SHA-256: `f07e7cdb3a6e786b0378e00bbe699a241be41c9e099c004a4faa90fa82b4239f`;
- no usable parsed text layer; rendered scan images control.

## Pass 1 closure

Part 003 Pass 1 is **COMPLETE 111/111**.

Completed capture:

- **P3-01: 223–233 / printed 206–216 — COMPLETE 11/11**;
- **P3-02: 234–244 / printed 217–227 — COMPLETE 11/11**;
- **P3-03: 245–255 / printed 228–238 — COMPLETE 11/11**;
- **P3-04: 256–266 / printed 239–249 — COMPLETE 11/11**;
- **P3-05: 267–277 / printed 250–260 — COMPLETE 11/11**;
- **P3-06: 278–288 / printed 261–271 — COMPLETE 11/11**;
- **P3-07: 289–299 / printed 272–282 — COMPLETE 11/11**;
- **P3-08: 300–310 / printed 283–293 — COMPLETE 11/11**;
- **P3-09: 311–321 / printed 294–304 — COMPLETE 11/11**;
- **P3-10: 322–332 / printed 305–315 — COMPLETE 11/11**;
- **final remainder: 333 / printed 316 — COMPLETE 1/1**.

Final unit: **332→333 genuine continuation**. Scan 332 begins the severe-rule / famine vignette; scan 333 continues and closes it with Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567. External **333→334 remains deferred** until Part 004 intake.

All 111 Part-003 page records remain:

- `status: "needs-review"`
- `visual_fidelity: "needs-review"`

Do not promote records during Pass 2A.

## Pass 2A rule

Pass 2A is **direct textual verification against rendered source scans**. For each page compare:

- every source-visible word and punctuation mark;
- paragraph and quotation boundaries relevant to textual fidelity;
- quoted Kural wording and printed lineation;
- printed `அதிகாரம்` / பாடல் metadata;
- physical continuations across scans;
- separation of printed body text from illustrations, running/page furniture, stamps and other non-body marks.

Correct only source-supported differences. Do not normalize, modernize, import standard/web Kural wording, use another edition, or guess from OCR/memory. Keep `status: "needs-review"` / `visual_fidelity: "needs-review"` until later gates close.

## Exact next activity — Part 003 Pass 2A / Batch 1

Process **scans 223–232 / printed 206–215 — 10 physical scans** in one iteration, following the established Part 002 Pass-2A precedent.

Requirements:

1. fetch live `main` first;
2. resolve the supplied Part 003 PDF and inspect rendered scans directly;
3. fetch current page records `0223`–`0232` before comparison;
4. compare source-visible wording, punctuation, paragraph/quotation boundaries, Kural text/lineation and printed metadata word-for-word against the scans;
5. make only source-supported corrections;
6. inspect scan **233 / printed 216** only as a continuity witness when needed; scan 233 begins a vignette that continues to scan 234;
7. create/update `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_003.md` to log the batch and every correction/no-change result;
8. keep all records at `needs-review` / `visual_fidelity: needs-review`;
9. audit the exact changed-file set before advancing;
10. do not begin Pass 2B until Pass 2A covers all 111 scans.