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
- Kural sequence also continues directly: Part 002 ends at Kural **40**; Part 003 begins at Kural **41**.
- the supplied Part 003 file reaches Kural **145** on printed page **29**.

### Part 003 scan map

- 42 / local 1 / printed 9 — `5. இல்வாழ்க்கை`, குறள் 41–45 — **needs-review**
- 43 / local 2 / printed 10 — `5. இல்வாழ்க்கை`, குறள் 46–50 — **needs-review**
- 44 / local 3 / printed 11 — `6. வாழ்க்கைத் துணைநலம்`, குறள் 51–55 — **needs-review**
- 45 / local 4 / printed 12 — `6. வாழ்க்கைத் துணைநலம்`, குறள் 56–60 — **needs-review**
- 46 / local 5 / printed 13 — `7. மக்கட்பேறு`, குறள் 61–65 — **needs-review**
- 47 / local 6 / printed 14 — `7. மக்கட்பேறு`, குறள் 66–70 — **needs-review**
- 48 / local 7 / printed 15 — `8. அன்புடைமை`, குறள் 71–75 — **needs-review**
- 49 / local 8 / printed 16 — `8. அன்புடைமை`, குறள் 76–80 — not-started
- 50 / local 9 / printed 17 — `9. விருந்தோம்பல்`, குறள் 81–85 — not-started
- 51 / local 10 / printed 18 — `9. விருந்தோம்பல்`, குறள் 86–90 — not-started
- 52 / local 11 / printed 19 — `10. இனியவை கூறல்`, குறள் 91–95 — not-started
- 53 / local 12 / printed 20 — `10. இனியவை கூறல்`, குறள் 96–100 — not-started
- 54 / local 13 / printed 21 — `11. செய்ந்நன்றியறிதல்`, குறள் 101–105 — not-started
- 55 / local 14 / printed 22 — `11. செய்ந்நன்றியறிதல்`, குறள் 106–110 — not-started
- 56 / local 15 / printed 23 — `12. நடுவு நிலைமை`, குறள் 111–115 — not-started
- 57 / local 16 / printed 24 — `12. நடுவு நிலைமை`, குறள் 116–120 — not-started
- 58 / local 17 / printed 25 — `13. அடக்கம் உடைமை`, குறள் 121–125 — not-started
- 59 / local 18 / printed 26 — `13. அடக்கம் உடைமை`, குறள் 126–130 — not-started
- 60 / local 19 / printed 27 — `14. ஒழுக்கம் உடைமை`, குறள் 131–135 — not-started
- 61 / local 20 / printed 28 — `14. ஒழுக்கம் உடைமை`, குறள் 136–140 — not-started
- 62 / local 21 / printed 29 — `15. பிறனில் விழையாமை`, குறள் 141–145 — not-started

### Current Part 003 status

- page records created: **7 / 21** — scans 42–48
- `needs-review`: **7**
- `not-started`: **14**
- `verified`: **0**

### Files created in the first Part 003 batch

- `works/thirukkural/pages/0042-aram-ilvaazhkkai-01.md`
- `works/thirukkural/pages/0043-aram-ilvaazhkkai-02.md`
- `works/thirukkural/pages/0044-aram-vaazhkkaith-thunainalam-01.md`
- `works/thirukkural/pages/0045-aram-vaazhkkaith-thunainalam-02.md`
- `works/thirukkural/pages/0046-aram-makkatperu-01.md`
- `works/thirukkural/pages/0047-aram-makkatperu-02.md`
- `works/thirukkural/pages/0048-aram-anbudaimai-01.md`

Each is intentionally first-pass only and uses `status: "needs-review"` plus the Part 003 local-page/source-page metadata. Do not promote any of them to `verified` until the later verification cycle.

## Files kept synchronized

- `works/thirukkural/metadata/source.md`
- `works/thirukkural/indexes/page-map.md`
- `works/thirukkural/README.md`
- root `README.md`
- this `HANDOVER.md`

## Next exact activity

Continue first-pass transcription for **Part 003 scans 49–55**.

1. scan 49 / printed 16 — finish `8. அன்புடைமை`, Kural 76–80.
2. scans 50–51 / printed 17–18 — `9. விருந்தோம்பல்`, Kural 81–90.
3. scans 52–53 / printed 19–20 — `10. இனியவை கூறல்`, Kural 91–100.
4. scans 54–55 / printed 21–22 — `11. செய்ந்நன்றியறிதல்`, Kural 101–110.
5. Preserve source-specific Kural spelling, spacing, line breaks, punctuation and Kalaignar commentary exactly as printed.
6. Keep every new page `needs-review`.
7. After scans 49–55, continue scans 56–62; only after all 21 Part 003 page records exist should the separate visual-verification cycle begin.

## Source authority rule

The supplied scans remain the controlling source for this edition. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. Apparent historical/typographical forms stay as printed unless rereading this exact scan supports a correction.
