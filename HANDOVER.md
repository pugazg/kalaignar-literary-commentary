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
- overall scan range: **21–41**
- page records: **21 / 21**
- `verified`: **21 / 21**
- audit complete
- release decision: **ARCHIVAL-READY**
- audit report: `works/thirukkural/AUDIT_PART_002.md`

Do not redo or renumber Part 002.

## Part 003

Source: `திருக்குறள்_கலைஞர்_உரை_part_003_pages_42-62.pdf`

### Source continuity

- local PDF pages: **21**
- overall scan range: **42–62**
- printed page range: **9–29**
- Part 003 local page 1 / overall scan 42 visibly begins printed page **9**, directly after Part 002 scan 41 / printed page **8**.
- Kural sequence continues directly: Part 002 ends at Kural **40**; Part 003 begins at Kural **41**.
- supplied Part 003 reaches Kural **145** on printed page **29**.

### Part 003 scan map

- 42 / local 1 / printed 9 — `5. இல்வாழ்க்கை`, குறள் 41–45 — **verified**
- 43 / local 2 / printed 10 — `5. இல்வாழ்க்கை`, குறள் 46–50 — **verified**
- 44 / local 3 / printed 11 — `6. வாழ்க்கைத் துணைநலம்`, குறள் 51–55 — **verified**
- 45 / local 4 / printed 12 — `6. வாழ்க்கைத் துணைநலம்`, குறள் 56–60 — **verified**
- 46 / local 5 / printed 13 — `7. மக்கட்பேறு`, குறள் 61–65 — **verified**
- 47 / local 6 / printed 14 — `7. மக்கட்பேறு`, குறள் 66–70 — **verified**
- 48 / local 7 / printed 15 — `8. அன்புடைமை`, குறள் 71–75 — **verified**
- 49 / local 8 / printed 16 — `8. அன்புடைமை`, குறள் 76–80 — **needs-review**
- 50 / local 9 / printed 17 — `9. விருந்தோம்பல்`, குறள் 81–85 — **needs-review**
- 51 / local 10 / printed 18 — `9. விருந்தோம்பல்`, குறள் 86–90 — **needs-review**
- 52 / local 11 / printed 19 — `10. இனியவை கூறல்`, குறள் 91–95 — **needs-review**
- 53 / local 12 / printed 20 — `10. இனியவை கூறல்`, குறள் 96–100 — **needs-review**
- 54 / local 13 / printed 21 — `11. செய்ந்நன்றியறிதல்`, குறள் 101–105 — **needs-review**
- 55 / local 14 / printed 22 — `11. செய்ந்நன்றியறிதல்`, குறள் 106–110 — **needs-review**
- 56 / local 15 / printed 23 — `12. நடுவு நிலைமை`, குறள் 111–115 — **needs-review**
- 57 / local 16 / printed 24 — `12. நடுவு நிலைமை`, குறள் 116–120 — **needs-review**
- 58 / local 17 / printed 25 — `13. அடக்கம் உடைமை`, குறள் 121–125 — **needs-review**
- 59 / local 18 / printed 26 — `13. அடக்கம் உடைமை`, குறள் 126–130 — **needs-review**
- 60 / local 19 / printed 27 — `14. ஒழுக்கம் உடைமை`, குறள் 131–135 — **needs-review**
- 61 / local 20 / printed 28 — `14. ஒழுக்கம் உடைமை`, குறள் 136–140 — **needs-review**
- 62 / local 21 / printed 29 — `15. பிறனில் விழையாமை`, குறள் 141–145 — **needs-review**

### Current Part 003 status

- page records created: **21 / 21**
- `verified`: **7** — scans 42–48
- `needs-review`: **14** — scans 49–62
- `not-started`: **0**

### Verification completed — scans 42–48

Direct visual comparison against the exact Part 003 source pages is complete for scans **42–48** / printed pages **9–15** / Kural **41–75**.

- All seven first-pass transcriptions matched the source wording and commentary.
- No text correction was required in this verification batch.
- Source-specific spelling, joins, spacing and punctuation were retained, including forms such as `போஒய்ப்`, `திண்மைஉண் டாகப்`, `பெற்றாற் பெறின்பெறுவர்`, `மக்கட்பே றல்ல`, `குழலினி தியாழினி`, `அன்போ டியைந்த`, and `அன்புற் றமர்ந்த`.
- The verified records now use `status: "verified"` and `transcription_method: "direct visual comparison with source scan"`.

## Files kept synchronized

- `works/thirukkural/metadata/source.md`
- `works/thirukkural/indexes/page-map.md`
- `works/thirukkural/README.md`
- root `README.md`
- this `HANDOVER.md`

## Next exact activity

Continue the separate direct visual-verification cycle for **Part 003 scans 49–55**.

1. scan 49 / printed 16 — `8. அன்புடைமை`, Kural 76–80.
2. scans 50–51 / printed 17–18 — `9. விருந்தோம்பல்`, Kural 81–90.
3. scans 52–53 / printed 19–20 — `10. இனியவை கூறல்`, Kural 91–100.
4. scans 54–55 / printed 21–22 — `11. செய்ந்நன்றியறிதல்`, Kural 101–110.
5. Compare character-by-character against the exact scan.
6. Preserve source-specific spelling, spacing, line breaks, punctuation and Kalaignar commentary exactly as printed.
7. Correct only source-supported differences.
8. Promote each page to `verified` only after its comparison is complete.
9. After scans 49–55, continue verification with scans 56–62.
10. Create `AUDIT_PART_003.md` only after all Part 003 pages have completed direct visual verification.

## Source authority rule

The supplied scans remain the controlling source for this edition. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. Apparent historical/typographical forms stay as printed unless rereading this exact scan supports a correction.
