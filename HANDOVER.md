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
- page records now exist for **all scans 21–41**
- `needs-review`: **21**
- `verified`: **0**
- `not-started`: **0**

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
- 34 / 1 — `1. வழிபாடு`, குறள் 1–5 + Kalaignar commentary
- 35 / 2 — `1. வழிபாடு`, குறள் 6–10 + commentary
- 36 / 3 — `2. வான் சிறப்பு`, குறள் 11–15 + commentary
- 37 / 4 — `2. வான் சிறப்பு`, குறள் 16–20 + commentary
- 38 / 5 — `3. நீத்தார் பெருமை`, குறள் 21–25 + commentary
- 39 / 6 — `3. நீத்தார் பெருமை`, குறள் 26–30 + commentary
- 40 / 7 — `4. அறன் வலியுறுத்தல்`, குறள் 31–35 + commentary
- 41 / 8 — `4. அறன் வலியுறுத்தல்`, குறள் 36–40 + commentary

`*` `xxvi` and `xxxi` are supported by the same-source contents/sequence but the numeral is not visibly printed on those scans. This basis is explicitly documented in the relevant page records.

## Part 002 completed page records

Scans 21–33 already existed from earlier rounds. The latest round added:

- `works/thirukkural/pages/0034-aram-vazhipadu-01.md`
- `works/thirukkural/pages/0035-aram-vazhipadu-02.md`
- `works/thirukkural/pages/0036-aram-vaan-sirappu-01.md`
- `works/thirukkural/pages/0037-aram-vaan-sirappu-02.md`
- `works/thirukkural/pages/0038-aram-neeththar-perumai-01.md`
- `works/thirukkural/pages/0039-aram-neeththar-perumai-02.md`
- `works/thirukkural/pages/0040-aram-aran-valiyuruththal-01.md`
- `works/thirukkural/pages/0041-aram-aran-valiyuruththal-02.md`

All Part 002 page records intentionally use:

- `status: "needs-review"`
- `transcription_method: "first-pass direct visual transcription from source scan; source scan remains authoritative"`

Do not promote any Part 002 record to `verified` until a separate direct visual verification pass.

## Source-sensitive readings / distinctions to preserve

Earlier Part 002 first-pass readings needing later verification include:

- scan 21: `நோக்கமிம்`, `ஏஎர்`, `துன்புறூஉந்`, `இன்புறூஉம்`
- scan 22: `ஆற்றேன்இந்`, `நோயைநோய்`, `தும்மினே னாக`
- scan 23: `புத்தேளிர்`, `நீரியைந் தன்னா ரகத்து`
- scan 24 heading: **`அய். புத்தம்புது விளக்கம்`** — do not normalize to `ஐ.`
- scan 25: `அடுத்தூர்வது அஃதொப்ப தில்`
- scan 27: `தமிழர்க் கென்றே`; pagination `xxvi` is source-supported but not visibly printed

Index-section differences must remain distinct unless the exact scan disproves them. Examples:

- scan 28 `உறுப்புநலன் அழிதல்` vs scan 30 `உறுப்பு நலன் அழிதல்`
- scan 28 `செய்ந்நன்றியறிதல்` vs scan 30 `செய்ந்நன்றி யறிதல்`
- scan 29 `நாணுத் துறவுரைத்தல்` vs scan 30 `நாணுத்துறவு உரைத்தல்`

New main-body forms needing close verification include:

- scan 34: Kural spacing/forms such as `நீடுவாழ் வார்`
- scan 36: `வானின் றுலகம்`, `உள்நின் றுடற்றும்`, `சார்வாய்மற் றாங்கே`
- scan 37: commentary phrase currently read as **`ஒழுக்கமே கெட்டகடும்`** — verify character-by-character from the exact scan before any correction
- scan 38: `அகல்விசும்பு ளார்கோமான்`
- scan 39: `நாற்றமென றைந்தின்`, `அறவோர்மற் றெவ்வுயிர்க்கும்`
- scan 40: `அறத்தினூஉங்கு`, `அறத்தினூஉங்`, `அழுக்கா றவாவெகுளி`
- scan 41: `அறத்தா றிதுவென`, `இன்பமற் றெல்லாம்`

Do not harmonize any of these from memory or another edition.

## Files to keep synchronized

- `works/thirukkural/metadata/source.md`
- `works/thirukkural/indexes/page-map.md`
- `works/thirukkural/README.md`
- root `README.md`
- this `HANDOVER.md`

## Next exact activity

Run **Part 002 direct visual verification**, beginning with scans **21–27**.

1. Compare each page character-by-character against the supplied scan.
2. Correct only differences supported by this exact scan.
3. Preserve headings, punctuation, Kural line breaks, spacing, historical/typographical forms and source-specific wording.
4. Keep reverse-side bleed-through separate from current-page text.
5. After scans 21–27 are verified, proceed to scans 28–33, then scans 34–41.
6. When all Part 002 pages are reviewed, create `works/thirukkural/AUDIT_PART_002.md` and record a release decision.

## Source authority rule

The supplied scans remain the controlling source for this edition. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. Apparent typographical/historical forms stay as printed unless rereading this exact scan supports a correction.
