# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–009 **ARCHIVAL-READY** continuously through overall scan 191 / printed page 158 / Kural 780 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–008 **released through Kural 670**; Part 009 first-pass **COMPLETE 22/22 `draft`** through Kural 780 |
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

Part 009 English has completed its **first-pass translation** across all **22 aligned pages**, scans **170–191 / printed pages 137–158 / Kural 671–780**. All 22 Part 009 English records remain `draft`; direct source-check has not yet begun.

### Part 009 Tamil — ARCHIVAL-READY

Audit: [`works/thirukkural/AUDIT_PART_009.md`](works/thirukkural/AUDIT_PART_009.md).

The source-visible structural sequence is preserved as:

`அமைச்சியல்` → `அரணியல்` → `கூழியல்` → `படையியல்`.

Source-sensitive audited readings protected for later English checking include:

- Kural **717**: `கற்றறிந்தார் கல்வி விளங்கும் கசடறச் / சொற்றெரிதல் முன்னர் இழுக்கு.`;
- Kural **725 commentary**: `தருக்கமென்படும் அளவைக் திறமும்`;
- Kural **733 commentary**: `மளவுக்கு வளம்`;
- Kural **771 commentary**: `நடுகல்லாய்ப் போனவர்கள்`.

### Part 009 English — FIRST-PASS COMPLETE

Current state:

- aligned pages: **22 / 22**;
- `draft`: **22 / 22**;
- `source-checked`: **0**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

All pages are explicitly `project_translation` records grounded in the verified/audited Tamil archive. Kalaignar's institutional vocabulary and direct images have been retained in the first pass.

The already controlled `அமைச்சியல்` remains **Ministerial Affairs**. The newly encountered Part 009 structural labels currently use provisional first-pass metadata renderings `அரணியல்` → **Fortification Affairs**, `கூழியல்` → **Wealth**, and `படையியல்` → **Military Affairs**. These are not yet final glossary decisions.

Part 010 remains untranscribed; its first page was inspected previously only to establish continuity at printed page **159 / Kural 781 / chapter 79 `நட்பு`**.

## அடுத்த செயல்

Perform **Part 009 English direct source-check** for all **22 draft pages**, scans **170–191 / Kural 671–780**.

Compare every English Kural and commentary against the audited Tamil record, preserve source-sensitive wording and Kalaignar's interpretive direction, document substantive corrections, and promote only passing pages to `source-checked`.

Do not combine this with editorial/glossary review or release, and do not begin Part 010 Tamil transcription during the same activity.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).
