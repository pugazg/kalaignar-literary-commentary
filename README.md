# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–003 audited / archival-ready for supplied material |
| Thirukkural — Kalaignar's Commentary | English project translation | Part 001 released; Part 002 **7/21 drafts complete** |
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

### Part 001 English — RELEASE COMPLETE

- aligned English page files: **20 / 20**
- `release-ready`: **19** — scans 1–7 and 9–20
- `source-limited`: **1** — scan 8

Release decision: **RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS**.

Review artefacts:

- [`works/thirukkural/translations/en/reviews/PART_001_REVIEW.md`](works/thirukkural/translations/en/reviews/PART_001_REVIEW.md)
- [`works/thirukkural/translations/en/reviews/PART_001_RELEASE_REPORT.md`](works/thirukkural/translations/en/reviews/PART_001_RELEASE_REPORT.md)

### Part 002 English — FIRST PASS IN PROGRESS

- aligned English page files: **7 / 21**
- `draft`: **7** — scans 21–27
- source-check/editorial/release: not yet started

Scans **21–26** complete Professor Ma. Nannan's **Critical Appreciation** in first-pass English, and scan **27** contains the **Publisher's Note**. The controlled glossary has been extended for the new analytical headings and source-sensitive terms.

Review-sensitive items remain explicit rather than silently resolved: scan 25 now provides the complete quoted Kural containing `அடுத்தூர்வது அஃதொப்பதில்`, with a provisional Part 002 English rendering pending source-check; scan 26 retains `மக்கள் நெஞ்சின் மலிவுப் பதிப்பு` with a contextual gloss; scan 27 records printed page **xxvi** as a same-source pagination inference because the numeral is not visibly printed.

### Part 003 English

Not yet started. Tamil scans **42–62** are already audited / archival-ready.

Next English activity: continue **Part 002 scans 28–33**, covering the alphabetical chapter index, chapter-term glossary index, `அறம்` title page, and blank verso. Kural 1–40 translation begins only after those six records are complete.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md) and [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md).
