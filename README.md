# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–003 audited / archival-ready for supplied material |
| Thirukkural — Kalaignar's Commentary | English project translation | Part 001 released; Part 002 **21/21 editorial-reviewed; release gate pending** |
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

### Part 002 English — EDITORIAL REVIEW COMPLETE

- aligned English pages: **21 / 21**
- `editorial-reviewed`: **21** — scans 21–41
- `source-checked`: **0**
- `draft`: **0**
- release gate: pending

The completed Part 002 editorial review preserves Kalaignar's own source-sensitive readings instead of conventional external interpretations. The full chapter index remains an index-local project translation, this edition's own glossary remains a distinct source layer, and source-specific expressions such as **“the low-priced edition of the people's hearts”** remain intact rather than being smoothed into different imagery.

The cross-part `அடுத்தூர்வது அஃதொப்பதில்` decision is explicit: Part 002 uses **“nothing equals that for driving it away”** from the complete Kural and Nannan's adjacent explanation, while released Part 001 scan 19 remains unchanged with the compact phrase retained in Tamil.

Review artefact: [`works/thirukkural/translations/en/reviews/PART_002_REVIEW.md`](works/thirukkural/translations/en/reviews/PART_002_REVIEW.md).

### Part 003 English

Not yet started. Tamil scans **42–62** are already audited / archival-ready.

Next English activity: perform the separate **Part 002 release gate**, create `PART_002_RELEASE_REPORT.md`, and—if all checks pass—promote the 21 Part 002 pages to `release-ready`. Do not begin Part 003 English in the same activity.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md) and [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md).
