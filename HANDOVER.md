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

Verification-cycle corrections retained in final Part 004 archive:

1. scan 63 / Kural 150 — `அறன்வரையா னல்ல செயினும் பிறன்வரையாள்`;
2. scan 63 / Kural 150 commentary — source `செயலைவிடத்`;
3. scan 64 / Kural 151 — source spacing `நிலம் போலத்`;
4. scan 64 / Kural 151 commentary — source `தன்மீது`.

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

- page records: **7 / 22**;
- scans represented: **85–91**;
- local pages represented: **1–7**;
- printed pages represented: **52–58**;
- Kural coverage: **256–290**;
- `needs-review`: **7**;
- `verified`: **0**;
- uncreated records: **15** — scans 92–106;
- direct visual verification has **not** begun;
- no Part 005 audit exists.

Every current Part 005 record uses:

`status: "needs-review"`

and:

`transcription_method: "manual transcription from source scan; direct visual verification pending"`

## Part 005 first-pass batch 1 completed

Created files:

- `0085-aram-pulaal-maruththal-02.md` — scan 85 / local 1 / printed 52 — Kural 256–260, completion of chapter 26 `புலால் மறுத்தல்`;
- `0086-aram-thavam-01.md` — scan 86 / local 2 / printed 53 — Kural 261–265;
- `0087-aram-thavam-02.md` — scan 87 / local 3 / printed 54 — Kural 266–270;
- `0088-aram-koodaa-ozhukkam-01.md` — scan 88 / local 4 / printed 55 — Kural 271–275;
- `0089-aram-koodaa-ozhukkam-02.md` — scan 89 / local 5 / printed 56 — Kural 276–280;
- `0090-aram-kallaamai-01.md` — scan 90 / local 6 / printed 57 — Kural 281–285;
- `0091-aram-kallaamai-02.md` — scan 91 / local 7 / printed 58 — Kural 286–290.

Batch 1 chapter coverage:

- completion of `26. புலால் மறுத்தல்` — Kural 256–260;
- `27. தவம்` — Kural 261–270;
- `28. கூடா ஒழுக்கம்` — Kural 271–280;
- `29. கள்ளாமை` — Kural 281–290.

The first-pass transcription was made directly from the supplied page images. It deliberately remains unverified; do not silently promote these pages before a separate direct visual-comparison activity.

# Exact next activity

Continue **Part 005 Tamil first-pass transcription** for overall scans **92–98** / Part 005 local pages **8–14** / printed pages **59–65** / Kural **291–325**.

The actual source pages have been inspected and confirm this mapping:

- scan 92 / local 8 / printed 59 — `30. வாய்மை`, Kural 291–295;
- scan 93 / local 9 / printed 60 — continuation, Kural 296–300;
- scan 94 / local 10 / printed 61 — `31. வெகுளாமை`, Kural 301–305;
- scan 95 / local 11 / printed 62 — continuation, Kural 306–310;
- scan 96 / local 12 / printed 63 — `32. இன்னா செய்யாமை`, Kural 311–315;
- scan 97 / local 13 / printed 64 — continuation, Kural 316–320;
- scan 98 / local 14 / printed 65 — beginning of `33. கொல்லாமை`, Kural 321–325.

For every page in this next batch:

1. inspect the actual supplied Part 005 scan page image;
2. create exactly one Markdown record using the matching overall scan number;
3. use `part: 5` and the correct `part_page` / printed page;
4. use source filename `திருக்குறள்_கலைஞர்_உரை_part_005_pages_85-106.pdf`;
5. preserve source-specific Kural spelling, joins, spacing, punctuation and two-line structure rather than substituting a standard/web text;
6. preserve Kalaignar commentary exactly as printed;
7. retain the source marker `<!-- மூல ஸ்கேன் பக்கம்: N; Part 005 உள்ளூர் பக்கம்: M; அச்சுப் பக்கம்: P -->`;
8. keep every new page at `status: "needs-review"`;
9. use `transcription_method: "manual transcription from source scan; direct visual verification pending"`.

After scans 92–98 are created, synchronize `works/thirukkural/README.md`, root `README.md`, and this handover, then stop.

**Do not begin Part 005 direct visual verification, do not transcribe scans 99 onward, and do not begin Part 004 English translation in the same activity.**
