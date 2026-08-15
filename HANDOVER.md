# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. Preserve source-specific Kural spelling, joining, spacing, punctuation, line breaks and Kalaignar commentary exactly as printed.

The English layer is a **project-created translation**, not an official/publisher English edition. It must retain Kalaignar's own language, images, emphases and interpretive direction and must not import external English Kural wording or another commentator's interpretation.

Permanent cadence:

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release report.**

# திருக்குறள் — established archival state

- Part 001 — scans 1–20: **ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**; 19 verified + scan 8 partial.
- Part 002 — scans 21–41: **ARCHIVAL-READY**, 21/21 verified.
- Part 003 — scans 42–62: **ARCHIVAL-READY**, 21/21 verified; printed pages 9–29; Kural 41–145.
- Part 004 — scans 63–84: **ARCHIVAL-READY**, 22/22 verified and audited; printed pages 30–51; Kural 146–255.

Do not redo or renumber Parts 001–004.

English project translation currently released:

- Part 001 — 19 `release-ready` + scan 8 `source-limited`;
- Part 002 — 21/21 `release-ready`;
- Part 003 — 21/21 `release-ready`.

Part 004 English is eligible because its Tamil archive is archival-ready, but the immediate Tamil archival queue continues Part 005 verification first.

# Part 005 Tamil — FIRST PASS COMPLETE / VERIFICATION IN PROGRESS

Source filename:

`திருக்குறள்_கலைஞர்_உரை_part_005_pages_85-106.pdf`

Confirmed supplied source range:

- local PDF pages: **22**;
- overall scans: **85–106**;
- printed pages: **52–73**;
- Kural range: **256–365**;
- scan 85 begins with Kural **256**, directly continuing Part 004 scan 84 / Kural 255;
- scan 106 ends with Kural **365**, midway through chapter 37 `அவா அறுத்தல்`.

Current repository state for Part 005:

- page records: **22 / 22**;
- first-pass transcription: **22 / 22 complete**;
- `verified`: **7** — scans 85–91 / local pages 1–7 / printed pages 52–58 / Kural 256–290;
- `needs-review`: **15** — scans 92–106 / local pages 8–22 / printed pages 59–73 / Kural 291–365;
- uncreated records: **0**;
- direct visual verification: **in progress**;
- no Part 005 audit exists.

## Part 005 verification batch 1 completed

Direct visual comparison was completed for:

- scan 85 / printed 52 — Kural 256–260, completion of `26. புலால் மறுத்தல்`;
- scans 86–87 / printed 53–54 — `27. தவம்`, Kural 261–270;
- scans 88–89 / printed 55–56 — `28. கூடா ஒழுக்கம்`, Kural 271–280;
- scans 90–91 / printed 57–58 — `29. கள்ளாமை`, Kural 281–290.

All seven records now use:

`status: "verified"`

and:

`transcription_method: "direct visual comparison with source scan"`

The first-pass transcription for scans 85–91 matched the actual supplied scans. **No source-text corrections were required in this verification batch.** Source-specific Kural spelling, joins/spacing, punctuation, line breaks and Kalaignar commentary remain as printed.

Do not reopen or normalize scans 85–91 unless a later audit identifies a specific source-supported issue.

# Exact next activity

Perform **Part 005 Tamil direct visual verification for scans 92–98** / local pages **8–14** / printed pages **59–65** / Kural **291–325**.

Batch mapping:

- scan 92 / local 8 / printed 59 — `30. வாய்மை`, Kural 291–295;
- scan 93 / local 9 / printed 60 — continuation, Kural 296–300;
- scan 94 / local 10 / printed 61 — `31. வெகுளாமை`, Kural 301–305;
- scan 95 / local 11 / printed 62 — continuation, Kural 306–310;
- scan 96 / local 12 / printed 63 — `32. இன்னா செய்யாமை`, Kural 311–315;
- scan 97 / local 13 / printed 64 — continuation, Kural 316–320;
- scan 98 / local 14 / printed 65 — beginning of `33. கொல்லாமை`, Kural 321–325.

For each record:

1. inspect the actual corresponding scan image from the supplied Part 005 PDF;
2. compare Kural wording, source-specific joins/spacing, punctuation, line breaks and Kalaignar commentary character-by-character;
3. correct only differences supported by the scan;
4. do not import a standard/web Kural text or silently modernize Tamil;
5. if fully confirmed, set `status: "verified"`;
6. set `transcription_method: "direct visual comparison with source scan"`;
7. preserve the existing source marker and scan/local/printed-page metadata.

After scans 92–98 are completed, synchronize `works/thirukkural/README.md`, root `README.md`, and this handover, then stop.

**Do not begin scans 99 onward verification, do not create the Part 005 audit, and do not begin Part 004 English translation in the same activity.**
