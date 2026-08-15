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

# Part 004 Tamil — FIRST-PASS TRANSCRIPTION COMPLETE

Current repository state:

- page records: **22 / 22**;
- created scans: **63–84**;
- printed pages: **30–51**;
- Kural coverage: **146–255**;
- status of every Part 004 record: `needs-review`;
- transcription method: `manual transcription from source scan; direct visual verification pending`.

Coverage / files:

- `0063-aram-piranil-vizhaiyaamai-02.md` — Kural 146–150, continuation of chapter 15;
- `0064-aram-poraiyudaimai-01.md` and `0065-aram-poraiyudaimai-02.md` — chapter 16, Kural 151–160;
- `0066-aram-azhukkaaraamai-01.md` and `0067-aram-azhukkaaraamai-02.md` — chapter 17, Kural 161–170;
- `0068-aram-vehkaamai-01.md` and `0069-aram-vehkaamai-02.md` — chapter 18, Kural 171–180;
- `0070-aram-purangkooraamai-01.md` and `0071-aram-purangkooraamai-02.md` — chapter 19, Kural 181–190;
- `0072-aram-payanila-sollaamai-01.md` and `0073-aram-payanila-sollaamai-02.md` — chapter 20, Kural 191–200;
- `0074-aram-theevinaiyachcham-01.md` and `0075-aram-theevinaiyachcham-02.md` — chapter 21, Kural 201–210;
- `0076-aram-oppuravarithal-01.md` and `0077-aram-oppuravarithal-02.md` — chapter 22, Kural 211–220;
- `0078-aram-eegai-01.md` and `0079-aram-eegai-02.md` — chapter 23, Kural 221–230;
- `0080-aram-pugazh-01.md` and `0081-aram-pugazh-02.md` — chapter 24, Kural 231–240;
- `0082-aram-aruludaimai-01.md` and `0083-aram-aruludaimai-02.md` — chapter 25, Kural 241–250;
- `0084-aram-pulaal-maruththal-01.md` — chapter 26 beginning, Kural 251–255.

Source section transition:

- scans 63–81 are under `அறம் — இல்லறவியல்`;
- scan 82 / printed page 49 begins `அறம் — துறவறவியல் — அருளுடைமை`;
- scans 82–84 therefore use `துறவறவியல்` in metadata.

All 22 records are **first-pass archival transcriptions only**. None is yet verified. Do not create `AUDIT_PART_004.md` until the separate direct visual-verification cycle has completed for all 22 pages.

Part 005 remains source-inspected and queued. **No Part 005 page record exists yet.** Do not begin Part 005 transcription until Part 004 is archival-ready.

# Exact next activity

Begin the separate **Part 004 Tamil direct visual-verification pass** for overall scans **63–69** / Part 004 local pages **1–7** / printed pages **30–36** / Kural **146–180**.

Verification batch mapping:

- scan 63 — continuation of `15. பிறனில் விழையாமை`, Kural 146–150;
- scans 64–65 — `16. பொறையுடைமை`, Kural 151–160;
- scans 66–67 — `17. அழுக்காறாமை`, Kural 161–170;
- scans 68–69 — `18. வெஃகாமை`, Kural 171–180.

For every page in this batch:

1. fetch the current repository page record;
2. inspect the actual supplied PDF page image;
3. compare the record character by character against the scan;
4. preserve source-specific Kural spelling, joins, spacing, punctuation and two-line structure — never substitute a standard/web Kural text;
5. compare Kalaignar commentary word for word and correct only scan-supported mismatches;
6. verify metadata and source marker (`scan_page`, `part: 4`, `part_page`, printed page, section and source filename);
7. if the page fully matches after any necessary correction, set `status: "verified"` and `transcription_method: "direct visual comparison with source scan"`;
8. if any character remains genuinely uncertain, keep the page out of `verified` and document the uncertainty rather than guessing.

After scans 63–69 are checked, synchronize `works/thirukkural/README.md`, root `README.md` and this handover, then stop. **Do not verify scans 70–84, do not create the Part 004 audit, do not begin Part 005 transcription, and do not begin Part 004 English translation in the same activity.**

## Permanent cadence

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release report.**
