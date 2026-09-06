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
- `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_002.md`
- `works/kuraloviyam/indexes/page-map.md`

## Part 002 Pass 1 — COMPLETE

All **111 / 111** physical scans are captured as page-aligned Tamil records: overall scans **112–222 / printed 95–205**.

- P2-01 / scans **112–122** — COMPLETE
- P2-02 / scans **123–133** — COMPLETE
- P2-03 / scans **134–144** — COMPLETE
- P2-04 / scans **145–155** — COMPLETE
- P2-05 / scans **156–166** — COMPLETE
- P2-06 / scans **167–177** — COMPLETE
- P2-07 / scans **178–188** — COMPLETE
- P2-08 / scans **189–199** — COMPLETE
- P2-09 / scans **200–210** — COMPLETE
- P2-10 / scans **211–221** — COMPLETE
- final remainder / scan **222** — COMPLETE

All Part 002 records remain `needs-review` / `visual_fidelity: needs-review` as required by the staged workflow.

Final continuity controls from Pass 1:

- **122→123** continuation preserved;
- **133→134** clean;
- **144→145** continuation preserved;
- **155→156** clean;
- **166→167** continuation preserved;
- **177→178** continuation preserved;
- **188→189** clean;
- **199→200** clean;
- **210→211** clean;
- **221→222** genuine continuation preserved;
- scan **222 / printed 205** closes the pastoral/ஆயர்குடி vignette with Chapter 128 / Kural 1275 and is the final physical scan of Part 002.

No standard/published/web Kural wording, another edition, OCR guess or memory was used to fill uncertain readings.

## Part 002 Pass 2A — ACTIVE

### Batch 1 — COMPLETE

Overall scans **112–121 / printed 95–104** directly compared against the rendered source.

Corrections:

- scan **113**: `காமத்துப்பால் வாழ்வாக` → `காமத்துப்பால் வாயிலாக`;
- scan **115**: `அடடே!` → `அடேடே!`;
- scan **120**: `அவன் மன்னித்து` → `அவள் மன்னித்து`.

### Batch 2 — COMPLETE

Overall scans **122–131 / printed 105–114** directly compared against the rendered source.

Corrections:

- scan **122**: `விட்டவில்லை` → `விடவில்லை`;
- scan **123**: `பேழையைக் தாக்கிக்கொண்டு` → `பேழையைத் தூக்கிக்கொண்டு`; `கேலியில்லாமல்` → `தேவையில்லாமல்`;
- scan **124**: `கோவையப்பழ` → `கோவைப்பழ`; `கண்ணழகும்` → `கன்னமுங்`;
- scan **125**: `அழுவாளேன்?` → `அழுவானேன்?`;
- scan **127**: `வணக்கத்தைக் சூழ்ந்திருந்தோர்` → `வணக்கத்தைச் சூழ்ந்திருந்தோர்`; `அம்மலோ!` → `அம்மவோ!`; `கைகளிலே` → `கைகளுள்ளே`;
- scan **129**: `ஊடி இருந்தேமாத்` → `ஊடி யிருந்தேமாத்` in the printed Kural line;
- scan **130**: restored source-visible `அறவே அவரது விழிகளின் ஒளி பழுதாகி விடாத காரணத்தால்`;
- scan **131**: restored source-visible `முதியவர் அந்த இளந்தளிருக்கு முத்த மழை பொழிந்தார்.`

Scans **126** and **128** required no textual correction. Printed Kural wording/lineation and `அதிகாரம்` / பாடல் metadata were checked directly. Continuity from **121→122→123** was confirmed. Scan 131 closes its vignette cleanly.

Current Pass 2A coverage: **20 / 111 scans**, overall scans **112–131 / printed 95–114**.

This is Pass 2A only. Page records remain `status: "needs-review"` / `visual_fidelity: "needs-review"`; final `verified` is unavailable until Pass 2B, Pass 3, Part audit and final synchronization close.

## Exact current activity

Continue **Part 002 Pass 2A — direct textual verification**.

Next verification batch: **overall scans 132–141 / printed pages 115–124**.

1. fetch live `main`;
2. resolve the same controlling Part 002 source;
3. inspect rendered scans **132–141** directly;
4. fetch the corresponding existing page records before changing them;
5. compare every source-visible printed word, punctuation, paragraph boundary, Kural lineation and printed `அதிகாரம்` / பாடல் metadata directly against the source;
6. correct only source-supported discrepancies; do not normalize or replace this edition's wording with standard Kural text;
7. append the results to `PASS2_TEXTUAL_VERIFICATION_PART_002.md` and advance the exact next frontier;
8. keep final `verified` unavailable until Pass 2B and Pass 3 also close.

Scan 131 closes its vignette, so scan 132 begins the next vignette cleanly. Part 003 must not begin until Part 002 is fully closed.
