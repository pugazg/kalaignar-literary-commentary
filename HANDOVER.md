# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Project scope

Archive Kalaignar M. Karunanidhi's literary commentary works in source-faithful, page-by-page Markdown.

Planned works:

1. திருக்குறள் — கலைஞர் உரை
2. சங்கத்தமிழ் — Tamil
3. Sangatamil — English translation
4. குறளோவியம் — Tamil
5. Kuraloviyam — English translation

## Reference implementation studied

`pugazg/tolkappiyap-poonga`

The archive follows the same core principles: scan authority, one record per scan page, stable page filenames, explicit status model, metadata, manifests, no silent normalization, and visible review state.

## Current source

`திருக்குறள்_கலைஞர்_உரை_part_001_pages_1-20.pdf`

- 20 scan pages in this attachment.
- The attachment is a partial book segment, not evidence of total book length.
- Visible edition information: first edition December 2007; second edition March 2010.
- Publisher: பூம்புகார் பதிப்பகம், சென்னை.
- Price shown: ரூ. 180/-.

## Completed

Repository foundation:

- root `README.md`
- `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
- `works/thirukkural/README.md`
- `works/thirukkural/metadata/source.md`
- `works/thirukkural/indexes/page-map.md`

Page records exist for **all scans 1–20** in part 001.

Current status:

- scans 1–7 — `verified`
- scan 8 — handwritten facsimile — `partial`; high-resolution review complete, uncertain body deliberately not guessed
- scans 9–12 — `பேராசிரியரின் அணிந்துரை` — `verified`
- scans 13–19 — மதிப்புரை by பேராசிரியர் மா. நன்னன் — first-pass complete, `needs-review`
- scan 20 — `அ. பா நலம்`, `ஆ. அணி நலம்`, `இ. அடை நலம்` begins — first-pass complete, `needs-review`

Current count:

- `verified`: **11**
- `needs-review`: **8**
- `partial`: **1**

First-pass transcription of scans 13–20 used the rendered source pages directly. Tamil OCR was used only as an assistant for character recognition and was checked against the scan; OCR is not source authority.

## Verification completed

### Scan 7 — `முகவுரை`

Direct character-by-character visual comparison with the source scan is complete. The page is `verified` with `transcription_method: "direct visual comparison with source scan"` and a source-page marker.

Two first-pass transcription errors were corrected because the exact scan visibly supports the correction:

- `முன்னூற்று ஐம்பது நான்கு` → `முன்னூற்று ஐம்பத்து நான்கு`
- `பொருளையொன்னியில்` → `பொருளையன்றி`

No modernization or external-edition substitution was used.

### Scan 8 — handwritten facsimile

A new **300-DPI high-resolution render** was inspected directly.

Confidently recoverable elements:

- handwritten heading: **`முகவுரையின் ஒரு முன்னுரை!`**
- decorative separator below the heading
- Kalaignar's signature at the bottom
- date: **`27/12/2007`**

The continuous handwritten body remains insufficiently legible for a reliable source-faithful transcription. Although individual shapes/words appear partly recognizable, they were not entered when the full word or sentence could not be confidently established. `status: "partial"` is therefore intentionally retained. A clearer facsimile/source would be required before attempting the missing body text.

### Scans 9–12 — `பேராசிரியரின் அணிந்துரை`

All four pages were opened at readable/high resolution and compared character by character against the existing Markdown. Printed poetic line breaks, punctuation, quote marks, word joining and visually emphasized lines were preserved.

Results:

- scan 9 — `verified`; one first-pass character reading was corrected: `செல்வமீனும்` → **`செல்வமினும்`**, because the exact scan clearly supports `செல்வமினும்`.
- scan 9 source-supported forms including `மநுவாதிக்கு`, `உற்றிடுமியற்கைச்`, `‘தொழல்’`, and `வான்றோய் முகில்பொழி தூநீர் அனையதாய்` were retained rather than normalized.
- scans 10–12 — `verified`; no source-supported wording correction was required. Their first-pass transcription was confirmed by direct visual comparison.
- all four files now use `status: "verified"` and `transcription_method: "direct visual comparison with source scan"`.

## Next exact activity

Continue the **visual verification round with scans 13–16** — the first four pages of பேராசிரியர் மா. நன்னன்'s `மதிப்புரை`.

1. scan 13 — verify the opening of `மதிப்புரை` and `1. தேவை`, including the numbered/quoted wording and paragraph boundaries.
2. scan 14 — continue `தேவை`; preserve source wording even where it appears archaic, unusual, or editorially awkward.
3. scan 15 — verify `2. வழிபாடு` completely.
4. scan 16 — verify the opening of `3. பெண்வழிச் சேறல்`, including the numbered list and the source-sensitive sentence around `அக் கருத்துக்காட்பட்ட ...`.
5. Correct only what the exact scan supports; do not use an internet Thirukkural text or another edition as a silent authority.
6. For each completed page, set `status: "verified"`, use `transcription_method: "direct visual comparison with source scan"`, and ensure the source-page marker is present.
7. Update `works/thirukkural/indexes/page-map.md`, `works/thirukkural/README.md`, and this handover.

## Source-sensitive forms still pending verification

Treat these as provisional first-pass readings until their own page is visually verified:

- scan 13: `அய்ந்து`, `ஈகையறம்`, `ஒழுகலாறு`
- scan 14: `மன்பதையைச்`
- scan 16: the printed form around `அக் கருத்துக்காட்பட்ட ...` requires careful direct confirmation
- scan 18: `முன்னவை யிரண்டையும்விட`, `இயற்கையின் அமைதி`
- scan 19: the quotation rendered in first pass as `அடுத்தூர்வது அஃதொப்பதில்` must be verified directly from the scan
- scan 20: preserve the Kural wording exactly as printed, including `அசையியற்கு உண்டாண்டோர் ஏஎர்யான் நோக்கப் ...`; do not substitute an internet or standard-edition version

## Important source observations

- Reverse-side bleed-through is visible on several front-matter pages; do not transcribe it as current-page text.
- Handwriting and signatures must be kept separate from printed text.
- Do not import internet/standard Thirukkural wording to 'correct' the source.
- Paragraph line wrapping may be normalized in Markdown, but poetic/Kural line breaks must remain source-faithful.
- Apparent typographical or historical spelling forms must remain unchanged unless a visual reread of this exact scan supports a correction.
