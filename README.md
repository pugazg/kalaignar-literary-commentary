# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–003 audited / archival-ready for supplied material |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–002 released; Part 003 not started |
| சங்கத்தமிழ் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Sangatamil | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |
| குறளோவியம் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Kuraloviyam | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |

## மூலக் கொள்கை

> **ஸ்கேன் தான் அதிகாரப்பூர்வ மூல ஆதாரம். Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது.

## English layers — published source vs project translation

இந்த repository இரண்டு வகை English material-ஐ தெளிவாகப் பிரிக்கிறது:

1. **Published / official English source** — தனியாக வெளியிடப்பட்ட source கிடைத்தால், அதன் சொந்த pagination / wording / metadata-உடன் source-controlled edition ஆக archive செய்யப்படும்.
2. **Project-created English translation** — audited Tamil source-இலிருந்து உருவாக்கப்படும் மொழிபெயர்ப்பு; `translation_type: "project_translation"` என்று வெளிப்படையாகக் குறிக்கப்படும்.

The project translation follows an explicit fidelity rule: **retain Kalaignar's own language, images and interpretive direction; do not replace them with familiar standard Kural interpretations.** The same source-first discipline applies to Nannan, publisher prose, indexes and source glossaries.

## தற்போதைய நிலை — திருக்குறள்

Tamil Parts 001–003 are archival-ready for the supplied material. The Tamil archive currently reaches overall scan **62** / printed page **29** / Kural **145**.

### Part 001 English — RELEASE COMPLETE

- aligned English pages: **20 / 20**
- `release-ready`: **19**
- `source-limited`: **1** — scan 8
- release decision: **RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS**

### Part 002 English — RELEASE COMPLETE

- aligned English pages: **21 / 21**
- `release-ready`: **21** — scans 21–41
- `editorial-reviewed`: **0**
- `source-checked`: **0**
- `draft`: **0**
- release decision: **RELEASE-READY**

The released Part 002 layer preserves Kalaignar's own source-sensitive readings rather than conventional external interpretations. The full chapter index remains an index-local project translation, this edition's own glossary remains a distinct source layer, and Nannan's source metaphors remain intact.

The cross-part `அடுத்தூர்வது அஃதொப்பதில்` decision remains explicit: Part 002 uses **“nothing equals that for driving it away”** from the complete Kural and Nannan's adjacent explanation, while released Part 001 scan 19 remains unchanged with the compact phrase retained in Tamil.

Review/release artefacts:

- [`works/thirukkural/translations/en/reviews/PART_002_REVIEW.md`](works/thirukkural/translations/en/reviews/PART_002_REVIEW.md)
- [`works/thirukkural/translations/en/reviews/PART_002_RELEASE_REPORT.md`](works/thirukkural/translations/en/reviews/PART_002_RELEASE_REPORT.md)

### Part 003 English

Not yet started. Tamil scans **42–62** are already audited / archival-ready and contain Kural **41–145** plus Kalaignar's commentary.

Next English activity: begin **Part 003 first-pass translation with scans 42–48**, covering Kural **41–75**. Create matching English pages as `draft`, preserve Kalaignar's commentary as the primary interpretive aid, and do not import published English Kural wording or outside commentary.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md) and [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md).
