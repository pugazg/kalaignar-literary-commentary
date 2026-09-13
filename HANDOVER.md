# HANDOVER — Kalaignar Literary Commentary Archive

Last refreshed for Kuraloviyam **Part 004 English editorial review 66/111; ER3 scans 400–432 next**: **2026-09-12**.

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

## Durable Kuraloviyam state

### Part 004 — FULLY CLOSED

- final checkpoint — **PASS / CLOSED**;
- Tamil — **111/111 textual + visual verified / 0 exceptions**;
- English — **111/111 `release-ready`**;
- durable final record — `works/kuraloviyam/PART_004_FINAL_CLOSURE.md`.

### Part 005 — PASS 1 COMPLETE / PASS 2A ACTIVE

Controlling source: `TVA_BOK_0065733_குறளோவியம்_part_005_pages_445-555.pdf`.

- source intake — **PASS / COMPLETE**;
- P5-01 — **445–455 / printed 428–438 — COMPLETE 11/11**;
- P5-02 — **456–466 / printed 439–449 — COMPLETE 11/11**;
- P5-03 — **467–477 / printed 450–460 — COMPLETE 11/11**;
- P5-04 — **478–488 / printed 461–471 — COMPLETE 11/11**;
- P5-05 — **489–499 / printed 472–482 — COMPLETE 11/11**;
- P5-06 — **500–510 / printed 483–493 — COMPLETE 11/11**;
- P5-07 — **511–521 / printed 494–504 — COMPLETE 11/11**;
- P5-08 — **522–532 / printed 505–515 — COMPLETE 11/11**;
- P5-09 — **533–543 / printed 516–526 — COMPLETE 11/11**;
- P5-10 / final remainder — **544–555 / printed 527–538 — COMPLETE 12/12**;
- cumulative Pass 1 — **111/111 COMPLETE**;
- all 111 records — `needs-review` / visual `needs-review`;
- final Pass-1 page endpoint — `e636f7d4c6bd02fb9db244a8989e22a04b6c0cb6`;
- exact final Pass-1 compare from `ede8f2e8f950359abe2da5d3c9db116c0d04f71a` to `e636f7d4c6bd02fb9db244a8989e22a04b6c0cb6` — **12 files only / scans 544–555**;
- **555→556 — CLEAN**, preserved from the source-gated Part 006 boundary;
- durable Pass-1 progress — `works/kuraloviyam/PART_005_PASS1_PROGRESS.md`;
- Pass 2A Batch 1 — **445–455 / printed 428–438 — COMPLETE 11/11**;
- Pass 2A Batch 2 — **456–466 / printed 439–449 — COMPLETE 11/11**;
- Pass 2A Batch 3 — **467–477 / printed 450–460 — COMPLETE 11/11**;
- Pass 2A Batch 4 — **478–488 / printed 461–471 — COMPLETE 11/11**;
- Pass 2A Batch 5 — **489–499 / printed 472–482 — COMPLETE 11/11**;
- Pass 2A Batch 6 — **500–510 / printed 483–493 — COMPLETE 11/11**;
- Pass 2A Batch 7 — **511–521 / printed 494–504 — COMPLETE 11/11**;
- Pass 2A Batch 8 — **522–532 / printed 505–515 — COMPLETE 11/11**;
- Pass 2A Batch 9 — **533–543 / printed 516–526 — COMPLETE 11/11**;
- cumulative Pass 2A — **99/111**;
- Batch-1 corrections — **2 records / 3 readings**;
- Batch-2 corrections — **5 records / 6 readings**;
- Batch-3 source-supported corrections — **7 records / 10 readings**: scan 467 `திருக்கிட்டு` → `திடுக்கிட்டு`; scan 468 `புகழிப் பித்தர்களென்பான்` → `பதவிப் பித்தர்களென்பான்`; scan 469 `தாய்மையாக` → `தூய்மையாக`, `இணையில்லாமல்` → `இணைபிரியாமல்`, `முட்டா` → `மூடா`; scan 471 `எழுதுகோவியமாக்கலாமா` → `எழுத்தோவியமாக்கலாமா`; scan 473 `அவைக்கனத்தில்` → `அவைக்களத்தில்`, `அவையவிட்டு` → `அவையைவிட்டு`; scan 476 `முத்தமிட்டீர்க ளே` → `முத்தமிட்டீர்களே`; scan 477 `தனியர் இதழ்கள்` → `தளிர் இதழ்கள்`;
- Batch-3 correction commit — `b6ce17d55759f05f80af760ac9d3d2cd0ec96bac` — exact compare **7 page files only / scans 467, 468, 469, 471, 473, 476, 477**;
- Batch-4 source-supported corrections — **6 records / 8 readings**: scan 480 `முத்துக் களால்` → `முத்துக்களால்`; scan 481 `அவற்றம் எழுத்துக்கள்` → `அவர்தம் எழுத்துக்கள்`; scan 482 `அக் தண்ணீர்` → `அத் தண்ணீர்`; scan 486 `நாளாயிரம்` → `நானாயிரம்` twice; scan 487 `அங்கேதான்` → `அங்குதான்`; scan 488 `கனவனில்லையெனக்` → `கணவனில்லையெனக்`, `கலங்கியமுதான்` → `கலங்கியழுதான்`;
- Batch-4 correction commit — `4902fd9fef350947103be839135a1c7d3a7c4d6e` — exact compare **6 page files only / scans 480, 481, 482, 486, 487, 488**;
- Batch-5 source-supported corrections — **3 records / 4 readings**: scan 490 Kural `பொருள்செய்து ஏமார்த்தல்` → `பொருள்செய்தே மார்த்தல்`; scan 492 `என்பதென்று` → `என்பது என்று`; scan 493 `திடுக்கத்தை` → `திடீர்க்கதையை`;
- Batch-5 correction commit — `5d9478576f4296e34338447145c518686cd925af` — exact compare **3 page files only / scans 490, 492, 493**;
- Batch-6 source-supported corrections — **2 records / 2 readings**: scan 500 `கூடிக்கிளித்ததை` → `கூடிக் களித்ததை`; scan 510 `நடைபெற்றதான்` → `நடைபெற்றுத்தான்`;
- Batch-6 correction commit — `fe14f3a9e284bd91b03ddaa927eb4d4595e86d30` — exact compare **2 page files only / scans 500, 510**;
- Batch-7 source-supported corrections — **2 records / 3 readings**: scan 518 `அந்திக்குக் கோபுரம்` → `அநீதிக்குக் கோபுரம்`, `எச்சத்துக்கும்` → `எச்சக்கும்`; scan 519 `ஆதிக்க வெங்கைகள்` → `ஆதிக்க வேங்கைகள்`;
- Batch-7 correction commit — `7c87cc0b41de0141062d1847fae8e8fc73fc40b1` — exact compare **2 page files only / scans 518, 519**;
- Batch-8 source-supported corrections — **9 records / 18 readings**: scans 524–532; page correction commit `ba6e0ba0b7b438476bbafb846212e05c080f6028`;
- exact Batch-8 compare — **9 page files only / scans 524–532**;
- Batch-9 source-supported corrections — **1 record / 1 reading**: scan 534 `அனைத்தவிர மற்ற அனைத்தையும்` → source-visible `அதைத் தவிர மற்ற அனைத்தையும்`;
- Batch-9 correction commit — `b3216bbb18464744a06e79232d973f46575c1145` — exact compare **1 page file only / scan 534**;
- **543→544 — GENUINE CONTINUATION**, checked from scan 544 / printed 527 witness;
- all 111 records remain `needs-review` / visual `needs-review`;
- durable Pass-2A log — `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_005.md`.

### Part 006 — SOURCE INTAKE COMPLETE / WAITING

- source intake — **PASS / COMPLETE**;
- scans — **556–666**;
- physical source endpoint — **scan 666**;
- Tamil Pass 1 — **NOT STARTED / waiting behind Part 005**.

## Exact next activity — குறளோவியம்

Continue **Part 005 Pass 2A / Batch 10 final remainder — scans 544–555 / printed 527–538**. Preserve the incoming **543→544 GENUINE CONTINUATION**. The outgoing **555→556 CLEAN** boundary is already source-resolved; do not begin Part 006 transcription. Keep all pages `needs-review` until the later required Pass 2B / Pass 3 / audit gates close. Do not begin Part 006 transcription yet.
