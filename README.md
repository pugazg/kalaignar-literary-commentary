# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

Last synchronized with live `main`: **2026-08-18**.

## திட்டமிட்ட / உள்ள நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–015 **ARCHIVAL-READY through scan 323**; commentary through printed page 270 / Kural 1330 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–015 **RELEASED through the end of the supplied volume** |
| Thirukkural semantic structure | பால் → இயல் → அதிகாரம் | **COMPLETE — 3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள் mapped** |
| சங்கத் தமிழ் | தமிழ் | **ACTIVE — source intake started under `works/sangatamil/`; current supplied fragment usable through scan 150; physical records mapped through scan 24** |
| Sangatamil | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த source-controlled edition ஆக archive செய்யப்படும் |
| குறளோவியம் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Kuraloviyam | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |

## மூலக் கொள்கை

> **ஸ்கேன் தான் அதிகாரப்பூர்வ மூல ஆதாரம். Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது.

Source PDFs are working/control sources and are not committed unless the user explicitly changes that policy.

## English layers — published source vs project translation

1. **Published / official English source** — தனியாக வெளியிடப்பட்ட source கிடைத்தால், அதன் சொந்த pagination / wording / metadata-உடன் source-controlled edition ஆக archive செய்யப்படும்.
2. **Project-created English translation** — audited Tamil source-இலிருந்து உருவாக்கப்படும் மொழிபெயர்ப்பு; `translation_type: "project_translation"` என்று வெளிப்படையாகக் குறிக்கப்படும்.

A published English *Sangatamil* source, if supplied, must remain independent of the Tamil physical-page archive. It must not be used to silently rewrite the Tamil edition.

Permanent source/translation cadence for a new source unit:

**Tamil source intake → Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English source intake or project-translation gate as applicable.**

# Canonical current state — திருக்குறள்

The supplied **திருக்குறள் — கலைஞர் உரை** volume is complete across all currently defined layers.

### Tamil archival layer

Parts **001–015 are audited / archival-ready continuously** through:

- overall scans **1–323**;
- commentary through printed page **270 / Kural 1330**;
- scans **304–321**: `குறள் முதற்குறிப்பு அகரவரிசை`, printed pages 271–288;
- scan **322**: blank leaf;
- scan **323**: back cover.

Part 001 scan 8 remains the documented source-limited handwritten facsimile exception. Tamil audits exist continuously through `works/thirukkural/AUDIT_PART_015.md`.

### English project translation

English Parts **001–015 are released continuously through the end of the supplied volume**.

Current authority:

- [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md)
- [`works/thirukkural/translations/en/README.md`](works/thirukkural/translations/en/README.md)

### Semantic navigation/provenance

`works/thirukkural/structure/` is complete:

- **3 / 3 பால்**;
- **13 / 13 இயல்**;
- **133 / 133 அதிகாரம்**;
- **1,330 / 1,330 குறள்**.

Final audit:

- [`works/thirukkural/structure/STRUCTURE_AUDIT.md`](works/thirukkural/structure/STRUCTURE_AUDIT.md) — **PASS — SEMANTIC PROVENANCE MAPPING COMPLETE**.

Do not restart completed Thirukkural transcription, translation or semantic batches unless a new source or explicit correction task requires it.

# Canonical current state — சங்கத் தமிழ்

Active work path:

[`works/sangatamil/`](works/sangatamil/)

Current source filename:

`TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

## Source-integrity boundary

The current attachment is documented as an **incomplete/truncated source fragment**. The conversation source service exposes **150 usable scans**, and scan 150 is still continuing body text rather than end matter.

Therefore the current canonical boundary is:

- usable supplied scans: **1–150**;
- source completeness: **incomplete**;
- do **not** create scan 151+ records;
- do not infer missing pages from printed-page arithmetic or another edition;
- when a complete source is supplied, verify continuity at the existing boundary before extending the archive.

See [`works/sangatamil/metadata/source.md`](works/sangatamil/metadata/source.md).

## Methodology

The Sangath Tamil archive combines the established methods from:

- the Thirukkural source/audit/provenance workflow in this repository;
- the page-by-page / section README / direct visual verification discipline of `pugazg/tolkappiyap-poonga`.

Current layers:

- `pages/` — one canonical Markdown record per mapped physical scan;
- `sections/` — decorative thematic headings mapped in source order;
- `indexes/page-map.md` — physical scan/status map;
- `indexes/section-register.md` — verified section boundaries;
- `indexes/source-citation-register.md` — printed Sangam anthology / poem / poet provenance.

The book's decorative sections are **not assigned invented source chapter numbers**. Repository sequence numbers are navigation identifiers only.

## Startup state

Physical records currently exist through scan **24**.

Mapped source structure:

- scans **1–16** — front matter;
- scans **17–19** — `மலர்மாரி பொழிகின்றேன்!`;
- scans **20–24** — `யாதும் ஊரே; யாவரும் கேளிர்!`.

Verified non-text/title/blank/illustration pages are separated from `partial` and `not-started` text pages. No continuous text page has been called `verified` merely because its heading or metadata was identified.

The source-citation register already preserves directly inspected printed provenance samples, including `புறநானூறு`, `அகநானூறு` and `குறுந்தொகை` references. These remain source citations, not externally corrected concordance entries.

Work-specific controls:

- [`SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`](SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md)
- [`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`](NEXT_CHAT_PROMPT_SANGATH_TAMIL.md)
- [`works/sangatamil/README.md`](works/sangatamil/README.md)
- [`works/sangatamil/metadata/transcription-policy.md`](works/sangatamil/metadata/transcription-policy.md)

## Repository-state discipline

Current progress must be determined from actual `main` files and the controlling scan, not from stale chat summaries.

For the active Sangath Tamil work, precedence is:

**controlling scan → physical page records → completed verification/audit artefacts → source/page/section indexes → current work README → root HANDOVER / README → historical snapshots.**

## அடுத்த செயல்

Active next gate: **சங்கத் தமிழ் front matter scans 9–14 / printed pages IV–IX**.

Complete, in source order:

- `ஈ. இராமலிங்கனர் மடல்!`;
- `அணிந்துரை`;
- `பதிப்புரை`.

Transcribe directly from the scan and promote a text page to `verified` only after direct visual comparison. After that gate, continue with the first body section `மலர்மாரி பொழிகின்றேன்!` — scans **17–19**.

Current handover: [`HANDOVER.md`](HANDOVER.md).
