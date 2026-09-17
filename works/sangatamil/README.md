# சங்கத் தமிழ் — கலைஞர் மு. கருணாநிதி

Source-first archival workspace for the 497-scan volume TVA_BOK_0042551_சங்கத்_தமிழ்.pdf.

## Current state — 2026-09-17

Gate A — COMPLETE / PASS:
- canonical page records — 497/497
- duplicate aliases — 0
- missing scans — 0

Gate B — COMPLETE / PASS:
- completed batches — B01–B20
- structurally reviewed — 497/497
- remaining — 0
- unresolved structural placement issues — 0

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
- cumulative discrepancy records — 140
- mode — audit-only / no page-wording changes
- latest ledger commit — bf82324200e91ff05b76aed18b06c18b37883b90

Latest B20 page-layer endpoint: e8919ea260fdc3c8a5e8fef643bdd1ff3691a49c

Gate-B closure / latest durable B20 progress checkpoint: 90caaeb3bd92201a75d45f617727721b9c3e0df7

B15 mixed-page repair preserved: 6525498cd8e14871575e9ae0203060af2fe4450a — scans 358–359 are mixed text/illustration records; scan 359 must not regress to illustration-only.

## Active authoritative controls

1. PRODUCTIVE_COMPLETION_PLAN.md
2. C2_SOURCE_CORRECTION_PROGRESS.md
3. POST_C2_RECONCILIATION.md
4. GATE_G_METADATA_STATUS_AUDIT.md
5. GEMINI_TEXT_LOCK.md — historical lexical-lock baseline
6. STRUCTURAL_FIDELITY_PROGRESS.md
7. GATE_A_HYGIENE_REPORT.md
8. ../../SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md
9. ../../NEXT_CHAT_PROMPT_SANGATH_TAMIL.md

MULTI_PASS_WORKFLOW.md and GEMINI_RECONCILIATION_PLAN.md are historical/superseded methodology records; they are not live frontier authorities.

## Authority split

- PDF scan — physical-page and structural authority
- Gemini File1.md … File10.md — historical lexical scaffold
- user Gate-C2 adjudications — controlling authority for the 140 recorded Gate-C discrepancies
- repository — preservation layer

Gate B corrects placement, headings, paragraph order, punctuation, quotation structure, verse lineation, spacing, separators, continuation order, illustration/divider/blank placement and provenance/gloss block structure while preserving legitimate Gemini lexical wording.

Clearly unsupported extraction debris is excluded. Legitimate scan/Gemini lexical disagreements are recorded rather than silently source-corrected.

## Archival layers

1. pages/ — canonical physical scan records
2. sections/ — canonical source-order navigation, **Gate E COMPLETE / PASS**
3. indexes/page-map.md — physical status map
4. indexes/section-register.md — **Gate E COMPLETE / PASS**
5. indexes/source-citation-register.md — finalized in Gate F

## Status rule

Gate-B structural completion does not automatically promote a page to verified. Gate C2 is now closed for all 140 recorded Gate-C discrepancies, but that does **not** equal a fresh token-by-token verification of every word in all 497 scans; whole-volume word-for-word scan verification is therefore still not claimed.

Gate D — COMPLETE / PASS:
- physical scans — 497/497
- canonical records — 497/497
- unresolved physical / visual / continuity issues — 0
- page changes during Gate D — 0
- durable report — `PHYSICAL_CONTINUITY_AUDIT.md`

Gate E — COMPLETE / PASS:
- source-order section-role entries — 104
- assigned scans — 497/497 exactly once
- section READMEs — 104
- canonical page-wording changes — 0
- durable report — `SECTION_COVERAGE_AUDIT.md`

## Gate F closure

Gate F — **COMPLETE / PASS**:
- batches — **F01–F20**
- provenance-audited scans — **497/497**
- formal citation-provenance units — **115**
- standalone source-note-only provenance records — **4**
- canonical page-wording changes — **0**
- unresolved provenance gaps — **0**
- physical provenance endpoint — **scan 497 / back cover**

Durable outputs:
- indexes/source-citation-register.md
- PROVENANCE_AUDIT.md

## Gate C2 — user-adjudicated lexical/source correction

Gate C2 is **COMPLETE / APPLIED**:

- C2-01 through C2-20 — complete
- disposition coverage — **497/497 scans**
- historical Gate-C discrepancies adjudicated — **140/140**
- remaining discrepancies — **0**
- no C2-locked scan range remains
- durable record — `C2_SOURCE_CORRECTION_PROGRESS.md`
- post-C2 reconciliation R1 — **COMPLETE / PASS**
- reconciliation record — `POST_C2_RECONCILIATION.md`
- scan 8 handwritten `முன்னுரை` remains description-only by explicit user direction

Whole-volume wording must **not** be described as word-for-word scan verified.

## Gate G closure

Gate G — **COMPLETE / PASS**:
- canonical page records audited — **497/497**
- required metadata field presence after repair — **497/497**
- demonstrable defects repaired — **11 missing `visual_fidelity` fields**
- final `status` distribution — **43 verified / 453 needs-review / 1 partial**
- final `visual_fidelity` distribution — **43 verified / 454 needs-review / 0 missing**
- canonical wording changes — **0**
- unresolved Gate-G inconsistencies — **0**
- durable report — `GATE_G_METADATA_STATUS_AUDIT.md`
- page-layer correction endpoint — `fd024e4c0b1d3f21a3849c360d509350ce808db5`

The mixed page-level status distribution is intentional; C2 resolved the recorded discrepancy ledger but did not perform a fresh token-by-token reread of every source word.

## Gate H closure

Gate H — **COMPLETE / PASS**:
- source-order sections indexed — **104/104**
- physical scan coverage inherited — **497/497**
- formal provenance units indexed — **115/115**
- source-note-only records indexed — **4/4**
- provenance leaves — **119**
- canonical page-wording changes — **0**
- durable report — `GATE_H_DERIVED_NAVIGATION_REPORT.md`
- derived navigation root — `navigation/`
- Gate-H commit — `c9e0b7a4a7963f3dc046e79951d718b2a3d9a41a`

## Final Gate I closure

Gate I — **COMPLETE / PASS**. The Sangath Tamil archival pipeline is closed through derived navigation and final synchronization.

Final declaration:

**ARCHIVAL STRUCTURE / PHYSICAL / SECTION / PROVENANCE / METADATA / NAVIGATION CLOSED — RECORDED C2 DISCREPANCIES ADJUDICATED — WHOLE-VOLUME WORD-FOR-WORD SCAN VERIFICATION NOT CLAIMED.**

## Maintained English translation — ACTIVE

A separately scoped project-created English layer is active under `translations/en/`, modeled on the maintained-English Kuraloviyam workflow. Drafts D1–D6 scans **1–222 are COMPLETE / PASS**.

Controls:
- `translations/en/README.md`
- `translations/en/TRANSLATION_GUIDE.md`
- `translations/en/TRANSLATION_STATUS.md`
- `translations/en/GLOSSARY.md`

This downstream layer does **not** reopen or mass-promote the canonical Tamil records and does not change the declaration that whole-volume word-for-word scan verification is not claimed.

## Exact next activity

**English Draft D7 — scans 223–259**, continuing first-pass page-aligned drafting. D1–D6 are closed at **222/497** with **221 draft + 1 source-limited (scan 8)**.
