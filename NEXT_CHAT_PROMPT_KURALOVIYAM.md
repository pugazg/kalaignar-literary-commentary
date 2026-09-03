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

Repository `scan_page` never restarts for a split PDF.

Part 001 has no usable parsed text layer; the rendered source scan is controlling.

## Completed state

Part 001 source intake is complete and Pass 1 is complete: **111 / 111 physical scans captured**. Scan 18 begins the main body at printed page 1; scan 111 is printed page 94.

### Part 001 Pass 2A — textual verification through scan 44 COMPLETE

The durable verification record is:

`works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_001.md`

Pass 2A has directly compared overall scans **1–44** against the rendered source.

Recent Batch-4 source-supported corrections:

- scan 35 — `மழை பொழிந்து` → `மழை பொழிந்தது`;
- scan 36 — restored the source dash after `‘வேண்டுதல் வேண்டாமை இலான்’`; removed the non-source hyphen from `அதிகாரம் 5 - இல்வாழ்க்கை`;
- scan 37 — `வேலை நிகழ்த்த` → `வேலை நிறுத்த`; `என இன்னும் மொண்டு தரும்` → `என இன்பம் மொண்டு தரும்`;
- scan 38 — Kural spacing `இந்நோய்` → `இந் நோய்`;
- scan 40 — `எழுதி காட்டுகிறார்` → `எழுதிக் காட்டுகிறார்`;
- scan 42 — `பிறவி உள்ளது என` → `பிறவி உள்ளதென`;
- scan 43 — `ஒரு பார்வையால் அவனுக்கு வேதனை உண்டாக்குகிறாள்` → `ஒரு பார்வையால் அவனுக்கு வேதனை உண்டாகிறது`.

Scans **34, 39, 41 and 44** required no page-record textual correction after direct source comparison.

Earlier source limitations remain:

- scans **13–15** — handwritten/facsimile bodies remain `partial`; do not reconstruct them;
- scan **19** — a small physically washed-out/faint printed region remains `partial`; do not infer lost words from context.

### Mandatory Pass 2B safeguard

After the user identified the scan-11 `ர` / `ற` miss, the workflow was strengthened. Once Pass 2A reaches scan 111, perform an independent **Pass 2B lexical-fidelity re-read** across every printed word in Part 001 before Pass 3.

Pass 2B must specifically look for character-level confusions such as `ர/ற`, `ன/ண`, `ல/ள/ழ`, vowel marks, old/uncommon printed forms, names, quotations and Kural text. Pass 3 remains a separate visual-structure gate and must not be relied on as the lexical safety net.

## Exact next activity

If live `main` has not advanced beyond this frontier:

1. continue **Part 001 Pass 2A — textual verification**;
2. process **overall scans 45–55**;
3. compare each existing Markdown page record directly against the rendered source scan;
4. verify source-visible wording, punctuation, paragraph boundaries, headings, quoted/Kural text, printed-page metadata and separation of printed text from handwriting/stamps/other non-source marks;
5. correct only what the controlling scan visibly supports;
6. do not modernize, normalize, silently repair old/uncommon forms, or import a standard Kural reading from memory/web sources;
7. append results to `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_001.md` without claiming Pass 2B or Pass 3 completion;
8. preserve genuine source limitations as `partial` / `blocked`; never reconstruct from context;
9. audit the changed-file set before advancing beyond scan 55.

Do not restart Pass 1. Do not begin Pass 2B until Pass 2A reaches scan 111. Do not begin Pass 3, the Part audit, or English translation before both Pass 2A and Pass 2B are complete.
