# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

Last synchronized with live main: **2026-09-17**.

## திட்டமிட்ட / உள்ள நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–015 **ARCHIVAL-READY through scan 323**; commentary through printed page 270 / Kural 1330 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–015 **RELEASED through the end of the supplied volume** |
| Thirukkural semantic structure | பால் → இயல் → அதிகாரம் | **COMPLETE — 3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள் mapped** |
| சங்கத் தமிழ் | தமிழ் | **CLOSED — Gates A–I + Gate C2 COMPLETE / PASS; post-C2 reconciliation R1 COMPLETE / PASS** |
| Sangatamil | English project translation | **ACTIVE — Drafts D1–D7 scans 1–259 COMPLETE / PASS; 259/497 drafted; D8 scans 260–296 next** |
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
Historical lexical-lock baseline: works/sangatamil/GEMINI_TEXT_LOCK.md
Final C2 adjudication record: works/sangatamil/C2_SOURCE_CORRECTION_PROGRESS.md
Post-C2 reconciliation: works/sangatamil/POST_C2_RECONCILIATION.md

Authority split:
- PDF scan — physical/structural authority
- Gemini File1–File10 — historical lexical scaffold
- user Gate-C2 adjudications — controlling authority for the 140 recorded Gate-C discrepancies
- repository — preservation layer

## Current progress

Gate A — COMPLETE / PASS: 497/497 canonical records; 0 duplicates; 0 missing.

Gate B — COMPLETE / PASS:
- B01–B20 complete
- 497/497 structurally reviewed
- 0 remaining
- 0 unresolved structural placement issues

Gate C — COMPLETE / PASS:
- C01 scans 1–25 — COMPLETE / PASS
- C02 scans 26–50 — COMPLETE / PASS
- C03 scans 51–75 — COMPLETE / PASS
- C04 scans 76–100 — COMPLETE / PASS
- C05 scans 101–125 — COMPLETE / PASS
- C06 scans 126–150 — COMPLETE / PASS / CLEAN
- C07 scans 151–175 — COMPLETE / PASS
- C08 scans 176–200 — COMPLETE / PASS
- C09 scans 201–225 — COMPLETE / PASS
- C10 scans 226–250 — COMPLETE / PASS
- C11 scans 251–275 — COMPLETE / PASS
- C12 scans 276–300 — COMPLETE / PASS
- C13 scans 301–325 — COMPLETE / PASS
- C14 scans 326–350 — COMPLETE / PASS
- C15 scans 351–375 — COMPLETE / PASS
- C16 scans 376–400 — COMPLETE / PASS
- C17 scans 401–425 — COMPLETE / PASS
- C18 scans 426–450 — COMPLETE / PASS
- C19 scans 451–475 — COMPLETE / PASS
- C20 scans 476–497 — COMPLETE / PASS — FINAL
- audited — 497/497
- remaining — 0
- closure — 497/497
- 140 cumulative substantive discrepancies recorded
- Gate C itself was audit-only; subsequent user-authorized Gate C2 resolved all 140 recorded discrepancies

Latest B20 page-layer endpoint: e8919ea260fdc3c8a5e8fef643bdd1ff3691a49c
Gate-B closure / B20 progress: 90caaeb3bd92201a75d45f617727721b9c3e0df7
Latest durable B16 progress checkpoint: 40e2c594a7a9f7f4baa88375b23e84d39c619235

B15 mixed-page repair preserved: 6525498cd8e14871575e9ae0203060af2fe4450a — scans 358–359 are mixed text/illustration records.

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

Gate D — **COMPLETE / PASS**: 497/497 physical scans closed; 497 canonical records; 0 unresolved physical / visual / continuity issues; durable report `works/sangatamil/PHYSICAL_CONTINUITY_AUDIT.md`.

Gate E — **COMPLETE / PASS**: 104 source-order section-role entries; 497/497 scans assigned exactly once; 0 canonical page-wording changes; durable report `works/sangatamil/SECTION_COVERAGE_AUDIT.md`.

Gate F — **COMPLETE / PASS — F01–F20 scans 1–497 / 115 formal citation-provenance units / 4 standalone source-note-only provenance records / 0 canonical page-wording changes**

Current handover: HANDOVER.md.


## Gate C2 final state — சங்கத் தமிழ்

- C2-01 through C2-20 — **COMPLETE / APPLIED**
- disposition coverage — **497/497 scans**
- historical Gate-C discrepancy records adjudicated — **140/140**
- remaining discrepancy records — **0**
- no C2-locked scan range remains
- scan **8** handwritten முன்னுரை — description-only; no handwriting transcription required by user direction
- durable progress — `works/sangatamil/C2_SOURCE_CORRECTION_PROGRESS.md`
- post-C2 reconciliation R1 — **COMPLETE / PASS**
- reconciliation record — `works/sangatamil/POST_C2_RECONCILIATION.md`
- whole-volume word-for-word scan verification — **NOT CLAIMED**

Gate G — **COMPLETE / PASS — 497/497 metadata/status audited / 11 missing visual-fidelity fields repaired / 0 unresolved / 0 wording changes**.

Gate H — **COMPLETE / PASS — derived navigation built from 104 sections / 115 formal provenance units + 4 source-note-only records / 0 page changes**.

Gate I — **COMPLETE / PASS — final synchronization / closure**.

Exact Tamil archival activity: **none; Sangath Tamil archival pipeline is closed**. Separate downstream activity: **maintained English Draft D8, scans 260–296**; D1–D7 are complete at **259/497**.
