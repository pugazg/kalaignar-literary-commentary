# திருக்குறள் — Part 001 archival audit

Audit date: **2026-08-14**

Source: `திருக்குறள்_கலைஞர்_உரை_part_001_pages_1-20.pdf`

## Release decision

**ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**

Part 001 is structurally complete and source-reviewed. All printed / blank pages are verified. Scan 8 is not missing work: it has been high-resolution reviewed and is intentionally retained as `partial` because the continuous handwriting cannot be transcribed reliably from the available scan.

## Audit scope

This pass checked:

1. scan continuity and one-record-per-scan coverage;
2. filename / `scan_page` continuity;
3. printed-page numbering;
4. front-matter and source metadata;
5. status and `transcription_method` consistency;
6. source-page markers;
7. printed text vs handwriting / bleed-through separation;
8. known unresolved items.

## 1. Scan coverage — PASS

Repository tree contains exactly **20 page records** for this source part:

`0001-...md` through `0020-...md`, with no missing scan number and no duplicate page record.

The manifest also records **20 / 20** scan pages represented.

## 2. Scan and printed-page continuity — PASS

- scans 1–6: no printed page number recorded;
- scan 7: `vi`;
- scan 8: `vii`;
- scans 9–20: continuous `viii` through `xix`.

The `scan_page` values and source-page markers follow scan order 1–20.

## 3. Source identity and publication metadata — PASS

The repository metadata matches the supplied scan for the information visible in Part 001:

- work: **திருக்குறள் — கலைஞர் உரை**;
- author / commentator: **கலைஞர் மு. கருணாநிதி**;
- publisher: **பூம்புகார் பதிப்பகம்**;
- address: **127 (ப. எண். 63), பிரகாசம் சாலை (பிராட்வே), சென்னை - 600 108**;
- telephone: **25267543**;
- price: **ரூ. 180/-**;
- வெளியீட்டு எண்: **700**;
- முதற் பதிப்பு: **டிசம்பர், 2007**;
- இரண்டாவது பதிப்பு: **மார்ச் 2010**;
- உரிமை: **உரையாசிரியருக்கு**;
- printer: **ஈகிள் பிரஸ், சென்னை - 600 013**;
- printed code: **P. C. No. : 98152J11**.

The attachment remains correctly described as a **20-page partial source segment**, not as evidence of the full book's total scan count.

## 4. Contents / section-label audit — PASS WITH SOURCE DISTINCTION PRESERVED

The printed contents page lists page `vii` as **`முகவுரையுடன் ஒரு முன்னுரை`**.

The handwritten facsimile on scan 8 itself has the heading **`முகவுரையின் ஒரு முன்னுரை!`**.

These are two different source-supported forms appearing in two different places. They are intentionally preserved as printed / written rather than normalized into one form.

Other visible front-matter sequence in this part is consistent:

- `முகவுரை` — vi
- `பேராசிரியரின் அணிந்துரை` — viii
- `மதிப்புரை` — xii

## 5. Status consistency — PASS

Final status count:

- `verified`: **19**
- `needs-review`: **0**
- `partial`: **1** — scan 8
- uncreated records: **0**

All verified page records use:

`transcription_method: "direct visual comparison with source scan"`

Scan 8 correctly uses a separate high-resolution visual-inspection method and remains `partial`.

## 6. Source-page markers — PASS

Every page record in Part 001 has an explicit bottom marker identifying its scan page and printed page where applicable.

Verified pages use the repository-standard form:

`<!-- மூல ஸ்கேன் பக்கம்: N; அச்சுப் பக்கம்: ... -->`

Scan 8 also carries a source-page marker even though its status is `partial`.

## 7. Non-text / bleed-through handling — PASS

Reverse-side bleed-through visible on several front-matter scans is not treated as current-page body text.

Scan 8 keeps handwriting, signature, date and bleed-through conceptually separate. The signature and date are recorded as visual elements rather than silently merged into running prose.

No audit evidence was found that reverse-side bleed-through has been transcribed as current-page text in the Part 001 page records.

## 8. Known transcription corrections already resolved

The verification cycle corrected only readings supported by this exact scan. Important examples retained in the audit trail include:

- scan 7: `முன்னூற்று ஐம்பத்து நான்கு`; `பொருளையன்றி`;
- scan 9: `செல்வமினும்`;
- scan 19: quotation boundary includes `கூடும்` inside the quotation;
- scan 20: source-printed Kural wording was preserved rather than replaced by another edition.

Unusual source forms confirmed during visual verification remain unchanged.

## 9. Known unresolved item — REVIEWED, NOT FAILED

### Scan 8 — handwritten facsimile

Status: `partial`

High-resolution review established with confidence:

- handwritten heading: **`முகவுரையின் ஒரு முன்னுரை!`**;
- Kalaignar's signature;
- date: **27/12/2007**.

The continuous handwritten body is not sufficiently legible for a source-faithful transcription from the available scan. It must not be reconstructed from context, memory, OCR guesswork, or another source.

This is a **documented source limitation**, not an unprocessed page.

## Final Part 001 state

Part 001 satisfies the repository's source-first archival requirements for the supplied material:

- complete scan coverage;
- no duplicate / missing page record;
- verified printed and blank pages;
- explicit uncertainty for the handwritten facsimile;
- synchronized scan / printed-page identity;
- source metadata preserved;
- source-page markers present;
- no silent modernization or external-edition substitution.

**Part 001 may therefore be treated as archival-ready, with scan 8 retained as a known reviewed partial.**

## Next activity

Continue only when one of the following is available:

1. the **next Thirukkural source PDF batch**, in which case continue the page sequence without renumbering or duplicating Part 001; or
2. a **clearer scan / facsimile of scan 8**, in which case reopen only that page and add only readings directly supported by the clearer source.
