# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–012 **ARCHIVAL-READY continuously through scan 260 / printed page 227 / Kural 1115** |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–011 **RELEASED continuously through Kural 1010**; Part 012 eligible for first pass |
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

Tamil Parts **001–012** are now audited / archival-ready continuously through overall scan **260** / printed page **227** / Kural **1115**.

Part 012 Tamil audit: [`works/thirukkural/AUDIT_PART_012.md`](works/thirukkural/AUDIT_PART_012.md) — **PASS / ARCHIVAL-READY**.

Part 012 audited scope is **23 / 23 physical pages**, scans **238–260**, with continuous Kural numbering **1011–1115**. Printed pagination is source-supported as **205–218**, followed by two unnumbered physical leaves, then **221–227**.

The source-visible Part 012 transition is preserved:

- scans **238–251**: `பொருள் — குடியியல்`;
- scan **252**: standalone `இன்பம்` title leaf;
- scan **253**: blank/reverse-show-through leaf;
- scans **254–260**: `இன்பம் — களவியல்`.

The incoming boundary passes at printed page **204 → 205 / Kural 1010 → 1011**. The supplied Part 013 first page confirms the outgoing continuation at printed page **227 → 228 / Kural 1115 → 1116**, without starting Part 013 transcription.

The three Part 012 verification corrections remain authoritative, and the unusual source readings at Kural **1077** (`ஈங்கை விதிரார்...`) and Kural **1098** (`அசையியற் குண்டாண்டோர்...`) remain protected against normalization.

English Parts **001–011** remain fully released through Kural **1010**. Part 012 English has **not** started, but is now eligible because the Tamil audit passed.

Additional supplied Tamil sources Parts **013–015** remain received but not started.

## அடுத்த செயல்

The exact next activity is **Part 012 English project translation — first pass** for all **23 aligned physical pages / scans 238–260**.

Create Part 012 English records only as `translation_type: "project_translation"` and `status: "draft"`, preserve the section-title and blank leaves as aligned records, and stop after first pass. Do not combine that gate with source-check, editorial review, release, or Part 013 Tamil transcription.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).
