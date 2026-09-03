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

### Part 001 Pass 2A — textual verification through scan 22 COMPLETE

The durable verification record is:

`works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_001.md`

Pass 2A has directly compared overall scans **1–22** against the rendered source.

Important source-supported corrections already made include:

- scans 1–2 — author line → `கலைஞர் மு.கருணாநிதி`;
- scan 5 — `வாரந்தோறும்` → `வாரந் தோறும்`;
- scan 11 — `பெற்றுள்ளன.` → `பெற்றுள.` and, after user flag/direct re-check, `உறனுண்டு` → `உரனுண்டு`;
- scan 13 — `முன்னாம் பதிப்பின் முகப்புரை` → `மூன்றாம் பதிப்பின் முகப்புரை`;
- scan 14 — author line → `கலைஞர் மு.கருணாநிதி`;
- scan 17 — `வண்ணங்கள்` → `வர்ணனைகள்`; deferred parentheticals resolved from the scan; `அம்மன் திருமண நிலையம்` → `திருமகள் நிலையம்`;
- scan 19 — `பொன்னால்` → `பொன்னை`; central washed-out/faint printed words remain source-limited and the page is `partial` rather than reconstructed;
- scan 20 — `காட்டிக் கொண்டிருக்கிறார்` → `காட்டிக் கொண்டிருக்கின்றார்`; `இன்னுங்கூடப்` → `இன்னும்கூடப்`.

Scans **13–15** remain `partial` because handwritten/facsimile bodies cannot safely be established word-for-word. Scan **19** is also `partial` because a small central printed-text region is physically washed out/faint in the controlling scan.

### Mandatory Pass 2B safeguard

After the user identified the scan-11 `ர` / `ற` miss, the workflow was strengthened. Once Pass 2A reaches scan 111, perform an independent **Pass 2B lexical-fidelity re-read** across every printed word in Part 001 before Pass 3.

Pass 2B must specifically look for character-level confusions such as `ர/ற`, `ன/ண`, `ல/ள/ழ`, vowel marks, old/uncommon printed forms, names, quotations and Kural text. Pass 3 remains a separate visual-structure gate and must not be relied on as the lexical safety net.

## Exact next activity

If live `main` has not advanced beyond this frontier:

1. continue **Part 001 Pass 2A — textual verification**;
2. process **overall scans 23–33**;
3. compare each existing Markdown page record directly against the rendered source scan;
4. verify source-visible wording, punctuation, paragraph boundaries, headings, quoted/Kural text, printed-page metadata and separation of printed text from handwriting/stamps/other non-source marks;
5. correct only what the controlling scan visibly supports;
6. do not modernize, normalize, silently repair old/uncommon forms, or import a standard Kural reading from memory/web sources;
7. append results to `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_001.md` without claiming Pass 2B or Pass 3 completion;
8. preserve genuine source limitations as `partial` / `blocked`; never reconstruct from context;
9. audit the changed-file set before advancing beyond scan 33.

Do not restart Pass 1. Do not begin Pass 2B until Pass 2A reaches scan 111. Do not begin Pass 3, the Part audit, or English translation before both Pass 2A and Pass 2B are complete.
