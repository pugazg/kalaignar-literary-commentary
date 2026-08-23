# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

Last synchronized with live `main`: **2026-08-23**.

## திட்டமிட்ட / உள்ள நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–015 **ARCHIVAL-READY through scan 323**; commentary through printed page 270 / Kural 1330 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–015 **RELEASED through the end of the supplied volume** |
| Thirukkural semantic structure | பால் → இயல் → அதிகாரம் | **COMPLETE — 3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள் mapped** |
| சங்கத் தமிழ் | தமிழ் | **ACTIVE — complete 497-scan source confirmed; physical records through scan 53; Pass 1 transcription/capture resumes at scan 54** |
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

Active path: [`works/sangatamil/`](works/sangatamil/)

Controlling source: `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

The actual PDF has been independently confirmed as **497 scans**; scan **497 is the back cover**. The earlier 150-page preview figure is retired.

Canonical source range: **1–497**.

## Canonical workflow

Sangath Tamil now uses a **whole-volume multi-pass workflow** so that transcription and later archival checks are separated instead of being mixed in every page iteration.

Canonical plan: [`works/sangatamil/MULTI_PASS_WORKFLOW.md`](works/sangatamil/MULTI_PASS_WORKFLOW.md).

Pass order:

1. **Pass 1 — transcription / physical capture only, through scan 497**;
2. **Pass 2 — textual verification, scan 1 → 497**;
3. **Pass 3 — visual-text fidelity verification, scan 1 → 497**;
4. **Pass 4 — physical-page and continuity audit, scan 1 → 497**;
5. **Pass 5 — section-structure audit, scan 1 → 497**;
6. **Pass 6 — Sangam source / provenance audit, scan 1 → 497**;
7. **Pass 7 — metadata / status consistency audit, scan 1 → 497**;
8. **Pass 8 — whole-volume synchronization and final audit**.

Only **Pass 1** is active now.

## Current physical progress

Physical Markdown records exist through **scan 53**.

Current immediate sequence:

- scan 50 / printed 35 — `மாதரின் கண்ட மலர்கள்` opening, completed under the earlier verified-page cadence;
- scan 51 / printed 36 — transcription-only, `needs-review`;
- scan 52 — illustration capture, `needs-review`;
- scan 53 / printed 38 — fast transcription-only, `needs-review`;
- **scan 54 — next Pass-1 capture**.

Earlier completed/verified material remains preserved:

- scans **9–14 / printed IV–IX** — front-matter text gate;
- `மலர்மாரி பொழிகின்றேன்!` — scans **17–19**;
- `யாதும் ஊரே; யாவரும் கேளிர்!` — scans **20–24**;
- `மானங்காத்த மறவன்!` — scans **25–30**;
- `துணை நின்றார் தோழி!` — scans **31–36**;
- `சுமந்தவன் சுமந்த சோகம்!` — scans **37–41**;
- `பாவை புகழ்ந்த பன்றி` — scans **42–46**;
- `காக்கைக்கு நன்றி காட்ட...` — scans **47–49**.

Existing verified pages are not downgraded by the workflow change. The later systematic passes still sweep scan 1 through scan 497 so the final volume state is uniform and auditable.

## Current Pass-1 discipline

Routine page capture now means only:

- one source reading;
- create the physical page record;
- transcribe visible text;
- preserve obvious line/paragraph breaks and immediately visible headings;
- factual capture for illustration/blank/non-text pages;
- printed page number only when visible;
- normally leave new records `needs-review`;
- commit and move forward.

Do not mix routine second-pass verification, provenance review, section-end investigation, continuity audit, metadata audit or documentation synchronization into Pass 1.

## Verified printed Sangam provenance already preserved

- scan 19 — `பத்துப்பாட்டு (குறிஞ்சிப்பாட்டு)` / `61 முதல் 95 முடிய` / `கபிலர்`;
- scan 24 — `புறநானூறு - பாடல் : 192` / `கணியன் பூங்குன்றன்`;
- scan 30 — `புறநானூறு : பாடல்: 74` / `சேரமான் கணைக்கால் இரும்பொறை`;
- scan 36 — `ஐங்குறுநூறு : பாடல் : 180` / `அம்மூவனார்`;
- scan 41 — `புறநானூறு : பாடல் : 286` / `ஒளவையார்`;
- scan 46 — `அகநானூறு : பாடல் : 248` / `கபிலர்`;
- scan 49 — `குறுந்தொகை : பாடல் : 210` / `காக்கைப்பாடினியார் நச்செள்ளையார்`.

New provenance encountered during Pass 1 is captured as page text if visible but is systematically verified/finalized in Pass 6.

Current controls:

- [`SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`](SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md)
- [`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`](NEXT_CHAT_PROMPT_SANGATH_TAMIL.md)
- [`works/sangatamil/README.md`](works/sangatamil/README.md)
- [`works/sangatamil/MULTI_PASS_WORKFLOW.md`](works/sangatamil/MULTI_PASS_WORKFLOW.md)
- [`works/sangatamil/metadata/source.md`](works/sangatamil/metadata/source.md)
- [`works/sangatamil/metadata/transcription-policy.md`](works/sangatamil/metadata/transcription-policy.md)
- [`works/sangatamil/indexes/page-map.md`](works/sangatamil/indexes/page-map.md)
- [`works/sangatamil/indexes/section-register.md`](works/sangatamil/indexes/section-register.md)
- [`works/sangatamil/indexes/source-citation-register.md`](works/sangatamil/indexes/source-citation-register.md)

## Repository-state discipline

For active Sangath Tamil work, precedence is:

**controlling scan → physical page records → completed verification/audit artefacts → canonical multi-pass workflow → source/page/section/citation indexes → work README → root HANDOVER / README → historical snapshots.**

## அடுத்த செயல்

**Pass 1 only: capture/transcribe scan 54, commit it as a first-pass page record, then continue sequentially toward scan 497.**

Current handover: [`HANDOVER.md`](HANDOVER.md).