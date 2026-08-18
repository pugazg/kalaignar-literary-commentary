# HANDOVER — Kalaignar Literary Commentary Archive

Last synchronized with live `main`: **2026-08-18**.

## Repository

`pugazg/kalaignar-literary-commentary`

Current active work:

`works/sangatamil/`

Completed baseline retained:

`works/thirukkural/`

# Mandatory startup — active சங்கத் தமிழ் work

Before making any Sangath Tamil repository change, read completely:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`
5. `works/sangatamil/README.md`
6. `works/sangatamil/metadata/source.md`
7. `works/sangatamil/metadata/transcription-policy.md`
8. `works/sangatamil/indexes/page-map.md`
9. `works/sangatamil/indexes/section-register.md`
10. `works/sangatamil/indexes/source-citation-register.md`

Then inspect current GitHub `main` and the actual attached source scans needed for the active batch. Repository state and source evidence are authoritative over conversational summaries.

# Repository-state precedence

For active Sangath Tamil work:

1. controlling source scan;
2. physical page records under `works/sangatamil/pages/`;
3. completed direct-verification / audit artefacts when they exist;
4. `metadata/source.md` and physical/section/citation indexes;
5. `works/sangatamil/README.md`;
6. this handover and root README;
7. older conversational or historical snapshots.

For completed Thirukkural work, its completed audits, translation reports and semantic structure audit remain authoritative.

# Permanent source rule

> **The scan is the authority. Markdown is a faithful preservation layer, not a rewritten edition.**

Never silently:

- modernize or normalize Kalaignar's Tamil;
- correct spelling, sandhi, punctuation or grammar because another edition differs;
- replace a printed Sangam quotation from memory, the web or a critical edition;
- alter printed anthology names, poem numbers or poet attributions from external knowledge;
- reconstruct unclear handwriting from context;
- identify an unlabelled illustrated person from appearance alone;
- invent printed pagination;
- infer absent scan pages from arithmetic.

OCR/search may assist, but `verified` requires direct visual comparison with the controlling scan.

# Active work — சங்கத் தமிழ்

## Source identity

- work: **சங்கத் தமிழ்**
- author: **கலைஞர் மு. கருணாநிதி**
- source filename: `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`
- imported-byte SHA-256 recorded in `works/sangatamil/metadata/source.md`
- source PDF is a working/control source and is not committed to GitHub unless the user explicitly changes that policy.

Publication facts already secured from scan 7 include:

- publisher: `ராக்போர்ட் பப்ளிகேஷன்ஸ் (பி) லிட். - சென்னை - 600 083`;
- edition: `ஒன்று`;
- copies: `3,000`;
- date: `ஆகஸ்ட் 1987`;
- price: `ரூ. 125/-`;
- physical size: `14 x 21½ செ.மீ.`.

Scan 7 remains `partial` because its lower production-detail lines have not yet completed a character-level verification pass.

## Critical source-integrity warning

The current supplied attachment cannot be treated as the complete book.

The conversation file service exposes **150 usable scans**. Scan **150 is still continuing body text**, not end matter. The mounted PDF bytes also showed conflicting/truncated structural information during intake.

Therefore the current canonical source boundary is:

- usable source fragment: **scans 1–150**;
- completeness: **incomplete / truncated fragment**;
- **do not create scan 151+ page records**;
- do not infer later content or missing pagination from another edition;
- when a complete PDF is supplied, inspect it independently and prove scan 150 → 151 continuity before extending the archive.

This is a source-preservation control, not a claim about the complete book's actual total length.

## Methodology adopted

The active work follows both established benchmark projects:

### From Thirukkural

- canonical physical-page archive separated from semantic/navigation layers;
- explicit source/audit gates;
- no silent correction;
- later English work kept separate from Tamil source authority;
- handover/status documents synchronized with live repository state.

### From `pugazg/tolkappiyap-poonga`

- one Markdown record per physical scan page;
- stable zero-padded filenames;
- direct scan verification before `verified`;
- separate records for blank/title/facsimile/illustration pages;
- section READMEs as navigation manifests;
- exact scan/printed-page provenance;
- source-order structured indexes.

### Sangath Tamil addition — printed Sangam provenance

Because this source explicitly prints anthology/work names, poem numbers, poet attributions and `பொருள் விளக்கம்`, maintain a dedicated register:

`works/sangatamil/indexes/source-citation-register.md`

The register preserves the citation **as printed in this edition**. Any future comparison against another Sangam edition belongs in a separate comparison layer and must not silently alter the physical archive.

# Current repository structure — சங்கத் தமிழ்

```text
works/sangatamil/
  README.md
  metadata/
    source.md
    transcription-policy.md
  indexes/
    page-map.md
    section-register.md
    source-citation-register.md
  pages/
    0001-...md through 0024-...md
  sections/
    000-front-matter/
    001-malarmari-pozhiginren/
    002-yaathum-oore-yaavarum-kelir/
