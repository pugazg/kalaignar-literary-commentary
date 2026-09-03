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

The user reports the complete original Kuraloviyam PDF as **666 physical pages**, manually split into **six parts of 111 pages** because the original exceeds the upload limit.

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

Part 001 Pass 1 is complete continuously through **overall scan 100**. Exactly **100 page-aligned records** exist for scans 1–100.

Recent completed batches:

- scans **71–80 / printed 54–63** — beauty/eyes; freedom-fighter/assembly; travelling-family gratitude; oppressive-rule uprising; tearful-eye love-sickness; old-age/gambling analogy;
- scans **81–90 / printed 64–73** — mirror/pallor; victorious king/Valluvar; dream-of-lover; overreaching-prince/uprising; love-sickness/shame/pallor;
- scans **91–92 / printed 74–75** — contrasting public judgments of two commanders, concluding with `கணைகொடிது யாழ்கோடு...`;
- scans **93–94 / printed 76–77** — public-announcement / eye-as-drum vignette, with `மறைபெறல் ஊரார்க்கு...` and `வாராக்கால் துஞ்சா...`;
- scans **95–96 / printed 78–79** — young poet / கயல்விழி prospective-bride vignette, concluding with `கண்ணுடையர் என்பவர் கற்றோர்...`;
- scans **97–98 / printed 80–81** — flowers, tearful eyes, reunion and momentary separation, with `சிறுமை நமக்கொழியச்...` and `முயக்கிடைத் தண்வளி...`;
- scans **99–100 / printed 82–83** — `ஊர்க்காவலன்` / tiger-danger vignette begins and continues beyond scan 100.

Pass-1 printed-text records remain `needs-review` / `visual_fidelity: needs-review`. Scans 13–15 remain source-limited `partial`; do not reconstruct their handwriting.

Latest page-batch audit:

`2847046061f0fd41e8214f2567008fd58449522f` → `e9752f7a0bd70b080cad0882cc8c05e6b5263de2`

The comparison confirmed **10 sequential page commits**, exactly the expected ten page files for scans **91–100**, and no unrelated file changes.

## Exact next activity

If live `main` has not advanced beyond this frontier:

1. continue **Part 001 Pass 1**;
2. process **overall scans 101–110**;
3. create exactly one Markdown record per physical scan under `works/kuraloviyam/pages/`;
4. continue directly from the `ஊர்க்காவலன்` / tiger-danger narrative at printed page 83 into the next source pages;
5. transcribe only source-supported visible text;
6. preserve source-supported illustration/text relationships and printed pagination;
7. distinguish printed prose from signatures, handwriting, stamps, photographs and illustrations;
8. use overall `scan_page`, `part: 1`, and local `part_page`;
9. normally leave new records `needs-review` / `visual_fidelity: needs-review`;
10. do not replace printed Kural or quoted wording from memory/web sources;
11. audit the changed-file set, then record the frontier before the final Part 001 scan 111.

Do not reopen scans 1–100 merely for stylistic harmonization during Pass 1. Do not jump to textual verification, visual verification, part audit or English translation before Part 001 Pass 1 is complete.
