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
- page records exist for **all scans 21–41**
- `verified`: **13** — scans 21–33
- `needs-review`: **8** — scans 34–41
- `not-started`: **0**

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
- 34 / 1 — `1. வழிபாடு`, குறள் 1–5 + Kalaignar commentary — needs-review
- 35 / 2 — `1. வழிபாடு`, குறள் 6–10 + commentary — needs-review
- 36 / 3 — `2. வான் சிறப்பு`, குறள் 11–15 + commentary — needs-review
- 37 / 4 — `2. வான் சிறப்பு`, குறள் 16–20 + commentary — needs-review
- 38 / 5 — `3. நீத்தார் பெருமை`, குறள் 21–25 + commentary — needs-review
- 39 / 6 — `3. நீத்தார் பெருமை`, குறள் 26–30 + commentary — needs-review
- 40 / 7 — `4. அறன் வலியுறுத்தல்`, குறள் 31–35 + commentary — needs-review
- 41 / 8 — `4. அறன் வலியுறுத்தல்`, குறள் 36–40 + commentary — needs-review

`*` `xxvi` and `xxxi` are supported by the same-source contents/sequence but the numeral is not visibly printed on those scans. This basis is explicitly documented in the relevant page records.

## Verification completed — scans 21–27

Direct visual comparison against Part 002 local PDF pages 1–7 is complete.

Each verified page uses:

- `status: "verified"`
- `transcription_method: "direct visual comparison with source scan"`
- `part: 2`
- correct `part_page` metadata and an explicit Part 002 local-page source marker

### Scans 21–26

No wording correction was required during final comparison. Source-sensitive forms explicitly rechecked and retained include:

- scan 21: `நோக்கமிம்`, `ஏஎர்`, `துன்புறூஉந்`, `இன்புறூஉம்`
- scan 22: `ஆற்றேன்இந்`, `நோயைநோய்`, `தும்மினே னாக`
- scan 23: `புத்தேளிர்`, `நீரியைந் தன்னா ரகத்து`
- scan 24: heading **`அய். புத்தம்புது விளக்கம்`**; do not normalize to `ஐ.`
- scan 25: `அடுத்தூர்வது அஃதொப்ப தில்`
- scan 26: `இற்றெனக் கிளந்து, தெற்றெனக் காட்டுவதையே`; final source word `வேண்டாவாகும்`

### Scan 27 — `பதிப்புரை`

The final visual pass found genuine first-pass errors and corrected them from the exact scan:

- `எந்நிலையையூட்டும்` → **`எந்நினைவையூட்டும்`**
- `உலக நிலையையூட்டுதல்` → **`உலக நினைவையூட்டுதல்`**
- restored source punctuation spacing: `நிகர் !`, `அதுவொன்றே நிகர் !`, `எந்நினைவையூட்டும் ?`
- preserved the printed sign-off as **`- பூம்புகார் பதிப்பகத்தார்`**

The page itself does not visibly print `xxvi`; `xxvi` remains a same-source pagination inference from the contents and `xxv → xxvii` sequence, not invented visible text.

## Verification completed — scans 28–33

Direct visual comparison against Part 002 local PDF pages 8–13 is complete.

### Scans 28–29 — `திருக்குறள் அதிகார அகர வரிசை`

Every listed authority name and authority number was checked against the scan. The source entries matched the first-pass transcription.

Source forms retained include:

- `உறுப்புநலன் அழிதல்`
- `செய்ந்நன்றியறிதல்`
- `நாணுத் துறவுரைத்தல்`
- `படர்மெலிந் திரங்கல்`
- `மன்னரைச்சேர்ந்தொழுகல்`
- `வாழ்க்கைத் துணைநலம்`

The non-source editorial heading `அதிகார எண் — தொடர்ச்சி` that had been introduced in the scan-29 Markdown was removed; the source page itself prints only the continuing index columns / column headings.

