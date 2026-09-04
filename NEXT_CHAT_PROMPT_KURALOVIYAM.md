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

### Part 001 Pass 2A — textual verification through scan 110 COMPLETE

The durable verification record is:

`works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_001.md`

Pass 2A has directly compared overall scans **1–110** against the rendered source.

Recent Batch-10 source-supported corrections:

- scan 100 — `நாட்டாளைக் கடத்தலாமா?` → `நாட்களைக் கடத்தலாமா?`; `இன்று கேட்டுகிறேன்` → `இன்று கேட்கிறேன்`;
- scan 101 — `உன் ஆட்களையெடுத்து` → `உன் ஆட்களைவைத்து`; source citation punctuation restored;
- scan 103 — `இல்லம் புகுந்து கொண்டேன்` → `இல்லில் புகுந்து கொண்டேன்`; `ஏமாற்றச் செய்திட` → source-visible `ஏமாறச் செய்திட`; source citation punctuation restored;
- scan 105 — `அதுதான் இது:` → source-visible `அதுதான் இது;`; source citation punctuation restored;
- scan 107 — restored source punctuation `அடக்கினால் என்ன- அடக்காவிட்டால் என்ன?` and citation punctuation;
- scan 108 — `இந்த எழிலாகச் சித்திரப் பெண்` → `இந்த எழுதாத சித்திரப் பெண்`; `நெஞ்சு எடுகளைத்` → `நெஞ்சு ஏடுகளைத்`; `சித்திரக் கோடுகளைத் தொட்டு தொட்டு` → `சித்திரக்கோடுகளைத் தொட்டுத் தொட்டு`; source citation punctuation restored;
- scan 109 — `எழுத்து மொழிகள் கற்றவர்` → source-visible `ஏழெட்டு மொழிகள் கற்றவர்`;
- scan 110 — `அவர் படித்து முடிக்காத நூலே உலகத்திலே இல்லை` → source-visible `அவர் படித்து முடிக்காத நூல்களே உலகத்திலே இல்லை`.

Scans **102, 104 and 106** required no page-record textual correction after direct source comparison.

Earlier source limitations remain:

- scans **13–15** — handwritten/facsimile bodies remain `partial`; do not reconstruct them;
- scan **19** — a small physically washed-out/faint printed region remains `partial`; do not infer lost words from context.

### Mandatory Pass 2B safeguard

After the user identified the scan-11 `ர` / `ற` miss, the workflow was strengthened. Once Pass 2A reaches scan 111, perform an independent **Pass 2B lexical-fidelity re-read** across every printed word in Part 001 before Pass 3.

Pass 2B must specifically look for character-level confusions such as `ர/ற`, `ன/ண`, `ல/ள/ழ`, vowel marks, old/uncommon printed forms, names, quotations and Kural text. Pass 3 remains a separate visual-structure gate and must not be relied on as the lexical safety net.

## Exact next activity

If live `main` has not advanced beyond this frontier:

1. continue **Part 001 Pass 2A — textual verification**;
2. process **overall scan 111 only**;
3. compare the existing Markdown page record directly against rendered source scan 111;
4. verify source-visible wording, punctuation, paragraph boundaries, headings, quoted/Kural text, printed-page metadata and separation of printed text from handwriting/stamps/other non-source marks;
5. correct only what the controlling scan visibly supports;
6. do not modernize, normalize, silently repair old/uncommon forms, or import a standard Kural reading from memory/web sources;
7. append the scan-111 result to `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_001.md` and mark **Pass 2A complete through scan 111**, without claiming Pass 2B or Pass 3 completion;
8. preserve genuine source limitations as `partial` / `blocked`; never reconstruct from context;
9. audit the changed-file set and stop after closing Pass 2A.

Do not restart Pass 1. Do not begin Pass 2B in the same activity as scan 111. After Pass 2A is fully closed, the next separate activity is Part 001 **Pass 2B independent lexical-fidelity re-read**, beginning from scans 1–11. Do not begin Pass 3, the Part audit, or English translation before Pass 2B is complete.
