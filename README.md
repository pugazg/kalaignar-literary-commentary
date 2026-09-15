# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

Last synchronized with live main: **2026-09-15**.

## திட்டமிட்ட / உள்ள நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–015 **ARCHIVAL-READY through scan 323**; commentary through printed page 270 / Kural 1330 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–015 **RELEASED through the end of the supplied volume** |
| Thirukkural semantic structure | பால் → இயல் → அதிகாரம் | **COMPLETE — 3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள் mapped** |
| சங்கத் தமிழ் | தமிழ் | **ACTIVE — Gate A CLOSED; Gate B B01–B14 COMPLETE; 350/497 structurally reviewed; frontier scan 351** |
| Sangatamil | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த source-controlled edition ஆக archive செய்யப்படும் |
| குறளோவியம் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Kuraloviyam | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |

## மூலக் கொள்கை

> **ஸ்கேன் தான் அதிகாரப்பூர்வ மூல ஆதாரம். Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது.

For source-controlled Tamil pages, `verified` remains a later source-gate status and must not be used merely because a first-pass transcription exists.

# Canonical completed state — திருக்குறள்

The supplied **திருக்குறள் — கலைஞர் உரை** volume remains complete across all defined layers:

- Tamil Parts **001–015** archival-ready through scans **1–323**;
- commentary through printed page **270 / Kural 1330**;
- English project translation Parts **001–015 released**;
- semantic provenance complete: **3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள்**;
- final semantic audit: [`works/thirukkural/structure/STRUCTURE_AUDIT.md`](works/thirukkural/structure/STRUCTURE_AUDIT.md) — **PASS**.

Do not restart completed Thirukkural batches unless a new source or explicit correction task requires it.

# Canonical active state — சங்கத் தமிழ்

Active path: works/sangatamil/

Controlling source: TVA_BOK_0042551_சங்கத்_தமிழ்.pdf

Canonical physical range: 1–497; scan 497 is the back cover.

## Active workflow

Authoritative plan: works/sangatamil/PRODUCTIVE_COMPLETION_PLAN.md
Current lexical rule: works/sangatamil/GEMINI_TEXT_LOCK.md
Live progress: works/sangatamil/STRUCTURAL_FIDELITY_PROGRESS.md

Authority split:
- Gemini File1–File10 — locked lexical wording
- PDF scan — physical/structural authority
- repository — preservation layer

## Current progress

Gate A — COMPLETE / PASS: 497/497 canonical records; 0 duplicates; 0 missing.

Gate B — IN PROGRESS:
- B01–B14 complete
- 350/497 structurally reviewed
- 147 remaining
- frontier — scan 351
- Gate C — NOT STARTED

Latest B14 page-layer endpoint: c227e5f2d95b6ad464fdf6e730639827c7c92941
Latest durable progress/live-main checkpoint: dfc23c0f9366248c7a2fa301dc4fb215cf374bf0

## Current controls

- SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md
- NEXT_CHAT_PROMPT_SANGATH_TAMIL.md
- works/sangatamil/README.md
- works/sangatamil/PRODUCTIVE_COMPLETION_PLAN.md
- works/sangatamil/GEMINI_TEXT_LOCK.md
- works/sangatamil/STRUCTURAL_FIDELITY_PROGRESS.md
- works/sangatamil/indexes/page-map.md
- works/sangatamil/indexes/section-register.md
- works/sangatamil/indexes/source-citation-register.md

MULTI_PASS_WORKFLOW.md and GEMINI_RECONCILIATION_PLAN.md are retained as historical/superseded methodology records.

## அடுத்த செயல்

Gate B B15 — scans 351–375, using TVA_BOK_0042551_சங்கத்_தமிழ்_part_008_pages_351-400.pdf + File8.md.

Current handover: HANDOVER.md.
