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

Current internal frontier:

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

## User-directed Part 003 Pass 1 cadence

Process **11 physical scan pages per normal Part 003 Pass 1 iteration**. A final remainder may be shorter. These are workflow boundaries only and do not imply textual boundaries.

Completed:

- P3-01: **223–233 / printed 206–216 — COMPLETE 11/11**;
- P3-02: **234–244 / printed 217–227 — COMPLETE 11/11**;
- P3-03: **245–255 / printed 228–238 — COMPLETE 11/11**;
- P3-04: **256–266 / printed 239–249 — COMPLETE 11/11**;
- P3-05: **267–277 / printed 250–260 — COMPLETE 11/11**;
- P3-06: **278–288 / printed 261–271 — COMPLETE 11/11**;
- P3-07: **289–299 / printed 272–282 — COMPLETE 11/11**;
- P3-08: **300–310 / printed 283–293 — COMPLETE 11/11**;
- P3-09: **311–321 / printed 294–304 — COMPLETE 11/11**;
- P3-10: **322–332 / printed 305–315 — COMPLETE 11/11**.

Remaining:

- final remainder: **333 / printed 316 — NEXT**.

## Part 003 Pass 1 — ACTIVE

**110 / 111 scans captured — scans 223–332 / printed 206–315.**

All 110 page records exist under `works/kuraloviyam/pages/` and remain at:

- `status: "needs-review"`
- `visual_fidelity: "needs-review"`

P3-10 captured:

- scans **322–323** — classroom / `வலியறிதல்` vignette; Chapter 48 / Kurals 479, 473;
- scans **324–325** — Iraaman / Annam-Amudham chastity vignette; Chapter 6 / Kural 57;
- scans **326–327** — Ezhini / Iniyan “Yama” love vignette; Chapter 109 / Kural 1083;
- scans **328–329** — solitary-beauty / unused-wealth analogy; Chapter 101 / Kural 1007;
- scans **330–331** — burden / moral-faults / `அழுக்காறு` vignette; Chapter 4 / Kural 35;
- scan **332** — severe-rule / famine vignette begins and continues directly to scan 333.

Scan 333 / printed 316 was inspected only as the P3-10 outgoing boundary witness. It continues scan 332 and closes the final visible Part 003 unit with Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567. Do not create scan 333 until the final-remainder activity.

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

## Exact next activity — Part 003 Pass 1 / final remainder

Process **overall scan 333 / printed 316 — 1 page**.

Begin scan **333 / printed 316** as the direct continuation of the severe-rule / famine vignette begun on scan 332. Preserve the source-visible closing Kural and metadata: Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567. Do not infer the external **333→334** boundary before Part 004 is supplied.

After the final remainder:

1. update `PART_003_PASS1_PROGRESS.md`, README, handover, next-chat prompt and page map/frontier;
2. audit the exact changed-file set;
3. confirm the new scan 333 record remains appropriate Pass-1 status;
4. mark Part 003 Pass 1 complete 111/111 and advance only to the next authorized archival gate, not directly to English.