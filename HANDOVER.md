# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. Preserve source-specific Kural spelling, joining, spacing, punctuation, line breaks and Kalaignar commentary exactly as printed.

The English layer is a **project-created translation**, not an official/publisher English edition. It must retain Kalaignar's own language, images, emphases and interpretive direction and must not import external English Kural wording or another commentator's interpretation.

# திருக்குறள் — established archival state

- Part 001 — scans 1–20: **ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**; 19 verified + scan 8 partial.
- Part 002 — scans 21–41: **ARCHIVAL-READY**, 21/21 verified.
- Part 003 — scans 42–62: **ARCHIVAL-READY**, 21/21 verified; printed pages 9–29; Kural 41–145.

Do not redo or renumber Parts 001–003.

English project translation for Parts 001–003 is also complete for the supplied material:

- Part 001 — 19 `release-ready` + scan 8 `source-limited`;
- Part 002 — 21/21 `release-ready`;
- Part 003 — 21/21 `release-ready`.

Part 003 review/release records remain authoritative for previously settled English choices:

- `works/thirukkural/translations/en/reviews/PART_003_REVIEW.md`
- `works/thirukkural/translations/en/reviews/PART_003_RELEASE_REPORT.md`
- `works/thirukkural/translations/en/GLOSSARY.md`
- `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`

Do not begin new English translation until the corresponding Tamil part is archival-ready.

# Newly supplied Tamil sources — inspected 2026-08-15

Two new PDFs were supplied and inspected from the actual page images.

## Part 004

Source filename:

`திருக்குறள்_கலைஞர்_உரை_part_004_pages_63-84.pdf`

Source facts confirmed from the scan:

- local PDF pages: **22**;
- overall scan range: **63–84**;
- printed page range: **30–51**;
- Kural range: **146–255**;
- scan 63 / printed page 30 begins with Kural **146**, directly continuing Part 003 after Kural 145;
- scan 84 / printed page 51 ends with Kural **255**, halfway through chapter `26. புலால் மறுத்தல்`.

## Part 005

Source filename:

`திருக்குறள்_கலைஞர்_உரை_part_005_pages_85-106.pdf`

Source facts confirmed from the scan:

- local PDF pages: **22**;
- overall scan range: **85–106**;
- printed page range: **52–73**;
- Kural range: **256–365**;
- scan 85 / printed page 52 begins with Kural **256**, directly continuing Part 004;
- scan 106 / printed page 73 ends with Kural **365**, halfway through chapter `37. அவா அறுத்தல்`.

The supplied physical source now reaches overall scan **106** / printed page **73** / Kural **365**.

# Part 004 Tamil — FIRST-PASS TRANSCRIPTION IN PROGRESS

Current repository state:

- page records: **7 / 22**;
- created scans: **63–69**;
- printed pages: **30–36**;
- Kural coverage: **146–180**;
- status of every new Part 004 record: `needs-review`;
- transcription method: `manual transcription from source scan; direct visual verification pending`.

Current files:

- `0063-aram-piranil-vizhaiyaamai-02.md` — Kural 146–150, continuation of chapter 15;
- `0064-aram-poraiyudaimai-01.md` — Kural 151–155;
- `0065-aram-poraiyudaimai-02.md` — Kural 156–160;
- `0066-aram-azhukkaaraamai-01.md` — Kural 161–165;
- `0067-aram-azhukkaaraamai-02.md` — Kural 166–170;
- `0068-aram-vehkaamai-01.md` — Kural 171–175;
- `0069-aram-vehkaamai-02.md` — Kural 176–180.

These are **first-pass archival transcriptions only**. Do not promote them to `verified` during transcription. A separate direct visual-comparison cycle must follow after all Part 004 page records exist.

No Part 005 page record has been created yet. Do not begin Part 005 until Part 004 first-pass transcription is complete.

# Exact next activity

Continue **Part 004 Tamil first-pass transcription** for overall scans **70–76** / Part 004 local pages **8–14** / printed pages **37–43** / Kural **181–215**.

Required mapping:

- scan 70 / local 8 / printed 37 — `19. புறங்கூறாமை`, Kural 181–185;
- scan 71 / local 9 / printed 38 — continuation, Kural 186–190;
- scan 72 / local 10 / printed 39 — `20. பயனில சொல்லாமை`, Kural 191–195;
- scan 73 / local 11 / printed 40 — continuation, Kural 196–200;
- scan 74 / local 12 / printed 41 — `21. தீவினையச்சம்`, Kural 201–205;
- scan 75 / local 13 / printed 42 — continuation, Kural 206–210;
- scan 76 / local 14 / printed 43 — `22. ஒப்புரவறிதல்`, Kural 211–215.

For each page:

1. inspect the actual scan;
2. create exactly one Markdown record matching the overall scan;
3. preserve source wording / word joins / spacing / punctuation rather than standardizing the Kural;
4. preserve Kalaignar's commentary as printed;
5. use `part: 4`, correct `part_page`, printed page and source filename;
6. keep `status: "needs-review"`;
7. use `transcription_method: "manual transcription from source scan; direct visual verification pending"`;
8. retain the source marker `<!-- மூல ஸ்கேன் பக்கம்: N; Part 004 உள்ளூர் பக்கம்: M; அச்சுப் பக்கம்: P -->`.

After scans 70–76 are created, synchronize `works/thirukkural/README.md`, root `README.md` and this handover. **Do not start the Part 004 verification pass and do not start Part 005 in that same activity.**

## Permanent cadence

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release report.**
