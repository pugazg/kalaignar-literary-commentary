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
- source continuity confirmed: local page 1 / overall scan 21 is printed **xx**, directly after Part 001 scan 20 / printed **xix**
- page records: **21 / 21**
- `verified`: **21 / 21**
- `needs-review`: **0**
- `not-started`: **0**
- audit/release report: **pending**

### Part 002 scan map

- 21 / xx — மதிப்புரை: `ஈ. உரைக் குறள்`, `உ. இடைமிடை சொல்நலம்` — **verified**
- 22 / xxi — `ஊ. தெளிவு`, `எ. சுருக்க விளக்கம்`, `ஏ. புதுப்பொருள்` — **verified**
- 23 / xxii — புதுப்பொருள் continuation — **verified**
- 24 / xxiii — `அய். புத்தம்புது விளக்கம்`, `ஒ. நுண்மாண் நுழைபுலம்` — **verified**
- 25 / xxiv — நுண்மாண் நுழைபுலம் continuation / `6. நன்றி` — **verified**
- 26 / xxv — `நன்றி` conclusion of மதிப்புரை — **verified**
- 27 / xxvi* — `பதிப்புரை`, signed `பூம்புகார் பதிப்பகத்தார்` — **verified**
- 28 / xxvii — `திருக்குறள் அதிகார அகர வரிசை` page 1 — **verified**
- 29 / xxviii — same index page 2 — **verified**
- 30 / xxix — `அதிகார அருஞ்சொற்பொருள் அகரவரிசை` page 1 — **verified**
- 31 / xxx — same index page 2 — **verified**
- 32 / xxxi* — `திருக்குறள் / கலைஞர் உரை / அறம்` title page — **verified**
- 33 / — — blank verso with reverse-side bleed-through only — **verified**
- 34 / 1 — `1. வழிபாடு`, குறள் 1–5 + Kalaignar commentary — **verified**
- 35 / 2 — `1. வழிபாடு`, குறள் 6–10 + commentary — **verified**
- 36 / 3 — `2. வான் சிறப்பு`, குறள் 11–15 + commentary — **verified**
- 37 / 4 — `2. வான் சிறப்பு`, குறள் 16–20 + commentary — **verified**
- 38 / 5 — `3. நீத்தார் பெருமை`, குறள் 21–25 + commentary — **verified**
- 39 / 6 — `3. நீத்தார் பெருமை`, குறள் 26–30 + commentary — **verified**
- 40 / 7 — `4. அறன் வலியுறுத்தல்`, குறள் 31–35 + commentary — **verified**
- 41 / 8 — `4. அறன் வலியுறுத்தல்`, குறள் 36–40 + commentary — **verified**

`*` `xxvi` and `xxxi` are supported by the same-source contents/sequence but the numeral is not visibly printed on those scans. This basis is explicitly documented in the relevant page records.

## Verification summary

### Scans 21–27

- scans 21–26 matched the first-pass wording during final comparison.
- source-sensitive forms were retained, including `நோக்கமிம்`, `ஏஎர்`, `ஆற்றேன்இந்`, `நோயைநோய்`, `தும்மினே னாக`, `புத்தேளிர்`, `நீரியைந் தன்னா ரகத்து`, `அய். புத்தம்புது விளக்கம்`, `அடுத்தூர்வது அஃதொப்ப தில்`, and `வேண்டாவாகும்`.
- scan 27 corrections from the exact scan:
  - `எந்நிலையையூட்டும்` → **`எந்நினைவையூட்டும்`**
  - `உலக நிலையையூட்டுதல்` → **`உலக நினைவையூட்டுதல்`**
  - source punctuation spacing restored; sign-off preserved as `- பூம்புகார் பதிப்பகத்தார்`.

### Scans 28–33

- both index sections were checked directly.
- source-specific differences remain distinct: `உறுப்புநலன் அழிதல்` vs `உறுப்பு நலன் அழிதல்`; `செய்ந்நன்றியறிதல்` vs `செய்ந்நன்றி யறிதல்`; `நாணுத் துறவுரைத்தல்` vs `நாணுத்துறவு உரைத்தல்`.
- non-source continuation headings previously added to scans 29 and 31 were removed.
- scan 32 title text was confirmed; `xxxi` remains source-supported/inferred.
- scan 33 was confirmed blank/current-page-text-free; reverse-side bleed-through is excluded.

### Scans 34–41

Direct visual verification is complete for Kural **1–40** and Kalaignar's commentary.

- scans 34–36 and 38–41 matched their first-pass wording.
- source-specific Kural forms were retained, including `நீடுவாழ் வார்`, `வானின் றுலகம்`, `உள்நின் றுடற்றும்`, `சார்வாய்மற் றாங்கே`, `அகல்விசும்பு ளார்கோமான்`, `நாற்றமென றைந்தின்`, `அறவோர்மற் றெவ்வுயிர்க்கும்`, `அறத்தினூஉங்கு`, `அறத்தினூஉங்`, `அழுக்கா றவாவெகுளி`, `அறத்தா றிதுவென`, and `இன்பமற் றெல்லாம்`.
- scan 37 commentary had one genuine first-pass error corrected from the exact scan:
  - `ஒழுக்கமே கெட்டகடும்` → **`ஒழுக்கமே கெட்டுக்கூடும்`**

Every Part 002 page now uses `status: "verified"` and `transcription_method: "direct visual comparison with source scan"`.

## Files to keep synchronized

- `works/thirukkural/metadata/source.md`
- `works/thirukkural/indexes/page-map.md`
- `works/thirukkural/README.md`
- root `README.md`
- this `HANDOVER.md`

## Next exact activity

Run the **Part 002 release/audit pass**.

1. Confirm exactly one page record for each overall scan 21–41, with no gaps or duplicates.
2. Confirm `part: 2`, local `part_page: 1–21`, and printed-page continuity/bases.
3. Confirm all 21 records are `verified` and use `direct visual comparison with source scan`.
4. Confirm source filename and source-page markers are present/consistent.
5. Confirm scan 27 (`xxvi`) and scan 32 (`xxxi`) remain explicitly source-supported pagination inferences rather than visible numerals.
6. Confirm scan 33 is a verified blank/bleed-through-only page.
7. Create `works/thirukkural/AUDIT_PART_002.md` and record the release decision.
8. Synchronize root README, work README, page map and this handover with the audit result.

## Source authority rule

The supplied scans remain the controlling source for this edition. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. Apparent typographical/historical forms stay as printed unless rereading this exact scan supports a correction.
