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

English project translation for Parts 001–003 is complete for the supplied material:

- Part 001 — 19 `release-ready` + scan 8 `source-limited`;
- Part 002 — 21/21 `release-ready`;
- Part 003 — 21/21 `release-ready`.

Do not begin new English translation until the corresponding Tamil part is archival-ready.

# Newly supplied Tamil sources — inspected 2026-08-15

## Part 004

Source filename:

`திருக்குறள்_கலைஞர்_உரை_part_004_pages_63-84.pdf`

Confirmed source range:

- local PDF pages: **22**;
- overall scans: **63–84**;
- printed pages: **30–51**;
- Kural range: **146–255**;
- scan 63 begins with Kural **146**, directly continuing scan 62 / Kural 145;
- scan 84 ends with Kural **255**, midway through `26. புலால் மறுத்தல்`.

## Part 005

Source filename:

`திருக்குறள்_கலைஞர்_உரை_part_005_pages_85-106.pdf`

Confirmed source range:

- local PDF pages: **22**;
- overall scans: **85–106**;
- printed pages: **52–73**;
- Kural range: **256–365**;
- scan 85 begins with Kural **256**, directly continuing Part 004;
- scan 106 ends with Kural **365**, midway through `37. அவா அறுத்தல்`.

The supplied physical source currently reaches overall scan **106** / printed page **73** / Kural **365**.

# Part 004 Tamil — FIRST-PASS TRANSCRIPTION IN PROGRESS

Current repository state:

- page records: **14 / 22**;
- created scans: **63–76**;
- printed pages: **30–43**;
- Kural coverage: **146–215**;
- status of every Part 004 record: `needs-review`;
- transcription method: `manual transcription from source scan; direct visual verification pending`.

Current files / coverage:

- `0063-aram-piranil-vizhaiyaamai-02.md` — Kural 146–150, continuation of chapter 15;
- `0064-aram-poraiyudaimai-01.md` and `0065-aram-poraiyudaimai-02.md` — chapter 16, Kural 151–160;
- `0066-aram-azhukkaaraamai-01.md` and `0067-aram-azhukkaaraamai-02.md` — chapter 17, Kural 161–170;
- `0068-aram-vehkaamai-01.md` and `0069-aram-vehkaamai-02.md` — chapter 18, Kural 171–180;
- `0070-aram-purangkooraamai-01.md` and `0071-aram-purangkooraamai-02.md` — chapter 19, Kural 181–190;
- `0072-aram-payanila-sollaamai-01.md` and `0073-aram-payanila-sollaamai-02.md` — chapter 20, Kural 191–200;
- `0074-aram-theevinaiyachcham-01.md` and `0075-aram-theevinaiyachcham-02.md` — chapter 21, Kural 201–210;
- `0076-aram-oppuravarithal-01.md` — chapter 22 beginning, Kural 211–215.

These are **first-pass archival transcriptions only**. Do not promote any Part 004 page to `verified` during transcription. A separate direct visual-comparison cycle must begin only after all 22 Part 004 records exist.

No Part 005 page record exists yet. Do not begin Part 005 until Part 004 first-pass transcription is complete.

# Exact next activity

Complete **Part 004 Tamil first-pass transcription** for the remaining overall scans **77–84** / Part 004 local pages **15–22** / printed pages **44–51** / Kural **216–255**.

Required mapping:

- scan 77 / local 15 / printed 44 — continuation of `22. ஒப்புரவறிதல்`, Kural 216–220;
- scan 78 / local 16 / printed 45 — `23. ஈகை`, Kural 221–225;
- scan 79 / local 17 / printed 46 — continuation, Kural 226–230;
- scan 80 / local 18 / printed 47 — `24. புகழ்`, Kural 231–235;
- scan 81 / local 19 / printed 48 — continuation, Kural 236–240;
- scan 82 / local 20 / printed 49 — `25. அருளுடைமை`, Kural 241–245;
- scan 83 / local 21 / printed 50 — continuation, Kural 246–250;
- scan 84 / local 22 / printed 51 — `26. புலால் மறுத்தல்`, Kural 251–255.

For each page:

1. inspect the actual scan;
2. create exactly one Markdown record matching the overall scan;
3. preserve source wording, word joins, spacing, punctuation and line breaks rather than standardizing the Kural;
4. preserve Kalaignar's commentary as printed;
5. use `part: 4`, the correct `part_page`, printed page and source filename;
6. keep `status: "needs-review"`;
7. use `transcription_method: "manual transcription from source scan; direct visual verification pending"`;
8. retain the source marker `<!-- மூல ஸ்கேன் பக்கம்: N; Part 004 உள்ளூர் பக்கம்: M; அச்சுப் பக்கம்: P -->`.

After scans 77–84 are created, synchronize `works/thirukkural/README.md`, root `README.md` and this handover, then stop. **Do not begin the Part 004 direct visual-verification pass and do not begin Part 005 transcription in the same activity.**

## Permanent cadence

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release report.**
