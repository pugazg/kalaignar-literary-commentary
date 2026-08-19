# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

Last synchronized with live `main`: **2026-08-19**.

## திட்டமிட்ட / உள்ள நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–015 **ARCHIVAL-READY through scan 323**; commentary through printed page 270 / Kural 1330 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–015 **RELEASED through the end of the supplied volume** |
| Thirukkural semantic structure | பால் → இயல் → அதிகாரம் | **COMPLETE — 3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள் mapped** |
| சங்கத் தமிழ் | தமிழ் | **ACTIVE — complete 497-scan source confirmed; physical records through scan 30; first three body sections complete** |
| Sangatamil | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த source-controlled edition ஆக archive செய்யப்படும் |
| குறளோவியம் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Kuraloviyam | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |

## மூலக் கொள்கை

> **ஸ்கேன் தான் அதிகாரப்பூர்வ மூல ஆதாரம். Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது.

For source-controlled Tamil pages, `verified` requires both textual fidelity and meaningful visual text fidelity.

# Canonical completed state — திருக்குறள்

The supplied **திருக்குறள் — கலைஞர் உரை** volume remains complete across all defined layers:

- Tamil Parts **001–015** archival-ready through scans **1–323**;
- commentary through printed page **270 / Kural 1330**;
- English project translation Parts **001–015 released**;
- semantic provenance complete: **3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள்**;
- final semantic audit: [`works/thirukkural/structure/STRUCTURE_AUDIT.md`](works/thirukkural/structure/STRUCTURE_AUDIT.md) — **PASS**.

Do not restart completed Thirukkural batches unless a new source or explicit correction task requires it.

# Canonical active state — சங்கத் தமிழ்

Active path: [`works/sangatamil/`](works/sangatamil/)

Controlling source: `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

## Verified source extent

The actual PDF has been independently confirmed as **497 scans**; scan **497 is the back cover**. The earlier 150-page preview figure is retired.

Canonical source range: **1–497**.

## Current physical / structural progress

Physical Markdown records now exist through scan **30**.

Completed:

- scans **9–14 / printed IV–IX** — front-matter text gate;
- `மலர்மாரி பொழிகின்றேன்!` — scans **17–19**;
- `யாதும் ஊரே; யாவரும் கேளிர்!` — scans **20–24**;
- `மானங்காத்த மறவன்!` — scans **25–30**.

Verified printed Sangam provenance currently includes:

- scan 19 — `பத்துப்பாட்டு (குறிஞ்சிப்பாட்டு)` / `61 முதல் 95 முடிய` / `கபிலர்`;
- scan 24 — `புறநானூறு - பாடல் : 192` / `கணியன் பூங்குன்றன்`;
- scan 30 — `புறநானூறு : பாடல்: 74` / `சேரமான் கணைக்கால் இரும்பொறை`.

Current controls:

- [`SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`](SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md)
- [`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`](NEXT_CHAT_PROMPT_SANGATH_TAMIL.md)
- [`works/sangatamil/README.md`](works/sangatamil/README.md)
- [`works/sangatamil/metadata/source.md`](works/sangatamil/metadata/source.md)
- [`works/sangatamil/indexes/page-map.md`](works/sangatamil/indexes/page-map.md)
- [`works/sangatamil/indexes/section-register.md`](works/sangatamil/indexes/section-register.md)
- [`works/sangatamil/indexes/source-citation-register.md`](works/sangatamil/indexes/source-citation-register.md)

## Repository-state discipline

For active Sangath Tamil work, precedence is:

**controlling scan → physical page records → completed verification/audit artefacts → source/page/section/citation indexes → work README → root HANDOVER / README → historical snapshots.**

## அடுத்த செயல்

Begin the next decorative section at **scan 31 / printed page 16**:

**`துணை நின்றார் தோழி!`**

First determine its full scan boundary from the next decorative heading, then create/transcribe/verify its physical page records in source order.

Current handover: [`HANDOVER.md`](HANDOVER.md).
