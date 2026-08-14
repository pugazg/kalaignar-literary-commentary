# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Part 001 archival-ready — 19 verified + 1 reviewed partial |
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

முதல் கிடைத்த ஸ்கேன் தொகுதி: `திருக்குறள்_கலைஞர்_உரை_part_001_pages_1-20.pdf` — **20 ஸ்கேன் பக்கங்கள்**.

- 20 / 20 page records உருவாக்கப்பட்டுள்ளன.
- `verified`: **19**
- `needs-review`: **0**
- `partial`: **1** — scan 8 handwritten facsimile; high-resolution review complete
- duplicate / missing page records: **0**

Part 001 release/audit pass முடிந்தது. தீர்மானம்:

**ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**

Scan 8 unprocessed page அல்ல. தலைப்பு, கையொப்பம், `27/12/2007` தேதி உறுதியாகப் பதிவாகியுள்ளன; body handwriting கிடைத்த scan quality-ல் source-faithful ஆக முழுமையாக வாசிக்க முடியாததால் அது திட்டமிட்டு `partial` ஆக வைக்கப்பட்டுள்ளது.

Audit report: [`works/thirukkural/AUDIT_PART_001.md`](works/thirukkural/AUDIT_PART_001.md).

அடுத்த செயல்: **அடுத்த Thirukkural source PDF batch** கிடைக்கும் போது தொடருதல்; அல்லது scan 8-ன் தெளிவான facsimile கிடைத்தால் அந்தப் பக்கத்தை மட்டும் மீண்டும் திறத்தல்.

விரிவான நிலை: [`works/thirukkural/README.md`](works/thirukkural/README.md) மற்றும் [`works/thirukkural/indexes/page-map.md`](works/thirukkural/indexes/page-map.md).
