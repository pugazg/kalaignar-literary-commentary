# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–002 archival-ready; Part 003 **21/21 records, 14 verified** |
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
    AUDIT_PART_002.md
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
- `verified`: **14** — scans 42–55
- `needs-review`: **7** — scans 56–62
- `not-started`: **0**

The source itself confirms direct continuity from Part 002: scan 41 ends at printed page 8 / Kural 40, and Part 003 scan 42 begins printed page 9 / Kural 41.

Part 003 first-pass transcription is complete through Kural **145**. Direct visual verification is complete through scan **55** / printed page **22** / Kural **110**. Verification batches 42–48 and 49–55 matched the source without requiring text corrections.

Next activity: finish direct visual verification with **scans 56–62**, then create `AUDIT_PART_003.md`.

விரிவான நிலை: [`works/thirukkural/README.md`](works/thirukkural/README.md) மற்றும் [`works/thirukkural/indexes/page-map.md`](works/thirukkural/indexes/page-map.md).
