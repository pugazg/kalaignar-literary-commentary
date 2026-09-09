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
12. `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_003.md`
13. `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_002.md` as Pass-2A precedent
14. `works/kuraloviyam/PART_002_TAMIL_ARCHIVAL_READY.md`
15. `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`
16. `works/kuraloviyam/translations/en/reviews/PART_002_ENGLISH_RELEASE_REPORT.md`

## Durable state

- Part 001: **CLOSED**.
- Part 002 Tamil: **ARCHIVAL-READY / CLOSED — 111/111 textual + visual verified**.
- Part 002 English: **RELEASE COMPLETE / CLOSED — 111/111 release-ready**.
- Part 003 source intake: **PASS / COMPLETE**.
- Part 003 Pass 1: **COMPLETE — scans 223–333 / 111 of 111 captured**.
- Part 003 Pass 2A: **ACTIVE — 33/111 verified through scan 255 / printed 238**.
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

Part 003 Pass 1 is **COMPLETE 111/111**. Final unit **332→333 is a genuine continuation**; scan 333 closes it with Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567. External **333→334 remains deferred** until Part 004 intake.

All 111 Part-003 page records remain:

- `status: "needs-review"`
- `visual_fidelity: "needs-review"`

Do not promote records during Pass 2A.

## Pass 2A rule and cadence

Pass 2A is **direct textual verification against rendered source scans**. For each page compare:

- every source-visible word and punctuation mark;
- paragraph and quotation boundaries relevant to textual fidelity;
- quoted Kural wording and printed lineation;
- printed `அதிகாரம்` / பாடல் metadata;
- physical continuations across scans;
- separation of printed body text from illustrations, running/page furniture, stamps and other non-body marks.

Correct only source-supported differences. Do not normalize, modernize, import standard/web Kural wording, use another edition, or guess from OCR/memory. Keep `status: "needs-review"` / `visual_fidelity: "needs-review"` until later gates close.

User directive: **process 11 physical scans in each normal Pass-2A iteration**, with a shorter final remainder if necessary. Workflow boundaries do not imply textual boundaries.

## Pass 2A Batch 1 — COMPLETE

**Scans 223–233 / printed 206–216 — COMPLETE 11/11.** Eight records corrected; scans **229, 231, 233** no-change. The genuine **233→234** continuation was reconfirmed from scan 234.

## Pass 2A Batch 2 — COMPLETE

**Scans 234–244 / printed 217–227 — COMPLETE 11/11.** Nine records corrected: **234, 235, 236, 237, 238, 240, 242, 243, 244**. Scans **239 and 241** required no textual correction. Scan **245 / printed 228** was inspected only as the boundary witness and confirms **244→245 CLEAN**.

## Pass 2A Batch 3 — COMPLETE

**Scans 245–255 / printed 228–238 — COMPLETE 11/11.** Ten records corrected: **245, 246, 247, 248, 249, 250, 251, 252, 253, 255**. Scan **254** required no textual correction. Scan **256 / printed 239** was inspected only as the boundary witness and confirms **255→256 CLEAN**.

Important Batch-3 source-specific readings restored include `இணைபிரியாத்`, `மணநிகழ்ச்சி`, `முற்றாத இளங்காயைப்`, `மணாளனைத்`, `வளத்தைக்`, `கொள்ளுதல்`, `வரிப்புலி`, `பொற்களஞ்சியங்களாகப்`, `தத்துப்பிள்ளை`, `திண்ணை`, `ஏக்கத்தை`, `நீங்களும்`, `சினந்து`, `தேடக்கூடியது`, `கரம்பிடித்து`, plus source quotation punctuation around the relevant Kural blocks. See `PASS2_TEXTUAL_VERIFICATION_PART_003.md` for the complete per-scan record.

## Exact next activity — Part 003 Pass 2A / Batch 4

Process **scans 256–266 / printed 239–249 — 11 physical scans** in one iteration.

Requirements:

1. fetch live `main` first;
2. resolve the supplied Part 003 PDF and inspect rendered scans directly;
3. begin after the confirmed clean **255→256** boundary;
4. fetch current page records `0256`–`0266` before comparison;
5. compare source-visible wording, punctuation, paragraph/quotation boundaries, Kural text/lineation and printed metadata word-for-word against the scans;
6. make only source-supported corrections;
7. inspect scan **267 / printed 250** only as a continuity/boundary witness when needed; Pass-1 mapping records **266→267 as a genuine continuation**;
8. update `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_003.md` to log every correction/no-change result;
9. keep all records at `needs-review` / `visual_fidelity: needs-review`;
10. audit the exact changed-file set before advancing;
11. do not begin Pass 2B until Pass 2A covers all 111 scans.