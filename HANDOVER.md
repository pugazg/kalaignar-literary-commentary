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

First-pass transcription is complete for all 21 scans.

Current verification state:

- `verified`: **7 / 21** — scans 149–155;
- `needs-review`: **14 / 21** — scans 156–169;
- `partial`: **0**;
- `blocked`: **0**;
- Part 008 audit: **not started**;
- Part 008 English: **not started**.

## Verification Batch 1 — COMPLETE

Directly compared scans **149–155 / printed pages 116–122 / Kural 566–600** against their Tamil Markdown records:

- scan 149 — completes chapter 57 `வெருவந்த செய்யாமை`, Kural 566–570;
- scans 150–151 — chapter 58 `கண்ணோட்டம்`, Kural 571–580;
- scans 152–153 — chapter 59 `ஒற்றாடல்`, Kural 581–590;
- scans 154–155 — chapter 60 `ஊக்கம் உடைமை`, Kural 591–600.

All seven records now use:

- `status: "verified"`;
- `transcription_method: "direct visual comparison with source scan"`.

### Actual correction made in Batch 1

One first-pass spacing error was found on scan **153 / Kural 589 commentary**:

- first-pass: `ஒத்திருந் தால்`
- source-verified: **`ஒத்திருந்தால்`**

No other wording correction was required in scans 149–155.

## Structural transition still to verify

Scan **162 / printed page 129** changes the running header from `பொருள் — அரசியல்` to **`பொருள் — அமைச்சியல் — அமைச்சு`**. The first-pass page record already preserves this transition; Batch 2 must verify it directly against the scan.

# Exact next activity

Perform **Part 008 Tamil direct visual verification — Batch 2 only** for overall scans **156–162** / printed pages **123–129** / Kural **601–635**.

Scope:

- scans **156–157** — chapter 61 `மடி இன்மை`, Kural **601–610**;
- scans **158–159** — chapter 62 `ஆள்வினை உடைமை`, Kural **611–620**;
- scans **160–161** — chapter 63 `இடுக்கண் அழியாமை`, Kural **621–630**;
- scan **162** — chapter 64 `அமைச்சு` begins, Kural **631–635**, including the running-header transition into `அமைச்சியல்`.

Required procedure:

1. fresh-fetch this handover and the work README;
2. inspect the controlling scans 156–162 directly;
3. compare each corresponding Tamil Markdown record line-by-line with the scan, including Kural wording, joins, punctuation, verse line breaks and Kalaignar commentary;
4. correct only differences directly supported by the scan — do not normalize source-specific forms;
5. promote passing pages from `needs-review` to `verified` and set `transcription_method: "direct visual comparison with source scan"`;
6. document actual corrections, if any;
7. synchronize root/work README and this handover;
8. stop after scan 162.

Do **not** in this activity:

- verify scans 163–169;
- create `AUDIT_PART_008.md`;
- begin Part 008 English translation;
- begin Part 009 Tamil transcription;
- modify released English Parts 001–007.

After Batch 2, the final Part 008 verification batch should be scans **163–169 / Kural 636–670**.
