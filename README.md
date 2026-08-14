# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | part 001 — 20/20 page records; verification நடைபெற வேண்டும் |
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
    metadata/
    indexes/
    pages/
    sections/
```

ஒவ்வொரு நூலும் தனித்த `works/<work-slug>/` அடைவில் சுயமாகப் பதிவாகும். தமிழ்–ஆங்கில இணை பதிப்புகள் கிடைக்கும் நூல்களுக்கு பின்னர் இருமொழி alignment / translation-review அடுக்குகள் சேர்க்கப்படும்.

## மூலக் கொள்கை

> **ஸ்கேன் தான் அதிகாரப்பூர்வ மூல ஆதாரம். Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது. தெளிவில்லாத வாசிப்புகள் வெளிப்படையாக `needs-review`, `partial`, அல்லது `blocked` எனக் குறிக்கப்பட வேண்டும்.

## தற்போதைய செயல் — திருக்குறள்

முதல் கிடைத்த ஸ்கேன் தொகுதி: `திருக்குறள்_கலைஞர்_உரை_part_001_pages_1-20.pdf` — **20 ஸ்கேன் பக்கங்கள்**.

- 20 / 20 page records உருவாக்கப்பட்டுள்ளன.
- scans 1–6: `verified`
- scan 7: `needs-review`
- scan 8 handwritten facsimile: `partial`
- scans 9–20: source-based first-pass transcription complete; `needs-review`

அடுத்த செயல்: scans **7–20**-க்கு direct visual verification செய்து, scan ஆதரிக்கும் வடிவங்களையே வைத்துக் கொண்டு ஒவ்வொரு பக்கத்தையும் `verified` நிலைக்கு நகர்த்துதல்.

விரிவான நிலை: [`works/thirukkural/README.md`](works/thirukkural/README.md) மற்றும் [`works/thirukkural/indexes/page-map.md`](works/thirukkural/indexes/page-map.md).
