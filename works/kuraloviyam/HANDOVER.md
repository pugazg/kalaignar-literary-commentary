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

Tamil Part 001 / scans **1–111** is archival-ready: **107 `verified` + 4 `partial`**, visual fidelity **111/111 verified**. English Part 001 is closed with **107 `release-ready` + 4 `source-limited`**; limited scans remain 13, 14, 15, 19.

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

- `works/kuraloviyam/SOURCE_INTAKE_PART_002.md`
- `works/kuraloviyam/PART_002_PASS1_PROGRESS.md`
- `works/kuraloviyam/indexes/page-map.md`

### Standard iteration cadence

Process **11 physical scans per iteration**. Workflow cutoffs never create source boundaries.

112–122; 123–133; 134–144; 145–155; 156–166; 167–177; 178–188; 189–199; 200–210; 211–221; final 222.

## Part 002 Pass 1 progress

- P2-01 / scans **112–122** — COMPLETE
- P2-02 / scans **123–133** — COMPLETE
- P2-03 / scans **134–144** — COMPLETE
- P2-04 / scans **145–155** — COMPLETE
- P2-05 / scans **156–166** — COMPLETE
- P2-06 / scans **167–177** — COMPLETE
- P2-07 / scans **178–188** — COMPLETE
- P2-08 / scans **189–199** — COMPLETE
- P2-09 / scans **200–210** — COMPLETE

Current coverage: **99 / 111 scans**, overall **112–210 / printed 95–193**.

All Part 002 records remain `needs-review` / `visual_fidelity: needs-review` as required for Pass 1.

P2-09 source units:

- 200–201 — lovers/embrace vignette; Chapter 111 / Kural 1108;
- 202–204 — battlefield/war-elephant vignette; scan 203 is illustration-only; Chapter 78 / Kural 774;
- 205–206 — `அலர்` / gossip vignette; Chapter 115 / Kural 1148;
- 207–208 — battlefield command/courage vignette; Chapter 78 / Kurals 776, 775;
- 209–210 — separation/tear-flood vignette; Chapter 117 / Kural 1170.

Continuity controls:

- **122→123** continuation preserved;
- **133→134** clean;
- **144→145** continuation preserved;
- **155→156** clean;
- **166→167** continuation preserved;
- **177→178** continuation preserved;
- **188→189** clean;
- **199→200** clean;
- scan **211 / printed 194** was inspected only as the P2-09 closing witness;
- **210→211 is a clean source boundary** and scan 211 begins a new illustrated sword/warriors vignette.

No standard/published/web Kural wording, another edition, OCR guess or memory was used to fill uncertain readings.

## Exact current activity

Proceed with **P2-10 / Part 002 Pass 1 — overall scans 211–221 / printed pages 194–204**:

1. fetch live `main`;
2. begin scan **211** at the confirmed clean **210→211** source boundary;
3. process exactly scans **211–221** source-first;
4. create one Tamil page record per scan with overall `scan_page`, `part: 2`, local `part_page`, printed pagination, page function, visual notes and visible Tamil text;
5. copy Kural/chapter metadata only from the rendered source image;
6. keep Pass 1 statuses as `needs-review`;
7. inspect scan **222** only as the closing boundary witness when needed;
8. update progress/page-map/README/HANDOVER/NEXT and advance the frontier to final scan **222**.

Do not import OCR guesses, another edition, standard Kural text, web material or memory to fill uncertain readings.

Part 003 must not begin until Part 002 is fully closed.
