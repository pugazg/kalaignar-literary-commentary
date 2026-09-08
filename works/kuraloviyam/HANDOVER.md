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
- **266→267 genuine continuation** — scan 266 begins the trade/separation vignette and scan 267 continues the same sentence/unit;
- **277→278 clean** — scan 277 closes the nettilingam-tree / drunken-climber vignette with Chapter 48 / Kural 476; scan 278 begins a new illustrated vignette;
- **288→289 genuine continuation** — scan 288 begins the Valluvar / renunciation vignette and scan 289 continues the same unit;
- **299→300 clean** — scan 299 closes the Mullai-kodi / Mukilan fisher-couple dream vignette with Chapter 122 / Kural 1218; scan 300 begins a new illustrated vignette;
- **310→311 clean** — scan 310 closes the autobiographical 1982 Madurai-to-Tiruchendur justice-march vignette with Chapters 60/63 / Kurals 594/624; scan 311 begins a new illustrated love vignette.

Outgoing **333→334 remains deferred** until Part 004 is supplied. Scan 333 / printed 316 closes the final visible Part 003 unit with Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567.

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
- P3-08: **300–310 / printed 283–293 — COMPLETE 11/11**.

Remaining:

- P3-09: **311–321 / printed 294–304**;
- P3-10: **322–332 / printed 305–315**;
- final remainder: **333 / printed 316**.

## Part 003 Pass 1 — ACTIVE

**88 / 111 scans captured — scans 223–310 / printed 206–293.**

All 88 page records exist under `works/kuraloviyam/pages/` and remain at:

- `status: "needs-review"`
- `visual_fidelity: "needs-review"`

P3-08 captured:

- scans **300–302** — Thirumagal / Moodevi labour-and-idleness vignette; Chapter 62 / Kural 617;
- scans **303–304** — Thingal / Sevvai love-separation, `ஊடல்`, and union vignette; Chapter 126 / Kurals 1256, 1260, 1257;
- scans **305–306** — Ezhini / Valanadu betrayal-and-useless-speech vignette; Chapter 20 / Kural 191;
- scans **307–308** — Vanchikkodi / Kadamban harvest-field separation-and-heart vignette; Chapter 130 / Kural 1300;
- scans **309–310** — autobiographical 1982 Madurai-to-Tiruchendur justice-march vignette; Chapters 60 and 63 / Kurals 594 and 624.

P3-08 was transcribed from rendered scans with targeted close visual checks on uncertain readings on scans 302, 305, 308, 309, and 310. The records remain Pass-1 `needs-review` and were not promoted.

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

## Exact next activity — Part 003 Pass 1 / P3-09

Process **overall scans 311–321 / printed 294–304 — 11 pages** in one iteration.

Scan **311 / printed 294** begins a new illustrated love vignette, confirmed as the clean outgoing boundary witness during P3-08. Use the supplied Part 003 PDF directly. Inspect scan **322 / printed 305** only as a boundary witness when needed; do not create its page record during P3-09.

After P3-09:

1. update `PART_003_PASS1_PROGRESS.md`, README, handover, next-chat prompt and page map/frontier;
2. audit the exact changed-file set;
3. confirm all 11 new page records remain appropriate Pass-1 statuses;
4. set P3-10 scans 322–332 as the next activity.