# HANDOVER — குறளோவியம்

Repository: `pugazg/kalaignar-literary-commentary`  
Branch: `main`  
Active work: `works/kuraloviyam/`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable Kuraloviyam work. Do not reopen closed Part 001 or Part 002 unless a genuinely new source/provenance/fidelity issue appears.

## Mandatory startup

Read before changing anything:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. `NEXT_CHAT_PROMPT_KURALOVIYAM.md`
5. this file
6. `works/kuraloviyam/README.md`
7. `works/kuraloviyam/metadata/source.md`
8. `works/kuraloviyam/metadata/transcription-policy.md`
9. `works/kuraloviyam/indexes/page-map.md`
10. `works/kuraloviyam/SOURCE_INTAKE_PART_003.md`
11. `works/kuraloviyam/PART_003_PASS1_PROGRESS.md`
12. `works/kuraloviyam/PART_002_TAMIL_ARCHIVAL_READY.md`
13. `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`
14. `works/kuraloviyam/translations/en/reviews/PART_002_ENGLISH_RELEASE_REPORT.md`

## Durable closed state

- Part 001: **CLOSED** — Tamil archival-ready; English **107 release-ready + 4 source-limited**.
- Part 002 Tamil: **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**.
- Part 002 English: **RELEASE COMPLETE / CLOSED — 111/111 release-ready**.
- Part 002 final Part checkpoint: **PASS / CLOSED**.

Do not repeat Part 001/002 verification or English work from stale prompts.

## Part 003 controlling source — ONBOARDED

`TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf`

Source intake: **PASS / COMPLETE**.

Confirmed identity:

- source family: `TVA_BOK_0065733`;
- local pages: **111**;
- overall scans: **223–333**;
- printed pages: **206–316**;
- file size: **93,488,924 bytes**;
- SHA-256: `f07e7cdb3a6e786b0378e00bbe699a241be41c9e099c004a4faa90fa82b4239f`;
- usable parsed text layer: **none**;
- rendered scan images are the controlling source.

Durable intake: `works/kuraloviyam/SOURCE_INTAKE_PART_003.md`.

## Resolved 222→223 boundary

The previously deferred cross-Part boundary is now closed.

- scan **222 / printed 205** closes the pastoral / `ஆயர்குடி` vignette with Chapter 128 / Kural 1275;
- scan **223 / printed 206** starts a new illustrated `பேதைமை` vignette;
- scan **224 / printed 207** closes that new unit with Chapter 84 / Kurals 838, 839;
- therefore **222→223 is a clean vignette boundary**.

No split text is reconstructed.

## Part 003 outgoing boundary

- scans **332–333 / printed 315–316** form the final visible Part 003 unit;
- scan **333** closes with Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567;
- external **333→334** remains deferred until Part 004 is supplied. Do not infer it.

## User-directed iteration size

Process **33 physical scan pages per normal Part 003 page-batched iteration**. A final remainder may be shorter. These are workflow boundaries only and do not imply textual boundaries.

Part 003 Pass 1 plan:

- P3-01: **223–255 / printed 206–238**;
- P3-02: **256–288 / printed 239–271**;
- P3-03: **289–321 / printed 272–304**;
- final remainder: **322–333 / printed 305–316**.

## Pass 1 rules

Pass 1 is physical capture/transcription only.

For each page:

- create one page-aligned Tamil record under `works/kuraloviyam/pages/`;
- preserve exact visible wording, punctuation, paragraph/dialogue structure, Kural blocks and printed metadata;
- preserve illustration/text relationship and record non-body marks separately;
- keep overall `scan_page` numbering; never restart at local page 1;
- default to `status: "needs-review"` and `visual_fidelity: "needs-review"`;
- do not import standard/web Kural wording, another edition, OCR guesses or memory;
- do not claim Pass 2A, Pass 2B or Pass 3 verification during Pass 1.

## Exact next activity — Part 003 Pass 1 / P3-01

Process **overall scans 223–255 / printed 206–238 — 33 pages** in one iteration.

Use the supplied Part 003 PDF directly. Inspect scan **256 / printed 239** only as a boundary witness when needed; do not create its page record during P3-01.

After P3-01:

1. update `PART_003_PASS1_PROGRESS.md` and the page map/frontier;
2. audit the exact changed-file set;
3. confirm all 33 new page records remain appropriate Pass-1 statuses;
4. set P3-02 scans 256–288 as the next activity.