### Scans 30–31 — `அதிகார அருஞ்சொற்பொருள் அகரவரிசை`

Every term/meaning pair was directly checked. Source differences from scans 28–29 remain intentionally distinct:

- scan 28 `உறுப்புநலன் அழிதல்` vs scan 30 `உறுப்பு நலன் அழிதல்`
- scan 28 `செய்ந்நன்றியறிதல்` vs scan 30 `செய்ந்நன்றி யறிதல்`
- scan 29 `நாணுத் துறவுரைத்தல்` vs scan 30 `நாணுத்துறவு உரைத்தல்`
- scan 31 `பெண் வழிச் சேறல்` is preserved with the source's spacing
- scan 31 `படைச் செருக்கு` is preserved with the source's spacing

The non-source editorial continuation heading previously added to scan 31 was removed; the source page is a continuation of the same index without that printed heading.

### Scan 32 — `அறம்` title page

Source text confirmed exactly as:

- `திருக்குறள்`
- `கலைஞர் உரை`
- `அறம்`

No numeral is visibly printed. `xxxi` remains recorded only because Part 001 contents says `அறத்துப்பால் — xxxi` and the surrounding front-matter sequence supports it.

### Scan 33 — blank verso

Confirmed as current-page-text-free. Only reverse-side bleed-through is visible. It is now `verified`; bleed-through remains excluded from body transcription.

## Main-body forms still awaiting verification

Scans 34–41 are first-pass only. Preserve and check closely:

- scan 34: `நீடுவாழ் வார்`
- scan 36: `வானின் றுலகம்`, `உள்நின் றுடற்றும்`, `சார்வாய்மற் றாங்கே`
- scan 37: commentary phrase currently read as **`ஒழுக்கமே கெட்டகடும்`** — verify directly before changing
- scan 38: `அகல்விசும்பு ளார்கோமான்`
- scan 39: `நாற்றமென றைந்தின்`, `அறவோர்மற் றெவ்வுயிர்க்கும்`
- scan 40: `அறத்தினூஉங்கு`, `அறத்தினூஉங்`, `அழுக்கா றவாவெகுளி`
- scan 41: `அறத்தா றிதுவென`, `இன்பமற் றெல்லாம்`

## Files to keep synchronized

- `works/thirukkural/metadata/source.md`
- `works/thirukkural/indexes/page-map.md`
- `works/thirukkural/README.md`
- root `README.md`
- this `HANDOVER.md`

## Next exact activity

Run direct visual verification for **Part 002 scans 34–41**.

1. scan 34 / printed 1 — `வழிபாடு`, குறள் 1–5 + Kalaignar commentary.
2. scan 35 / printed 2 — `வழிபாடு`, குறள் 6–10 + commentary.
3. scan 36 / printed 3 — `வான் சிறப்பு`, குறள் 11–15 + commentary.
4. scan 37 / printed 4 — `வான் சிறப்பு`, குறள் 16–20 + commentary; resolve the currently uncertain commentary phrase only from this exact scan.
5. scan 38 / printed 5 — `நீத்தார் பெருமை`, குறள் 21–25 + commentary.
6. scan 39 / printed 6 — `நீத்தார் பெருமை`, குறள் 26–30 + commentary.
7. scan 40 / printed 7 — `அறன் வலியுறுத்தல்`, குறள் 31–35 + commentary.
8. scan 41 / printed 8 — `அறன் வலியுறுத்தல்`, குறள் 36–40 + commentary.
9. Preserve exact printed Kural numbers, line breaks, spelling, word joining, punctuation and Kalaignar commentary. Do not substitute a standard/web Kural text.
10. After scans 34–41 are verified, create `works/thirukkural/AUDIT_PART_002.md` and record a release decision.

## Source authority rule

The supplied scans remain the controlling source for this edition. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. Apparent typographical/historical forms stay as printed unless rereading this exact scan supports a correction.