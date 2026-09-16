# சங்கத் தமிழ் — archival / provenance guidelines

This document governs active work under works/sangatamil/ in pugazg/kalaignar-literary-commentary.

The authoritative execution plan is works/sangatamil/PRODUCTIVE_COMPLETION_PLAN.md. The current lexical policy is works/sangatamil/GEMINI_TEXT_LOCK.md. Durable Gate-B progress is recorded in works/sangatamil/STRUCTURAL_FIDELITY_PROGRESS.md.

Historical methodology files such as MULTI_PASS_WORKFLOW.md and GEMINI_RECONCILIATION_PLAN.md are retained for provenance only and do not override the current gate plan or lexical lock.

## 1. Current controlling rule

> Keep the supplied legitimate words from the Gemini transcription. Correct source-supported structure and presentation from the PDF. Do not silently source-correct lexical words.

Authority split:

1. Gemini File1.md … File10.md = lexical/text-wording lock
2. controlling PDF scan = physical-page and structural authority
3. repository = preservation layer

For legitimate printed body text, do not replace Gemini words, characters, spellings, names, quoted wording, old/uncommon forms or lexical choices merely because the PDF visibly differs. Record the discrepancy for later lexical audit.

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

- Gate C — lexical discrepancy audit under the current lock
- Gate C2 — lexical/source correction only for batches explicitly adjudicated by the user; C2-01 and C2-02 are authorized/applied, later scans remain locked
- Gate D — physical / visual / continuity closure
- Gate E — canonical section reconstruction
- Gate F — Sangam provenance audit
- Gate G — metadata/status closure
- Gate H — derived navigation
- Gate I — final whole-volume synchronization/closure

Gate C2 is only partially authorized. Do not claim whole-volume word-for-word verification while scans 51–497 remain locked.

## 8. Documentation synchronization discipline

Operational documents must not retain an obsolete live frontier.

After each completed Gate-B batch, synchronize at minimum:

- works/sangatamil/STRUCTURAL_FIDELITY_PROGRESS.md
- NEXT_CHAT_PROMPT_SANGATH_TAMIL.md
- this guideline current-state block
- root HANDOVER.md
- works/sangatamil/README.md
- root README.md

Section/provenance derived indexes and section READMEs remain deferred to their designated later gates unless their current-state banner itself becomes false.

Historical/superseded methodology files must be clearly labelled historical and must not advertise an obsolete task as current.

## 9. Current durable state — refreshed 2026-09-16

Gate A — **COMPLETE / PASS**: 497/497 canonical page records; 0 duplicate aliases; 0 missing scans.

Gate B — **COMPLETE / PASS**:
- B01–B20 complete
- structurally reviewed — **497/497**
- remaining — **0**
- unresolved structural placement issues — **0**
- latest B20 page-layer endpoint — `e8919ea260fdc3c8a5e8fef643bdd1ff3691a49c`
- Gate-B closure / durable B20 progress commit — `90caaeb3bd92201a75d45f617727721b9c3e0df7`

Gate C — **COMPLETE / PASS**:
- C01 scans **1–25 — COMPLETE / PASS**
- C02 scans **26–50 — COMPLETE / PASS**
- C03 scans **51–75 — COMPLETE / PASS**
- C04 scans **76–100 — COMPLETE / PASS**
- C05 scans **101–125 — COMPLETE / PASS**
- C06 scans **126–150 — COMPLETE / PASS / CLEAN**
- C07 scans **151–175 — COMPLETE / PASS**
- C08 scans **176–200 — COMPLETE / PASS**
- C09 scans **201–225 — COMPLETE / PASS**
- C10 scans **226–250 — COMPLETE / PASS**
- C11 scans **251–275 — COMPLETE / PASS**
- C12 scans **276–300 — COMPLETE / PASS**
- C13 scans **301–325 — COMPLETE / PASS**
- C14 scans **326–350 — COMPLETE / PASS**
- C15 scans **351–375 — COMPLETE / PASS**
- C16 scans **376–400 — COMPLETE / PASS**
- C17 scans **401–425 — COMPLETE / PASS**
- C18 scans **426–450 — COMPLETE / PASS**
- C19 scans **451–475 — COMPLETE / PASS**
- C20 scans **476–497 — COMPLETE / PASS — FINAL**
- audited — **497/497**
- remaining — **0**
- closure — **497/497 audited**
- cumulative discrepancy records — **140**
- latest Gate-C ledger commit — `bf82324200e91ff05b76aed18b06c18b37883b90`
- Gate C2 — **PARTIALLY AUTHORIZED — scans 1–50 user-adjudicated/applied; scans 51–497 locked**

Wording state remains **Gemini-lexical-locked**, not word-for-word scan verified.

Durable extraction/mapping exceptions from Gate B remain authoritative in `STRUCTURAL_FIDELITY_PROGRESS.md`.

C20 execution note: the supplied Part-010 PDF/File10 pair was used for scans 476–497. Six substantive discrepancies were recorded across 5 scans. Gate C closed at 497/497 with 140 cumulative discrepancy records and 0 canonical page-wording changes. Gate C2 is partially authorized through scan 50 only.

Gate D — **COMPLETE / PASS**:
- physical scans audited — **497/497**;
- canonical records — **497/497**;
- unresolved physical / visual / continuity issues — **0**;
- canonical page changes during Gate D — **0**;
- durable report — `works/sangatamil/PHYSICAL_CONTINUITY_AUDIT.md`.

### Exact next activity

Gate E — **COMPLETE / PASS**: 104 source-order section-role entries; 497/497 scans assigned exactly once; 0 canonical page-wording changes; durable report `works/sangatamil/SECTION_COVERAGE_AUDIT.md`.

Gate F — **COMPLETE / PASS — F01–F20 scans 1–497 / 115 formal citation-provenance units / 4 standalone source-note-only provenance records / 0 canonical page-wording changes**


## Gate F provenance closure — 2026-09-16

- Gate F — **COMPLETE / PASS**
- scans audited — **497/497**
- formal citation-provenance units — **115**
- standalone source-note-only provenance records — **4**
- unresolved provenance gaps — **0**
- canonical page-wording changes — **0**
- Gate C2 — **PARTIALLY AUTHORIZED — C2-01/C2-02 applied through scan 50**
- scans 51–497 — **LOCKED**
- Gate G — **DEFERRED**
- next activity — **wait for user C2 findings for scans 51–75**


## Gate C2 manual-adjudication rule

The user's manual findings are the controlling evidence for Gate C2. Where a manual C2 ruling says **Gemini is correct**, preserve that wording even if the historical Gate-C ledger suggested a source divergence. Apply source wording or repository-placement repair only where the user authorizes it.

Current C2 state:
- C2-01 scans **1–25 — COMPLETE / APPLIED**
- C2-02 scans **26–50 — COMPLETE / APPLIED**
- scan **8** handwritten முன்னுரை — description-only; do not interpret/transcribe
- scans **51–497 — C2 NOT AUTHORIZED / Gemini lock remains**
- durable record — `works/sangatamil/C2_SOURCE_CORRECTION_PROGRESS.md`
