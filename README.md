# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

Last synchronized with live `main`: **2026-08-23**.

## திட்டமிட்ட / உள்ள நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–015 **ARCHIVAL-READY through scan 323**; commentary through printed page 270 / Kural 1330 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–015 **RELEASED through the end of the supplied volume** |
| Thirukkural semantic structure | பால் → இயல் → அதிகாரம் | **COMPLETE — 3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள் mapped** |
| சங்கத் தமிழ் | தமிழ் | **ACTIVE — complete 497-scan source confirmed; physical records through scan 45; first three body sections complete; section 004 corrective re-transcription done, verification pending** |
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

Physical Markdown records now exist through scan **45**.

Completed:

- scans **9–14 / printed IV–IX** — front-matter text gate;
- `மலர்மாரி பொழிகின்றேன்!` — scans **17–19**;
- `யாதும் ஊரே; யாவரும் கேளிர்!` — scans **20–24**;
- `மானங்காத்த மறவன்!` — scans **25–30**.

Corrective work completed but not yet promoted to verified:

- `துணை நின்றார் தோழி!` — scans **31–36 / printed 16–21**;
- scan 32 illustration remains verified;
- scans 31, 33, 34, 35 and 36 were re-transcribed directly from the controlling PDF after an audit found placeholder/inaccurate earlier records;
- a separate second character-by-character + visual-text fidelity pass is still required.

Later mapped work requiring audit before advancement:

- `சுமந்தவன் சுமந்த சோகம்!` — scans **37–41**; physical records exist; text pages remain `needs-review`;
- `பாவை புகழ்ந்த பன்றி` — starts scan **42**; records exist through scan **45**; end boundary pending.

Verified printed Sangam provenance currently includes:

- scan 19 — `பத்துப்பாட்டு (குறிஞ்சிப்பாட்டு)` / `61 முதல் 95 முடிய` / `கபிலர்`;
- scan 24 — `புறநானூறு - பாடல் : 192` / `கணியன் பூங்குன்றன்`;
- scan 30 — `புறநானூறு : பாடல்: 74` / `சேரமான் கணைக்கால் இரும்பொறை`.

Scan 36 has directly inspected, verification-pending provenance:

- `ஐங்குறுநூறு : பாடல் : 180` / `பாடியவர் : அம்மூவனார்`.

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

First complete the second textual + meaningful visual-fidelity verification for the corrected section:

**`துணை நின்றார் தோழி!` — scans 31–36 / printed 16–21.**

Then audit/re-transcribe the existing text records for `சுமந்தவன் சுமந்த சோகம்!` (scans 37–41), followed by `பாவை புகழ்ந்த பன்றி` through scan 45. Do not create new records beyond scan 45 until the already mapped range is trustworthy.

Current handover: [`HANDOVER.md`](HANDOVER.md).
