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

## Reference implementation

`pugazg/tolkappiyap-poonga`

Core rules: scan authority, one record per scan page, stable filenames, explicit review status, metadata/manifests, no silent normalization, and visible uncertainty.

# திருக்குறள் — current state

## Supplied source parts

### Part 001

`திருக்குறள்_கலைஞர்_உரை_part_001_pages_1-20.pdf`

- local pages: 20
- overall scans: 1–20
- audit complete
- release decision: **ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**
- `verified`: 19
- `partial`: 1 — scan 8 handwritten facsimile
- audit report: `works/thirukkural/AUDIT_PART_001.md`

Do not redo or renumber Part 001.

### Part 002

`திருக்குறள்_கலைஞர்_உரை_part_002_pages_21-41.pdf`

- local PDF pages: **21**
- overall scan range: **21–41**
- local page 1 / overall scan 21 carries printed page **xx**, directly following Part 001 scan 20 / printed page xix
- Part 002 is therefore a confirmed consecutive continuation of the same source edition

## Part 002 scan map

- scan 21 / printed xx — மதிப்புரை: source examples / `ஈ. உரைக் குறள்` / `உ. இடைமிடை சொல்நலம்`
- scan 22 / printed xxi — `ஊ. தெளிவு`, `எ. சுருக்க விளக்கம்`, `ஏ. புதுப்பொருள்`
- scan 23 / printed xxii — புதுப்பொருள் continuation
- scan 24 / printed xxiii — `அய். புத்தம்புது விளக்கம்`, `ஒ. நுண்மாண் நுழைபுலம்`
- scan 25 / printed xxiv — நுண்மாண் நுழைபுலம் continuation / `6. நன்றி`
- scan 26 / printed xxv — `நன்றி` continuation and conclusion of மதிப்புரை
- scan 27 — `பதிப்புரை`, signed `பூம்புகார் பதிப்பகத்தார்`; printed numeral not visible, but `xxvi` is supported by contents + xxv → xxvii sequence
- scans 28–29 / xxvii–xxviii — `திருக்குறள் அதிகார அகர வரிசை`
- scans 30–31 / xxix–xxx — `அதிகார அருஞ்சொற்பொருள் அகரவரிசை`
- scan 32 — `திருக்குறள் / கலைஞர் உரை / அறம்` section-title page; `xxxi` supported by contents/sequence though numeral not visible
- scan 33 — visually blank verso with reverse-side bleed-through
- scan 34 / printed 1 — `அறம் - பாயிரம் - வழிபாடு`; `1. வழிபாடு`, குறள் 1–5
- scan 35 / printed 2 — `1. வழிபாடு`, குறள் 6–10
- scan 36 / printed 3 — `2. வான் சிறப்பு`, குறள் 11–15
- scan 37 / printed 4 — `2. வான் சிறப்பு`, குறள் 16–20
- scan 38 / printed 5 — `3. நீத்தார் பெருமை`, குறள் 21–25
- scan 39 / printed 6 — `3. நீத்தார் பெருமை`, குறள் 26–30
- scan 40 / printed 7 — `4. அறன் வலியுறுத்தல்`, குறள் 31–35
- scan 41 / printed 8 — `4. அறன் வலியுறுத்தல்`, குறள் 36–40

## Part 002 work completed in current round

Created first-pass page records for scans **21–27**:

- `works/thirukkural/pages/0021-mathippurai-08.md`
- `works/thirukkural/pages/0022-mathippurai-09.md`
- `works/thirukkural/pages/0023-mathippurai-10.md`
- `works/thirukkural/pages/0024-mathippurai-11.md`
- `works/thirukkural/pages/0025-mathippurai-12.md`
- `works/thirukkural/pages/0026-mathippurai-13.md`
- `works/thirukkural/pages/0027-pathippurai.md`

All seven are intentionally:

- `status: "needs-review"`
- `transcription_method: "first-pass direct visual transcription from source scan; source scan remains authoritative"`

Do not promote them to `verified` until a separate direct visual verification pass.

## Part 002 current count

- source pages: **21**
- page records created: **7 / 21**
- `needs-review`: **7** — scans 21–27
- `not-started`: **14** — scans 28–41
- `verified`: **0** in Part 002

## Source-sensitive first-pass readings to verify later

These are deliberately retained from the exact scan and should be checked during final visual verification rather than normalized from another Thirukkural edition:

- scan 21: `நோக்கமிம்`, `ஏஎர்`, `துன்புறூஉந்`, `இன்புறூஉம்`
- scan 22: `ஆற்றேன்இந்`, `நோயைநோய்`; the printed Kural line appears as `தும்மினே னாக`; commentary quote/punctuation must be rechecked visually
- scan 23: `புத்தேளிர்`, `நீரியைந் தன்னா ரகத்து`
- scan 24: heading is visibly **`அய். புத்தம்புது விளக்கம்`**, not silently normalized to `ஐ.`; also preserve source Kural spacing
- scan 25: `அடுத்தூர்வது அஃதொப்ப தில்`; quote `இதற்கிணையாகக் கூறக்கூடிய பொது அறநூல் பிறிதேதுமில்லை`
- scan 26: source phrasing around `இற்றெனக் கிளந்து, தெற்றெனக் காட்டுவதையே` and final `வேண்டாவாகும்` should receive close verification
- scan 27: source wording includes `தமிழர்க் கென்றே`; pagination `xxvi` is inferred from same-source contents/sequence, not visibly printed on the page

## Files synchronized for Part 002 startup

- `works/thirukkural/metadata/source.md`
- `works/thirukkural/indexes/page-map.md`
- `works/thirukkural/README.md`
- this `HANDOVER.md`

## Next exact activity

Process **scans 28–33** from Part 002.

1. scan 28 / xxvii — transcribe first page of `திருக்குறள் அதிகார அகர வரிசை` exactly in source order.
2. scan 29 / xxviii — transcribe second page of that index.
3. scan 30 / xxix — transcribe first page of `அதிகார அருஞ்சொற்பொருள் அகரவரிசை`.
4. scan 31 / xxx — transcribe second page.
5. scan 32 — create the `அறம்` section-title record; note that `xxxi` comes from contents/sequence and is not visibly printed on the page.
6. scan 33 — create the blank-page record; do **not** transcribe reverse-side bleed-through.
7. Keep new textual records `needs-review` until a later verification pass.
8. After scans 28–33, proceed to main body scans 34–41 (Kural 1–40 + Kalaignar commentary).
9. After all 21 Part 002 records exist, conduct direct visual verification in small batches, then create a Part 002 audit/release report.

## Source authority rule

The supplied scans remain the controlling source for this edition. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. Do not substitute web/standard-edition Kural text. Apparent typographical or historical forms stay as printed unless rereading this exact scan supports a correction.
