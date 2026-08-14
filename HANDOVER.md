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

The new archive follows the same core principles: scan authority, one record per scan page, stable page filenames, explicit status model, metadata, manifests, no silent normalization, and visible review state.

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
- scan 8 — handwritten facsimile — `partial`; uncertain handwriting deliberately not guessed
- scans 9–12 — பேராசிரியரின் அணிந்துரை — first-pass complete, `needs-review`
- scans 13–19 — மதிப்புரை by பேராசிரியர் மா. நன்னன் — first-pass complete, `needs-review`
- scan 20 — `அ. பா நலம்`, `ஆ. அணி நலம்`, `இ. அடை நலம்` begins — first-pass complete, `needs-review`

First-pass transcription of scans 9–20 used the rendered source pages directly. Tamil OCR was used only as an assistant for character recognition and was checked against the scan; OCR is not source authority.

## Verification completed in latest activity

### Scan 7 — `முகவுரை`

Direct character-by-character visual comparison with the source scan is complete. The page is now `verified` with `transcription_method: "direct visual comparison with source scan"` and a source-page marker.

Two first-pass transcription errors were corrected because the exact scan visibly supports the correction:

- `முன்னூற்று ஐம்பது நான்கு` → `முன்னூற்று ஐம்பத்து நான்கு`
- `பொருளையொன்னியில்` → `பொருளையன்றி`

No modernization or external-edition substitution was used.

## Next exact activity

Continue the **visual verification round** with scan 8.

1. scan 8 — make a high-resolution attempt on the handwritten facsimile.
2. Add only text that can be confidently read from the scan itself.
3. Keep `status: "partial"` if any handwriting remains uncertain; do not infer missing words from context.
4. Preserve the visible signature and date `27/12/2007` separately from the transcription.
5. After scan 8 review, move to scans 9–12 and verify the full poetic `பேராசிரியரின் அணிந்துரை`, especially line breaks, sandhi/spelling and punctuation.
6. After each verified page, update front matter to `status: "verified"` and `transcription_method: "direct visual comparison with source scan"`.
7. Keep `works/thirukkural/indexes/page-map.md`, `works/thirukkural/README.md`, and this handover synchronized with verified counts.

## Source-sensitive forms to recheck, not silently normalize

Several printed forms in this edition may look unusual. Treat them as source forms until the verification pass proves otherwise. Examples encountered in the first pass include:

- scan 9: `மநுவாதிக்கு`, `செல்வமீனும்`, `உற்றிடுமியற்கைச்`, `தொழல்`, `வான்றோய் முகில்பொழி தூநீர் அனையதாய்`
- scan 13: `அய்ந்து`, `ஈகையறம்`, `ஒழுகலாறு`
- scan 14: `மன்பதையைச்`
- scan 16: the printed form around `அக் கருத்துக்காட்பட்ட ...` requires careful final visual confirmation
- scan 18: `முன்னவை யிரண்டையும்விட`, `இயற்கையின் அமைதி`
- scan 19: the quotation rendered in first pass as `அடுத்தூர்வது அஃதொப்பதில்` must be verified directly from the scan
- scan 20: preserve the Kural wording exactly as printed, including `அசையியற்கு உண்டாண்டோர் ஏஎர்யான் நோக்கப் ...`; do not substitute an internet or standard-edition version

## Important source observations

- Reverse-side bleed-through is visible on several front-matter pages; do not transcribe it as current-page text.
- Handwriting and signatures must be kept separate from printed text.
- Do not import internet/standard Thirukkural wording to 'correct' the source.
- Paragraph line wrapping may be normalized in Markdown, but poetic/Kural line breaks must remain source-faithful.
- Apparent typographical or historical spelling forms must remain unchanged unless a visual reread of this exact scan supports a correction.
