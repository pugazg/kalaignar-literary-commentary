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
- Gate C2 — lexical source correction only if explicitly authorized by the user
- Gate D — physical / visual / continuity closure
- Gate E — canonical section reconstruction
- Gate F — Sangam provenance audit
- Gate G — metadata/status closure
- Gate H — derived navigation
- Gate I — final whole-volume synchronization/closure

Until Gate C2 is explicitly authorized, do not claim word-for-word scan lexical verification for the whole volume.

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

Gate B — **IN PROGRESS**:
- B01–B18 complete
- structurally reviewed — **450/497**
- remaining — **47**
- frontier — **scan 451**
- latest B18 page-layer endpoint — `0b77065c14ab3495fd3282c7697db5fb86b2cbcc`
- latest durable B18 progress commit — `3342dcf878f72692bfa86b19f4b73e8ea56fc434`
- Gate C — **NOT STARTED**

Durable extraction exceptions:
- File9 Book Pages **401–412** are not reliable one-to-one lexical blocks for physical scans **413–424**.
- File9 Phase 20 advertises Book Pages **413–438**, but its supplied payload ends at **Page 425**. Usable Page 414–425 blocks cover scans **426–437**; scans **438–450** have no File9 lexical block and must not receive a synthetic mapping.

Durable mixed-page correction: scan **359** is mixed text/illustration, not illustration-only.

### Exact next activity

Process Gate B B19 scans **451–475** using `TVA_BOK_0042551_சங்கத்_தமிழ்_part_010_pages_451-497.pdf` + `File10.md`. Resolve File10 comment mapping against the PDF before applying the lock. Expected next frontier after B19: **scan 476**. Do not start Gate C.
