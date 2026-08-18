# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

Last synchronized with live `main`: **2026-08-18**.

## திட்டமிட்ட / உள்ள நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–015 **ARCHIVAL-READY through scan 323**; commentary through printed page 270 / Kural 1330 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–015 **RELEASED through the end of the supplied volume** |
| Thirukkural semantic structure | பால் → இயல் → அதிகாரம் | **COMPLETE — 3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள் mapped** |
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

The project-created English translation retains Kalaignar's language, images, social vocabulary and interpretive direction. It must not silently substitute familiar standard Kural interpretations.

Permanent source/translation cadence:

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

## Canonical current state — திருக்குறள்

### Tamil archival layer

Parts **001–015 are audited / archival-ready continuously** through the end of the supplied volume:

- overall scans **1–323**;
- commentary through printed page **270 / Kural 1330**;
- scans **304–321**: `குறள் முதற்குறிப்பு அகரவரிசை`, printed pages 271–288;
- scan **322**: blank leaf;
- scan **323**: back cover.

Part 001 scan 8 remains the documented source-limited handwritten facsimile exception. Tamil audit artefacts exist continuously from `works/thirukkural/AUDIT_PART_001.md` through `AUDIT_PART_015.md`.

### English project translation

English Parts **001–015 are released continuously through the end of the supplied volume**.

Current status authority:

- [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md)
- [`works/thirukkural/translations/en/README.md`](works/thirukkural/translations/en/README.md)

Part 015's completed gate artefacts include:

- [`works/thirukkural/AUDIT_PART_015.md`](works/thirukkural/AUDIT_PART_015.md)
- [`works/thirukkural/translations/en/reviews/PART_015_REVIEW.md`](works/thirukkural/translations/en/reviews/PART_015_REVIEW.md)
- [`works/thirukkural/translations/en/reviews/PART_015_RELEASE_REPORT.md`](works/thirukkural/translations/en/reviews/PART_015_RELEASE_REPORT.md)

### Semantic navigation/provenance layer

`works/thirukkural/structure/` is complete:

- **3 / 3 பால்**;
- **13 / 13 இயல்**;
- **133 / 133 அதிகாரம்**;
- **1,330 / 1,330 குறள்**.

Every semantic chapter node points back to verified Tamil physical-page record(s) and corresponding released English record(s). Exact scan/Part/printed-page provenance is documented without moving or rewriting the physical-page archives.

The final audit is:

- [`works/thirukkural/structure/STRUCTURE_AUDIT.md`](works/thirukkural/structure/STRUCTURE_AUDIT.md) — **PASS — SEMANTIC PROVENANCE MAPPING COMPLETE**.

## Repository-state discipline

Current progress must be determined from the actual `main` tree and completed audit/review/release artefacts, not from stale saved prompts or historical status paragraphs.

When documents disagree about progress, use this precedence:

**actual page files → completed Tamil audits / English review-release reports → translation status → completed structure audit → current handover / current READMEs → explicitly historical snapshots.**

Historical Part-specific handovers/prompts remain in the repository as provenance and are not current workflow instructions.

## அடுத்த செயல்

There is **no unfinished Thirukkural source transcription, Tamil audit, English translation/release, or semantic chapter mapping** for the supplied volume.

Do not infer continuation after Kural **1330**. Future work should begin from either:

- a newly supplied Thirukkural source, supplement or alternate edition;
- another Kalaignar literary-commentary work;
- or a separately defined enhancement/audit task that does not silently alter released source-controlled text.

Current handover: [`HANDOVER.md`](HANDOVER.md).
