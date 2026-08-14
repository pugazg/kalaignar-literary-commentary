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
- Edition information visible: first edition December 2007; second edition March 2010.

## Completed

Repository foundation:

- root `README.md`
- `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
- `works/thirukkural/README.md`
- `works/thirukkural/metadata/source.md`
- `works/thirukkural/indexes/page-map.md`

Page records completed:

- scan 1 — cover — `verified`
- scan 2 — title page — `verified`
- scan 3 — blank — `verified`
- scan 4 — publication details — `verified`
- scan 5 — edition details — `verified`
- scan 6 — contents — `verified`
- scan 7 — முகவுரை — first-pass transcription, `needs-review`
- scan 8 — handwritten facsimile — `partial`; uncertain handwriting deliberately not guessed

## Next exact activity

Create and transcribe scan pages **9–20** in order:

- 9–12: `பேராசிரியரின் அணிந்துரை`
- 13–19: `மதிப்புரை` by பேராசிரியர் மா. நன்னன்
- 20: begins `அ. பா நலம்`, then `ஆ. அணி நலம்`, `இ. அடை நலம்`

After pages 9–20 are created:

1. update `indexes/page-map.md` statuses and filenames;
2. update `works/thirukkural/README.md` progress;
3. run visual verification of scan page 7;
4. make a high-resolution attempt on page 8 handwriting without guessing unclear text;
5. preserve printed wording exactly even where another Thirukkural edition differs.

## Important source observations

- Reverse-side bleed-through is visible on several front-matter pages; do not transcribe it as current-page text.
- Handwriting and signatures must be kept separate from printed text.
- Do not import internet/standard Thirukkural wording to 'correct' the source.
