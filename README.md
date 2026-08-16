# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–011 **ARCHIVAL-READY through scan 237 / printed page 204 / Kural 1010**; Part 012 direct visual verification **COMPLETE 23/23**, audit pending |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–011 **RELEASED continuously through Kural 1010**; Part 012 English not started |
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

Tamil Parts **001–011** are audited / archival-ready continuously through overall scan **237** / printed page **204** / Kural **1010**.

English Parts **001–011** have completed the full translation workflow continuously through Kural **1010**. Part 011 release report: [`works/thirukkural/translations/en/reviews/PART_011_RELEASE_REPORT.md`](works/thirukkural/translations/en/reviews/PART_011_RELEASE_REPORT.md) — **PASS / RELEASE APPROVED**.

### Part 012 Tamil direct verification

The controlling source `திருக்குறள்_கலைஞர்_உரை_part_012_pages_238-260.pdf` has now completed the separate **Tamil direct visual verification gate — 23 / 23 verified**.

Verified Part 012 scope:

- overall scans **238–260**;
- printed pages **205–218**, then an unnumbered `இன்பம்` title leaf and an unnumbered blank/reverse-show-through leaf, then printed pages **221–227**;
- Kural **1011–1115**;
- all **23 / 23** records `status: "verified"`;
- `needs-review`: **0**;
- Tamil audit **not started**;
- English Part 012 **not started / not yet eligible**.

The incoming Part 011 → Part 012 boundary is source-supported at printed page **204 → 205 / Kural 1010 → 1011**.

The source structure is directly verified as:

- scans **238–251** remain `பொருள் — குடியியல்` through Kural **1080**;
- scan **252** is the centered `இன்பம்` section-title leaf;
- scan **253** has no independent printed body text;
- from scan **254 / printed page 221 / Kural 1081**, the running hierarchy is `இன்பம் — களவியல்`;
- Part 012 ends at scan **260 / printed page 227 / Kural 1115**, midway through chapter 112 `நலம் புனைந்து உரைத்தல்`.

Exactly three first-pass errors were corrected during direct verification: the Kural **1018 commentary** ending, Kural **1035 commentary** `உண்ணும்`, and Kural **1048 commentary** `செய்வதுபோல`. The unusual source readings at Kural **1077** (`ஈங்கை விதிரார்...`) and Kural **1098** (`அசையியற் குண்டாண்டோர்...`) were directly confirmed and retained rather than normalized.

The supplied Part 013 first page confirms the next physical boundary at printed page **228 / Kural 1116**, but **Part 013 transcription has not been started**. Additional supplied sources Parts **013–015** remain not started.

Part 012 is **not yet archival-ready**: that decision belongs to the separate audit gate.

## அடுத்த செயல்

Perform the separate **Part 012 Tamil audit / archival-ready gate** and create `works/thirukkural/AUDIT_PART_012.md` only after the audit review is complete.

Do **not** combine that audit with Part 012 English translation or Part 013 transcription.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).