```

Work-specific root controls:

- `SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`
- `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`

# Current mapped physical boundary

Physical Markdown records exist through **scan 24**.

## Front matter — scans 1–16

Current status:

- scan 1 cover — `verified`;
- scan 2 title page — `verified`;
- scan 3 later library/ownership sticker — `verified` as non-body annotation;
- scans 4–5 ruled blank leaves — `verified`;
- scan 6 internal title page — `verified`;
- scan 7 publication details — `partial`;
- scan 8 / printed III handwritten `முன்னுரை` facsimile — `partial`;
- scan 9 / printed IV `ஈ. இராமலிங்கனர் மடல்!` — `not-started`;
- scans 10–13 / printed V–VIII `அணிந்துரை` — `not-started`;
- scan 14 / printed IX `பதிப்புரை` — `not-started`;
- scan 15 blank leaf — `verified`;
- scan 16 internal `சங்கத் தமிழ்` title leaf — `verified`.

Do not promote scans 7–14 merely because headings or partial metadata are visible.

## First body section

`மலர்மாரி பொழிகின்றேன்!`

- scans **17–19**;
- scan 17 visibly begins at printed page **2**;
- scan 18 is a full-page illustration and is `verified` as an image record;
- scan 19 visibly carries printed page **4**;
- text pages remain `not-started`.

The missing printed-page 1 mapping is **not inferred**.

## Second body section

`யாதும் ஊரே; யாவரும் கேளிர்!`

- scans **20–24**;
- visible start: scan 20 / printed page **5**;
- scan 22 illustration — `verified` as an image record;
- scan 24 prints the provenance `புறநானூறு - பாடல் : 192 / பாடியவர் : கணியன் பூங்குன்றனார்`;
- continuous body text remains `not-started`.

# Citation-register startup samples

Directly inspected provenance samples currently recorded include:

- scan 24 — `புறநானூறு`, பாடல் 192, `கணியன் பூங்குன்றனார்`;
- scan 46 — `அகநானூறு`, பாடல் 248, `கபிலர்`;
- scan 49 — `குறுந்தொகை`, பாடல் 210, `காக்கைப்பாடினியார் நச்செள்ளையார்`;
- scan 147 — `குறுந்தொகை`, பாடல்கள் 32 and 157, `அள்ளூர் நன்முல்லையார்`.

These entries are **sampled source provenance**, not verified full-page transcriptions. Promote their register status only when the containing physical page has been fully transcribed and verified.

# Exact next activity

Complete the first front-matter text gate:

**scans 9–14 / printed pages IV–IX**.

In source order:

1. scan 9 — `ஈ. இராமலிங்கனர் மடல்!`;
2. scans 10–13 — `அணிந்துரை`;
3. scan 14 — `பதிப்புரை`.

For each page:

- transcribe the full printed text directly from the scan;
- preserve paragraph boundaries, punctuation and source-specific wording;
- do not use OCR as authority;
- compare the completed Markdown directly with the scan;
- only then change `status` to `verified` and add the source-page marker.

After scans 9–14 pass, process the first body section:

**`மலர்மாரி பொழிகின்றேன்!` — scans 17–19**.

Do not jump to bulk body transcription before the front-matter gate is clean.

# Completed Thirukkural baseline — DO NOT RESTART

`works/thirukkural/` remains complete:

- Tamil Parts **001–015** archival-ready through scan **323**;
- commentary complete through printed page **270 / Kural 1330**;
- English project translation Parts **001–015** released;
- semantic provenance complete for **3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள்**;
- `works/thirukkural/structure/STRUCTURE_AUDIT.md` records final PASS.

Do not restart old Thirukkural Part 014/015 or chapter-mapping batches while Sangath Tamil is active.

# Future English Sangatamil rule

The repository anticipates a separately published English *Sangatamil*. If supplied:

- archive it as its own source-controlled edition;
- preserve its own pagination and wording;
- align it with Tamil only in a separate layer;
- do not use it to rewrite Tamil page records.

If the user explicitly asks for a project-created English translation instead, create it only after the corresponding Tamil source unit is audited and label it `translation_type: "project_translation"`.
