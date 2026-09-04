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

### Part 001 Pass 2A — COMPLETE

The durable verification record is:

`works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_001.md`

Pass 2A has now directly compared **all overall scans 1–111** against the rendered source.

Final Pass-2A work:

- scans **100–110** were completed as Batch 10 with source-supported corrections on scans 100, 101, 103, 105, 107, 108, 109 and 110;
- scan **111 / printed 94** was then directly compared against the rendered source as Batch 11;
- scan 111 prose and both `சொல்வன்மை` Kurals were confirmed;
- scan 111 citation punctuation was corrected from the repository's non-source em dash to the source-visible hyphen form: `அதிகாரம் - 65 - சொல்வன்மை; பாடல்கள் - 648, 650`.

Pass 2A is therefore **111 / 111 COMPLETE**. Do not restart or repeat it.

Earlier source limitations remain:

- scans **13–15** — handwritten/facsimile bodies remain `partial`; do not reconstruct them;
- scan **19** — a small physically washed-out/faint printed region remains `partial`; do not infer lost words from context.

### Mandatory Pass 2B safeguard

After the user identified the scan-11 `ர` / `ற` miss (`உறனுண்டு` → source-visible `உரனுண்டு`), the workflow was strengthened with an independent **Pass 2B lexical-fidelity re-read** before Pass 3.

Pass 2B is not a confirmation of Pass 2A. It must independently re-read the printed source word by word, with particular attention to:

- `ர / ற`;
- `ன / ண`;
- `ல / ள / ழ`;
- vowel signs and pulli/compound-letter distinctions;
- source-visible spacing and joining;
- old/uncommon printed forms;
- names and titles;
- quotations and Kural text;
- punctuation where it affects textual fidelity.

Do not import standard Kural readings, modern spellings, contextual guesses, or web/reference text. The rendered scan remains controlling.

Pass 3 remains a separate visual-structure / visual-text fidelity gate and must not be relied upon as the lexical safety net.

## Exact next activity

If live `main` has not advanced beyond this frontier:

1. begin **Part 001 Pass 2B — independent lexical-fidelity re-read**;
2. process **overall scans 1–11**;
3. re-read every source-visible printed word independently against the rendered scan rather than merely reviewing the Pass-2A change list;
4. compare the independent reading against each existing Markdown page record;
5. correct only differences visibly supported by the controlling scan;
6. pay special attention to character-level confusions (`ர/ற`, `ன/ண`, `ல/ள/ழ`), vowel signs, old/uncommon forms, names, quoted text, Kurals, and source-visible joining/spacing;
7. keep handwriting, stamps, signatures and other non-body marks separate from printed source text;
8. preserve genuine source limitations as `partial` / `blocked`; never reconstruct unclear handwriting or washed-out printing from context;
9. record Pass-2B results durably without claiming Pass 3 completion or assigning final `verified` status;
10. audit the changed-file set before advancing beyond scan 11.

Do not begin Part 002. Do not begin Pass 3, the Part audit, or English translation before Part 001 Pass 2B is complete.