# HANDOVER — குறளோவியம்

Repository: `pugazg/kalaignar-literary-commentary`

Branch: `main`

Active work: `works/kuraloviyam/`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve any newer durable Kuraloviyam work. Do not reopen closed Part 001 Tamil or English work unless a genuinely new source/provenance issue appears.

## Source family

- source ID: `TVA_BOK_0065733`;
- complete extent reported by user: **666 physical pages**;
- split ranges: 1–111, 112–222, 223–333, 334–444, 445–555, 556–666;
- repository `scan_page` never restarts per split.

## Part 001 — CLOSED

Tamil Part 001 / scans **1–111** is archival-ready. Final Tamil state: **107 `verified` + 4 `partial`**; partial scans **13, 14, 15, 19**; visual fidelity **111/111 verified**.

English Part 001 is also closed:

- first-pass drafting: 111/111 complete;
- source-check: 111/111 complete;
- glossary reconciliation: 111/111 complete;
- editorial review: 111/111 complete;
- Part-level review: PASS;
- release report: **APPROVED WITH EXPLICIT SOURCE LIMITATIONS**;
- final statuses: **107 `release-ready` + 4 `source-limited`**;
- source-limited scans remain 13, 14, 15, 19;
- no unavailable wording was reconstructed.

Durable English release report:

`works/kuraloviyam/translations/en/reviews/PART_001_ENGLISH_RELEASE_REPORT.md`

## Part 002 — ACTIVE

Controlling split source:

`TVA_BOK_0065733_குறளோவியம்_part_002_pages_112-222.pdf`

Source intake: **COMPLETE**.

- local pages: **111**;
- overall scans: **112–222**;
- file size: **93,279,161 bytes**;
- SHA-256: `4397caf9ba405ba65f50865c85e24461ea56bd2efa3dd589d31469877c9a4bda`;
- no usable parsed text layer;
- rendered page images are controlling.

Durable records:

- source intake: `works/kuraloviyam/SOURCE_INTAKE_PART_002.md`;
- Pass 1 progress: `works/kuraloviyam/PART_002_PASS1_PROGRESS.md`.

### Resolved 111→112 boundary

The real Part 002 source resolves the old split-boundary question:

- scan 111 / printed 94 closes the learned-speaker / `சொல்வன்மை` vignette;
- scan 112 / printed 95 begins a new illustrated love vignette;
- **111→112 is a clean vignette boundary**.

Do not reconstruct anything across the split.

### Standard iteration cadence

Process **11 physical scans per iteration**. The final single-scan remainder may be shorter.

Planned scan batches:

112–122; 123–133; 134–144; 145–155; 156–166; 167–177; 178–188; 189–199; 200–210; 211–221; final 222.

Iteration boundaries are workflow boundaries only; never force a source/narrative boundary at an 11-page cutoff.

## Part 002 Pass 1 progress

### P2-01 — COMPLETE

Processed scans **112–122 / printed pages 95–105**.

### P2-02 — COMPLETE

Processed scans **123–133 / printed pages 106–116**.

Current Pass 1 coverage: **22 / 111 scans**, overall scans **112–133**.

All Part 002 records created so far remain `needs-review` / `visual_fidelity: needs-review` as required for Pass 1.

P2-02 source units:

- scan 123 closes the merchant/rest-house vignette; Chapter 51 / Kural 510;
- scans 124–125 — young-woman/heart vignette; Chapter 130 / Kural 1291;
- scans 126–127 — Gandhi vignette; Chapter 83 / Kural 828;
- scans 128–129 — sneezing/lovers vignette; Chapter 132 / Kurals 1317, 1312;
- scans 130–131 — elderly-man/public-meeting vignette; Chapter 10 / Kural 100;
- scans 132–133 — lovers' quarrel vignette; Chapter 132 / Kurals 1313, 1320.

Continuity controls:

- **122→123** is a real continuation and was preserved;
- scan **134 / printed 117** was inspected only as the P2-02 closing boundary witness;
- **133→134 is a clean source boundary**; scan 134 begins a new illustrated vignette.

No standard/published/web Kural wording, another edition, OCR guess or memory was used to fill uncertain readings.

## Exact current activity

Proceed with **P2-03 / Part 002 Pass 1 — overall scans 134–144 / printed pages 117–127**:

1. fetch live `main`;
2. begin at the confirmed clean **133→134** boundary;
3. process exactly scans **134–144** from the rendered Part 002 source;
4. create one Tamil page record per scan with overall `scan_page`, `part: 2`, local `part_page`, printed pagination, page function, visual notes and visible Tamil text;
5. copy Kural/chapter metadata only from the source image;
6. keep Pass 1 statuses as `needs-review`;
7. inspect scan **145** only as the closing boundary witness when needed;
8. update `PART_002_PASS1_PROGRESS.md`, page map, README, HANDOVER and next-chat prompt, then advance the durable frontier to **145–155**.

Do not import OCR guesses, another edition, standard Kural text, web material or memory to fill uncertain readings.

Part 003 must not begin until Part 002 is fully closed.
