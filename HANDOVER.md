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
- page records now exist for **scans 21–33**
- all Part 002 records remain `needs-review`; none is `verified` yet

### Part 002 scan map

- 21 / xx — மதிப்புரை: `ஈ. உரைக் குறள்`, `உ. இடைமிடை சொல்நலம்`
- 22 / xxi — `ஊ. தெளிவு`, `எ. சுருக்க விளக்கம்`, `ஏ. புதுப்பொருள்`
- 23 / xxii — புதுப்பொருள் continuation
- 24 / xxiii — `அய். புத்தம்புது விளக்கம்`, `ஒ. நுண்மாண் நுழைபுலம்`
- 25 / xxiv — நுண்மாண் நுழைபுலம் continuation / `6. நன்றி`
- 26 / xxv — `நன்றி` conclusion of மதிப்புரை
- 27 / xxvi* — `பதிப்புரை`, signed `பூம்புகார் பதிப்பகத்தார்`
- 28 / xxvii — `திருக்குறள் அதிகார அகர வரிசை` page 1
- 29 / xxviii — same index page 2
- 30 / xxix — `அதிகார அருஞ்சொற்பொருள் அகரவரிசை` page 1
- 31 / xxx — same index page 2
- 32 / xxxi* — `திருக்குறள் / கலைஞர் உரை / அறம்` title page
- 33 / — — blank verso with reverse-side bleed-through only
- 34 / 1 — `1. வழிபாடு`, குறள் 1–5
- 35 / 2 — `1. வழிபாடு`, குறள் 6–10
- 36 / 3 — `2. வான் சிறப்பு`, குறள் 11–15
- 37 / 4 — `2. வான் சிறப்பு`, குறள் 16–20
- 38 / 5 — `3. நீத்தார் பெருமை`, குறள் 21–25
- 39 / 6 — `3. நீத்தார் பெருமை`, குறள் 26–30
- 40 / 7 — `4. அறன் வலியுறுத்தல்`, குறள் 31–35
- 41 / 8 — `4. அறன் வலியுறுத்தல்`, குறள் 36–40

`*` `xxvi` and `xxxi` are supported by the same-source contents/sequence but the numeral is not visibly printed on those scans. This basis is explicitly documented in the relevant page records.

## Part 002 completed page records

Scans **21–27**:

- `pages/0021-mathippurai-08.md`
- `pages/0022-mathippurai-09.md`
- `pages/0023-mathippurai-10.md`
- `pages/0024-mathippurai-11.md`
- `pages/0025-mathippurai-12.md`
- `pages/0026-mathippurai-13.md`
- `pages/0027-pathippurai.md`

Scans **28–33**:

- `pages/0028-athikara-akara-varisai-01.md`
- `pages/0029-athikara-akara-varisai-02.md`
- `pages/0030-athikara-arunchol-akaravarisai-01.md`
- `pages/0031-athikara-arunchol-akaravarisai-02.md`
- `pages/0032-aram-title.md`
- `pages/0033-blank.md`

All are intentionally `needs-review`. Scans 28–29 preserve the printed authority index in source order; scans 30–31 preserve the printed term/meaning pairs. Scan 33 excludes reverse-side bleed-through from transcription and remains `needs-review` until an explicit final visual pass.

## Part 002 current count

- source pages: **21**
- page records created: **13 / 21** — scans 21–33
- `needs-review`: **13**
- `not-started`: **8** — scans 34–41
- `verified`: **0**

## Source-sensitive readings / distinctions to preserve

Earlier Part 002 first-pass readings needing later verification include:

- scan 21: `நோக்கமிம்`, `ஏஎர்`, `துன்புறூஉந்`, `இன்புறூஉம்`
- scan 22: `ஆற்றேன்இந்`, `நோயைநோய்`, `தும்மினே னாக`
- scan 23: `புத்தேளிர்`, `நீரியைந் தன்னா ரகத்து`
- scan 24 heading: **`அய். புத்தம்புது விளக்கம்`** — do not normalize to `ஐ.`
- scan 25: `அடுத்தூர்வது அஃதொப்ப தில்`
- scan 27: `தமிழர்க் கென்றே`; pagination `xxvi` is source-supported but not visibly printed

Index-section differences must also remain distinct unless the exact scan disproves them. Examples:

- scan 28 `உறுப்புநலன் அழிதல்` vs scan 30 `உறுப்பு நலன் அழிதல்`
- scan 28 `செய்ந்நன்றியறிதல்` vs scan 30 `செய்ந்நன்றி யறிதல்`
- scan 29 `நாணுத் துறவுரைத்தல்` vs scan 30 `நாணுத்துறவு உரைத்தல்`

Do not harmonize these from memory or another edition.

## Files to keep synchronized

- `works/thirukkural/metadata/source.md`
- `works/thirukkural/indexes/page-map.md`
- `works/thirukkural/README.md`
- root `README.md`
- this `HANDOVER.md`

## Next exact activity

Process **scans 34–41** from Part 002 — the first main Kural commentary body.

1. scan 34 / printed 1 — `அறம் - பாயிரம் - வழிபாடு`; குறள் 1–5 + Kalaignar commentary.
2. scan 35 / printed 2 — `வழிபாடு`; குறள் 6–10 + commentary.
3. scan 36 / printed 3 — `வான் சிறப்பு`; குறள் 11–15 + commentary.
4. scan 37 / printed 4 — `வான் சிறப்பு`; குறள் 16–20 + commentary.
5. scan 38 / printed 5 — `நீத்தார் பெருமை`; குறள் 21–25 + commentary.
6. scan 39 / printed 6 — `நீத்தார் பெருமை`; குறள் 26–30 + commentary.
7. scan 40 / printed 7 — `அறன் வலியுறுத்தல்`; குறள் 31–35 + commentary.
8. scan 41 / printed 8 — `அறன் வலியுறுத்தல்`; குறள் 36–40 + commentary.

For every page, preserve printed Kural number, line breaks, spacing, spelling, sandhi, punctuation and Kalaignar commentary exactly from this scan. Do not substitute a standard/web Kural text. Keep new records `needs-review` until a separate direct visual verification pass.

After scans 34–41 exist, Part 002 will have 21/21 page records. Then run final visual verification in small batches and create a Part 002 audit/release report.

## Source authority rule

The supplied scans remain the controlling source for this edition. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. Apparent typographical/historical forms stay as printed unless rereading this exact scan supports a correction.
