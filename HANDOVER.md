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

Part 004 English is eligible because its Tamil archive is archival-ready, but the immediate archival queue is continuing the already supplied Part 005 Tamil source first.

# Part 004 Tamil — ARCHIVAL-READY

Source:

`திருக்குறள்_கலைஞர்_உரை_part_004_pages_63-84.pdf`

Confirmed range:

- local PDF pages: **22**;
- overall scans: **63–84**;
- printed pages: **30–51**;
- Kural range: **146–255**;
- scan 63 continues chapter 15 `பிறனில் விழையாமை` from Kural 146;
- scan 84 ends at Kural 255, midway through chapter 26 `புலால் மறுத்தல்`.

All 22 records are `verified` with `transcription_method: "direct visual comparison with source scan"`.

The archival audit exists at:

`works/thirukkural/AUDIT_PART_004.md`

Audit result: **ARCHIVAL-READY**.

# Part 005 Tamil source — FIRST-PASS IN PROGRESS

Source filename:

`திருக்குறள்_கலைஞர்_உரை_part_005_pages_85-106.pdf`

Confirmed full supplied source range:

- local PDF pages: **22**;
- overall scans: **85–106**;
- printed pages: **52–73**;
- Kural range: **256–365**;
- scan 85 begins with Kural **256**, directly continuing Part 004 scan 84 / Kural 255;
- scan 106 ends with Kural **365**, midway through chapter 37 `அவா அறுத்தல்`.

Current repository state for Part 005:

- page records: **14 / 22**;
- scans represented: **85–98**;
- local pages represented: **1–14**;
- printed pages represented: **52–65**;
- Kural coverage: **256–325**;
- `needs-review`: **14**;
- `verified`: **0**;
- uncreated records: **8** — scans 99–106;
- direct visual verification has **not** begun;
- no Part 005 audit exists.

Every current Part 005 record uses:

`status: "needs-review"`

and:

`transcription_method: "manual transcription from source scan; direct visual verification pending"`

## Part 005 first-pass batches completed

Batch 1 created scans **85–91** / Kural **256–290**:

- completion of `26. புலால் மறுத்தல்` — 256–260;
- `27. தவம்` — 261–270;
- `28. கூடா ஒழுக்கம்` — 271–280;
- `29. கள்ளாமை` — 281–290.

Batch 2 created scans **92–98** / Kural **291–325**:

- `30. வாய்மை` — 291–300;
- `31. வெகுளாமை` — 301–310;
- `32. இன்னா செய்யாமை` — 311–320;
- beginning of `33. கொல்லாமை` — 321–325.

Created batch-2 files:

- `0092-aram-vaaymai-01.md` — scan 92 / local 8 / printed 59 — Kural 291–295;
- `0093-aram-vaaymai-02.md` — scan 93 / local 9 / printed 60 — Kural 296–300;
- `0094-aram-vegulaamai-01.md` — scan 94 / local 10 / printed 61 — Kural 301–305;
- `0095-aram-vegulaamai-02.md` — scan 95 / local 11 / printed 62 — Kural 306–310;
- `0096-aram-innaa-seyyaamai-01.md` — scan 96 / local 12 / printed 63 — Kural 311–315;
- `0097-aram-innaa-seyyaamai-02.md` — scan 97 / local 13 / printed 64 — Kural 316–320;
- `0098-aram-kollaamai-01.md` — scan 98 / local 14 / printed 65 — Kural 321–325.

The first-pass transcription was made directly from the supplied page images. It deliberately remains unverified; do not silently promote these pages before a separate direct visual-comparison activity.

# Exact next activity

Finish **Part 005 Tamil first-pass transcription** for overall scans **99–106** / Part 005 local pages **15–22** / printed pages **66–73** / Kural **326–365**.

The actual supplied source pages have been inspected and confirm this mapping:

- scan 99 / local 15 / printed 66 — completion of `33. கொல்லாமை`, Kural 326–330;
- scan 100 / local 16 / printed 67 — `34. நிலையாமை`, Kural 331–335;
- scan 101 / local 17 / printed 68 — continuation, Kural 336–340;
- scan 102 / local 18 / printed 69 — `35. துறவு`, Kural 341–345;
- scan 103 / local 19 / printed 70 — continuation, Kural 346–350;
- scan 104 / local 20 / printed 71 — `36. மெய்யுணர்தல்`, Kural 351–355;
- scan 105 / local 21 / printed 72 — continuation, Kural 356–360;
- scan 106 / local 22 / printed 73 — beginning of `37. அவா அறுத்தல்`, Kural 361–365.

For every page in this final first-pass batch:

1. inspect the actual supplied Part 005 scan page image;
2. create exactly one Markdown record using the matching overall scan number;
3. use `part: 5` and the correct `part_page` / printed page;
4. use source filename `திருக்குறள்_கலைஞர்_உரை_part_005_pages_85-106.pdf`;
5. preserve source-specific Kural spelling, joins, spacing, punctuation and two-line structure rather than substituting a standard/web text;
6. preserve Kalaignar commentary exactly as printed;
7. retain the source marker `<!-- மூல ஸ்கேன் பக்கம்: N; Part 005 உள்ளூர் பக்கம்: M; அச்சுப் பக்கம்: P -->`;
8. keep every new page at `status: "needs-review"`;
9. use `transcription_method: "manual transcription from source scan; direct visual verification pending"`.

After scans 99–106 are created, Part 005 first-pass transcription will be **22/22 complete**. Synchronize `works/thirukkural/README.md`, root `README.md`, and this handover, then stop.

**Do not begin Part 005 direct visual verification and do not begin Part 004 English translation in the same activity.**
