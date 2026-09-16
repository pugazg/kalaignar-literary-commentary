# சங்கத் தமிழ் — archival / provenance guidelines

This document governs active work under works/sangatamil/ in pugazg/kalaignar-literary-commentary.

The authoritative execution plan is works/sangatamil/PRODUCTIVE_COMPLETION_PLAN.md. `GEMINI_TEXT_LOCK.md` is the historical lexical-lock baseline; the final user-adjudicated lexical authority for recorded discrepancies is `works/sangatamil/C2_SOURCE_CORRECTION_PROGRESS.md`. Post-C2 dependency synchronization is recorded in `works/sangatamil/POST_C2_RECONCILIATION.md`.

Historical methodology files such as MULTI_PASS_WORKFLOW.md and GEMINI_RECONCILIATION_PLAN.md are retained for provenance only and do not override the current gate plan or lexical lock.

## 1. Current controlling rule

> Preserve the final canonical wording established by the completed gate chain. Do not reopen user-adjudicated C2 decisions or silently normalize historical forms.

Authority split:

1. controlling PDF scan = physical-page and structural authority;
2. Gemini File1.md … File10.md = historical lexical scaffold used by Gates B/C;
3. user Gate-C2 adjudications = controlling authority for the 140 recorded Gate-C discrepancies;
4. repository = preservation layer.

All 140 recorded Gate-C discrepancies have now been dispositioned. User-confirmed **Gemini is correct** readings remain protected; user-authorized source/repository corrections remain canonical. New lexical changes require new evidence or explicit user instruction.

### 1.1 Structural corrections allowed in Gate B

Use the PDF to correct physical placement, printed page metadata, paragraph order/boundaries, punctuation, quotation structure, headings, speaker-label placement, verse lineation, spacing/alignment, separators, provenance / பொருள் விளக்கம் placement, continuation order, illustration/divider/blank placement and running-header/footer handling.

### 1.2 Non-source extraction debris

Exclude library/accession stamps, handwriting OCR garbage, scanner artefacts, bleed-through garbage, duplicated page furniture, extraction wrappers, mixed-script artefacts and clearly unsupported tokens from literary body text.

### 1.3 Missing lexical material

If the scan visibly contains legitimate lexical wording absent from Gemini, do not source-transcribe it into the body during Gate B unless the user explicitly authorizes lexical recovery. Record the omission for later Gate C/C2 handling.

## 2. Source boundary

- controlling source — TVA_BOK_0042551_சங்கத்_தமிழ்.pdf
- physical scans — 1–497
- scan 497 — back cover
- never create scan 498+
- printed-page numbers come from the scan, never arithmetic
- every physical scan has one canonical Markdown record under works/sangatamil/pages/

Gate A is closed at 497/497 canonical records / 0 duplicates / 0 missing.

## 3. Gemini and split-PDF workflow

The complete lexical layer is File1.md … File10.md. Use the split PDF covering the live frontier with the matching FileN.md. Gemini page comments are navigation aids only; they do not control physical scan sequencing and may omit illustrations/dividers or displace continuation lines.

## 4. Gate-B procedure

For each scan: fetch live main, fetch the canonical page record, inspect the controlling scan, align Gemini locked wording, preserve legitimate Gemini lexical words, correct only source-supported structure/presentation, remove clearly unsupported debris, record lexical disagreements/omissions, preserve non-text physical pages, and keep status promotion separate.

Normal Gate-B batch: 25 physical scans.

At batch close: compare batch base → page-layer endpoint, verify only intended page files changed, update STRUCTURAL_FIDELITY_PROGRESS.md separately, then refresh the operational current-state documents listed in section 8.

## 5. Verse / prose / quotation handling

Gemini controls legitimate lexical wording; the scan controls organization. Correct verse lineation, stanza grouping, prose paragraphs, dialogue grouping, speaker labels, quotation punctuation and block boundaries, provenance / பொருள் விளக்கம் placement, headings and separators from the scan.

Do not substitute a web/critical-edition Sangam verse or a scan-derived alternative lexical reading for locked Gemini text during Gate B.

## 6. Illustration / divider / blank / marks

Illustration/divider/blank pages remain canonical physical records. For illustration-only pages, use factual visual description and only transcribe source-visible printed captions. Handwriting, stamps and scanner artefacts are not literary body text.

## 7. Later gates

- Gate C — **COMPLETE / PASS**
- Gate C2 — **COMPLETE / APPLIED — 497/497 disposition coverage / 140/140 records**
- Post-C2 reconciliation R1 — **COMPLETE / PASS**
- Gate D — **COMPLETE / PASS**
- Gate E — **COMPLETE / PASS**
- Gate F — **COMPLETE / PASS**
- Gate G — **COMPLETE / PASS — 497/497 metadata/status audited / 11 missing visual-fidelity fields repaired / 0 unresolved**
- Gate H — **ACTIVE / NEXT — derived navigation**
- Gate I — final whole-volume synchronization/closure

Do not claim whole-volume word-for-word verification merely from C2 closure; C2 resolved the recorded discrepancy ledger rather than re-running every token in the source.

## 8. Documentation synchronization discipline

Operational documents must not retain an obsolete live frontier. Current live status is controlled by the productive completion plan, C2 closure record, post-C2 reconciliation record, root/work READMEs, HANDOVER, and the next-chat prompt.

Historical Gate-B/C/D/E/F reports may retain their original gate-time methodology when clearly labelled historical, but current-state banners and handoffs must reflect completed C2 and reconciliation.

## 9. Current durable state — refreshed 2026-09-16

- Gate A — **COMPLETE / PASS — 497/497 canonical records / 0 duplicates / 0 missing**
- Gate B — **COMPLETE / PASS — 497/497 structurally reviewed / 0 unresolved placement issues**
- Gate C — **COMPLETE / PASS — 497/497 audited / 140 historical discrepancy records**
- Gate C2 — **COMPLETE / APPLIED — 497/497 disposition coverage / 140/140 records adjudicated / 0 remaining**
- Gate D — **COMPLETE / PASS — 497/497 physical/visual/continuity / 0 unresolved**
- Gate E — **COMPLETE / PASS — 104 section-role entries / 497/497 scans assigned exactly once**
- Gate F — **COMPLETE / PASS — 115 formal provenance units + 4 source-note-only records / 0 unresolved provenance gaps**
- Post-C2 reconciliation R1 — **COMPLETE / PASS**
- Gate G — **COMPLETE / PASS — 497/497 audited / 0 unresolved metadata-status inconsistencies**
- Gate-G durable report — `works/sangatamil/GATE_G_METADATA_STATUS_AUDIT.md`
- no C2-locked scan range remains
- whole-volume word-for-word scan verification — **NOT CLAIMED**
- reconciliation record — `works/sangatamil/POST_C2_RECONCILIATION.md`

### Exact next activity

Proceed to **Gate H — derived navigation layer**. Build only downstream navigation/crosswalk/index artifacts from the closed canonical layer; do not mutate page wording or reopen Gates B–G.
