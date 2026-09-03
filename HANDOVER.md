# HANDOVER — Kalaignar Literary Commentary Archive

Last refreshed for Kuraloviyam Pass 1 through **scan 60**: **2026-09-03**. Sangath Tamil workflow state below is retained from its latest dedicated handover and live `main` remains authoritative.

## Repository

`pugazg/kalaignar-literary-commentary`

Branch: `main`

Current active/source-ready works:

- `works/sangatamil/`
- `works/kuraloviyam/`

Completed benchmark retained: `works/thirukkural/`

## LIVE MAIN IS AUTHORITATIVE

**Fetch live `main` first and treat it as authoritative.**

The latest durable Sangath Tamil policy checkpoint recorded in this handover is:

`a4d13ade0b0c8ecccbe4609a438457d871163fdb` — `sangatamil: Lock Gemini lexical transcription policy`

Later commits may advance `main`. Preserve any newer durable state. Do not reset, overwrite, repeat, or reopen later completed work merely because this handover records an older SHA.

## Mandatory startup — active சங்கத் தமிழ் work

Before making any repository change, read completely:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`
5. `works/sangatamil/GEMINI_TEXT_LOCK.md` **— current user-approved lexical override**
6. `works/sangatamil/README.md`
7. `works/sangatamil/MULTI_PASS_WORKFLOW.md`
8. `works/sangatamil/GEMINI_RECONCILIATION_PLAN.md`
9. `works/sangatamil/metadata/source.md`
10. `works/sangatamil/metadata/transcription-policy.md`
11. `works/sangatamil/indexes/page-map.md`
12. `works/sangatamil/indexes/section-register.md`
13. `works/sangatamil/indexes/source-citation-register.md`

If older workflow documents conflict with `GEMINI_TEXT_LOCK.md` or the refreshed Sangath Tamil guidelines, **the current user-approved Gemini text lock controls this correction workflow**.

Then fetch the live page/history state and inspect the actual supplied scan before writing.

# Permanent current correction rule

> **Keep the supplied words from Gemini transcription. Correct only source-supported structure—page placement, paragraph order, punctuation, quotation structure, headings, speaker labels, poetry lineation, spacing—and remove non-source material such as library stamps, handwriting-derived/OCR garbage. Do not silently correct lexical words.**

The current authority split is:

- **Gemini `File1.md` … `File10.md` = lexical/text-wording lock**;
- **PDF scan = physical-page and structural authority**;
- **repository = preservation layer**.

For legitimate printed source text, do not replace Gemini words, characters, spellings, names, quoted wording, old/uncommon forms, or lexical choices simply because the scan or another edition appears to differ.

A lexical word may change only when the user explicitly authorizes it. The exception is deletion of **clearly non-source material** accidentally captured as text, such as library/accession stamps, handwriting OCR garbage, scanner artefacts, bleed-through garbage, or duplicated page furniture.

If the scan contains an entire lexical passage missing from Gemini, flag it for follow-up rather than silently source-transcribing new wording unless the user explicitly authorizes recovery.

# Active source — சங்கத் தமிழ்

- controlling source: `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`
- author: **கலைஞர் மு. கருணாநிதி**
- physical extent: **497 scans**
- scan **497**: back cover
- canonical physical range: **1–497**
- never create scan 498+
- printed pagination must come from the scan, never arithmetic

Pass-1 physical capture is complete through **scan 497**.

## Split-PDF source workflow

For page-level work in a fresh chat, resolve the relevant split PDF and matching Gemini file. Immediate available/current starting pair:

- `TVA_BOK_0042551_சங்கத்_தமிழ்_part_001_pages_1-50.pdf`
- `File1.md`

The next pair is:

- `TVA_BOK_0042551_சங்கத்_தமிழ்_part_002_pages_51-100.pdf`
- `File2.md`

Later work should use the corresponding later split PDF + `FileN.md` pair supplied by the user.

Gemini page comments are navigation aids only; they do not establish physical scan numbering. The scan does.

# Workflow history and supersession

Pass 1 physical capture is complete.

A scan-led lexical Pass 2 began and reached scan **13** at:

`a9b7b118a5b729c4e670b453260dc06327a011a3` — `sangatamil: Pass 2 reconcile scan 13`

That scan-led lexical correction mode is now **discontinued**.

The user-approved lexical lock was recorded at:

`a4d13ade0b0c8ecccbe4609a438457d871163fdb` — `sangatamil: Lock Gemini lexical transcription policy`

Do not continue the old rule of changing Gemini words to match the scan.

# Current active activity — Gemini-locked structural correction

The current work is a structural/presentation correction pass using:

- supplied Gemini words as the locked lexical layer;
- the scan for physical placement and structure.

Allowed source-supported corrections include:

- physical page placement / printed page metadata;
- paragraph order and boundaries;
- punctuation;
- quotation structure;
- headings/hierarchy;
- speaker-label placement/formatting;
- poetry/verse lineation and stanza grouping;
- spacing/indentation;
- separators and block placement;
- continuation order;
- removal of non-source OCR/stamp/handwriting garbage from body text.

Do **not** silently modify legitimate lexical words.

For scans **1–13**, earlier source-based lexical edits may exist. When the new structural pass encounters them, restore the corresponding supplied Gemini lexical wording where it differs, while retaining source-supported structural corrections. Do not treat those earlier scan-led lexical edits as authoritative over the current user directive.

## Batch discipline

Normal batch: **about 10 physical scans**, adjusted to a nearby natural boundary when useful.

For every batch:

1. fetch live `main`;
2. resolve the matching split PDF + Gemini file;
3. fetch current page records;
4. inspect scans directly;
5. preserve Gemini lexical wording;
6. apply only allowed structural/presentation corrections;
7. remove clearly non-source material from body text;
8. commit sequentially;
9. compare batch base → head;
10. confirm only intended page records changed;
11. fetch live `main` again and record the next frontier.

When the user says **“proceed with next activity”**, execute the recorded next batch directly. Do not merely explain the plan, ask for files already supplied, or stop because the controlling source has been split.

# Exact next activity — சங்கத் தமிழ்

In a fresh Sangath Tamil chat:

1. fetch live `main`;
2. complete mandatory startup reading above;
3. resolve the current split PDF + Gemini file required by live state;
4. continue the **Gemini-locked structural correction pass** from the actual live frontier;
5. preserve Gemini words, correct only source-supported structure/punctuation/spacing, and remove non-source material;
6. audit the changed-file set before advancing.

Do not restart Pass 1. Do not resume scan-led lexical Pass 2 at scan 14.

# Completed Thirukkural baseline — DO NOT RESTART

`works/thirukkural/` remains complete:

- Tamil Parts **001–015** archival-ready through scan **323**;
- commentary through printed page **270 / Kural 1330**;
- English project translation Parts **001–015** released;
- semantic provenance complete for **3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள்**;
- final structure audit PASS.

# Active source-ready work — குறளோவியம்

The user supplied the first split of the Kuraloviyam source on **2026-09-03**.

## Mandatory startup — குறளோவியம்

Before Kuraloviyam repository changes, read completely:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. `NEXT_CHAT_PROMPT_KURALOVIYAM.md`
5. `works/kuraloviyam/README.md`
6. `works/kuraloviyam/SOURCE_INTAKE_PART_001.md`
7. `works/kuraloviyam/metadata/source.md`
8. `works/kuraloviyam/metadata/transcription-policy.md`
9. `works/kuraloviyam/indexes/page-map.md`

Then inspect the actual supplied scan images before writing.

## Kuraloviyam source identity

- source family: `TVA_BOK_0065733`
- title: **குறளோவியம்**
- author: **கலைஞர் மு. கருணாநிதி**
- complete source extent reported by user: **666 physical PDF pages**
- split plan: **6 parts × 111 pages**
- canonical overall ranges:
  - Part 001: 1–111
  - Part 002: 112–222
  - Part 003: 223–333
  - Part 004: 334–444
  - Part 005: 445–555
  - Part 006: 556–666
- overall `scan_page` numbering never restarts per split.

Current supplied source:

`TVA_BOK_0065733_குறளோவியம்_part_001_pages_1-111.pdf`

Part 001 has no usable parsed text layer. Rendered scan images are controlling.

## Kuraloviyam Part 001 intake — COMPLETE

Confirmed:

- local pages: **111/111**;
- overall scans: **1–111**;
- scan 1: front cover;
- scans 2–3: title/publication/edition matter;
- scans 4–17: front matter;
- scan 18: main body begins at printed page **1**, heading `பேராசிரியர்`;
- scan 111: printed page **94**.

## Kuraloviyam Part 001 Pass 1 — scans 1–60 COMPLETE

Page-aligned records now exist continuously for **overall scans 1–60**:

- scans **1–3** — cover / title-publisher / edition-imprint;
- scans **4–8 / printed iii–vii** — `முகப்புரை`;
- scans **9–12 / printed viii–xi** — `மதிப்புரை` through its conclusion;
- scans **13–15 / printed xii–xiv** — handwritten/facsimile prefaces, retained `partial` where a safe word-for-word reading is not possible;
- scan **16 / printed xv** — first-edition photograph / commemorative note;
- scan **17 / printed xvi** — `ஆறாம் பதிப்பின் பதிப்புரை`;
- scans **18–20 / printed 1–3** — `பேராசிரியர்`;
- scan **21 / printed 4** — `மகா வித்துவான் தண்டபாணி தேசிகர்`;
- scans **22–23 / printed 5–6** — `டாக்டர் வ.சுப.மாணிக்கம்`;
- scan **24 / printed 7** — `மதுரை யாதவர் கல்லூரி முதல்வர் தமிழ்க்குடிமகன்`;
- scan **25 / printed 8** — `காசி ஆனந்தன்`;
- scans **26–27 / printed 9–10** — `ஆட்சிமொழிக் காவலர் இராமலிங்கனார்`;
- scan **28 / printed 11** — `ஆசிரியர் சாவி`;
- scan **29 / printed 12** — `டாக்டர் மெ.சுந்தரம்`;
- scan **30 / printed 13** — `டாக்டர் மா.நன்னன்`;
- scan **31 / printed 14** — `கலைஞர் ஏற்புரை`;
- scan **32** — section-title leaf `கலைஞரின் குறளோவியம்`, with no printed page number claimed;
- scan **33 / printed 16** — blank source-side leaf with reverse-side bleed-through only;
- scans **34–40 / printed 17–23** — opening illustrated/body sequence of `கலைஞரின் குறளோவியம்`;
- scans **41–42 / printed 24–25** — education/rebirth and `மெய்யுணர்தல்` discussion;
- scans **43–44 / printed 26–27** — lover/beloved gaze vignette;
- scans **45–47 / printed 28–30** — boastful-youth / promised-feats vignette;
- scans **48–49 / printed 31–32** — heart/dream vignette;
- scans **50–51 / printed 33–34** — palanquin vignette and Valluvar's correction, ending with `அறத்தாறு இதுவென வேண்டா சிவிகை...`;
- scans **52–53 / printed 35–36** — Ilango/Chenguttuvan renunciation vignette;
- scans **54–55 / printed 37–38** — moon/maiden and beloved-shoulder vignette;
- scans **56–57 / printed 39–40** — Valluvar/student discussion of sword-like and kin-like enemies;
- scans **58–59 / printed 41–42** — interpretation of `தெய்வந் தொழாஅள்...` and rain imagery;
- scan **60 / printed 43** — martial-history vignette begins and continues into scan 61.

Printed-text records remain `needs-review` / `visual_fidelity: needs-review` during Pass 1. The handwriting in scans 13–15 was not guessed or reconstructed.

The scans 51–60 page-batch audit compared:

`6b78e804788c22f292ead41bbcfd9a9c4c70cdfa` → `c49f14637143ee40862b295d8888619a5bd95345`

and confirmed **10 sequential page commits** adding exactly the ten expected page records for scans 51–60 before documentation synchronization.

Do not reopen scans 1–60 merely for stylistic harmonization during Pass 1. Later textual and visual verification passes will perform the source-check gates.

# Exact next activity — குறளோவியம்

1. fetch live `main`;
2. complete the Kuraloviyam mandatory startup reading above;
3. resolve the already supplied Part 001 PDF;
4. continue **Part 001 Pass 1 physical capture/transcription**;
5. process **overall scans 61–70**;
6. continue directly from the martial-history vignette at printed page 43 into the next source pages and preserve physical-page continuity;
7. create one page-aligned Markdown record per physical scan under `works/kuraloviyam/pages/`;
8. preserve source-visible wording and meaningful illustration/text relationships only;
9. normally leave new records `needs-review` / `visual_fidelity: needs-review`;
10. audit the changed-file set and record the next frontier.

Do not jump to verification, part audit or English translation before the relevant Tamil Pass-1 capture gate is complete.
