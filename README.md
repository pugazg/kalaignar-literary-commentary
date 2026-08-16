# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–012 **ARCHIVAL-READY through scan 260 / printed page 227 / Kural 1115**; Part 013 Tamil first-pass **COMPLETE 22/22**, verification pending |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–012 **RELEASED continuously through Kural 1115**; Part 013 English not started |
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

Tamil Parts **001–012** remain audited / archival-ready continuously through overall scan **260** / printed page **227** / Kural **1115**.

English Parts **001–012** remain fully released continuously through Kural **1115**.

Part 012 Tamil audit: [`works/thirukkural/AUDIT_PART_012.md`](works/thirukkural/AUDIT_PART_012.md) — **PASS / ARCHIVAL-READY**.

Part 012 English release report: [`works/thirukkural/translations/en/reviews/PART_012_RELEASE_REPORT.md`](works/thirukkural/translations/en/reviews/PART_012_RELEASE_REPORT.md) — **PASS / RELEASE APPROVED**.

### Part 013 Tamil first pass

The supplied controlling source `திருக்குறள்_கலைஞர்_உரை_part_013_pages_261-282.pdf` has now completed its separate Tamil source-inspection / first-pass transcription gate.

Current Part 013 state:

- physical pages **22 / 22**;
- overall scans **261–282**;
- printed pages **228–249**;
- Kural **1116–1225**;
- all **22 / 22** records `status: "needs-review"`;
- direct visual verification **pending**;
- Tamil audit **not started**;
- English Part 013 **not started / not yet eligible**.

The Part 012 → Part 013 boundary is continuous at printed page **227 → 228 / Kural 1115 → 1116**. Scan 261 completes chapter 112 `நலம் புனைந்து உரைத்தல்`; chapters **113–122** are complete within the supplied Part 013 source; chapter **123 `பொழுதுகண்டு இரங்கல்`** begins on scan 282 and is present only through Kural **1225**.

The source-visible structural transition is preserved as:

- scans **261–277**: `இன்பம் — களவியல்`;
- scans **278–282**: `இன்பம் — கற்பியல்`, beginning at printed page **245 / Kural 1201**.

Source-sensitive first-pass forms, including scan **268 / Kural 1152 commentary** `வந்துதிகிறது!` and the supplied Kural **1220** reading on scan 281, have been retained for direct verification rather than normalized from another edition.

Parts **014–015** remain received but not started.

## அடுத்த செயல்

The exact next activity is the separate **Part 013 Tamil direct visual verification** gate for all **22 first-pass records / scans 261–282**.

Compare every record directly against the controlling scan and promote only passing pages to `verified`, documenting every real correction. Recheck the `களவியல் → கற்பியல்` hierarchy transition and all unusual/source-sensitive printed forms.

Do **not** combine verification with `AUDIT_PART_013.md`, Part 013 English translation, or Parts 014–015 transcription.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).
