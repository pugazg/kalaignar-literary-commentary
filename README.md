# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

Last synchronized with live `main`: **2026-08-19**.

## திட்டமிட்ட / உள்ள நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–015 **ARCHIVAL-READY through scan 323**; commentary through printed page 270 / Kural 1330 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–015 **RELEASED through the end of the supplied volume** |
| Thirukkural semantic structure | பால் → இயல் → அதிகாரம் | **COMPLETE — 3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள் mapped** |
| சங்கத் தமிழ் | தமிழ் | **ACTIVE — complete 497-scan source confirmed; physical records through scan 24; front-matter text gate and first body section complete** |
| Sangatamil | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த source-controlled edition ஆக archive செய்யப்படும் |
| குறளோவியம் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Kuraloviyam | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |

## மூலக் கொள்கை

> **ஸ்கேன் தான் அதிகாரப்பூர்வ மூல ஆதாரம். Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது.

Source PDFs are working/control sources and are not committed unless the user explicitly changes that policy.

For source-controlled Tamil pages, `verified` requires both:

- **textual fidelity** — wording, spelling, punctuation, line content and order;
- **meaningful visual text fidelity** — verse/stanza/paragraph structure, heading hierarchy, separators, emphasis and text/image relationship.

## English layers — published source vs project translation

1. **Published / official English source** — தனியாக வெளியிடப்பட்ட source கிடைத்தால், அதன் சொந்த pagination / wording / metadata-உடன் source-controlled edition ஆக archive செய்யப்படும்.
2. **Project-created English translation** — audited Tamil source-இலிருந்து உருவாக்கப்படும் மொழிபெயர்ப்பு; `translation_type: "project_translation"` என்று வெளிப்படையாகக் குறிக்கப்படும்.

Published English sources must remain independent of Tamil physical-page archives and must not silently rewrite them.

# Canonical completed state — திருக்குறள்

The supplied **திருக்குறள் — கலைஞர் உரை** volume remains complete across all defined layers:

- Tamil Parts **001–015** archival-ready through scans **1–323**;
- commentary through printed page **270 / Kural 1330**;
- English project translation Parts **001–015 released**;
- semantic provenance complete: **3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள்**;
- final semantic audit: [`works/thirukkural/structure/STRUCTURE_AUDIT.md`](works/thirukkural/structure/STRUCTURE_AUDIT.md) — **PASS**.

Do not restart completed Thirukkural batches unless a new source or explicit correction task requires it.

# Canonical active state — சங்கத் தமிழ்

Active path: [`works/sangatamil/`](works/sangatamil/)

Controlling source:

`TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

## Verified source extent

The actual PDF has been independently confirmed as **497 scans**:

- `pdfinfo`: 497 pages;
- scans 493–497 render successfully;
- scan **497 is the back cover**.

The earlier 150-page figure was a preview-service limitation and is retired. Canonical source range is **1–497**; do not create scan 498+ records or infer printed pagination from scan arithmetic.

## Current physical / structural progress

Physical Markdown records currently exist through scan **24**.

Mapped source order:

- scans **1–16** — front matter;
- scans **17–19** — `மலர்மாரி பொழிகின்றேன்!`;
- scans **20–24** — `யாதும் ஊரே; யாவரும் கேளிர்!`;
- scans **25–497** — progressive discovery/transcription pending.

### Completed front-matter text gate

Scans **9–14 / printed IV–IX** are directly transcribed and verified for textual + visual fidelity:

- `ஈ. இராமலிங்கனர் மடல்!`;
- `அணிந்துரை`;
- `பதிப்புரை`.

Scans 7–8 remain explicitly `partial` page records.

### Completed first body section

`மலர்மாரி பொழிகின்றேன்!` — scans **17–19** is complete:

- scan 17 text verified;
- scan 18 illustration verified;
- scan 19 text verified.

The quotation continuity across the scan-18 illustration is explicitly preserved. Scan 19's printed provenance — `பத்துப்பாட்டு (குறிஞ்சிப்பாட்டு) / 61 முதல் 95 முடிய / பாடியவர் : கபிலர்` — is recorded in the Sangam citation register.

Current controls:

- [`SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`](SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md)
- [`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`](NEXT_CHAT_PROMPT_SANGATH_TAMIL.md)
- [`works/sangatamil/README.md`](works/sangatamil/README.md)
- [`works/sangatamil/metadata/source.md`](works/sangatamil/metadata/source.md)
- [`works/sangatamil/indexes/page-map.md`](works/sangatamil/indexes/page-map.md)
- [`works/sangatamil/indexes/section-register.md`](works/sangatamil/indexes/section-register.md)
- [`works/sangatamil/indexes/source-citation-register.md`](works/sangatamil/indexes/source-citation-register.md)

## Repository-state discipline

For active Sangath Tamil work, precedence is:

**controlling scan → physical page records → completed verification/audit artefacts → source/page/section/citation indexes → work README → root HANDOVER / README → historical snapshots.**

## அடுத்த செயல்

Process the second body section:

**`யாதும் ஊரே; யாவரும் கேளிர்!` — scans 20–24**.

Preserve scan 22 as a full-page illustration and verify the printed scan-24 provenance:

`புறநானூறு - பாடல் : 192 / பாடியவர் : கணியன் பூங்குன்றனார்`.

Current handover: [`HANDOVER.md`](HANDOVER.md).
