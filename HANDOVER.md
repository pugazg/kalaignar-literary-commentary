# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Project scope

Archive Kalaignar M. Karunanidhi's literary commentary works in source-faithful, page-by-page Markdown.

Planned works:

1. திருக்குறள் — கலைஞர் உரை
2. சங்கத்தமிழ் — Tamil
3. Sangatamil — English translation
4. குறளோவியம் — Tamil
5. Kuraloviyam — English translation

Reference implementation: `pugazg/tolkappiyap-poonga`.

Core rules: scan authority, one record per scan page, stable filenames, explicit review status, metadata/manifests, no silent normalization, and visible uncertainty.

# திருக்குறள் — current state

## Part 001

Source: `திருக்குறள்_கலைஞர்_உரை_part_001_pages_1-20.pdf`

- overall scans: **1–20**
- audit complete
- release decision: **ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**
- `verified`: 19
- `partial`: 1 — scan 8 handwritten facsimile
- audit report: `works/thirukkural/AUDIT_PART_001.md`

Do not redo or renumber Part 001.

## Part 002

Source: `திருக்குறள்_கலைஞர்_உரை_part_002_pages_21-41.pdf`

- local PDF pages: **21**
- overall scans: **21–41**
- `verified`: **21 / 21**
- audit complete
- release decision: **ARCHIVAL-READY**
- audit report: `works/thirukkural/AUDIT_PART_002.md`

Do not redo or renumber Part 002.

## Part 003

Source: `திருக்குறள்_கலைஞர்_உரை_part_003_pages_42-62.pdf`

### Final source range

- local PDF pages: **21**
- overall scans: **42–62**
- printed pages: **9–29**
- Kural range: **41–145**
- starts directly after Part 002 scan 41 / printed page 8 / Kural 40
- ends at scan 62 / printed page 29 / Kural 145

### Chapter coverage

- `5. இல்வாழ்க்கை` — 41–50
- `6. வாழ்க்கைத் துணைநலம்` — 51–60
- `7. மக்கட்பேறு` — 61–70
- `8. அன்புடைமை` — 71–80
- `9. விருந்தோம்பல்` — 81–90
- `10. இனியவை கூறல்` — 91–100
- `11. செய்ந்நன்றியறிதல்` — 101–110
- `12. நடுவு நிலைமை` — 111–120
- `13. அடக்கம் உடைமை` — 121–130
- `14. ஒழுக்கம் உடைமை` — 131–140
- `15. பிறனில் விழையாமை` — 141–145 in this supplied part

### Final Part 003 state

- page records: **21 / 21**
- `verified`: **21 / 21**
- `needs-review`: **0**
- `partial`: **0**
- `blocked`: **0**
- all records use `transcription_method: "direct visual comparison with source scan"`
- all three verification batches (42–48, 49–55, 56–62) matched the supplied scan; no source-text correction was required during Part 003 verification
- audit complete
- release decision: **ARCHIVAL-READY**
- audit report: `works/thirukkural/AUDIT_PART_003.md`

Source-specific Kural spelling, word joins, spacing, punctuation, line breaks and Kalaignar commentary were retained rather than normalized or replaced from another edition.

Do not redo or renumber Part 003.

## Files kept synchronized

- `works/thirukkural/metadata/source.md`
- `works/thirukkural/indexes/page-map.md`
- `works/thirukkural/README.md`
- root `README.md`
- `works/thirukkural/AUDIT_PART_003.md`
- this `HANDOVER.md`

## Next exact activity

Continue only when the **next Thirukkural source PDF batch** is supplied.

1. Inspect the actual next scan before creating metadata or page records.
2. Confirm whether it directly follows overall scan **62** / printed page **29** / Kural **145**.
3. Continue with overall scan **63** only if the source itself supports that sequence.
4. Do not alter or renumber Parts 001–003.
5. Preserve source-specific Tamil, Kural typography and Kalaignar commentary exactly as printed.
6. Keep newly created pages `needs-review` until a separate direct visual-verification cycle is complete.
7. Do not infer the total page count of the full book from the material supplied so far.

## Source authority rule

The supplied scans remain the controlling source for this edition. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. Apparent historical/typographical forms stay as printed unless rereading the exact controlling scan supports a correction.
