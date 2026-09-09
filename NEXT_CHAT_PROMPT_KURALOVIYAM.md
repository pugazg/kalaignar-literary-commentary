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
13. `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_003.md`
14. `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_002.md` as Pass-2B precedent
15. `works/kuraloviyam/PART_002_TAMIL_ARCHIVAL_READY.md`
16. `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`
17. `works/kuraloviyam/translations/en/reviews/PART_002_ENGLISH_RELEASE_REPORT.md`

## Durable state

- Part 001: **CLOSED**.
- Part 002 Tamil: **ARCHIVAL-READY / CLOSED — 111/111 textual + visual verified**.
- Part 002 English: **RELEASE COMPLETE / CLOSED — 111/111 release-ready**.
- Part 003 source intake: **PASS / COMPLETE**.
- Part 003 Pass 1: **COMPLETE — scans 223–333 / 111 of 111 captured**.
- Part 003 Pass 2A: **COMPLETE — scans 223–333 / 111 of 111 directly verified**.
- Part 003 Pass 2B: **ACTIVE — 20/111 independently re-read through scan 242 / printed 225**.
- Part 003 Pass 3, audit and Tamil archival-ready: **not-started**.
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

## Pass 1 and Pass 2A closure

Part 003 Pass 1 is **COMPLETE 111/111**. Part 003 Pass 2A is also **COMPLETE 111/111**. Final unit **332→333 is a genuine continuation**; scan 333 closes it with Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567. External **333→334 remains deferred** until Part 004 intake.

All 111 Part-003 page records remain:

- `status: "needs-review"`
- `visual_fidelity: "needs-review"`

Do not promote records during Pass 2B.

Durable Pass-2A record: `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_003.md`.

## Pass 2B rule and cadence

Pass 2B is an **independent lexical-fidelity re-read** against freshly rendered source scans. Follow `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_002.md` as precedent and the live Part-003 Pass-2B log as the active durable record.

Independently re-read every source-visible printed word, with special attention to:

- `ர/ற`;
- `ன/ண`;
- `ல/ள/ழ`;
- vowel signs and compound letters;
- source-visible joining/spacing;
- old or uncommon forms;
- names and quotations;
- Kural wording and printed lineation;
- paragraph/quotation boundaries and punctuation;
- printed `அதிகாரம்` / பாடல் metadata.

The rendered source scan remains controlling. Do not use OCR guesswork, normalization, another/standard edition, web text, context reconstruction or memory to replace source-visible wording.

Normal Pass-2B cadence: **10 physical scans per batch**, with a shorter final remainder if necessary. Keep all records at `needs-review` / `visual_fidelity: needs-review` throughout Pass 2B. Pass 3 remains blocked until Pass 2B closes all 111 scans.

## Pass 2B Batch 1 — COMPLETE

**Scans 223–232 / printed 206–215 — COMPLETE 10/10.** Corrections on scans **223 and 226**; eight scans no-change; **232→233 CLEAN** confirmed from scan 233 witness.

## Pass 2B Batch 2 — COMPLETE

**Scans 233–242 / printed 216–225 — COMPLETE 10/10.** Scan **243 / printed 226** was inspected only as the outgoing witness and confirms **242→243 CLEAN**.

New Pass-2B corrections:

- scan **235** — source-visible joining restored: `நடந்து சென்று` → `நடந்துசென்று`;
- scan **236** — source-visible exclamation restored: `அடே டே..!` → `அடேடே!`.

Scans **233, 234, 237, 238, 239, 240, 241 and 242** required no new Pass-2B correction.

Durable Pass-2B record: `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_003.md`.

## Exact next activity — Part 003 Pass 2B / Batch 3

Process **scans 243–252 / printed 226–235 — 10 physical scans** in one independent lexical-fidelity iteration.

Requirements:

1. fetch live `main` first;
2. resolve the supplied Part 003 PDF and freshly render/inspect scans **243–252** directly;
3. begin after confirmed **242→243 CLEAN**;
4. fetch current page records `0243`–`0252` before comparison;
5. independently re-read every source-visible word and punctuation mark using the Pass-2B rules above;
6. independently reconfirm Kural text/lineation, paragraph/quotation boundaries and printed metadata;
7. make only direct source-supported corrections;
8. update `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_003.md` and log every correction/no-change result;
9. keep all records at `needs-review` / `visual_fidelity: needs-review`;
10. audit the exact changed-file set before advancing;
11. do not begin Pass 3 until Pass 2B covers all 111 Part-003 scans.