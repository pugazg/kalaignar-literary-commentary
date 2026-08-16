# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–010 **ARCHIVAL-READY** continuously through overall scan 214 / printed page 181 / Kural 895 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–009 **released through Kural 780**; Part 010 **23/23 source-checked** through Kural 895 |
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

English Parts **001–009** have completed their full release workflow continuously through Kural **780**.

Part 010 English now has **23 / 23 source-checked pages** covering scans **192–214 / printed pages 159–181 / Kural 781–895**. No Part 010 page remains `draft`; editorial review and release are still pending.

Part 010 Tamil audit: [`works/thirukkural/AUDIT_PART_010.md`](works/thirukkural/AUDIT_PART_010.md) — **PASS / ARCHIVAL-READY**.

The direct English source-check corrected source drift at Kural **813, 822, 842, 849, 850, 867 and 887** while preserving Kalaignar's own argument. In particular, the source-confirmed Kural **869 commentary** repetition remains preserved, Kalaignar's supplied Kural **861** interpretation remains untouched, and Kural **895** keeps the distinction between ruler language in the Kural and government language in Kalaignar's commentary.

The current Part 010 structural rendering `நட்பியல்` → **Friendship** and chapter headings 79–90 remain **provisional** until the next editorial consistency / glossary-reconciliation gate.

The supplied source ends at Kural **895**, so no English Kural 896 onward has been created or inferred.

## அடுத்த செயல்

Perform the separate **Part 010 English editorial consistency / glossary reconciliation** for all **23 source-checked pages**.

Finalize source-supported structural/chapter terminology, update `GLOSSARY.md`, review readability and recurring terms without undoing source-check fidelity decisions, create `works/thirukkural/translations/en/reviews/PART_010_REVIEW.md`, and promote only passing pages to `editorial-reviewed`.

Do not combine that gate with release, and do not alter released English Parts 001–009 merely for harmonization.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).
