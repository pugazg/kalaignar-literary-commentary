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

## Reference implementation

`pugazg/tolkappiyap-poonga`

The archive follows the same core principles: scan authority, one record per scan page, stable filenames, explicit review status, metadata/manifests, no silent normalization, and visible uncertainty.

## Current source

`திருக்குறள்_கலைஞர்_உரை_part_001_pages_1-20.pdf`

- 20 scan pages
- partial book segment, not evidence of total book length
- visible edition information: first edition December 2007; second edition March 2010
- publisher: பூம்புகார் பதிப்பகம், சென்னை
- price shown: ரூ. 180/-

## Current Part 001 status

Page records exist for **all scans 1–20**.

- `verified`: **19**
- `needs-review`: **0**
- `partial`: **1** — scan 8 handwritten facsimile
- uncreated page records: **0**

All printed/blank pages in this source part have completed direct visual verification. Scan 8 has also been reviewed at high resolution, but its continuous handwritten body is not sufficiently legible for a reliable source-faithful transcription, so it remains intentionally `partial`.

## Completed verification history

### Scan 7 — `முகவுரை`

Direct character-by-character comparison complete. Corrections supported by the exact scan:

- `முன்னூற்று ஐம்பது நான்கு` → `முன்னூற்று ஐம்பத்து நான்கு`
- `பொருளையொன்னியில்` → `பொருளையன்றி`

### Scan 8 — handwritten facsimile

300-DPI visual review complete.

Confidently recoverable:

- heading: `முகவுரையின் ஒரு முன்னுரை!`
- Kalaignar's signature
- date: `27/12/2007`

The handwritten body remains unresolved and must not be reconstructed from context.

### Scans 9–12 — `பேராசிரியரின் அணிந்துரை`

All four pages verified. Poetic line breaks, punctuation, sandhi/word joining and source spelling preserved.

Scan 9 correction:

- `செல்வமீனும்` → `செல்வமினும்`

Source-supported forms retained after rereading include `மநுவாதிக்கு`, `உற்றிடுமியற்கைச்`, `‘தொழல்’`, and `வான்றோய் முகில்பொழி தூநீர் அனையதாய்`.

### Scans 13–16 — `மதிப்புரை`

All four pages verified. First-pass wording matched the scan; no textual correction was required.

Explicitly confirmed source forms include:

- scan 13: `அய்ந்து`, `ஈகையறம்`, `ஒழுகலாறு`
- scan 14: `மன்பதையைச்`
- scan 15: `அவைகளை யெல்லாம்`, `உறுதிப்படுத்தப் படாமையால்`
- scan 16: `அக் கருத்துக்காட்பட்ட`

### Scans 17–20 — final printed verification batch

All four pages verified.

- scan 17 — `பெண்வழிச் சேறல்` continuation; first-pass wording confirmed.
- scan 18 — `ஊழ்`; first-pass wording confirmed. `முன்னவை யிரண்டையும்விட` and `இயற்கையின் அமைதி` were directly verified and retained.
- scan 19 — one first-pass quotation-boundary error was corrected. The scan reads:
  - `“ஒருவர் தமக்கு உரிமையல்லாதவற்றை முயன்று பாதுகாத்தாலும் தங்காமல் போய் விடவும் கூடும்”`
  - the first pass had closed the quote before `கூடும்`.
  - `அடுத்தூர்வது அஃதொப்பதில்` was visually confirmed and retained.
- scan 20 — printed Kural wording and commentary were verified directly. Preserve the exact source form, including:
  - `அசையியற்கு உண்டாண்டோர் ஏஎர்யான் நோக்கப்`
  - `பசையினள் பைய நகும்.`

Do not substitute internet/standard-edition Kural text.

## Files to keep synchronized

- `works/thirukkural/README.md`
- `works/thirukkural/indexes/page-map.md`
- `works/thirukkural/metadata/source.md`
- this `HANDOVER.md`

Each verified page uses:

- `status: "verified"`
- `transcription_method: "direct visual comparison with source scan"`
- source-page marker at the bottom

## Next exact activity

Run a **Part 001 release/audit pass** before treating the batch as archival-ready.

1. Check scan continuity 1–20 and confirm exactly one Markdown page record per scan.
2. Check printed-page numbering, page types, front-matter metadata and section labels.
3. Check every page status and `transcription_method` for consistency.
4. Check source-page markers are present and correct.
5. Confirm no reverse-side bleed-through was accidentally transcribed as current-page text.
6. Record scan 8 as **reviewed but partial**, not as missing or failed work.
7. Create a concise audit/release report for Part 001.
8. After the audit, wait for the next Thirukkural source PDF batch or a clearer scan 8 facsimile.

## Source authority rule

The attached scan remains the controlling source for this edition. Do not silently modernize, normalize, correct, reconstruct or improve the Tamil. Apparent typographical/historical forms stay as printed unless a reread of this exact scan supports a correction.
