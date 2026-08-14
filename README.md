# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–003 audited / archival-ready for supplied material |
| Thirukkural — Kalaignar's Commentary | English project translation | Part 001 **20/20 aligned; 19 source-checked + 1 source-limited** |
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

## தற்போதைய நிலை — திருக்குறள்

Tamil Parts 001–003 are archival-ready for the supplied material. The Tamil archive currently reaches overall scan **62** / printed page **29** / Kural **145**.

Audits:

- [`works/thirukkural/AUDIT_PART_001.md`](works/thirukkural/AUDIT_PART_001.md)
- [`works/thirukkural/AUDIT_PART_002.md`](works/thirukkural/AUDIT_PART_002.md)
- [`works/thirukkural/AUDIT_PART_003.md`](works/thirukkural/AUDIT_PART_003.md)

## Thirukkural English project translation

Framework: [`works/thirukkural/translations/en/`](works/thirukkural/translations/en/README.md)

Permanent cadence:

**Tamil transcription → Tamil visual verification → Tamil audit → English draft → English source-check → editorial consistency review → part-level English release report.**

Current Part 001 English status:

- aligned English page files: **20 / 20**
- `source-checked`: **19** — scans 1–7 and 9–20
- `source-limited`: **1** — scan 8; alignment check complete
- `draft`: **0**
- `editorial-reviewed`: **0**
- `release-ready`: **0**

The Part 001 English source-check stage is now complete. The final batch, scans 13–20, corrected only source-supported fidelity issues and retained unresolved source-sensitive wording explicitly rather than forcing an external interpretation. In particular, scan 19 now preserves `அடுத்தூர்வது அஃதொப்பதில்` in Tamil after withdrawing the insecure first-pass English expansion.

Next English activity: run the full **Part 001 editorial-consistency / glossary reconciliation pass**, document decisions in `works/thirukkural/translations/en/reviews/PART_001_REVIEW.md`, and only then promote eligible pages to `editorial-reviewed`.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md) and [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md).
