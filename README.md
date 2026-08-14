# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–003 audited / archival-ready for supplied material |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–002 released; Part 003 **14/21 first-pass drafts complete** |
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
- release decision: **RELEASE-READY**

Review/release artefacts:

- [`works/thirukkural/translations/en/reviews/PART_002_REVIEW.md`](works/thirukkural/translations/en/reviews/PART_002_REVIEW.md)
- [`works/thirukkural/translations/en/reviews/PART_002_RELEASE_REPORT.md`](works/thirukkural/translations/en/reviews/PART_002_RELEASE_REPORT.md)

### Part 003 English — FIRST PASS IN PROGRESS

- English pages: **14 / 21** — scans 42–55
- `draft`: **14**
- current English coverage: Kural **41–110**
- remaining first-pass pages: **7** — scans 56–62

The completed Part 003 drafts currently cover **Domestic Life**, **The Worth of a Life Partner**, **The Blessing of Children**, **Love**, **Hospitality**, **Speaking Pleasant Words**, and **Gratitude for Help Received**. Kalaignar's commentary remains the primary interpretive aid; no published English Kural wording or outside commentary is imported.

Source-sensitive draft choices remain visible for later checking—for example Kural 86's **heaven of fame**, Kural 87's hospitality-as-**sacrifice**, Kural 101's unbidden-help reading, and Kural 107's explanation that seven-times-seven generations/births signifies remembrance without a time limit. Repeated Kurals **83, 94 and 98** retain their already released Part 002 wording.

Next English activity: complete **Part 003 first-pass translation with scans 56–62**, covering Kural **111–145**: **Impartiality**, **Self-Control**, **Good Conduct**, and the supplied beginning of **Not Desiring Another Man's Wife**. Keep all remaining pages as `draft`; source-check begins only after the full Part 003 first pass reaches **21/21**.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md) and [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md).
