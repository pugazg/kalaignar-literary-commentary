# Next Chat Prompt — குறளோவியம் archival project

Continue the Kalaignar Literary Commentary archival project directly in:

`pugazg/kalaignar-literary-commentary`

Branch: `main`

Active work: `works/kuraloviyam/`

Current controlling split source:

`TVA_BOK_0065733_குறளோவியம்_part_001_pages_1-111.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve the newest durable state. Do not reset or repeat completed work because this prompt contains an older checkpoint.

## Mandatory startup

Before any repository change, read completely:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this `NEXT_CHAT_PROMPT_KURALOVIYAM.md`
5. `works/kuraloviyam/README.md`
6. `works/kuraloviyam/SOURCE_INTAKE_PART_001.md`
7. `works/kuraloviyam/metadata/source.md`
8. `works/kuraloviyam/metadata/transcription-policy.md`
9. `works/kuraloviyam/indexes/page-map.md`
10. `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_001.md`
11. `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_001.md`

Then inspect the actual supplied source scans before writing.

## Source identity

The user reports the complete Kuraloviyam PDF as **666 physical pages**, manually split into **six parts of 111 pages** because the original exceeds the upload limit.

Canonical overall scan mapping:

- Part 001: 1–111
- Part 002: 112–222
- Part 003: 223–333
- Part 004: 334–444
- Part 005: 445–555
- Part 006: 556–666

Repository `scan_page` never restarts for a split PDF. Part 001 has no usable parsed text layer; the rendered source scan is controlling.

## Completed state

Part 001 source intake and Pass 1 are complete: **111 / 111 physical scans captured**. Scan 18 begins the main body at printed page 1; scan 111 is printed page 94.

### Part 001 Pass 2A — COMPLETE

`works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_001.md` records direct textual verification for **all scans 1–111**. Do not restart Pass 2A.

### Part 001 Pass 2B — scans 1–88 COMPLETE

The durable independent lexical-fidelity record is:

`works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_001.md`

Overall scans **1–88** have now been independently re-read word by word against the rendered source after Pass 2A was closed.

Batch-8 source-supported corrections for scans 78–88:

- scan **78 / printed 61** — `நிலாப் புதுமையைக்` → source-visible `நிலாப் பதுமையைக்`;
- scan **79 / printed 62** — `ஆடியில் பார்த்துப்` → source-visible `ஆடியிற் பார்த்துப்`;
- scan **82 / printed 65** — `இந்தநிறம் ஏற்பட்டது` → source-visible `இந்நிறம் ஏற்பட்டது`; the later quoted phrase remains source-visible `இந்த நிறம்`;
- scan **84 / printed 67** — `வேல்பட்டு பகையரசன்` → source-visible `வேல்பட்டுப் பகையரசன்`;
- scan **88 / printed 71** — `அடியபடும் உங்களுக்கு` → source-visible `அடிபடும் உங்களுக்கு`.

Scans **80–81, 83, and 85–87** required no new Pass-2B page-record correction.

Earlier source limitations remain:

- scans **13–15** — handwritten/facsimile bodies remain `partial`; printed headings/material were checked, but handwriting must not be reconstructed;
- scan **19** — the physically washed-out/faint central printed region remains `partial`; do not infer missing words from context.

## Pass 2B rule

Pass 2B is an independent second reading, not a confirmation of the Pass-2A change list. Re-read every source-visible printed word against the rendered scan with special attention to:

- `ர / ற`;
- `ன / ண`;
- `ல / ள / ழ`;
- vowel signs and compound-letter distinctions;
- source-visible spacing and joining;
- old/uncommon printed forms;
- names and titles;
- quotations and Kural text;
- punctuation where it affects textual fidelity.

Do not import standard Kural readings, modern spellings, contextual guesses, OCR guesses or web/reference text. The rendered scan remains controlling.

Pass 3 remains a separate visual-structure / visual-text fidelity gate and must not be used as the lexical safety net.

## Exact next activity

If live `main` has not advanced beyond this frontier:

1. continue **Part 001 Pass 2B — independent lexical-fidelity re-read**;
2. process **overall scans 89–99**;
3. independently re-read every source-visible printed word against the rendered scan;
4. compare that independent reading against each existing Markdown page record;
5. correct only differences visibly supported by the controlling scan;
6. pay special attention to character-level confusions, vowel signs, old/uncommon forms, names, quotations/Kurals, joining and spacing;
7. preserve genuine source limitations as `partial` / `blocked`; never reconstruct from context;
8. append Batch-9 results to `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_001.md` without claiming Pass 3 completion or assigning final `verified` status;
9. audit the changed-file set before advancing beyond scan 99.

Do not begin Part 002. Do not begin Pass 3, the Part audit, or English translation before Part 001 Pass 2B is complete.