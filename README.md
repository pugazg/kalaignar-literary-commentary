# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–008 **ARCHIVAL-READY** through overall scan 169 / printed page 136 / Kural 670 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–007 **released through Kural 565**; Part 008 **EDITORIAL REVIEW COMPLETE 21/21** through Kural 670 |
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

English Parts **001–007** have completed their full release workflow continuously through Kural **565**.

### Part 008 Tamil — ARCHIVAL-READY

Part 008 covers scans **149–169 / printed pages 116–136 / Kural 566–670**. All **21 / 21** Tamil page records are directly visually verified and the separate archival audit has passed.

Audit: [`works/thirukkural/AUDIT_PART_008.md`](works/thirukkural/AUDIT_PART_008.md).

The source-visible structural transition at scan **162 / printed page 129 / Kural 631** is preserved in Tamil as:

`பொருள் — அரசியல்` → **`பொருள் — அமைச்சியல் — அமைச்சு`**.

### Part 008 English — EDITORIAL REVIEW COMPLETE

All **21 / 21** aligned Part 008 project-translation pages have completed first pass, direct source-check and editorial consistency / glossary reconciliation.

Current Part 008 English state:

- `draft`: **0**;
- `source-checked`: **0**;
- `editorial-reviewed`: **21 / 21**;
- `release-ready`: **0**.

Editorial review: [`works/thirukkural/translations/en/reviews/PART_008_REVIEW.md`](works/thirukkural/translations/en/reviews/PART_008_REVIEW.md).

The controlled main-body English headings now extend through Kural **670**. The Tamil `அரசியல்` → `அமைச்சியல்` distinction is editorially controlled as:

`Porul — Statecraft` → **`Porul — Ministerial Affairs`**.

`Ministerial Affairs` is now the controlled project rendering of `அமைச்சியல்` for this supplied main-body section, and the global English glossary has been extended accordingly.

All six Part 008 source-check corrections remain protected. Three small editorial readability refinements were made at Kurals **602, 627 and 641**; no other substantive body-text change was made.

## அடுத்த செயல்

Perform the separate **Part 008 English release gate** for all 21 `editorial-reviewed` pages.

That gate must perform the final continuity/alignment and controlled-term check, create `PART_008_RELEASE_REPORT.md` only if it passes, and only then promote the pages to `release-ready`.

Do not combine the Part 008 release gate with Part 009 Tamil transcription.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).
