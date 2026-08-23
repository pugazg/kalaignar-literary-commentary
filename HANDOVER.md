# HANDOVER — Kalaignar Literary Commentary Archive

Last synchronized with live `main`: **2026-08-23**.

## Repository

`pugazg/kalaignar-literary-commentary`

Current active work: `works/sangatamil/`

Completed benchmark retained: `works/thirukkural/`

# Mandatory startup — active சங்கத் தமிழ் work

Before making any Sangath Tamil repository change, read completely:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`
5. `works/sangatamil/README.md`
6. `works/sangatamil/MULTI_PASS_WORKFLOW.md`
7. `works/sangatamil/metadata/source.md`
8. `works/sangatamil/metadata/transcription-policy.md`
9. `works/sangatamil/indexes/page-map.md`
10. `works/sangatamil/indexes/section-register.md`
11. `works/sangatamil/indexes/source-citation-register.md`

Then inspect current GitHub `main` and the actual source scan required for the active pass.

# Permanent source / fidelity rule

> **The scan is the authority. Markdown is a faithful preservation layer, not a rewritten edition.**

Never silently modernize, normalize, correct from another edition, replace quotations, alter printed anthology/poem/poet labels, reconstruct unclear source, invent pagination, or infer missing source content.

`verified` remains a later source-gate status; a fast transcription-only record must not be promoted merely because a first pass exists.

# Active source — சங்கத் தமிழ்

- source: `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`
- author: **கலைஞர் மு. கருணாநிதி**
- verified source extent: **497 scans**
- scan **497**: back cover
- canonical range: **1–497**
- do not create scan 498+ records
- printed pagination must be read from the scan, not inferred.

The earlier 150-page figure was a preview-service limitation and is retired.

# Workflow change — canonical from 2026-08-23

The earlier mixed per-page cadence is retired for Sangath Tamil.

The project now uses a **whole-volume multi-pass workflow** so that only one activity is performed at a time across the book.

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

Do not combine a later pass into routine Pass-1 capture merely because an issue is noticed.

# Pass 1 — active now

Pass 1 is deliberately fast and limited.

Per scan:

- inspect once;
- create the physical Markdown record;
- transcribe visible text;
- preserve obvious line/paragraph breaks and directly visible headings;
- create factual records for illustration/blank/non-text pages;
- record printed pagination only when visible;
- leave uncertain readings for later review rather than performing extended forensic resolution;
- normally use `status: needs-review` and `visual_fidelity: needs-review`;
- commit and continue.

Do not routinely perform during Pass 1:

- second character-by-character verification;
- textual verification;
- visual-fidelity audit;
- repeated crop/zoom investigation;
- provenance verification;
- external-edition comparison;
- section-end investigation;
- continuity audit;
- metadata consistency audit;
- per-page updates to README/index/HANDOVER documents.

# Current physical boundary

Physical Markdown records now exist through **scan 53**.

Current immediate records:

- scan 50 / printed 35 — `மாதரின் கண்ட மலர்கள்` opening, completed under the earlier verified-page cadence;
- scan 51 / printed 36 — transcription-only, `needs-review`;
- scan 52 — illustration capture, `needs-review`;
- scan 53 / printed 38 — fast transcription-only, `needs-review`.

Scans **7–8** remain `partial` source/page records.

# Existing completed / verified body work

These earlier verified records remain preserved and are not downgraded:

- `மலர்மாரி பொழிகின்றேன்!` — scans **17–19**;
- `யாதும் ஊரே; யாவரும் கேளிர்!` — scans **20–24**;
- `மானங்காத்த மறவன்!` — scans **25–30**;
- `துணை நின்றார் தோழி!` — scans **31–36**;
- `சுமந்தவன் சுமந்த சோகம்!` — scans **37–41**;
- `பாவை புகழ்ந்த பன்றி` — scans **42–46**;
- `காக்கைக்கு நன்றி காட்ட...` — scans **47–49**.

The later full-volume Passes 2–7 still run from scan 1 through scan 497 so the final audit is systematic across the entire source.

Verified printed provenance already preserved:

- scan 19 — `பத்துப்பாட்டு (குறிஞ்சிப்பாட்டு)` / `61 முதல் 95 முடிய` / `கபிலர்`
- scan 24 — `புறநானூறு - பாடல் : 192` / `கணியன் பூங்குன்றன்`
- scan 30 — `புறநானூறு : பாடல்: 74` / `சேரமான் கணைக்கால் இரும்பொறை`
- scan 36 — `ஐங்குறுநூறு : பாடல் : 180` / `அம்மூவனார்`
- scan 41 — `புறநானூறு : பாடல் : 286` / source-visible `ஒளவையார்`
- scan 46 — `அகநானூறு : பாடல் : 248` / `கபிலர்`
- scan 49 — `குறுந்தொகை : பாடல் : 210` / `காக்கைப்பாடினியார் நச்செள்ளையார்`

New provenance encountered during Pass 1 does not require immediate register synchronization; the systematic provenance sweep is Pass 6.

# Section 008 — current provisional context

Decorative heading: **`மாதரின் கண்ட மலர்கள்`**

- starts at scan **50 / printed 35**;
- records currently exist through scan **53**;
- section end remains provisional/unmapped;
- Pass 1 must not stop to investigate the section end;
- canonical section structure will be established in Pass 5.

# Exact next activity

**Pass 1 only: process scan 54 as fast transcription/physical capture, commit the page record, then continue sequentially toward scan 497.**

Do not perform Pass 2–8 work in that routine page iteration.

# Completed Thirukkural baseline — DO NOT RESTART

`works/thirukkural/` remains complete:

- Tamil Parts **001–015** archival-ready through scan **323**;
- commentary through printed page **270 / Kural 1330**;
- English project translation Parts **001–015** released;
- semantic provenance complete for **3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள்**;
- final structure audit PASS.