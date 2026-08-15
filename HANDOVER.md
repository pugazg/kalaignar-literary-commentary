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

Part 004 English is now eligible because the Tamil archive has passed its audit, but do not begin it during the immediate Part 005 Tamil transcription activity.

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

All 22 records are:

`status: "verified"`

with:

`transcription_method: "direct visual comparison with source scan"`

The archival audit exists at:

`works/thirukkural/AUDIT_PART_004.md`

Audit result: **ARCHIVAL-READY**.

The audit reconfirmed:

- exactly 22 one-to-one page records;
- scan/local/printed-page continuity 63–84 / 1–22 / 30–51;
- Kural continuity 146–255 with no missing or duplicate number;
- chapter continuity from the continuation of chapter 15 through partial chapter 26;
- `இல்லறவியல்` → `துறவறவியல்` transition at scan 82 / printed page 49;
- no remaining `needs-review`, partial or blocked record;
- no unsupported standard/web Kural substitution.

Verification-cycle corrections retained in final Part 004 archive:

1. scan 63 / Kural 150 — `அறன்வரையா னல்ல செயினும் பிறன்வரையாள்`;
2. scan 63 / Kural 150 commentary — source `செயலைவிடத்`;
3. scan 64 / Kural 151 — source spacing `நிலம் போலத்`;
4. scan 64 / Kural 151 commentary — source `தன்மீது`.

Scans 65–84 required no further source-text correction during direct visual comparison.

# Part 005 Tamil source — inspected and queued

Source filename:

`திருக்குறள்_கலைஞர்_உரை_part_005_pages_85-106.pdf`

Confirmed source range:

- local PDF pages: **22**;
- overall scans: **85–106**;
- printed pages: **52–73**;
- Kural range: **256–365**;
- scan 85 begins with Kural **256**, directly continuing Part 004 scan 84 / Kural 255;
- scan 106 ends with Kural **365**, midway through chapter 37 `அவா அறுத்தல்`.

Current repository state for Part 005:

- page records: **0 / 22**;
- transcription has **not** begun;
- direct verification has **not** begun;
- no Part 005 audit exists.

The supplied physical source currently reaches overall scan **106** / printed page **73** / Kural **365**.

# Exact next activity

Begin **Part 005 Tamil first-pass transcription** for overall scans **85–91** / Part 005 local pages **1–7** / printed pages **52–58** / Kural **256–290**.

The actual source pages have been inspected and confirm this mapping:

- scan 85 / local 1 / printed 52 — completion of `26. புலால் மறுத்தல்`, Kural 256–260;
- scan 86 / local 2 / printed 53 — `27. தவம்`, Kural 261–265;
- scan 87 / local 3 / printed 54 — continuation, Kural 266–270;
- scan 88 / local 4 / printed 55 — `28. கூடா ஒழுக்கம்`, Kural 271–275;
- scan 89 / local 5 / printed 56 — continuation, Kural 276–280;
- scan 90 / local 6 / printed 57 — `29. கள்ளாமை`, Kural 281–285;
- scan 91 / local 7 / printed 58 — continuation, Kural 286–290.

For each page:

1. inspect the actual supplied Part 005 scan page image;
2. create exactly one Markdown record using the matching overall scan number;
3. use `part: 5` and the correct `part_page` / printed page;
4. use source filename `திருக்குறள்_கலைஞர்_உரை_part_005_pages_85-106.pdf`;
5. preserve source-specific Kural spelling, joins, spacing, punctuation and two-line structure rather than substituting a standard/web text;
6. preserve Kalaignar commentary exactly as printed;
7. retain the source marker `<!-- மூல ஸ்கேன் பக்கம்: N; Part 005 உள்ளூர் பக்கம்: M; அச்சுப் பக்கம்: P -->`;
8. keep every new page at `status: "needs-review"`;
9. use `transcription_method: "manual transcription from source scan; direct visual verification pending"`.

After scans 85–91 are created, synchronize `works/thirukkural/README.md`, root `README.md`, and this handover, then stop.

**Do not begin Part 005 direct visual verification, do not begin scans 92 onward, and do not begin Part 004 English translation in the same activity.**
