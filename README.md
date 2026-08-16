# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–012 **ARCHIVAL-READY continuously through scan 260 / printed page 227 / Kural 1115** |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–011 **RELEASED through Kural 1010**; Part 012 **SOURCE-CHECK COMPLETE — 23/23 source-checked** |
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

Tamil Parts **001–012** are audited / archival-ready continuously through overall scan **260** / printed page **227** / Kural **1115**.

Part 012 Tamil audit: [`works/thirukkural/AUDIT_PART_012.md`](works/thirukkural/AUDIT_PART_012.md) — **PASS / ARCHIVAL-READY**.

English Parts **001–011** remain fully released through Kural **1010**. Part 012 English has completed its first-pass translation and separate direct source-check for **all 23 aligned physical pages / scans 238–260**; all 23 records are now `status: "source-checked"`.

The source-check compared every translated Kural and every Kalaignar commentary paragraph against the verified Tamil record and directly re-inspected the controlling scan at source-sensitive locations. No source-fidelity body-text correction was required; the page-body translations remain unchanged from first pass while their status advanced to `source-checked`.

Part 012 continues to preserve the physical transition from `பொருள் — குடியியல்` through the standalone `இன்பம்` title and blank reverse leaf into `இன்பம் — களவியல்`. The established **Civic Life** and **Understanding Signs** renderings remain in use, while **Clandestine Love** and the new Part 012 chapter headings remain provisional pending editorial reconciliation.

The source-check explicitly retained the verified Kural **1018 / 1035 / 1048** commentary directions, Kalaignar's Kural **1062** challenge to the supposed creator, the source-specific Kural **1077 / 1098** readings, the Kural **1103** `lotus-eyed one` comparison and the Kural **1115** anicham-stalk / broken-waist / auspicious-drum explanation.

`GLOSSARY.md` was deliberately not changed during source-check.

Additional supplied Tamil sources Parts **013–015** remain received but not started.

## அடுத்த செயல்

The exact next activity is **Part 012 English editorial consistency / glossary reconciliation** for all **23 source-checked pages / scans 238–260**.

Reconcile `களவியல்` and chapter headings **102–112** against the supplied main body and existing project vocabulary, improve English consistency only where source fidelity permits, update `GLOSSARY.md` as supported, create `works/thirukkural/translations/en/reviews/PART_012_REVIEW.md`, and promote pages to `editorial-reviewed` only if that separate gate passes.

Do not combine editorial review with release, and do not begin Part 013 Tamil transcription in the same activity.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).
