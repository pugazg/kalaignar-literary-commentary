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

# Completed corrective section 004

`துணை நின்றார் தோழி!` — scans **31–36 / printed 16–21** — **COMPLETE / VERIFIED**.

Boundary is verified because scan 37 begins the next decorative heading `சுமந்தவன் சுமந்த சோகம்!`.

The inherited section was audited before advancement. That audit found:

- scan 31 — heading present but full source text missing;
- scans 33–35 — largely structural placeholders rather than complete transcriptions;
- scan 36 — substantive first-pass wording errors, including inside the Sangam quotation;
- scan 32 — verified illustration record was valid.

Corrective action:

- scans **31, 33, 34, 35 and 36** were completely re-transcribed from the controlling PDF;
- a separate second character-by-character + meaningful visual-text fidelity comparison was then performed rather than conflating first pass and verification;
- all section pages are now `verified`;
- the second pass made additional corrections including scan 35 `மனையறம்`, scan 36 `முல்லையினை`, and source-visible deliberate offset/right-aligned continuation lines;
- scan 36 quotation preserves printed forms `வலவர்`, `துறைசெழு`, and `அன்னவிவள்` without external normalization.

Verified scan-36 provenance:

- `ஐங்குறுநூறு : பாடல் : 180`
- `பாடியவர் : அம்மூவனார்`

The canonical citation register has been promoted to `verified` for this entry.

# Existing later mapped work — audit before trusting

## Section 005 — CURRENT NEXT GATE

`சுமந்தவன் சுமந்த சோகம்!` — scans **37–41 / printed 22–26**.

- boundary already verified;
- physical records exist;
- scan 38 illustration is verified;
- text records **37, 39, 40, 41** remain `needs-review` and must be audited/re-transcribed against the source before promotion;
- scan 41 visibly prints `புறநானூறு : பாடல் : 286` / `பாடியவர் : ஔவையார்`;
- do not register/promote that citation as verified until scan 41 passes textual + visual verification.

## Section 006

`பாவை புகழ்ந்த பன்றி` — begins at **scan 42 / printed 27**.

- physical records currently exist through scan **45 / printed 30**;
- scan 44 illustration is verified;
- text records remain `needs-review`;
- section end is still open until scan 46 onward is directly checked for the next decorative heading.

# Exact next activity

Do **not** create new records beyond scan 45 yet.

1. Audit section 005 against the controlling PDF: scans **37, 39, 40, 41**; scan 38 remains the existing verified illustration record.
2. Where the inherited records are placeholders or inaccurate, replace them with complete source-first transcriptions rather than patching around missing text.
3. Preserve every printed verse/dialogue line, meaningful indentation/alignment, heading, separator, source quotation, provenance block and `பொருள் விளக்கம்` exactly as source-supported.
4. Perform a separate second character-by-character + meaningful visual-text fidelity gate before any text page becomes `verified`.
5. When scan 41 passes, add/promote `புறநானூறு : பாடல் : 286` / `பாடியவர் : ஔவையார்` in the canonical citation register.
6. Synchronize section README, page map, section register, citation register, work/root README, handover and continuation prompt when section 005 closes.
7. Then audit section 006 through scan 45 and establish its end boundary from scan 46 onward.
8. Only after the existing mapped range is trustworthy should new source-order records be created beyond scan 45.

# Completed Thirukkural baseline — DO NOT RESTART

`works/thirukkural/` remains complete:

- Tamil Parts **001–015** archival-ready through scan **323**;
- commentary through printed page **270 / Kural 1330**;
- English project translation Parts **001–015** released;
- semantic provenance complete for **3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள்**;
- final structure audit PASS.
