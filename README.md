# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Part 001 archival-ready; Part 002 **21/21 records complete, 13 verified / 8 needs-review** |
| சங்கத்தமிழ் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Sangatamil | ஆங்கில மொழிபெயர்ப்பு | பின்னர் சேர்க்கப்படும் |
| குறளோவியம் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Kuraloviyam | ஆங்கில மொழிபெயர்ப்பு | பின்னர் சேர்க்கப்படும் |

## களஞ்சிய அமைப்பு

```text
README.md
LITERARY_COMMENTARY_PROCESSING_GUIDE.md
HANDOVER.md
works/
  thirukkural/
    README.md
    AUDIT_PART_001.md
    metadata/
    indexes/
    pages/
    sections/
```

ஒவ்வொரு நூலும் தனித்த `works/<work-slug>/` அடைவில் சுயமாகப் பதிவாகும். தமிழ்–ஆங்கில இணை பதிப்புகள் கிடைக்கும் நூல்களுக்கு பின்னர் இருமொழி alignment / translation-review அடுக்குகள் சேர்க்கப்படும்.

## மூலக் கொள்கை

> **ஸ்கேன் தான் அதிகாரப்பூர்வ மூல ஆதாரம். Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது. தெளிவில்லாத வாசிப்புகள் வெளிப்படையாக `needs-review`, `partial`, அல்லது `blocked` எனக் குறிக்கப்பட வேண்டும்.

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

- local PDF pages: **21**
- overall scans: **21–41**
- page records: **21 / 21**
- `verified`: **13** — scans 21–33
- `needs-review`: **8** — scans 34–41
- `not-started`: **0**

The first two Part 002 verification batches are complete. Scans 21–27 cover the end of `மதிப்புரை` and `பதிப்புரை`; scans 28–33 cover both index sections, the `அறம்` title page, and the blank verso. Source-specific index differences were preserved instead of harmonized, and scan 33 was confirmed to contain only reverse-side bleed-through rather than current-page body text.

Next activity: direct visual verification of **scans 34–41**, containing Kural **1–40** and Kalaignar's commentary across `வழிபாடு`, `வான் சிறப்பு`, `நீத்தார் பெருமை`, and `அறன் வலியுறுத்தல்`. After that, create the Part 002 audit/release report.

விரிவான நிலை: [`works/thirukkural/README.md`](works/thirukkural/README.md) மற்றும் [`works/thirukkural/indexes/page-map.md`](works/thirukkural/indexes/page-map.md).