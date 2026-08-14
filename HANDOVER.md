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

## Part 001 audit / release status

Audit completed on **2026-08-14**.

Report:

- `works/thirukkural/AUDIT_PART_001.md`

Decision:

**ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**

The audit confirmed:

- exactly **20** page records for scans 1–20;
- no missing or duplicate scan record;
- `scan_page` continuity 1–20;
- printed-page sequence `vi`–`xix` for scans 7–20;
- source identity and publication metadata consistent with the supplied scan;
- source-page markers present;
- all verified records use `transcription_method: "direct visual comparison with source scan"`;
- reverse-side bleed-through is not treated as current-page body text;
- scan 8 is reviewed-but-partial, not missing work.

One source distinction was explicitly retained rather than normalized:

- contents page label: `முகவுரையுடன் ஒரு முன்னுரை`;
- handwritten scan 8 heading: `முகவுரையின் ஒரு முன்னுரை!`.

Both are source-supported forms occurring in different places and must remain distinct.

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
- `works/thirukkural/AUDIT_PART_001.md`
- this `HANDOVER.md`

Each verified page uses:

- `status: "verified"`
- `transcription_method: "direct visual comparison with source scan"`
- source-page marker at the bottom

## Next exact activity

Part 001 is audited and archival-ready. Do **not** redo or renumber it.

Proceed only when new source material is supplied:

1. If the **next Thirukkural PDF batch** is supplied, inspect the actual scan first, determine how its scan sequence relates to Part 001, then continue without creating duplicate page records.
2. Preserve the existing source-first rules: scan authority, no silent normalization, one page record per scan, explicit uncertainty, and direct visual verification before `verified`.
3. Update `metadata/source.md` only with new source identity / pagination facts actually supported by the new batch.
4. Extend `indexes/page-map.md` for the new batch while preserving the completed Part 001 entries.
5. If instead a clearer scan 8 facsimile is supplied, reopen only `pages/0008-handwritten-note.md`; add only text directly supported by the clearer source and keep uncertainty explicit.

## Source authority rule

The attached scan remains the controlling source for this edition. Do not silently modernize, normalize, correct, reconstruct or improve the Tamil. Apparent typographical/historical forms stay as printed unless a reread of this exact scan supports a correction.