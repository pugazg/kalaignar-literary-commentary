# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–009 **ARCHIVAL-READY** continuously through overall scan 191 / printed page 158 / Kural 780 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–008 **released through Kural 670**; Part 009 eligible for English first pass |
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

Tamil Parts **001–009** are audited / archival-ready continuously through:

- overall scan **191**;
- printed page **158**;
- Kural **780**.

English Parts **001–008** have completed their full release workflow continuously through Kural **670**.

### Part 008 — completed English baseline

Part 008 Tamil covers scans **149–169 / printed pages 116–136 / Kural 566–670** and is **ARCHIVAL-READY**. Audit: [`works/thirukkural/AUDIT_PART_008.md`](works/thirukkural/AUDIT_PART_008.md).

Part 008 English is **RELEASE COMPLETE 21/21**. Review/release artefacts:

- [`works/thirukkural/translations/en/reviews/PART_008_REVIEW.md`](works/thirukkural/translations/en/reviews/PART_008_REVIEW.md)
- [`works/thirukkural/translations/en/reviews/PART_008_RELEASE_REPORT.md`](works/thirukkural/translations/en/reviews/PART_008_RELEASE_REPORT.md)

The controlled structural distinction remains `பொருள் — அரசியல்` → `பொருள் — அமைச்சியல்`, released in English as `Porul — Statecraft` → **`Porul — Ministerial Affairs`**.

### Part 009 Tamil — ARCHIVAL-READY

Part 009 source:

`திருக்குறள்_கலைஞர்_உரை_part_009_pages_170-191.pdf`

Final audited scope:

- **22 / 22** physical pages;
- scans **170–191**;
- printed pages **137–158**;
- Kural **671–780**;
- chapters **68–78**;
- `verified`: **22 / 22**;
- `needs-review`: **0**;
- `partial`: **0**;
- `blocked`: **0**;
- audit decision: **ARCHIVAL-READY**.

Audit: [`works/thirukkural/AUDIT_PART_009.md`](works/thirukkural/AUDIT_PART_009.md).

The source-visible structural sequence in Part 009 is preserved as:

`அமைச்சியல்` → `அரணியல்` → `கூழியல்` → `படையியல்`.

Direct visual verification found one real first-pass correction at **scan 190 / Kural 771 commentary**:

`நடுகல்லைப் போனவர்கள்` → **`நடுகல்லாய்ப் போனவர்கள்`**.

The audit also protects three visually confirmed source readings that must not be silently normalized:

- Kural **717**: `கற்றறிந்தார் கல்வி விளங்கும் கசடறச் / சொற்றெரிதல் முன்னர் இழுக்கு.`;
- Kural **725 commentary**: `தருக்கமென்படும் அளவைக் திறமும்`;
- Kural **733 commentary**: `மளவுக்கு வளம்`.

Adjacent source continuity is established at both boundaries:

- Part 008 printed **136** / Kural **670** → Part 009 printed **137** / Kural **671**;
- Part 009 printed **158** / Kural **780** → supplied Part 010 printed **159** / Kural **781**, chapter `79. நட்பு`.

Part 010 remains untranscribed.

## அடுத்த செயல்

Begin **Part 009 English project translation — first pass** for the **22 aligned pages**, scans **170–191 / Kural 671–780**.

English pages must be created as `draft` project translations only. Before translation, use the English translation guide, glossary, current translation status, Part 008 review/release artefacts and the new Part 009 Tamil audit. Preserve Kalaignar's language, direct images, institutional/social vocabulary, structural distinctions and the source-sensitive readings documented in the audit.

Do not combine the first pass with English source-check, editorial review or release, and do not begin Part 010 Tamil transcription during that activity.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).