# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–014 **ARCHIVAL-READY through scan 302 / printed page 269 / Kural 1325** |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–013 **RELEASED through scan 282 / Kural 1225**; Part 014 **DRAFT COMPLETE 20/20; source-check pending** |
| சங்கத்தமிழ் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Sangatamil | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |
| குறளோவியம் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Kuraloviyam | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |

## மூலக் கொள்கை

> **ஸ்கேன் தான் அதிகாரப்பூர்வ மூல ஆதாரம். Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது.

Source PDFs are working/control sources and are not committed unless the user explicitly changes that policy.

## English layers — published source vs project translation

1. **Published / official English source** — தனியாக வெளியிடப்பட்ட source கிடைத்தால், அதன் சொந்த pagination / wording / metadata-உடன் source-controlled edition ஆக archive செய்யப்படும்.
2. **Project-created English translation** — audited Tamil source-இலிருந்து உருவாக்கப்படும் மொழிபெயர்ப்பு; `translation_type: "project_translation"` என்று வெளிப்படையாகக் குறிக்கப்படும்.

The project translation follows an explicit fidelity rule: **retain Kalaignar's own language, images and interpretive direction; do not replace them with familiar standard Kural interpretations.**

Permanent workflow:

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

## Canonical current state — திருக்குறள்

### Tamil

Parts **001–014 are audited / archival-ready continuously** through:

- overall scan **302**;
- printed page **269**;
- Kural **1325**.

Part 001 retains one documented partial handwritten facsimile at scan 8. Audits exist continuously from `AUDIT_PART_001.md` through `AUDIT_PART_014.md`.

Part 013 covers scans **261–282 / printed 228–249 / Kural 1116–1225** and is archival-ready.

Part 014 covers scans **283–302 / printed 250–269 / Kural 1226–1325**, has **20/20 verified Tamil records**, and is **ARCHIVAL-READY**.

### English project translation

Parts **001–013 are fully released continuously** through overall scan **282 / printed page 249 / Kural 1225**.

Part 013 release artefacts:

- [`works/thirukkural/AUDIT_PART_013.md`](works/thirukkural/AUDIT_PART_013.md) — Tamil **PASS / ARCHIVAL-READY**;
- [`works/thirukkural/translations/en/reviews/PART_013_REVIEW.md`](works/thirukkural/translations/en/reviews/PART_013_REVIEW.md);
- [`works/thirukkural/translations/en/reviews/PART_013_RELEASE_REPORT.md`](works/thirukkural/translations/en/reviews/PART_013_RELEASE_REPORT.md) — **PASS / RELEASE APPROVED**.

Part 014 English already has **20/20 aligned draft pages** for scans **283–302 / Kural 1226–1325**. These pages are not missing and must not be recreated. Their next gate is direct source-check against the verified Tamil records.

### Part 015

The source file `திருக்குறள்_கலைஞர்_உரை_part_015_pages_303-323.pdf` is recorded as supplied, but **no Part 015 Tamil archival page records currently exist on `main`**. Its actual source must be inspected before any transcription begins.

## Repository-state discipline

Current progress must be determined from the actual `main` tree and completed audit/review/release artefacts, not from older saved prompts or historical status paragraphs.

When documents disagree about progress, use:

**actual page files → completed audits/reviews/release reports → `TRANSLATION_STATUS.md` → current handover/READMEs → older continuation documents.**

## அடுத்த செயல்

Perform the separate **Part 014 English source-check gate** for all 20 existing draft records, scans **283–302**.

Compare each English draft directly against the corresponding verified Tamil archival record. Make only source-supported corrections and promote passing pages to `source-checked`. Stop after that gate; do not combine it with editorial review, release, or Part 015 Tamil work.

Detailed current state:

- [`HANDOVER.md`](HANDOVER.md)
- [`works/thirukkural/README.md`](works/thirukkural/README.md)
- [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md)
