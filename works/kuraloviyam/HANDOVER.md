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

## Boundary state

Incoming **222→223 is clean**: scan 222 closes the pastoral / `ஆயர்குடி` vignette; scan 223 begins the new illustrated `பேதைமை` vignette.

Part 003 Pass-1 boundaries include:

- **233→234 genuine continuation**;
- **244→245 clean**;
- **255→256 clean**;
- **266→267 genuine continuation**;
- **277→278 clean**;
- **288→289 genuine continuation**;
- **299→300 clean**;
- **310→311 clean**;
- **321→322 clean**;
- **323→324 clean**;
- **325→326 clean**;
- **327→328 clean**;
- **329→330 clean**;
- **331→332 clean**;
- **332→333 genuine continuation** — scan 332 begins the severe-rule / famine vignette and scan 333 closes it with Chapter 57 / Kural 567.

Outgoing **333→334 remains deferred** until Part 004 is supplied.

## Part 003 Pass 1 — COMPLETE

**111 / 111 scans captured — scans 223–333 / printed 206–316.**

Completed capture:

- P3-01: **223–233 / printed 206–216 — COMPLETE 11/11**;
- P3-02: **234–244 / printed 217–227 — COMPLETE 11/11**;
- P3-03: **245–255 / printed 228–238 — COMPLETE 11/11**;
- P3-04: **256–266 / printed 239–249 — COMPLETE 11/11**;
- P3-05: **267–277 / printed 250–260 — COMPLETE 11/11**;
- P3-06: **278–288 / printed 261–271 — COMPLETE 11/11**;
- P3-07: **289–299 / printed 272–282 — COMPLETE 11/11**;
- P3-08: **300–310 / printed 283–293 — COMPLETE 11/11**;
- P3-09: **311–321 / printed 294–304 — COMPLETE 11/11**;
- P3-10: **322–332 / printed 305–315 — COMPLETE 11/11**;
- final remainder: **333 / printed 316 — COMPLETE 1/1**.

All 111 page records exist under `works/kuraloviyam/pages/` and remain at:

- `status: "needs-review"`
- `visual_fidelity: "needs-review"`

The final record `0333-kuraloviyam-316.md` directly continues scan 332, preserves the source-visible severe-rule / famine conclusion, and closes with Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567. Side vertical title/footer furniture is excluded from body text. The external **333→334** boundary is not inferred.

Pass 1 is capture/transcription only. It does **not** make the Part source-verified.

## Next gate — Pass 2A direct textual verification

Pass 2A must directly compare repository wording against rendered scans, including:

- every source-visible word and punctuation mark;
- paragraph and quotation boundaries relevant to textual fidelity;
- Kural wording and printed lineation;
- printed `அதிகாரம்` / பாடல் metadata;
- continuations across scan boundaries;
- separation of printed text from illustrations, page furniture and library marks.

During Pass 2A, keep records at `status: "needs-review"` / `visual_fidelity: "needs-review"`; final verified statuses require later Pass 2B, Pass 3, audit and final synchronization.

## Exact next activity — Part 003 Pass 2A / Batch 1

Process **overall scans 223–232 / printed 206–215 — 10 scans** as the first direct textual-verification batch, following the established Part 002 Pass-2A precedent.

1. fetch live `main` first;
2. use the supplied Part 003 controlling PDF and rendered scans directly;
3. fetch each existing page record before comparison;
4. correct only source-supported wording/punctuation/paragraph/Kural/metadata differences;
5. inspect scan **233 / printed 216** only as a continuity witness when needed because 233 begins a vignette that continues to 234;
6. create/update the dedicated `PASS2_TEXTUAL_VERIFICATION_PART_003.md` log when the gate begins;
7. keep textual and visual statuses at `needs-review` throughout Pass 2A;
8. audit the exact changed-file set before advancing.

Do not begin Pass 2B until Pass 2A has covered all 111 Part 003 scans. English remains blocked until Tamil archival closure.