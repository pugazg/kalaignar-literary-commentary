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

Part 001 Pass 1 is complete continuously through **overall scan 10**:

- scans **1–3** — cover / title-publisher / edition-imprint records;
- scans **4–8 / printed iii–vii** — `முகப்புரை`;
- scans **9–10 / printed viii–ix** — `மதிப்புரை` opening/continuation;
- exactly **10 page-aligned records** exist under `works/kuraloviyam/pages/` for scans 1–10;
- all remain `needs-review` / `visual_fidelity: needs-review` as required for Pass 1.

The page-batch base→head audit was:

`9da4d07f34d4d0b8f89735827725a0d72056d692` → `a88a032baad50a7fff30ffdf0a47a98a1c8cf6a9`

and confirmed 10 sequential page commits before documentation synchronization.

## Exact next activity

If live `main` has not advanced beyond this frontier:

1. continue **Part 001 Pass 1**;
2. process **overall scans 11–20**;
3. create exactly one Markdown record per physical scan under `works/kuraloviyam/pages/`;
4. continue the `மதிப்புரை` from the scan-10 boundary and preserve all physical-page continuity;
5. transcribe only source-supported visible text;
6. preserve roman/Arabic printed pagination only when visible;
7. distinguish printed prose from signatures, handwriting, stamps, photographs and illustrations;
8. use overall `scan_page`, `part: 1`, and local `part_page`;
9. normally leave new records `needs-review` / `visual_fidelity: needs-review`;
10. do not replace printed Kural or quoted wording from memory/web sources;
11. audit the changed-file set, then record the next frontier.

Do not reopen scans 1–10 merely for stylistic harmonization during Pass 1. Do not jump to textual verification, visual verification, part audit or English translation before Pass 1 capture for the relevant source unit is complete.
