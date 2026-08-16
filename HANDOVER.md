# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil.

The English layer is a **project-created translation**, not an official/publisher English edition. It must retain Kalaignar's own language, images, emphases and interpretive direction and must not import external English Kural wording or another commentator's interpretation.

Permanent cadence:

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release report.**

Do not collapse these stages.

# Established completed state

## Tamil

Parts **001–007 are audited / archival-ready** through overall scan **148** / printed page **115** / Kural **565**.

## English project translation

Parts **001–007 are released continuously through Kural 565**.

Released Parts 001–007 must not be revised merely because later parts introduce similar terminology. Any project-wide change must be deliberate, source-supported and documented.

# Part 008 Tamil — VERIFICATION IN PROGRESS

Source:

`திருக்குறள்_கலைஞர்_உரை_part_008_pages_149-169.pdf`

Physical pages: **21** / overall scans **149–169**.

Current state:

- first-pass records: **21 / 21 complete**;
- `verified`: **14 / 21** — scans 149–162 / Kural 566–635;
- `needs-review`: **7 / 21** — scans 163–169 / Kural 636–670;
- `partial`: **0**;
- `blocked`: **0**;
- Part 008 audit: **not started**;
- Part 008 English: **not started**.

## Verification history

### Batch 1 — scans 149–155 / Kural 566–600

Completed. One source-supported first-pass correction was required on scan 153 / Kural 589 commentary:

- `ஒத்திருந் தால்` → `ஒத்திருந்தால்`.

### Batch 2 — scans 156–162 / Kural 601–635

Completed. All seven first-pass records matched the controlling scan in Kural wording, joins, punctuation, line breaks and Kalaignar commentary. **No textual corrections were required.**

This batch directly verified:

- chapter 61 `மடி இன்மை`, Kural 601–610;
- chapter 62 `ஆள்வினை உடைமை`, Kural 611–620;
- chapter 63 `இடுக்கண் அழியாமை`, Kural 621–630;
- chapter 64 `அமைச்சு`, Kural 631–635.

Scan **162 / printed page 129** directly confirms the structural running-header transition from `பொருள் — அரசியல்` to **`பொருள் — அமைச்சியல் — அமைச்சு`**. Preserve that transition exactly.

# Exact next activity

Perform **Part 008 Tamil direct visual verification — Batch 3 only**, the final verification batch, for overall scans **163–169 / printed pages 130–136 / Kural 636–670**.

Scope:

- scan 163 — completes chapter 64 `அமைச்சு`, Kural 636–640;
- scans 164–165 — chapter 65 `சொல்வன்மை`, Kural 641–650;
- scans 166–167 — chapter 66 `வினைத் தூய்மை`, Kural 651–660;
- scans 168–169 — chapter 67 `வினைத்திட்பம்`, Kural 661–670.

Required procedure:

1. fresh-fetch this handover and the work README;
2. inspect controlling source scans 163–169 directly;
3. compare every corresponding Tamil Markdown record line-by-line with the scan, including Kural wording, joins, punctuation, verse line breaks, headings and Kalaignar commentary;
4. correct only differences directly supported by the scan — never normalize the source;
5. for each page that passes, change `status` from `needs-review` to `verified` and `transcription_method` to `direct visual comparison with source scan`;
6. document every actual correction, if any;
7. synchronize root README, work README and this handover;
8. stop after scan 169.

Do **not** in this activity:

- create `AUDIT_PART_008.md`;
- begin Part 008 English translation;
- begin Part 009 Tamil transcription;
- modify released English Parts 001–007.

If all seven pages pass, Part 008 will become **21/21 verified**, but **ARCHIVAL-READY must wait for the separate Part 008 Tamil audit**.
