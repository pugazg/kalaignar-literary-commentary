# HANDOVER — Kalaignar Literary Commentary Archive

Last synchronized with live `main`: **2026-08-19**.

## Repository

`pugazg/kalaignar-literary-commentary`

Current active work:

`works/sangatamil/`

Completed benchmark retained:

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

Then inspect current GitHub `main` and the actual source scans required for the active batch. Repository state and source evidence are authoritative over conversational summaries.

# Repository-state precedence

For active Sangath Tamil work:

1. controlling source scan;
2. physical page records under `works/sangatamil/pages/`;
3. completed direct-verification / audit artefacts;
4. `metadata/source.md` and page/section/citation indexes;
5. `works/sangatamil/README.md`;
6. this handover and root README;
7. older conversational/historical snapshots.

# Permanent source / fidelity rule

> **The scan is the authority. Markdown is a faithful preservation layer, not a rewritten edition.**

Never silently:

- modernize or normalize Kalaignar's Tamil;
- correct spelling, sandhi, punctuation or grammar from another edition;
- replace a printed Sangam quotation from memory, the web or a critical edition;
- alter printed anthology names, poem numbers or poet attributions from external knowledge;
- reconstruct unclear handwriting or cropped text from context;
- identify an unlabelled illustrated person from appearance alone;
- invent printed pagination;
- infer absent source content from arithmetic.

`verified` requires direct source comparison for both:

1. **textual fidelity** — characters, wording, punctuation, line content and order;
2. **meaningful visual text fidelity** — verse/stanza/paragraph structure, indentation/alignment, heading hierarchy, separators, emphasis and text/image relationships.

OCR/search may assist location but is never authoritative.

# Active work — சங்கத் தமிழ்

## Source identity

- work: **சங்கத் தமிழ்**
- author: **கலைஞர் மு. கருணாநிதி**
- source filename: `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`
- imported-byte SHA-256: recorded in `works/sangatamil/metadata/source.md`
- source PDF is a working/control source and is not committed unless explicitly requested.

## Verified source boundary

The actual mounted PDF has been independently confirmed as **497 scans**:

- `pdfinfo` reports **497 pages**;
- scans **493–497** render successfully from the same PDF;
- scan **497 is the back cover**.

The earlier 150-page figure was a preview-service limit and is retired.

Canonical source range: **1–497**. Do not create scan 498+ records. Printed pagination must still be read from the scan and never inferred from scan arithmetic.

## Publication facts secured from source

- publisher: `ராக்போர்ட் பப்ளிகேஷன்ஸ் (பி) லிட். - சென்னை - 600 083`;
- edition: `ஒன்று`;
- copies: `3,000`;
- date: `ஆகஸ்ட் 1987`;
- price: `ரூ. 125/-`;
- physical size: `14 x 21½ செ.மீ.`.

Scan 7 remains `partial`; scan 8 handwritten `முன்னுரை` facsimile remains `partial`.

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

Physical Markdown records currently exist through **scan 24**.

# Completed work

## Front-matter printed-text gate — COMPLETE

Scans **9–14 / printed IV–IX** are directly transcribed and verified for textual + visual fidelity:

- scan 9 — `ஈ. இராமலிங்கனர் மடல்!`;
- scans 10–13 — `அணிந்துரை`;
- scan 14 — `பதிப்புரை`.

Do not re-transcribe these pages unless a source-supported correction is found.

## First body section — COMPLETE

`மலர்மாரி பொழிகின்றேன்!` — scans **17–19**:

- scan 17 — text `verified`, visual fidelity `verified`;
- scan 18 — full-page illustration `verified`;
- scan 19 — text `verified`, visual fidelity `verified`.

The Sangam quotation begins on scan 17, is physically interrupted by scan 18's illustration, and resumes on scan 19. This relationship is intentionally preserved in the physical page records.

Scan 19 prints:

- `பத்துப்பாட்டு (குறிஞ்சிப்பாட்டு)`;
- `61 முதல் 95 முடிய`;
- `பாடியவர் : கபிலர்`.

This is recorded as verified provenance in `works/sangatamil/indexes/source-citation-register.md`.

# Active next section

`யாதும் ஊரே; யாவரும் கேளிர்!`

Verified physical boundary:

- scans **20–24**;
- visible start: scan **20 / printed page 5**;
- scan **22** — full-page illustration already represented as `verified`;
- scan **24** prints `புறநானூறு - பாடல் : 192 / பாடியவர் : கணியன் பூங்குன்றனார்`;
- text pages 20, 21, 23, 24 remain the active transcription/verification work.

# Exact next activity

Complete `யாதும் ஊரே; யாவரும் கேளிர்!` — scans **20–24**.

For scans 20, 21, 23 and 24:

- transcribe the full source text directly from the PDF render;
- preserve verse lineation, prose/quotation blocks, decorative heading and page furniture;
- preserve the scan-22 illustration as a separate physical interruption in section continuity;
- on scan 24, preserve the printed `புறநானூறு` poem number and poet attribution exactly as printed;
- compare both textual and meaningful visual fidelity directly with the scan;
- only then promote each text page to `verified`.

After all five physical scans pass, update:

- `sections/002-yaathum-oore-yaavarum-kelir/README.md`;
- `indexes/page-map.md`;
- `indexes/section-register.md`;
- `indexes/source-citation-register.md`;
- work/root README and this handover.

Then identify the next decorative heading from scan 25 onward and continue progressively through the complete **497-scan** source.

# Completed Thirukkural baseline — DO NOT RESTART

`works/thirukkural/` remains complete:

- Tamil Parts **001–015** archival-ready through scan **323**;
- commentary complete through printed page **270 / Kural 1330**;
- English project translation Parts **001–015** released;
- semantic provenance complete for **3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள்**;
- `works/thirukkural/structure/STRUCTURE_AUDIT.md` records final PASS.

Do not restart old Thirukkural batches while Sangath Tamil is active unless the user supplies a new source or explicit correction task.
