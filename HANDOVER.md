# HANDOVER — Kalaignar Literary Commentary Archive

Last synchronized with live `main`: **2026-08-23**.

## Repository

`pugazg/kalaignar-literary-commentary`

Current active work: `works/sangatamil/`

Completed benchmark retained: `works/thirukkural/`

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

Then inspect current GitHub `main` and the actual source scans required for the active batch.

# Permanent source / fidelity rule

> **The scan is the authority. Markdown is a faithful preservation layer, not a rewritten edition.**

Never silently modernize, normalize, correct from another edition, replace quotations, alter printed anthology/poem/poet labels, reconstruct unclear source, invent pagination, or infer missing source content.

`verified` requires direct source comparison for both textual fidelity and meaningful visual text fidelity. OCR/search may assist only as a locator/draft aid and is never authoritative.

# Active source — சங்கத் தமிழ்

- source: `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`
- author: **கலைஞர் மு. கருணாநிதி**
- verified extent: **497 scans**
- scan **497**: back cover
- canonical range: **1–497**
- do not create scan 498+ records
- printed pagination must be read from the scan, not inferred.

The earlier 150-page figure was a preview-service limitation and is retired.

# Current physical boundary

Physical Markdown records currently exist through **scan 45**.

Scans **7–8** remain `partial` source/page records.

## Completed front matter

Scans **9–14 / printed IV–IX** — COMPLETE / directly verified.

## Completed body section 001

`மலர்மாரி பொழிகின்றேன்!` — scans **17–19** — COMPLETE.

Scan 19 provenance:

- `பத்துப்பாட்டு (குறிஞ்சிப்பாட்டு)`
- `61 முதல் 95 முடிய`
- `பாடியவர் : கபிலர்`

## Completed body section 002

`யாதும் ஊரே; யாவரும் கேளிர்!` — scans **20–24** — COMPLETE.

Scan 24 provenance exactly as printed:

- `புறநானூறு - பாடல் : 192`
- `பாடியவர் : கணியன் பூங்குன்றன்`

The quoted poem preserves source-visible form `ஆருது`.

## Completed body section 003

`மானங்காத்த மறவன்!` — scans **25–30 / printed 10–15** — COMPLETE.

- scan 25 — decorative opening + text verified;
- scan 26 — full-page illustration verified;
- scans 27–29 — text verified; later pencil marks/handwriting documented separately from body text;
- scan 30 — concluding text, quoted Sangam poem and `பொருள் விளக்கம்` verified.

Scan 30 provenance exactly as printed:

- `புறநானூறு : பாடல்: 74`
- `பாடியவர் : சேரமான் கணைக்கால் இரும்பொறை`

# Corrective source review — section 004

`துணை நின்றார் தோழி!` — scans **31–36 / printed 16–21**.

Boundary is verified because scan 37 begins the next decorative heading `சுமந்தவன் சுமந்த சோகம்!`.

Before advancing, the existing records were audited against the controlling source. The audit found:

- scan 31 — earlier record contained the heading but not the full source text;
- scans 33–35 — earlier records were structural placeholders without the full source text;
- scan 36 — earlier first-pass transcription contained substantive wording errors, including within the Sangam quotation;
- scan 32 — verified full-page illustration record remains valid.

Corrective action completed:

- scans **31, 33, 34, 35 and 36** were re-transcribed directly from the supplied PDF;
- source lineation / dialogue / meaningful alignment was represented in Markdown/limited HTML;
- scan 36 quotation was replaced with the source-visible reading, including `வலவர்`, `துறைசெழு`, and `அன்னவிவள்`;
- scan 36 provenance directly reads:
  - `ஐங்குறுநூறு : பாடல் : 180`
  - `பாடியவர் : அம்மூவனார்`;
- the provenance is now in `source-citation-register.md` as direct-source / verification-pending.

The corrected text pages intentionally remain `needs-review`: this corrective transcription is **not** being conflated with the independent second verification gate.

# Existing later mapped work — audit before trusting

## Section 005

`சுமந்தவன் சுமந்த சோகம்!` — scans **37–41 / printed 22–26**.

- boundary already verified;
- physical records exist;
- scan 38 illustration is verified;
- text records remain `needs-review` and must be audited/re-transcribed against the source before promotion;
- scan 41 visibly prints `புறநானூறு : பாடல் : 286` / `பாடியவர் : ஔவையார்`.

## Section 006

`பாவை புகழ்ந்த பன்றி` — begins at **scan 42 / printed 27**.

- physical records currently exist through scan **45 / printed 30**;
- scan 44 illustration is verified;
- text records remain `needs-review`;
- section end is still open until scan 46 onward is directly checked for the next decorative heading.

# Exact next activity

Do **not** create new records beyond scan 45 yet.

1. Perform the independent second character-by-character + visual-text fidelity verification for corrected section 004 scans **31, 33, 34, 35, 36**.
2. Promote only pages that pass both textual and meaningful visual-text fidelity checks to `verified`.
3. When scan 36 passes, promote its `ஐங்குறுநூறு : பாடல் : 180` / `அம்மூவனார்` register entry to `verified`.
4. Then audit and, where necessary, redo the existing section-005 text records, scans **37, 39, 40, 41**, before advancing.
5. Next audit section 006 text records through scan 45 and establish its end boundary from scan 46 onward.
6. Only after the existing mapped range is trustworthy should new source-order records be created beyond scan 45.
7. Synchronize page map, section register, citation register, work/root README, handover and continuation prompt at each completed section gate.

# Completed Thirukkural baseline — DO NOT RESTART

`works/thirukkural/` remains complete:

- Tamil Parts **001–015** archival-ready through scan **323**;
- commentary through printed page **270 / Kural 1330**;
- English project translation Parts **001–015** released;
- semantic provenance complete for **3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள்**;
- final structure audit PASS.
