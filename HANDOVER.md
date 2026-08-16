# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

Active work: `works/thirukkural/`

## Mandatory startup

Before making changes:

1. read `THIRUKKURAL_ARCHIVAL_GUIDELINES.md` completely;
2. read `LITERARY_COMMENTARY_PROCESSING_GUIDE.md` completely;
3. read this `HANDOVER.md` completely;
4. read `works/thirukkural/README.md`;
5. inspect existing target files before writing;
6. inspect the actual controlling source required by the active gate;
7. if English work later becomes active, fresh-read `TRANSLATION_GUIDE.md`, `GLOSSARY.md`, `TRANSLATION_STATUS.md`, and the latest review/release artefacts.

Repository state is authoritative.

## Source rule

The supplied Tamil scans are controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

Source PDFs are working/control sources and are not to be committed to GitHub unless the user explicitly requests that.

OCR/parsed text may assist but is never authoritative over direct inspection of the scan.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Keep these as separate gates.

Every project-created English page must identify `translation_type: "project_translation"`.

Released English material must not be revised merely to harmonize later vocabulary. Permanent earlier protections remain binding, including:

- chapter 38 `ஊழ்` → **Oozh**;
- Kalaignar's `இயற்கை நிலை` → **natural condition**;
- Kural 543 `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**;
- preservation of Kalaignar's governance, citizens, working-people, justice, public-resource and rational/inquiry vocabulary where the Tamil explicitly uses it.

# Established released baseline

## Tamil

Parts **001–011 are audited / ARCHIVAL-READY continuously** through overall scan **237 / printed page 204 / Kural 1010**.

Latest Tamil audit: `works/thirukkural/AUDIT_PART_011.md` — **PASS / ARCHIVAL-READY**.

## English

Parts **001–011 are fully released continuously through Kural 1010**.

Latest English release artefacts:

- `works/thirukkural/translations/en/reviews/PART_011_REVIEW.md`;
- `works/thirukkural/translations/en/reviews/PART_011_RELEASE_REPORT.md` — **PASS / RELEASE APPROVED**.

All released Part 011 corrections/protections recorded in those artefacts remain binding.

# Newly supplied sources

The following later source PDFs are now supplied:

- Part 012 — `திருக்குறள்_கலைஞர்_உரை_part_012_pages_238-260.pdf` — **23 pages**;
- Part 013 — `திருக்குறள்_கலைஞர்_உரை_part_013_pages_261-282.pdf` — **22 pages**;
- Part 014 — `திருக்குறள்_கலைஞர்_உரை_part_014_pages_283-302.pdf` — **20 pages**;
- Part 015 — `திருக்குறள்_கலைஞர்_உரை_part_015_pages_303-323.pdf` — **21 pages**.

Only Part **012** has been processed. Parts **013–015 are received but not started**.

# Part 012 controlling source

`திருக்குறள்_கலைஞர்_உரை_part_012_pages_238-260.pdf`

Supplied-file identity used during first-pass inspection: `file_00000000f4288211a7bbe05c015edc20`.

## Source intake findings

- physical pages: **23**;
- overall scans: **238–260**;
- Part-local pages: **1–23**;
- printed pages: **205–218**, then two unnumbered section leaves, then **221–227**;
- Kural range physically present: **1011–1115**;
- Part 011 → Part 012 boundary: printed **204 → 205 / Kural 1010 → 1011** — directly inspected and continuous.

Source-visible structure:

1. scans **238–251** — `பொருள் — குடியியல்`, chapters 102–108, Kural **1011–1080**;
2. scan **252** — centered section-title leaf `இன்பம்`;
3. scan **253** — no independent printed body text; reverse-side show-through only;
4. scans **254–260** — `இன்பம் — களவியல்`, beginning chapter 109 at Kural **1081** and continuing through Kural **1115**;
5. scan **260 / printed page 227** begins chapter 112 `நலம் புனைந்து உரைத்தல்`; only Kural **1111–1115** of that chapter are present in Part 012.

The supplied Part 013 first page was inspected only for outgoing-boundary context. It is printed page **228** and carries Kural **1116–1120**, confirming the physical continuation after Part 012. **No Part 013 page record has been created.**

# Part 012 Tamil first-pass state

**FIRST PASS COMPLETE — 23 / 23.**

Current status count:

- `needs-review`: **23 / 23**;
- `verified`: **0**;
- `partial`: **0**;
- `blocked`: **0**.

Every Part 012 first-pass page currently uses:

```yaml
status: "needs-review"
transcription_method: "manual transcription from source scan; direct visual verification pending"
```

No `AUDIT_PART_012.md` exists. Part 012 English has not started and is not eligible until Tamil audit passes.

## Part 012 page map / filenames

- scan 238 / p205 — ch102 `நாணுடைமை`, K1011–1015 — `0238-porul-naanudaimai-01.md`
- scan 239 / p206 — K1016–1020 — `0239-porul-naanudaimai-02.md`
- scan 240 / p207 — ch103 `குடிசெயல் வகை`, K1021–1025 — `0240-porul-kudiseyal-vagai-01.md`
- scan 241 / p208 — K1026–1030 — `0241-porul-kudiseyal-vagai-02.md`
- scan 242 / p209 — ch104 `உழவு`, K1031–1035 — `0242-porul-uzhavu-01.md`
- scan 243 / p210 — K1036–1040 — `0243-porul-uzhavu-02.md`
- scan 244 / p211 — ch105 `நல்குரவு`, K1041–1045 — `0244-porul-nalkuravu-01.md`
- scan 245 / p212 — K1046–1050 — `0245-porul-nalkuravu-02.md`
- scan 246 / p213 — ch106 `இரவு`, K1051–1055 — `0246-porul-iravu-01.md`
- scan 247 / p214 — K1056–1060 — `0247-porul-iravu-02.md`
- scan 248 / p215 — ch107 `இரவச்சம்`, K1061–1065 — `0248-porul-iravachcham-01.md`
- scan 249 / p216 — K1066–1070 — `0249-porul-iravachcham-02.md`
- scan 250 / p217 — ch108 `கயமை`, K1071–1075 — `0250-porul-kayamai-01.md`
- scan 251 / p218 — K1076–1080 — `0251-porul-kayamai-02.md`
- scan 252 / unnumbered — `இன்பம்` title — `0252-inbam-title.md`
- scan 253 / unnumbered — blank/reverse show-through — `0253-blank.md`
- scan 254 / p221 — ch109 `தகை அணங்குறுத்தல்`, K1081–1085 — `0254-inbam-thagai-ananguruththal-01.md`
- scan 255 / p222 — K1086–1090 — `0255-inbam-thagai-ananguruththal-02.md`
- scan 256 / p223 — ch110 `குறிப்பறிதல்`, K1091–1095 — `0256-inbam-kuripparithal-01.md`
- scan 257 / p224 — K1096–1100 — `0257-inbam-kuripparithal-02.md`
- scan 258 / p225 — ch111 `புணர்ச்சி மகிழ்தல்`, K1101–1105 — `0258-inbam-punarchchi-magizhthal-01.md`
- scan 259 / p226 — K1106–1110 — `0259-inbam-punarchchi-magizhthal-02.md`
- scan 260 / p227 — ch112 `நலம் புனைந்து உரைத்தல்`, K1111–1115 — `0260-inbam-nalam-punaindhuraiththal-01.md`

The `இன்பம்` title and following blank leaf follow the repository's existing `section-title` / `blank` physical-page precedent and must be verified rather than omitted.

## First-pass source-sensitive candidates for verification

Do not normalize these from memory or a standard Kural text. Re-read the scan directly:

- scan **251 / Kural 1077** — first-pass verse currently preserves the visibly read form `ஈங்கை விதிரார் ...`;
- scan **257 / Kural 1098** — first-pass verse currently preserves `அசையியற் குண்டாண்டோர் ...`;
- all unusual joins, punctuation and wording across the new `இன்பம்` section must be checked against the actual scan.

These are not declared corrections or errors yet; they are verification targets.

# Exact next activity

**Part 012 Tamil direct visual verification — all 23 physical pages, scans 238–260.**

Required procedure:

1. fresh-read the mandatory startup files above;
2. inspect the controlling Part 012 source directly, not a remembered or external Kural edition;
3. compare each of the 23 Markdown records line-by-line with its source scan;
4. verify Kural number, letter-for-letter verse wording, source-supported two-line structure, joins/spacing, punctuation, chapter heading, running-header hierarchy, Kalaignar commentary, printed-page metadata, scan/local-page metadata and source marker;
5. verify scan 252 as the `இன்பம்` section-title leaf and scan 253 as the blank/reverse-show-through leaf;
6. document every real first-pass correction discovered;
7. change a record to `status: "verified"` and `transcription_method: "direct visual comparison with source scan"` only after that page passes;
8. finish all **23 / 23** pages in this verification gate if safely possible;
9. stop after direct verification;
10. **do not create `AUDIT_PART_012.md` in the same activity**;
11. **do not begin Part 012 English**;
12. **do not begin Part 013 transcription**;
13. **do not alter released English Parts 001–011**.

After successful verification of all 23 pages, the exact next activity will be the separate **Part 012 Tamil audit / archival-ready gate**.
