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

### Standard iteration cadence

Process **11 physical scans per iteration**. Workflow cutoffs never create source boundaries.

112–122; 123–133; 134–144; 145–155; 156–166; 167–177; 178–188; 189–199; 200–210; 211–221; final 222.

## Part 002 Pass 1 progress

- P2-01 / scans **112–122** — COMPLETE
- P2-02 / scans **123–133** — COMPLETE
- P2-03 / scans **134–144** — COMPLETE

Current coverage: **33 / 111 scans**, overall **112–144 / printed 95–127**.

All Part 002 records remain `needs-review` / `visual_fidelity: needs-review` as required for Pass 1.

P2-03 source units:

- 134–135 — court music / taste vignette; Chapter 42 / Kural 420;
- 136–137 — princess/commander war-and-separation vignette; Chapter 123 / Kural 1224;
- 138–139 — owl/crows timing vignette; Chapter 49 / Kural 481;
- 140–141 — sisters/child/absent-lover vignette; Chapter 125 / Kural 1244;
- 142–143 — medical-hypocrisy vignette; Chapter 28 / Kural 277;
- 144 — secret-meeting vignette begins.

Continuity controls:

- **122→123** is a real continuation;
- **133→134** is a clean source boundary;
- scan **145 / printed 128** was inspected only as the P2-03 closing witness;
- **144→145 is a genuine narrative continuation** of the secret-meeting vignette.

No standard/published/web Kural wording, another edition, OCR guess or memory was used to fill uncertain readings.

## Exact current activity

Proceed with **P2-04 / Part 002 Pass 1 — overall scans 145–155 / printed pages 128–138**:

1. fetch live `main`;
2. begin scan **145** as the known continuation of scan 144;
3. process exactly scans **145–155** source-first;
4. create one Tamil page record per scan with overall `scan_page`, `part: 2`, local `part_page`, printed pagination, page function, visual notes and visible Tamil text;
5. copy Kural/chapter metadata only from the rendered source image;
6. keep Pass 1 statuses as `needs-review`;
7. inspect scan **156** only as the closing boundary witness when needed;
8. update progress/page-map/README/HANDOVER/NEXT and advance the frontier to **156–166**.

Do not import OCR guesses, another edition, standard Kural text, web material or memory to fill uncertain readings.

Part 003 must not begin until Part 002 is fully closed.
