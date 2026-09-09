# HANDOVER — Kalaignar Literary Commentary Archive

Last refreshed for Kuraloviyam **Part 003 Pass 1 through P3-10 / scan 332**: **2026-09-09**. Sangath Tamil workflow state below is retained from its latest dedicated handover and live `main` remains authoritative.

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

## Mandatory startup — குறளோவியம்

Before Kuraloviyam repository changes, read completely:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. `NEXT_CHAT_PROMPT_KURALOVIYAM.md`
5. `works/kuraloviyam/HANDOVER.md`
6. `works/kuraloviyam/README.md`
7. `works/kuraloviyam/metadata/source.md`
8. `works/kuraloviyam/metadata/transcription-policy.md`
9. `works/kuraloviyam/indexes/page-map.md`
10. `works/kuraloviyam/SOURCE_INTAKE_PART_003.md`
11. `works/kuraloviyam/PART_003_PASS1_PROGRESS.md`
12. `works/kuraloviyam/PART_002_TAMIL_ARCHIVAL_READY.md`
13. `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`
14. `works/kuraloviyam/translations/en/reviews/PART_002_ENGLISH_RELEASE_REPORT.md`

Then inspect the actual supplied scan images before writing.

## Kuraloviyam source family

- source family: `TVA_BOK_0065733`
- title: **குறளோவியம்**
- author: **கலைஞர் மு. கருணாநிதி**
- complete source extent reported by user: **666 physical PDF pages**
- split plan: **6 parts × 111 pages**
- repository `scan_page` always uses overall 1–666 numbering.

## Closed state

- Part 001 Tamil: **CLOSED / archival-ready**.
- Part 001 English: **CLOSED — 107 release-ready + 4 source-limited**.
- Part 002 Tamil: **ARCHIVAL-READY / CLOSED — 111/111 textual + visual verified**.
- Part 002 English: **RELEASE COMPLETE / CLOSED — 111/111 release-ready**.

Do not reopen Part 001 or Part 002 from stale prompts unless a genuinely new source/provenance/fidelity problem appears.

## Part 003 — active source

Controlling source:

`TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf`

Confirmed identity:

- local pages: **111**;
- overall scans: **223–333**;
- printed pages: **206–316**;
- file size: **93,488,924 bytes**;
- SHA-256: `f07e7cdb3a6e786b0378e00bbe699a241be41c9e099c004a4faa90fa82b4239f`;
- no usable parsed text layer; rendered scans control.

Source intake: **PASS / COMPLETE**.

## Part 003 Pass 1 — ACTIVE

Current capture state: **110 / 111 scans — overall scans 223–332 / printed 206–315**.

Completed batches:

- **P3-01 scans 223–233 / printed 206–216 — COMPLETE**;
- **P3-02 scans 234–244 / printed 217–227 — COMPLETE**;
- **P3-03 scans 245–255 / printed 228–238 — COMPLETE**;
- **P3-04 scans 256–266 / printed 239–249 — COMPLETE**;
- **P3-05 scans 267–277 / printed 250–260 — COMPLETE**;
- **P3-06 scans 278–288 / printed 261–271 — COMPLETE**;
- **P3-07 scans 289–299 / printed 272–282 — COMPLETE**;
- **P3-08 scans 300–310 / printed 283–293 — COMPLETE**;
- **P3-09 scans 311–321 / printed 294–304 — COMPLETE**;
- **P3-10 scans 322–332 / printed 305–315 — COMPLETE**.

Current internal boundaries:

- **233→234 genuine continuation**;
- **244→245 clean**;
- **255→256 clean**;
- **266→267 genuine continuation**;
- **277→278 clean**;
- **288→289 genuine continuation**;
- **299→300 clean**;
- **310→311 clean**;
- **321→322 clean**;
- **323→324 clean**;
- **325→326 clean**;
- **327→328 clean**;
- **329→330 clean**;
- **331→332 clean**;
- **332→333 genuine continuation**.

All Part-003 Pass-1 records remain `status: "needs-review"` and `visual_fidelity: "needs-review"`. Pass 1 is capture/transcription only; do not claim source verification.

P3-10 source units:

- scans **322–323** — classroom / `வலியறிதல்`; Chapter 48 / Kurals 479, 473;
- scans **324–325** — Iraaman / Annam-Amudham chastity; Chapter 6 / Kural 57;
- scans **326–327** — Ezhini / Iniyan “Yama” love; Chapter 109 / Kural 1083;
- scans **328–329** — solitary-beauty / unused-wealth analogy; Chapter 101 / Kural 1007;
- scans **330–331** — burden / moral-faults / `அழுக்காறு`; Chapter 4 / Kural 35;
- scan **332** — severe-rule / famine vignette begins and continues directly to scan 333.

Scan **333 / printed 316** has been inspected only as the P3-10 outgoing boundary witness. It continues scan 332 and closes the same unit with Chapter 57 — `வெருவந்த செய்யாமை` / Kural 567. The external **333→334** boundary remains deferred until Part 004 intake; do not infer it.

# Exact next activity — குறளோவியம்

1. fetch live `main`;
2. complete the Kuraloviyam mandatory startup reading above;
3. resolve the supplied Part 003 PDF;
4. process the **final Part 003 Pass-1 remainder — scan 333 / printed 316, one physical page**;
5. begin scan 333 as the direct continuation of the severe-rule / famine vignette begun on scan 332;
6. create exactly `works/kuraloviyam/pages/0333-kuraloviyam-316.md`;
7. preserve exact visible source wording, punctuation, dialogue, Kural block and Chapter 57 / Kural 567 metadata;
8. keep the new record at `needs-review` / `visual_fidelity: needs-review` unless a genuine source limitation requires otherwise;
9. do not normalize, modernize, import standard/web Kural wording, use another edition, or guess from OCR/memory;
10. do not infer **333→334** before Part 004 is supplied;
11. synchronize Kuraloviyam progress/frontier documents and audit the exact changed-file set;
12. mark Part 003 Pass 1 **COMPLETE 111/111** only after scan 333 exists;
13. advance only to the next authorized Tamil archival gate; English remains blocked until Tamil closure.