# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–009 **ARCHIVAL-READY** continuously through overall scan 191 / printed page 158 / Kural 780 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–008 **released through Kural 670**; Part 009 **EDITORIAL-REVIEWED 22/22** through Kural 780, release pending |
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

Tamil Parts **001–009** are audited / archival-ready continuously through overall scan **191** / printed page **158** / Kural **780**.

English Parts **001–008** have completed their full release workflow continuously through Kural **670**.

Part 009 English covers scans **170–191 / printed pages 137–158 / Kural 671–780**. Its first pass, direct source-check and editorial consistency / glossary reconciliation are complete; all **22 / 22** English pages are now `editorial-reviewed`. Review: [`works/thirukkural/translations/en/reviews/PART_009_REVIEW.md`](works/thirukkural/translations/en/reviews/PART_009_REVIEW.md).

The controlled Part 009 section sequence is:

`அமைச்சியல்` → **Ministerial Affairs** → `அரணியல்` → **Fortification Affairs** → `கூழியல்` → **Wealth** → `படையியல்` → **Military Affairs**.

Chapter 71 `குறிப்பறிதல்` is controlled as **Understanding Signs**; the earlier project-added `(Porul)` disambiguator has been removed. No substantive Kural/commentary body-text change was made during the Part 009 editorial gate.

Protected source-check and source-sensitive decisions remain intact, including Kural 680, 691, 717, the unusual Kural 725 and 733 commentary bases, Kural 771's **memorial stones** image, and Kural 773's **great manliness / manliness** framing.

Part 010 remains untranscribed; its first page was inspected previously only to establish continuity at printed page **159 / Kural 781 / chapter 79 `நட்பு`**.

## அடுத்த செயல்

Perform the separate **Part 009 English release gate** for all **22 `editorial-reviewed` pages**. Create `works/thirukkural/translations/en/reviews/PART_009_RELEASE_REPORT.md` only after the final continuity/alignment check passes, then promote the pages to `release-ready`.

Do not begin Part 010 Tamil transcription during the same activity.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).
