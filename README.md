# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–010 **ARCHIVAL-READY** continuously through overall scan 214 / printed page 181 / Kural 895 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–009 **released through Kural 780**; Part 010 eligible for first pass |
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

Tamil Parts **001–010** are audited / archival-ready continuously through overall scan **214** / printed page **181** / Kural **895**.

English Parts **001–009** have completed their full release workflow continuously through Kural **780**. Part 010 English has not begun and is now eligible for its separate first-pass translation gate.

Part 009 English covers scans **170–191 / printed pages 137–158 / Kural 671–780**. All **22 / 22** aligned English pages are `release-ready` after first pass, direct source-check, editorial consistency / glossary reconciliation and the separate release gate.

Editorial review: [`works/thirukkural/translations/en/reviews/PART_009_REVIEW.md`](works/thirukkural/translations/en/reviews/PART_009_REVIEW.md).

Release report: [`works/thirukkural/translations/en/reviews/PART_009_RELEASE_REPORT.md`](works/thirukkural/translations/en/reviews/PART_009_RELEASE_REPORT.md) — **PASS / RELEASE APPROVED**.

The released Part 009 section sequence is:

`அமைச்சியல்` → **Ministerial Affairs** → `அரணியல்` → **Fortification Affairs** → `கூழியல்` → **Wealth** → `படையியல்` → **Military Affairs**.

Protected source-check and source-sensitive decisions from released English Parts remain intact.

## Part 010 Tamil — ARCHIVAL-READY

Controlling source: `திருக்குறள்_கலைஞர்_உரை_part_010_pages_192-214.pdf`.

Tamil audit: [`works/thirukkural/AUDIT_PART_010.md`](works/thirukkural/AUDIT_PART_010.md) — **PASS / ARCHIVAL-READY**.

Final audited scope:

- physical pages: **23 / 23**;
- overall scans **192–214**;
- printed pages **159–181**;
- Kural **781–895**;
- source section throughout: `பொருள் — நட்பியல்`;
- chapters **79–90**, with chapter 90 represented only through Kural 895 because that is where the supplied source ends;
- final Tamil status: **23 `verified`, 0 `needs-review`, 0 `partial`, 0 `blocked`**.

The audit confirms continuous Part 009 → Part 010 intake at printed page **158 → 159** / Kural **780 → 781**. Direct visual verification required no first-pass body-text correction.

The source-sensitive scan **209 / Kural 869 commentary** repetition is confirmed and protected:

`அஞ்சிடும் கோழைகளாகவும், அறிவில்லாக் கோழைகளாகவும் பகைவர்கள் இருப்பின் அவர்களை எதிர்ப்போரை விட்டு வெற்றியெனும் இன்பம் விலகாமலே நிலைத்து நிற்கும்.`

The supplied Part 010 source ends at printed page **181 / Kural 895**. No Kural 896 onward is inferred without the next controlling source.

## அடுத்த செயல்

Begin **Part 010 English project translation — first pass** for all **23 aligned Tamil pages**, scans **192–214 / printed pages 159–181 / Kural 781–895**.

Create only `draft` project-translation pages in this gate. English direct source-check, editorial consistency / glossary review and release remain separate later activities.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).
