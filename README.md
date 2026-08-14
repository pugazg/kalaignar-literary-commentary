# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–003 audited / archival-ready for supplied material |
| Thirukkural — Kalaignar's Commentary | English project translation | framework established; page translation not yet started |
| சங்கத்தமிழ் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Sangatamil | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |
| குறளோவியம் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Kuraloviyam | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |

## களஞ்சிய அமைப்பு

```text
README.md
LITERARY_COMMENTARY_PROCESSING_GUIDE.md
HANDOVER.md
works/
  thirukkural/
    README.md
    AUDIT_PART_001.md
    AUDIT_PART_002.md
    AUDIT_PART_003.md
    metadata/
    indexes/
    pages/
    sections/
    translations/
      en/
        README.md
        TRANSLATION_GUIDE.md
        GLOSSARY.md
        TRANSLATION_STATUS.md
        pages/
        reviews/
```

ஒவ்வொரு நூலும் தனித்த `works/<work-slug>/` அடைவில் சுயமாகப் பதிவாகும்.

## மூலக் கொள்கை

> **ஸ்கேன் தான் அதிகாரப்பூர்வ மூல ஆதாரம். Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது. தெளிவில்லாத வாசிப்புகள் வெளிப்படையாக `needs-review`, `partial`, அல்லது `blocked` எனக் குறிக்கப்பட வேண்டும்.

## English layers — published source vs project translation

இந்த repository இரண்டு வகை English material-ஐ தெளிவாகப் பிரிக்கிறது:

1. **Published / official English source** — தனியாக வெளியிடப்பட்ட scan/source கிடைத்தால், அதன் சொந்த pagination / wording / metadata-உடன் source-controlled edition ஆக archive செய்யப்படும்.
2. **Project-created English translation** — audited Tamil source-இலிருந்து நாம் உருவாக்கும் மொழிபெயர்ப்பு. இது எப்போதும் `translation_type: "project_translation"` என்று வெளிப்படையாகக் குறிக்கப்படும்; publisher/official translation என்று காட்டப்படாது.

Thirukkural-க்கு தற்போது இரண்டாவது வகை — **project-created English translation** — framework உருவாக்கப்பட்டுள்ளது.

## தற்போதைய நிலை — திருக்குறள்

### Part 001

`திருக்குறள்_கலைஞர்_உரை_part_001_pages_1-20.pdf`

- overall scans: **1–20**
- page records: **20 / 20**
- `verified`: **19**
- `partial`: **1** — scan 8 handwritten facsimile
- release decision: **ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**
- audit: [`works/thirukkural/AUDIT_PART_001.md`](works/thirukkural/AUDIT_PART_001.md)

### Part 002

`திருக்குறள்_கலைஞர்_உரை_part_002_pages_21-41.pdf`

- overall scans: **21–41**
- page records: **21 / 21**
- `verified`: **21 / 21**
- release decision: **ARCHIVAL-READY**
- audit: [`works/thirukkural/AUDIT_PART_002.md`](works/thirukkural/AUDIT_PART_002.md)

### Part 003

`திருக்குறள்_கலைஞர்_உரை_part_003_pages_42-62.pdf`

- local PDF pages: **21**
- overall scans: **42–62**
- printed pages: **9–29**
- Kural range: **41–145**
- page records: **21 / 21**
- `verified`: **21 / 21**
- unresolved: **0**
- release decision: **ARCHIVAL-READY**
- audit: [`works/thirukkural/AUDIT_PART_003.md`](works/thirukkural/AUDIT_PART_003.md)

The source confirms direct continuity from Part 002: scan 41 ends at printed page 8 / Kural 40, and Part 003 scan 42 begins printed page 9 / Kural 41. The currently supplied material reaches scan **62** / printed page **29** / Kural **145**.

## Thirukkural English translation framework

Framework files are now available under [`works/thirukkural/translations/en/`](works/thirukkural/translations/en/README.md).

Permanent translation cadence:

**Tamil transcription → Tamil visual verification → Tamil audit → English draft → English source-check → editorial consistency review → part-level English release report.**

This means English translation proceeds after each Tamil part becomes archival-ready rather than waiting for the entire book.

Current English production status:

- framework: **established**
- English page files: **0**
- next translation batch: **Part 001 scans 1–7**

Next activity: begin Part 001 English first-pass translation in one-to-one page-aligned `draft` files.

விரிவான நிலை: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), மற்றும் [`works/thirukkural/indexes/page-map.md`](works/thirukkural/indexes/page-map.md).
