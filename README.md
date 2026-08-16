# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–008 **ARCHIVAL-READY** through Kural 670; Part 009 Tamil verification **COMPLETE 22/22** through Kural 780, audit pending |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–008 **released through Kural 670** |
| சங்கத்தமிழ் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Sangatamil | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |
| குறளோவியம் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Kuraloviyam | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |

## மூலக் கொள்கை

> **ஸ்கேன் தான் அதிகாரப்பூர்வ மூல ஆதாரம். Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது.

## English layers — published source vs project translation

1. **Published / official English source** — தனியாக வெளியிடப்பட்ட source கிடைத்தால், அதன் சொந்த pagination / wording / metadata-உடன் source-controlled edition ஆக archive செய்யப்படும்.
2. **Project-created English translation** — audited Tamil source-இலிருந்து உருவாக்கப்படும் மொழிபெயர்ப்பு; `translation_type: "project_translation"` என்று வெளிப்படையாகக் குறிக்கப்படும்.

The project translation follows an explicit fidelity rule: **retain Kalaignar's own language, images and interpretive direction; do not replace them with familiar standard Kural interpretations.**

## தற்போதைய நிலை — திருக்குறள்

Tamil Parts **001–008** are audited / archival-ready continuously through:

- overall scan **169**;
- printed page **136**;
- Kural **670**.

Part 009 Tamil is fully transcribed and directly visually verified through:

- overall scan **191**;
- printed page **158**;
- Kural **780**;

but its separate Tamil audit has **not yet been performed**, so Part 009 is not yet archival-ready.

English Parts **001–008** have completed their full release workflow continuously through Kural **670**.

### Part 008 — completed baseline

Part 008 Tamil covers scans **149–169 / printed pages 116–136 / Kural 566–670** and is **ARCHIVAL-READY**. Audit: [`works/thirukkural/AUDIT_PART_008.md`](works/thirukkural/AUDIT_PART_008.md).

Part 008 English is **RELEASE COMPLETE 21/21**. Review/release artefacts:

- [`works/thirukkural/translations/en/reviews/PART_008_REVIEW.md`](works/thirukkural/translations/en/reviews/PART_008_REVIEW.md)
- [`works/thirukkural/translations/en/reviews/PART_008_RELEASE_REPORT.md`](works/thirukkural/translations/en/reviews/PART_008_RELEASE_REPORT.md)

The controlled structural distinction remains `பொருள் — அரசியல்` → `பொருள் — அமைச்சியல்`, released in English as `Porul — Statecraft` → **`Porul — Ministerial Affairs`**.

### Part 009 Tamil — DIRECT VISUAL VERIFICATION COMPLETE

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_009_pages_170-191.pdf`

Verified scope and state:

- physical pages: **22**;
- scans **170–191**;
- printed pages **137–158**;
- Kural **671–780**;
- chapters **68–78**;
- `verified`: **22 / 22**;
- `needs-review`: **0**;
- `partial`: **0**;
- `blocked`: **0**;
- Tamil audit: **not started**.

The source-visible Part 009 structural transitions are preserved:

- `பொருள் — அமைச்சியல்` through scan 181;
- `பொருள் — அரணியல்` from scan 182;
- `பொருள் — கூழியல்` from scan 186;
- `பொருள் — படையியல்` from scan 188.

Direct verification found one first-pass correction at **scan 190 / Kural 771 commentary**: `நடுகல்லைப் போனவர்கள்` was corrected to the scan-supported **`நடுகல்லாய்ப் போனவர்கள்`**.

Three unusual source readings were visually confirmed and deliberately retained: Kural **717** (`கற்றறிந்தார் ... சொற்றெரிதல் ... இழுக்கு`), Kural **725 commentary** (`தருக்கமென்படும் அளவைக் திறமும்`), and Kural **733 commentary** (`மளவுக்கு வளம்`). They must not be silently normalized from another edition or expected grammar.

## அடுத்த செயல்

Perform the separate **Part 009 Tamil audit / archival-ready gate** across all **22 verified pages**, scans **170–191 / printed pages 137–158 / Kural 671–780**.

Create `works/thirukkural/AUDIT_PART_009.md` only during that audit. Declare Part 009 archival-ready only if the audit passes. Keep the gates separate: **do not begin Part 009 English translation or Part 010 Tamil transcription during the audit activity.**

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).
