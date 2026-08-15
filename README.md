# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–004 **ARCHIVAL-READY**; Part 005 first pass 22/22, verification **7/22** |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–003 released; Part 004 Tamil archival-ready; Part 005 Tamil verification in progress |
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

Tamil Parts 001–004 are archival-ready.

- Part 001 — scans **1–20**; 19 verified + scan 8 documented partial;
- Part 002 — scans **21–41**, 21/21 verified;
- Part 003 — scans **42–62**, 21/21 verified, through Kural **145**;
- Part 004 — scans **63–84**, printed pages **30–51**, Kural **146–255**, **22/22 verified and audited — ARCHIVAL-READY**;
- Part 005 — scans **85–106**, printed pages **52–73**, Kural **256–365**; first-pass repository transcription **22/22 complete**. Direct visual verification is now **7/22 complete**: scans 85–91 are `verified`, while scans 92–106 remain `needs-review`.

The supplied physical source reaches overall scan **106** / printed page **73** / Kural **365**.

### Tamil Part 004 — ARCHIVAL-READY

The separate archival audit has passed:

[`works/thirukkural/AUDIT_PART_004.md`](works/thirukkural/AUDIT_PART_004.md)

### Tamil Part 005 — VERIFICATION IN PROGRESS

First-pass records: **22 / 22**.

Verification state:

- `verified`: **7** — scans 85–91 / printed pages 52–58 / Kural 256–290;
- `needs-review`: **15** — scans 92–106 / printed pages 59–73 / Kural 291–365.

The first visual-verification batch was compared directly against the supplied scan pages. No source-text correction was required for scans 85–91; their first-pass transcription already matched the controlling source, including source-specific Kural joins/spacing and Kalaignar commentary.

### English Parts 001–003 — RELEASE COMPLETE

- Part 001: 19 `release-ready` + 1 `source-limited`;
- Part 002: **21/21 `release-ready`**;
- Part 003: **21/21 `release-ready`**, through Kural **145**.

Part 004 English is eligible to begin, but the immediate Tamil archival queue continues Part 005 direct visual verification first.

Next Tamil activity: **Part 005 direct visual verification for scans 92–98 / printed pages 59–65 / Kural 291–325**, covering `வாய்மை`, `வெகுளாமை`, `இன்னா செய்யாமை`, and the beginning of `கொல்லாமை`. Correct only differences supported by the actual scans and promote only fully confirmed records to `verified`. Do not begin the Part 005 audit, scans 99 onward verification, or Part 004 English translation in the same activity.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md) and [`HANDOVER.md`](HANDOVER.md).
