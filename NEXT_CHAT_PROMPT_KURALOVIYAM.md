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

Part 001 source intake is complete:

- local page count: **111/111**;
- scans 1–3: cover/title/publication matter;
- scans 4–17: front matter;
- scan 18: main body begins at printed page 1, heading `பேராசிரியர்`;
- scan 111: printed page 94.

### Part 001 Pass 1 — COMPLETE

Exactly **111 page-aligned records** exist continuously for overall scans **1–111**.

Final Pass-1 ranges:

- scans **99–101 / printed 82–84** — `ஊர்க்காவலன்` / tiger-danger vignette; delayed action leaves villagers to kill the tiger themselves, concluding with `நெடுநீர் மறவி மடிதுயில்...`;
- scans **102–103 / printed 85–86** — lovers / waiting / planned `ஊடல்`, concluding with `புலப்பல் எனச்சென்றேன்...`;
- scans **104–105 / printed 87–88** — வில்லவன் / unreliable-horse vignette, concluding with `அமரகத்து ஆற்றறுக்கும்...`;
- scans **106–107 / printed 89–90** — கலிங்கன்–கதிரவன் anger-control vignette, concluding with `செல்லிடத்துக் காப்பான்...`;
- scan **108 / printed 91** — lover-away / wall-tally vignette, concluding with `வாளற்றுப் புற்கென்ற...`;
- scans **109–111 / printed 92–94** — learned-speaker / assembly vignette, concluding with `விரைந்து தொழில்கேட்கும்...` and `இணரூழ்த்தும் நாறா...`.

Pass-1 printed-text records remain `needs-review` / `visual_fidelity: needs-review`. Scans **13–15** remain source-limited `partial`; do not reconstruct their handwriting.

Final Pass-1 page-batch audit:

`a7898940a9935cc86b659c4dac9fe5e8c09401b4` → `bc45693fedf1619bc839fc516f6c19f0fa408be5`

The comparison confirmed **11 sequential page commits**, exactly the expected eleven page records for scans **101–111**, and no unrelated file changes within the page batch.

## Exact next activity

If live `main` has not advanced beyond this frontier:

1. begin **Part 001 Pass 2 — textual verification**;
2. process **overall scans 1–11**;
3. compare each existing Markdown page record directly against the rendered source scan;
4. verify source-visible wording, punctuation, paragraph boundaries, headings, quoted/Kural text, printed-page metadata and separation of printed text from handwriting/stamps/other non-source marks;
5. correct only what the controlling scan visibly supports;
6. do not modernize, normalize, silently repair old/uncommon forms, or import a standard Kural reading from memory/web sources;
7. record the textual-verification result without claiming Pass 3 visual-text verification;
8. preserve genuine source limitations as `partial` / `blocked` where applicable;
9. audit the changed-file set before advancing to scans 11–21.

Do not restart Pass 1. Do not begin Pass 3, the Part audit, or English translation before Part 001 Pass 2 is complete.
