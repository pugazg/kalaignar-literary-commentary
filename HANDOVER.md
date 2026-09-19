# HANDOVER — Kalaignar Literary Commentary Archive

Last refreshed **2026-09-19**: Kuraloviyam remains closed; Sangath Tamil Gates **A–I are COMPLETE / PASS** and the Tamil archival pipeline is **CLOSED**; the separately scoped **maintained English project translation is ACTIVE** with first-pass Drafts D1–D14 scans **1–497 COMPLETE / CLOSED**, Source-Check SC1–SC14 scans **1–497 COMPLETE / CLOSED**, Glossary Reconciliation GR1–GR14 scans **1–497 COMPLETE / CLOSED**, Editorial Review ER1 scans **1–37 COMPLETE / PASS**, ER2 scans **38–74 COMPLETE / PASS**, ER3 scans **75–111 COMPLETE / PASS**, ER4 scans **112–148 COMPLETE / PASS**, ER5 scans **149–185 COMPLETE / PASS**, ER6 scans **186–222 COMPLETE / PASS**, ER7 scans **223–259 COMPLETE / PASS**, ER8 scans **260–296 COMPLETE / PASS**, ER9 scans **297–333 COMPLETE / PASS**, ER10 scans **334–370 COMPLETE / PASS**, ER11 scans **371–407 COMPLETE / PASS**, ER12 scans **408–444 COMPLETE / PASS**, ER13 scans **445–481 COMPLETE / PASS**, and ER14 scans **482–497 COMPLETE / PASS — EDITORIAL REVIEW CLOSED 497/497**.

## Repository

`pugazg/kalaignar-literary-commentary`

Branch: `main`

Current active/source-ready works:

- `works/sangatamil/`
- `works/kuraloviyam/`

Completed benchmark retained: `works/thirukkural/`

## LIVE MAIN IS AUTHORITATIVE

**Fetch live `main` first and treat it as authoritative.**

Current Sangath Tamil durable controls:

- `works/sangatamil/PRODUCTIVE_COMPLETION_PLAN.md`
- `works/sangatamil/C2_SOURCE_CORRECTION_PROGRESS.md`
- `works/sangatamil/POST_C2_RECONCILIATION.md`
- `works/sangatamil/GATE_G_METADATA_STATUS_AUDIT.md`
- `works/sangatamil/GATE_H_DERIVED_NAVIGATION_REPORT.md`
- `works/sangatamil/GATE_I_FINAL_CLOSURE.md`
- `works/sangatamil/navigation/README.md`
- `works/sangatamil/indexes/section-register.md`
- `works/sangatamil/indexes/source-citation-register.md`
- `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`

Latest Gate-G page-layer endpoint:

`fd024e4c0b1d3f21a3849c360d509350ce808db5`

Gate-G durable report commit:

`93afbcda3151abb86b7338252f8222dbf0111413`

Earlier Gate-B/C/F checkpoints remain historical evidence only. Later commits may advance `main`; never reset newer durable state merely because an older SHA appears below.

## Sangath Tamil — current productive state

- Gate A — **COMPLETE / PASS — 497/497 canonical records / 0 duplicates / 0 missing**
- Gate B — **COMPLETE / PASS — 497/497 structurally reviewed**
- Gate C — **COMPLETE / PASS — 497/497 audited / 140 historical discrepancy records**
- Gate C2 — **COMPLETE / APPLIED — 140/140 user-adjudicated / 0 locked remainder**
- Gate D — **COMPLETE / PASS — 497/497 physical / visual / continuity / 0 unresolved**
- Gate E — **COMPLETE / PASS — 104 section-role entries / 497/497 scans assigned exactly once**
- Gate F — **COMPLETE / PASS — 115 formal provenance units + 4 source-note-only records**
- Post-C2 reconciliation R1 — **COMPLETE / PASS — 0 canonical page mutations / 0 unresolved**
- Gate G — **COMPLETE / PASS — 497/497 metadata/status audited / 11 missing `visual_fidelity` fields repaired / 0 unresolved / 0 wording changes**
- Gate H — **COMPLETE / PASS — 104 sections / 115 formal units / 4 note-only / 119 provenance leaves / 0 canonical page changes**
- Gate I — **COMPLETE / PASS — final synchronization / closure**
- Gate-G historical page status distribution — **43 verified / 453 needs-review / 1 partial**
- current Tamil re-audit state after R03 — **47 verified / 449 needs-review / 1 partial**
- current visual-fidelity state after R03 — **47 verified / 450 needs-review / 0 missing**
- user-directed Tamil word-for-word verification — **IN PROGRESS**
- restart R01 scans **1–10** — **COMPLETE / PASS — 0 new lexical discrepancies / WFV-001 rejected / scan8 partial**
- restart R02 scans **11–20** — **COMPLETE / PASS — 0 new lexical discrepancies / 0 lexical substitutions / 0 page-layer mutations**
- restart R03 scans **21–30** — **COMPLETE / PASS WITH LEXICAL HOLDS — WFV-006..008 / 0 lexical substitutions / scans 25+30 needs-review**
- whole-volume word-for-word completion — **NOT YET CLAIMED**

The mixed page-level statuses are intentional. Gate C2 resolved all recorded Gate-C discrepancies but did not perform a fresh exhaustive token-by-token reread of every source word.

**Exact active Tamil activity: restarted Gemini-locked word-for-word + historical-glyph re-audit in 10-page iterations.** R01 scans **1–10**, R02 scans **11–20**, and R03 scans **21–30** are complete. R03 closed **PASS WITH LEXICAL HOLDS**: WFV-006 scan 25 (`பெற்றவனோ?` vs source `பெற்றவனே?`) and WFV-007/WFV-008 scan 30 (`ஆள்அன்று` vs source `ஆளன்று` in quotation and gloss) remain pending explicit user adjudication. **No lexical mutation was made.** Exact next range is **R04 scans 31–40** from the supplied Part001 PDF.

Mandatory companion control: `works/sangatamil/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`. Inspect difficult glyphs at enlarged/native resolution, check the 13 known families, and compare same-edition evidence. **Do not correct lexical words directly**: every new lexical/glyph difference goes to `LEXICAL_DISCREPANCY_LEDGER.md` and awaits explicit user adjudication.

**Maintained English release-report gate is PAUSED while the new Tamil word-for-word verification pass is active.** The English layer remains at **496 editorial-reviewed + 1 source-limited (scan 8)**. Tamil corrections discovered by this pass must receive targeted English impact reconciliation before any release approval or `release-ready` promotion.

English controls: `works/sangatamil/translations/en/README.md`, `TRANSLATION_GUIDE.md`, `TRANSLATION_STATUS.md`, and `GLOSSARY.md`.

Do not reopen the canonical Tamil layer for translation work. English release state does not imply fresh whole-volume word-for-word scan verification.

> Historical workflow sections later in this handover may preserve the frontier that was true when they were written. They are evidence, not the live execution frontier. The current state above controls.

## Mandatory startup — active சங்கத் தமிழ் work

Before making any repository change, read completely:

1. works/sangatamil/PRODUCTIVE_COMPLETION_PLAN.md
2. works/sangatamil/GEMINI_TEXT_LOCK.md — current user-approved lexical override
3. works/sangatamil/GATE_G_METADATA_STATUS_AUDIT.md
4. works/sangatamil/STRUCTURAL_FIDELITY_PROGRESS.md
5. works/sangatamil/GATE_A_HYGIENE_REPORT.md
6. SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md
7. root HANDOVER.md
8. NEXT_CHAT_PROMPT_SANGATH_TAMIL.md
9. works/sangatamil/README.md
10. works/sangatamil/metadata/source.md
11. works/sangatamil/metadata/transcription-policy.md
12. works/sangatamil/indexes/page-map.md
13. works/sangatamil/indexes/section-register.md
14. works/sangatamil/indexes/source-citation-register.md

Historical/superseded background only: works/sangatamil/MULTI_PASS_WORKFLOW.md and works/sangatamil/GEMINI_RECONCILIATION_PLAN.md.

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

For page-level work in a fresh chat, resolve the split PDF and Gemini file required by the live frontier.

Gate B source processing is closed through scan 497.

Current closed-gate state:

- Gate C — COMPLETE / PASS — scans 1–497 audited
- cumulative lexical discrepancy records — 140
- Gate C2 — COMPLETE / APPLIED — 140/140 adjudicated
- Gate D — COMPLETE / PASS — 497/497 physical scans closed
- Gate E — COMPLETE / PASS — 104 section-role entries / 497/497 assigned exactly once
- Gate F — COMPLETE / PASS — 115 formal provenance units + 4 source-note-only records
- post-C2 reconciliation R1 — COMPLETE / PASS
- Gate G — COMPLETE / PASS — 497/497 metadata/status audited / 11 field-presence repairs / 0 unresolved
- current active target — **Gate H derived navigation**
- closed derived authorities — `indexes/section-register.md`, `indexes/source-citation-register.md`, `GATE_G_METADATA_STATUS_AUDIT.md`

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

Normal Gate-B batch: **25 physical scans**, reduced only for unusually dense/damaged material.

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

Durable B15 correction: scan 359 is mixed text/illustration, not illustration-only; File8 page 348 is physically redistributed across scans 358–360.

Durable B17 exception: File9 Book Pages 401–412 are not reliable one-to-one lexical blocks for physical scans 413–424. Do not fabricate lexical alignment for them or similar broken blocks.

Durable B18 exception: File9 Phase 20 advertises Book Pages 413–438 but the supplied payload ends at Page 425. Usable Page 414–425 blocks cover scans 426–437; scans 438–450 have no File9 lexical block and were structurally reviewed without synthetic lexical alignment.

Durable B19 exception: File10 Page 449 becomes replacement material after a reliable prefix; scan 462 / printed 450 has no reliable File10 block; comments 450–455 are shifted across scans 463–468; Page 456 is a phantom image marker; mapping realigns at Page 457 / scan 469.

Durable B20 closure: final scans 476–497 completed with 7 page records changed, 15 reviewed unchanged, 0 unresolved structural placement issues. Gate-B lexical omissions/extraction exceptions are preserved for Gate C audit; do not reopen Gate B for source correction.

# Exact next activity — சங்கத் தமிழ்

The Tamil archival workflow is closed. Continue only the separately scoped maintained-English layer.

1. fetch live `main`;
2. read `works/sangatamil/translations/en/TRANSLATION_GUIDE.md`, `GLOSSARY.md`, `TRANSLATION_STATUS.md`, `SOURCE_CHECK_SC1_REPORT.md` through `SOURCE_CHECK_SC14_REPORT.md`, `GLOSSARY_RECONCILIATION_GR1_REPORT.md` through `GLOSSARY_RECONCILIATION_GR14_REPORT.md`, `EDITORIAL_REVIEW_ER1_REPORT.md`, `EDITORIAL_REVIEW_ER2_REPORT.md`, `EDITORIAL_REVIEW_ER3_REPORT.md`, `EDITORIAL_REVIEW_ER4_REPORT.md`, `EDITORIAL_REVIEW_ER5_REPORT.md`, `EDITORIAL_REVIEW_ER6_REPORT.md`, `EDITORIAL_REVIEW_ER7_REPORT.md`, `EDITORIAL_REVIEW_ER8_REPORT.md`, `EDITORIAL_REVIEW_ER9_REPORT.md`, `EDITORIAL_REVIEW_ER10_REPORT.md`, `EDITORIAL_REVIEW_ER11_REPORT.md`, `EDITORIAL_REVIEW_ER12_REPORT.md`, `EDITORIAL_REVIEW_ER13_REPORT.md`, `EDITORIAL_REVIEW_ER14_REPORT.md`, and `reviews/WHOLE_VOLUME_ENGLISH_REVIEW.md`;
3. confirm first-pass drafting, source-check and glossary reconciliation are **COMPLETE / CLOSED 497/497**, ER1 scans **1–37**, ER2 scans **38–74**, ER3 scans **75–111**, ER4 scans **112–148**, ER5 scans **149–185**, ER6 scans **186–222**, ER7 scans **223–259**, ER8 scans **260–296**, ER9 scans **297–333**, ER10 scans **334–370**, ER11 scans **371–407**, ER12 scans **408–444**, ER13 scans **445–481**, and ER14 scans **482–497 are COMPLETE / PASS — editorial review COMPLETE / CLOSED 497/497**;
4. confirm ER14 exact page-layer compare is **1 commit / exactly 16 modified English page files / 0 canonical Tamil changes / 16 status promotions**, with **8 source-faithful editorial refinements**;
5. read `works/sangatamil/translations/en/reviews/WHOLE_VOLUME_ENGLISH_REVIEW.md` and confirm the whole-volume / section-level review is **PASS / CLOSED**;
6. create `works/sangatamil/translations/en/reviews/WHOLE_VOLUME_ENGLISH_RELEASE_REPORT.md` for the active release unit scans **1–497**;
7. decide release approval using the closed English review state; preserve scan 8 as permanent `source-limited` and treat only the **496 `editorial-reviewed`** pages as eligible for promotion;
8. if and only if the release report approves release, promote eligible pages `editorial-reviewed` → `release-ready` by status-token-only changes with **0 approved English wording changes**;
9. change **0 canonical Tamil page files**, preserve `translation_type: "project_translation"`, and audit the exact promotion change-set before final synchronization.

Whole-volume word-for-word Tamil scan verification remains **NOT CLAIMED**. English workflow progress must not be interpreted as a Tamil status promotion.

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
- Pass 2A Batch 10 / final remainder — **544–555 / printed 527–538 — COMPLETE 12/12**;
- cumulative Pass 2A — **111/111 COMPLETE / PASS**;
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
- Batch-10 source-supported corrections — **6 records / 15 textual-or-punctuation readings**: scans **544, 545, 546, 549, 551, 552**;
- Batch-10 correction commit — `5be125724c549d4b1c82020ab5fb5bf0e01fc4b8` — exact compare **6 page files only / scans 544, 545, 546, 549, 551, 552**;
- Pass 2A — **COMPLETE / PASS 111/111**;
- **555→556 — CLEAN**, source-resolved from Part 005/006 intake;
- all 111 records remain `needs-review` / visual `needs-review`;
- durable Pass-2A log — `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_005.md`;
- Pass 2B Batch 1 — **445–455 / printed 428–438 — COMPLETE 11/11**;
- Pass 2B Batch 2 — **456–466 / printed 439–449 — COMPLETE 11/11**;
- Pass 2B Batch 3 — **467–477 / printed 450–460 — COMPLETE 11/11**;
- Pass 2B Batch 4 — **478–488 / printed 461–471 — COMPLETE 11/11**;
- Pass 2B Batch 5 — **489–499 / printed 472–482 — COMPLETE 11/11**;
- Pass 2B Batch 6 — **500–510 / printed 483–493 — COMPLETE 11/11**;
- Pass 2B Batch 7 — **511–521 / printed 494–504 — COMPLETE 11/11**;
- Pass 2B Batch 8 — **522–532 / printed 505–515 — COMPLETE 11/11**;
- Pass 2B Batch 9 — **533–543 / printed 516–526 — COMPLETE 11/11**;
- Pass 2B Batch 10 / final remainder — **544–555 / printed 527–538 — COMPLETE 12/12**;
- cumulative Pass 2B — **111/111 COMPLETE / PASS**;
- Batch-1 Pass-2B correction — **1 record / 1 lexical reading**: scan 453 `முத்தனியின்` → source-visible `முக்கனியின்`;
- Batch-1 Pass-2B correction commit — `8391075c43b72ec3e5973db080ba742e5e899c4b` — exact compare **1 page file only / scan 453**;
- **455→456 — GENUINE CONTINUATION**, confirmed from scan 456 / printed 439 witness;
- Batch-2 Pass-2B corrections — **3 records / 4 lexical-or-spacing readings**: scan 457 `இளங்கவிஞன்` → `இளங் கவிஞன்`; scan 463 `காட்டிக்கொண்டிருக்கிறோம்` → `காட்டிக் கொண்டிருக்கிறோம்`; scan 465 `கடுமையானச்` → `கடுமையாகச்`, `முயற்சிகளுண்டே` → `முயற்சிகள் உண்டே`;
- Batch-2 Pass-2B correction commit — `665a2691e0e1cdfcff740adb48a65783976b8adf` — exact compare **3 page files only / scans 457, 463, 465**;
- **466→467 — GENUINE CONTINUATION**, confirmed from scan 467 / printed 450 witness;
- Batch-3 Pass-2B corrections — **2 records / 2 source-visible joining readings**: scan 469 `சேர்ந்து கொண்டு` → `சேர்ந்துகொண்டு`; scan 477 `செய்து கொள்ள` → `செய்துகொள்ள`;
- Batch-3 Pass-2B correction commit — `c7228edbf258e2d15b3949df61fe364e9cada5e4` — exact compare **2 page files only / scans 469, 477**;
- **477→478 — CLEAN**, confirmed from scan 478 / printed 461 witness;
- Batch-4 Pass-2B corrections — **4 records / 9 lexical-or-spacing/punctuation readings**: scan 482 `களிச் நிலத்தின்` → `கரிசல் நிலத்தின்`; scan 485 `பரணியாக்கு` → `பரணியாக்குக`; scan 486 `நானாயிரம்` → `நாலாயிரம்` twice, `ஆண்டுக்கு` → `ஆண்டுகட்கு`, `செம்மொழி - தமிழ்மொழி` → `செம்மொழி-தமிழ்மொழி`, quote closure corrected at `தமிழ்க் குடி’யன்றோ!`, and `உடனடைப் பதுக்கியவாறும்` → `உதட்டைப் பிதுக்கியவாறும்`; scan 488 `தாபத்தைக்` → `தாபத்தைத்`;
- Batch-4 Pass-2B correction commit — `81456d09f7745a0834c3edc2170281945b91f478` — exact compare **4 page files only / scans 482, 485, 486, 488**;
- **488→489 — CLEAN**, confirmed from scan 489 / printed 472 witness;
- Batch-5 Pass-2B corrections — **5 records / 9 lexical-or-spacing/punctuation readings**: scan 490 `பொருள்களுடன்` → `பொருள் களுடன்`, `திமிரென` → `திடீரென`; scan 492 `மடியில்` → `மடியினில்`, `புரியவில்லை?”` → `புரியவில்லை!”`, `பிரிவெண்ணும்` → `பிரிவென்னும்`; scan 494 `முனைந்து` → `முயன்றது`, `பெருங்கோபத்தை` → `பெருங் கோபத்தை`; scan 496 `உடன்படவில்லை` → `உடன் படவில்லை`; scan 497 `பெருங்கயிறுகளாலும்` → `பெருங் கயிறுகளாலும்`;
- Batch-5 Pass-2B correction commit — `2c0b3b4ddff95c18c9312dbdffbc4ef2d41c2767` — exact compare **5 page files only / scans 490, 492, 494, 496, 497**;
- **499→500 — GENUINE CONTINUATION**, confirmed from scan 500 / printed 483 witness;
- Batch-6 Pass-2B corrections — **3 records / 6 lexical-or-spacing readings**: scan 500 `கனத்துக்கொண்டும்` → source-visible `கனைத்துக்கொண்டும்`; scan 506 `வாயடக்கமற்ற பிறவிகள்` → `வாயடக்கமற்றப் பிறவிகள்`; scan 510 `கனிவு` → `துணிவு`, `போதிலும் கூட` → `போதிலும்கூட`, and source gloss `சான்பு` → `சால்பு` twice;
- Batch-6 Pass-2B correction commit — `2cdd3c70ef34e61496d51e7996a2ade8d039e433` — exact compare **3 page files only / scans 500, 506, 510**;
- **510→511 — CLEAN**, confirmed from scan 511 / printed 494 witness;
- Batch-7 Pass-2B corrections — **3 records / 7 lexical-or-spacing readings**: scan 511 `பொற்பாவை` → source-visible `பொற்றாமரை`, `அந்த நாள்வரை` → `அந்நாள்வரை`, `எங்கினாள்` → `ஏங்கினாள்`; scan 512 second occurrence `போட்டுக்கொண்டு` → source-visible `போட்டுக் கொண்டு`, `உன் காதலனை` → `உன்காதலனை`, `வெண்ணெயை` → `வெண்ணெய்யை`; scan 519 source gloss `அஞ்சத்தக்கது` → `அஞ்சிட தக்கது`;
- Batch-7 Pass-2B correction commit — `ff38ae5c02ec44026482f8db9702d76e8eb424b1` — exact compare **3 page files only / scans 511, 512, 519**;
- **521→522 — CLEAN**, confirmed from scan 522 / printed 505 witness;
- Batch-8 Pass-2B corrections — **7 records / 12 lexical-or-spacing/punctuation readings**: scan 522 `ஒருவனைத்` → source-visible `ஒருவனைக்`; scan 523 `போரைக் தொடர்ந்து` → `போரைத் தொடர்ந்து`; scan 527 `எழுதிய தந்ததை` → `எழுதித் தந்ததை`; scan 528 queen-speech clause restored to source-visible `பயன்படுத்தினால்கூட, அந்தச் சொற்கள் காதைக் குடையும் நிலையிலே பாய்ந்தால் கூட அதைப் பொறுத்துக்கொள்கிற`; scan 529 `ஆயிரம்` → `ஆயன்`; scan 530 `எங்கிடும்` → `ஏங்கிடும்`, `நங்கினாலும்` → `நீங்கினாலும்`; scan 532 source punctuation restored at `புயல்காற்று - இவற்றினைக்` and `அதற்கு இது குறள்:-`;
- Batch-8 Pass-2B correction commit — `4af1b155dad0a81c5bd7fe68cd64569801a3718f` — exact compare **7 page files only / scans 522, 523, 527, 528, 529, 530, 532**;
- **532→533 — CLEAN**, confirmed from scan 533 / printed 516 witness;
- Batch-9 Pass-2B corrections — **3 records / 3 lexical-or-spacing readings**: scan 534 `அதைத் தவிர மற்ற அனைத்தையும்` → source-visible `அனைத்தையும்`; scan 538 `ஊற்றப்பட்ட` → source-visible `ஊற்றப் பட்ட`; scan 541 `இப்படிப்பார்க்கிறது` → source-visible `இப்பப்பார்க்கிறது`;
- Batch-9 Pass-2B correction commit — `909260dc502bb4ddeaa0defd5cb25692adf38653` — exact compare **3 page files only / scans 534, 538, 541**;
- **543→544 — GENUINE CONTINUATION**, confirmed from scan 544 / printed 527 witness;
- Batch-10 Pass-2B corrections — **3 records / 3 lexical-or-punctuation readings**: scan 544 `வீட்டு வாயில்` → `வீட்டு வாயிலில்`; scan 545 `உயிர் நீப்பார் மானம்` → `உயிர் நீப்பர் மானம்`; scan 549 `சென்றாள். ஊக்கமுடன்` → `சென்றாள், ஊக்கமுடன்`;
- Batch-10 Pass-2B correction commit — `892d3273ddf04f6b1a0364d0b77e9e4eb58d0c93` — exact compare **3 page files only / scans 544, 545, 549**;
- Pass 2B — **COMPLETE / PASS 111/111**;
- cumulative Pass-2B corrections — **34 page records / 56 source-supported readings**;
- **555→556 — CLEAN / source-resolved**;
- durable Pass-2B log — `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_005.md`;
- Pass 3 Batch 1 — **445–455 / printed 428–438 — COMPLETE 11/11**;
- Pass 3 Batch 2 — **456–466 / printed 439–449 — COMPLETE 11/11**;
- Pass 3 Batch 3 — **467–477 / printed 450–460 — COMPLETE 11/11**;
- Pass 3 Batch 4 — **478–489 / printed 461–472 — COMPLETE 12/12**;
- Pass 3 Batch 5 — **490–501 / printed 473–484 — COMPLETE 12/12**;
- Pass 3 Batch 6 — **502–526 / printed 485–509 — COMPLETE 25/25**;
- Pass 3 Batch 7 / final remainder — **527–555 / printed 510–538 — COMPLETE 29/29**;
- user-directed final-iteration override — **process all remaining 29 pages in one iteration**;
- Pass-3 structural/visual corrections — **6 pages / scans 472, 474, 481, 501, 531, 537**;
- Pass-3 Batch-7 corrections — **2 visual-note-only pages / scans 531, 537**;
- Pass-3 lexical/body-text changes — **0**;
- Batch-7 Pass-3 page correction commit — `558256c0624f32b3aee9479aebb70a734eab3118` — exact compare **2 page files only / scans 531, 537**;
- **455→456 — GENUINE CONTINUATION**, preserved;
- **466→467 — GENUINE CONTINUATION**, preserved;
- **477→478 — CLEAN**, preserved;
- **489→490 — GENUINE CONTINUATION**, preserved;
- **501→502 — GENUINE CONTINUATION**, preserved;
- **526→527 — CLEAN**, preserved;
- **555→556 — CLEAN / source-resolved**, preserved;
- Pass 3 — **COMPLETE / PASS 111/111**;
- durable Pass-3 log — `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_005.md`;
- Part 005 audit — **PASS / COMPLETE**;
- direct header inventory — **111/111 canonical records present**, scan 445–555 / local 1–111 / printed 428–538, with **0 gaps / 0 duplicates / 0 mapping anomalies**;
- source filename discipline — **111/111 exact controlling source filename**;
- final metadata/status synchronization — **PASS / CLOSED**;
- final Tamil textual status — **111 verified / 0 needs-review / 0 partial / 0 blocked / 0 source-limited**;
- final visual fidelity — **111 verified / 0 needs-review**;
- metadata-only promotion changed exactly **111 Part-005 page files**, each **+2/-2**, and no non-page file;
- durable audit — `works/kuraloviyam/PART_005_AUDIT.md`;
- durable final-status record — `works/kuraloviyam/PART_005_FINAL_STATUS_SYNC.md`;
- documentation synchronization — **COMPLETE / PASS**;
- documentation-only sync changed **0 page records**;
- durable documentation-sync record — `works/kuraloviyam/PART_005_DOCUMENTATION_SYNC.md`;
- Tamil archival-ready checkpoint — **PASS / CLOSED**;
- Part 005 Tamil — **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**;
- durable Tamil archival-ready record — `works/kuraloviyam/PART_005_TAMIL_ARCHIVAL_READY.md`;
- Part 005 English Draft D1 — **445–477 / printed 428–460 — COMPLETE 33/33**;
- cumulative Part-005 English drafting — **33/111 draft records created; 78 remaining**;
- D1 page commits — `5fc371a40987a0d837c42add97eba4297ca390e7`, `247e027157f9f2a2772ba3e024facfd8b1b13532`, `47ab95e0005abdb59ff7b49920ede25399cc08ce`;
- exact D1 compare from Tamil archival checkpoint `6277f88bfb7eabf1ed541fbe6b8b48cf55c34622` to D1 endpoint `47ab95e0005abdb59ff7b49920ede25399cc08ce` — **3 commits ahead / exactly 33 added English page files / 0 Tamil or control-file changes**;
- English Draft D2 — **478–510 / printed 461–493 — COMPLETE 33/33**;
- cumulative Part-005 English drafting — **66/111 draft records created; 45 remaining**;
- D2 page commits — `fb636ec87218a80927b8a8ca652ea252ab4ddc67`, `969dfd9139045b1e6d21cd8adce29dcb94360fc0`, `944813bb74d3fc344757a7eedf5f18d9d427c8fe`;
- exact D2 compare from `9ce71687265347c7646e9d605760e6b74202dae6` to `944813bb74d3fc344757a7eedf5f18d9d427c8fe` — **3 commits ahead / exactly 33 added English page files / 0 Tamil or control-file changes**;
- English Draft D3 — **511–543 / printed 494–526 — COMPLETE 33/33**;
- cumulative Part-005 English drafting — **99/111 draft records created; 12 remaining**;
- D3 page commits — `331d6e41e8155457f8bcea18e101eb5f1fe13e6f`, `6d5388ec95a14e552c348cecfb73fab440f8f135`, `eb8d8695df77bfc82bace2de775431ed9dd6b5e3`;
- exact D3 compare from `f5adde228fbc2a3af2123016f75e0aab8ba9f120` to `eb8d8695df77bfc82bace2de775431ed9dd6b5e3` — **3 commits ahead / exactly 33 added English page files / 0 Tamil or control-file changes**;
- English Draft D4 final remainder — **544–555 / printed 527–538 — COMPLETE 12/12**;
- Part-005 English first-pass drafting — **COMPLETE / CLOSED 111/111**;
- D4 page commit — `4d8a8d1b8e81c3827498e31a00b055b660b143d8`;
- exact D4 compare from `e077442534771d61efcc5ed31f7875b73ea65783` to `4d8a8d1b8e81c3827498e31a00b055b660b143d8` — **1 commit ahead / exactly 12 added English page files / 0 Tamil or control-file changes**;
- final drafting state — **111 draft / 0 source-checked / 0 editorial-reviewed / 0 release-ready / 0 source-limited / 0 blocked**;
- Part-005 English inventory — **111/111 present / 0 undrafted**;
- English source-check SC1 — **445–477 / printed 428–460 — COMPLETE / PASS 33/33**;
- SC1 page commits — `21e43aa606bca9101d681bd55157dd1db42f2af8`, `902d567aaf24e6018200a6a88755230a44713f67`, `d62e97d1f67ed999fb6f4a0db435cedccdbc4c2d`;
- exact SC1 compare from `9bed25feeab25329fb1b2cf10c41f9fddbfc5290` to `d62e97d1f67ed999fb6f4a0db435cedccdbc4c2d` — **3 commits ahead / exactly 33 modified English page files / 0 Tamil or control-file changes**;
- SC1 source-fidelity correction — **2 page files / scans 476–477**, restoring the audited Tamil physical-page split after `மணம்`; remaining **31 pages status-only**;
- English source-check SC2 — **478–510 / printed 461–493 — COMPLETE / PASS 33/33**;
- SC2 page commits — `9abb1163eea2313136bd8440ff34cd1e76a13db3`, `45ea10e2d0d908324331cad34f09ff5368b60eca`, `74f41ce00e29bd8ba448c790bfb6bfc46d9d1b72`;
- exact SC2 compare from `65f823bea48d4e5c1b52832877aa49349dfc7347` to `74f41ce00e29bd8ba448c790bfb6bfc46d9d1b72` — **3 commits ahead / exactly 33 modified English page files / 0 Tamil or control-file changes**;
- SC2 source-fidelity corrections — **3 page files / scans 492, 501, 502**:
  - scan 492 Kural line changed from “when love is restrained” to **“when love causes suffering”**, matching the audited Tamil source gloss `அடுங்கால் = வருத்தும்போது`;
  - scans 501–502 restored the audited physical-page sentence split and removed duplicated continuation wording;
- remaining **30 SC2 pages status-only**;
- English source-check SC3 — **511–543 / printed 494–526 — COMPLETE / PASS 33/33**;
- SC3 page commits — `9a4ae8f6605abbeb717295d992121da65ad30055`, `aadd749072ae55fe6107ff59e7a51657d903b868`, `fa2ca8b07844e56be4d3a3dfc926a7874b136ca1`;
- exact SC3 compare from `8a5f217bdad19321ce4bf51e0589ef2ec1277ea6` to `fa2ca8b07844e56be4d3a3dfc926a7874b136ca1` — **3 commits ahead / exactly 33 modified English page files / 0 Tamil or control-file changes**;
- SC3 source-fidelity corrections — **8 page files / scans 511, 512, 518, 519, 525, 533, 534, 537**:
  - scans 511–512 restore the audited physical-page split in the missing-goat dialogue;
  - scans 518–519 restore the audited physical-page split and the omitted revenge-drive qualifier;
  - scan 525 removes narration that belonged to scan 526;
  - scan 533 restores the source fragrance list **sandalwood / javvadu perfume / civet**;
  - scan 534 removes an unsupported hedge and restores the source's direct assertion;
  - scan 537 restores source referent **Kannan** instead of the inferred generic “her husband”;
- remaining **25 SC3 pages status-only**;
- English source-check SC4 final remainder — **544–555 / printed 527–538 — COMPLETE / PASS 12/12**;
- SC4 page commits — `6a275273a2eb05ddedbf637e95fff9c03e8254a5`, `1f14dec997d70c3ee13fe16f1560c1c58dd0c185`, `113846a357544a33b73d727d20115471f2f3411f`;
- exact SC4 compare from `c67e24794f25899f2a38c99dc1fc03af562240b3` to `113846a357544a33b73d727d20115471f2f3411f` — **3 commits ahead / exactly 12 modified English page files / 0 Tamil or control-file changes**;
- SC4 source-fidelity corrections — **4 page files / scans 549, 550, 553, 555**:
  - scans 549–550 restored the audited physical-page split in the education / daughter vignette;
  - scan 553 narrowed the source gloss `அலர் = பலர் அறிதல்` to **becoming known to many**, removing the added “gossip” gloss;
  - scan 555 restored the source-named **narambu-silandhi disease** and the explicit “kill little by little” force;
- remaining **8 SC4 pages status-only**;
- Part-005 English source-check — **COMPLETE / CLOSED 111/111**;
- English glossary reconciliation GR1 — **445–477 / printed 428–460 — COMPLETE / PASS 33/33**;
- GR1 commit — `fcbea72faefca6e521f1334e10363a7f0d13894b`;
- exact GR1 compare from `2294dbd8fb1c6b0f3ef49c09dee984e949bdfc3a` to `fcbea72faefca6e521f1334e10363a7f0d13894b` — **1 commit ahead / 2 modified files: GLOSSARY.md + English scan 445 / 0 Tamil changes / 0 status changes**;
- GR1 terminology correction — **scan 445 only**, source gloss `ஆகுல நீர = ஆரவாரத் தன்மை` reconciled from **clamorous display** to **clamorous nature**;
- English glossary reconciliation GR2 — **478–510 / printed 461–493 — COMPLETE / PASS 33/33**;
- GR2 commit — `3aa3b525e4c8f2335227e36a91aed43ed117d471`;
- exact GR2 compare from `2861c0b6058fed0c42f96b18c66114414911f5e5` to `3aa3b525e4c8f2335227e36a91aed43ed117d471` — **1 commit ahead / 5 modified files: GLOSSARY.md + English scans 479, 480, 494, 510 / 0 Tamil changes / 0 status changes**;
- GR2 terminology corrections — **4 page files / scans 479, 480, 494, 510**: `Anbaananthan` → **Anbanandan** on 479–480; Chapter 41 **Ignorance → Lack of Learning** on 494; scan 510 **cosmic age → oozhi** plus source-gloss restoration for `சான்றாண்மை`;
- English glossary reconciliation GR3 — **511–543 / printed 494–526 — COMPLETE / PASS 33/33**;
- GR3 page-correction commit — `538f8d1f948d95bd3d4618b70a8b061abd14e7bd`;
- GR3 endpoint — `736f1f14d167497798a6dba51a2fa44f0c8bd952`;
- exact GR3 compare from `3f1b63262d0bb56359856f2d39e7d9b6904ce80d` to `736f1f14d167497798a6dba51a2fa44f0c8bd952` — **2 commits ahead / 7 modified files: GLOSSARY.md + English scans 519, 521, 532, 534, 540, 542 / 0 Tamil changes / 0 status changes**;
- English glossary reconciliation GR4 final remainder — **544–555 / printed 527–538 — COMPLETE / PASS 12/12**;
- GR4 page-correction commit — `e08fc18fca5da8cebe2cc1106a40147fa7797f60`;
- GR4 endpoint — `a0eb5f0858f003106678b4f1a6ca4bb9ba6b0a05`;
- exact GR4 compare from `736f1f14d167497798a6dba51a2fa44f0c8bd952` to `a0eb5f0858f003106678b4f1a6ca4bb9ba6b0a05` — **2 commits ahead / 5 modified files: GLOSSARY.md + English scans 551, 553, 554, 555 / 0 Tamil changes / 0 status changes**;
- Part-005 English glossary reconciliation — **COMPLETE / CLOSED 111/111**;
- cumulative glossary reconciliation — **111/111 COMPLETE / CLOSED**;
- English editorial review ER1 — **445–477 / printed 428–460 — COMPLETE / PASS 33/33**;
- ER1 endpoint — `7e9c90a4109cd8a627d3d31bde74d226100c9aba`;
- exact ER1 compare from `8fd0069f235b69e31fb8c7cd4a6e80582e0cb305` to `7e9c90a4109cd8a627d3d31bde74d226100c9aba` — **6 commits ahead / exactly 33 modified English page files / 0 Tamil changes / 33 status promotions**;
- ER1 source-faithful readability refinements — **9 page files / scans 448, 457, 461, 465, 466, 468, 469, 472, 476**;
- English editorial review ER2 — **478–510 / printed 461–493 — COMPLETE / PASS 33/33**;
- ER2 endpoint — `ffd62952cf06cf2581768603e720c836996f6d5d`;
- exact ER2 compare from `a82aeaf53eeea125d2c60ba8b7a51e8dc486e9c8` to `ffd62952cf06cf2581768603e720c836996f6d5d` — **6 commits ahead / exactly 33 modified English page files / 0 Tamil changes / 33 status promotions**;
- ER2 source-faithful readability refinements — **12 page files / scans 478, 484, 490, 491, 493, 495, 496, 501, 503, 506, 507, 509**;
- English editorial review ER3 — **511–543 / printed 494–526 — COMPLETE / PASS 33/33**;
- ER3 endpoint — `048ceaad4cf6efc8dd7a4b293f4f63bfc3bf548d`;
- exact ER3 compare from `04a1ed0e556a4fed60795bc31216dd4c5c6d2b62` — **6 commits ahead / exactly 33 modified English page files / 0 Tamil changes / 33 status promotions**;
- ER3 source-faithful readability refinements — **19 page files / scans 512, 514, 516, 519, 522, 523, 525, 526, 528, 530, 531, 532, 534, 535, 536, 539, 540, 541, 542**;
- English editorial review ER4 final remainder — **544–555 / printed 527–538 — COMPLETE / PASS 12/12**;
- ER4 endpoint — `cde07e0d6a633cb66b7f42039cf9bdb82e2af12d`;
- exact ER4 compare from `048ceaad4cf6efc8dd7a4b293f4f63bfc3bf548d` — **2 commits ahead / exactly 12 modified English page files / 0 Tamil changes / 12 status promotions**;
- ER4 source-faithful readability refinements — **6 page files / scans 547, 550, 551, 552, 553, 554**;
- Part-005 English editorial review — **COMPLETE / CLOSED 111/111**;
- Part-005 Part-level English review — **PASS / CLOSED**;
- review record — `works/kuraloviyam/translations/en/reviews/PART_005_ENGLISH_REVIEW.md`;
- review base — `fdd71835084121e9f80cf812e5dd29dac7dd148d`;
- direct Part inventory/frontmatter audit — **111/111 English present and aligned / 111 editorial-reviewed / 111 source_tamil_status verified / 111 project_translation / 0 page-layer changes**;
- Chapter/Kural audit — **54 metadata pages / 55 Kural citations / 0 Chapter-Kural mismatches**;
- visual-material audit — **53 English visual sections / PASS**;
- Part-005 English release report — **APPROVED / CLOSED**;
- release report — `works/kuraloviyam/translations/en/reviews/PART_005_ENGLISH_RELEASE_REPORT.md`;
- release promotion base — `af50dbf8b6ab54e456d87b10cfdcd094e6d3a516`;
- release promotion endpoint — `3d35d4c67f17f77b8ff5de036a8a3989ec088a78`;
- exact promotion audit — **19 commits ahead / exactly 111 English page files / +1,-1 each / 0 non-page files / status-token-only**;
- current Part-005 English state — **0 source-checked / 0 draft / 0 editorial-reviewed / 111 release-ready / 0 source-limited / 0 blocked**;
- final Part-005 checkpoint — **PASS / CLOSED**;
- durable final closure — `works/kuraloviyam/PART_005_FINAL_CLOSURE.md`;
- Part 005 — **TAMIL + MAINTAINED ENGLISH FULLY CLOSED**.

### Part 006 — TAMIL CLOSED / ENGLISH GLOSSARY RECONCILIATION ACTIVE

- source intake — **PASS / COMPLETE**;
- scans — **556–666**;
- physical source endpoint — **scan 666**;
- Tamil Pass 1 — **COMPLETE 111/111**;
- P6-01 through P6-09 — **556–654 / printed 539–637 — COMPLETE**;
- P6-10 — **655–665 / printed 638–648 — COMPLETE 11/11**;
- final remainder — **666 / unnumbered pictorial back cover — COMPLETE 1/1**;
- final Pass-1 page commits — `8b6a5838b0fb02b3c5a8a64e9e5cc36a532c69c6`, `6f58cc1c4a12bcf06776507a42a47225d782cc2b`;
- exact final Pass-1 compare from `0935e9380db4aa406793db9a5f261354831466c7` — **2 commits / exactly 12 added Part 006 Tamil page files / 0 non-page changes**;
- scans **658–665** — `பொருளடக்கம்` backmatter;
- scan **666** — physical source endpoint / no external continuation;
- all **111** records remain `needs-review` / visual `needs-review`;
- Pass 2A Batch 1 — **556–566 / printed 539–549 — COMPLETE 11/11**;
- Pass 2A Batch 2 — **567–577 / printed 550–560 — COMPLETE 11/11**;
- Pass 2A Batch 3 — **578–588 / printed 561–571 — COMPLETE 11/11**;
- Pass 2A Batch 4 — **589–599 / printed 572–582 — COMPLETE 11/11**;
- Pass 2A Batch 5 — **600–610 / printed 583–593 — COMPLETE 11/11**;
- Pass 2A Batch 6 — **611–621 / printed 594–604 — COMPLETE 11/11**;
- Pass 2A Batch 7 — **622–632 / printed 605–615 — COMPLETE 11/11**;
- Pass 2A Batch 8 — **633–643 / printed 616–626 — COMPLETE 11/11**;
- Pass 2A Batch 9 — **644–654 / printed 627–637 — COMPLETE 11/11**;
- Pass 2A Batch 10 — **655–665 / printed 638–648 — COMPLETE 11/11**;
- final Pass-2A remainder — **666 / unnumbered pictorial back cover — COMPLETE 1/1 / no textual correction**;
- Batch 10 correction endpoint — `a88d9e186f5956b0fa24abc49c7b7f7a50ca46b5`;
- exact Batch 10 compare from `84de610b844dd594c1b8c0d4a75737e7f472e6f4` — **7 commits / exactly 7 modified Part 006 page files / scans 656, 657, 658, 659, 660, 661, 665 / 0 non-page changes**;
- Pass 2A — **COMPLETE / PASS 111/111**;
- Pass 2B Batch 1 — **556–566 / printed 539–549 — COMPLETE 11/11**;
- Pass 2B Batch 2 — **567–577 / printed 550–560 — COMPLETE 11/11**;
- Pass 2B Batch 3 — **578–588 / printed 561–571 — COMPLETE 11/11**;
- Pass 2B Batch 4 — **589–599 / printed 572–582 — COMPLETE 11/11**;
- Pass 2B Batch 5 — **600–610 / printed 583–593 — COMPLETE 11/11**;
- Pass 2B Batch 6 — **611–621 / printed 594–604 — COMPLETE 11/11**;
- Pass 2B Batch 7 — **622–632 / printed 605–615 — COMPLETE 11/11**;
- Pass 2B Batch 8 — **633–643 / printed 616–626 — COMPLETE 11/11**;
- Pass 2B Batch 9 — **644–654 / printed 627–637 — COMPLETE 11/11**;
- Pass 2B Batch 10 — **655–665 / printed 638–648 — COMPLETE 11/11**;
- Pass 2B final remainder — **666 / unnumbered pictorial back cover — COMPLETE 1/1 / no correction**;
- final-remainder exact compare — `9ad10d1f342e3313ce308bafe578d76a4ba06a54` → same commit — **identical / 0 commits / 0 changed files**;
- Pass 2B — **COMPLETE / PASS 111/111**;
- corrected Pass-2B page records — **23**;
- source endpoint — **665→666 CLEAN / PHYSICAL SOURCE ENDPOINT**;
- Pass 3 Batch 1 — **556–566 / printed 539–549 — COMPLETE 11/11**;
- Pass 3 Batch 2 — **567–577 / printed 550–560 — COMPLETE 11/11**;
- Pass 3 Batch 3 — **578–588 / printed 561–571 — COMPLETE 11/11**;
- Pass 3 Batch 4 — **589–599 / printed 572–582 — COMPLETE 11/11**;
- Pass 3 Batch 5 — **600–610 / printed 583–593 — COMPLETE 11/11**;
- Pass 3 Batch 6 — **611–621 / printed 594–604 — COMPLETE 11/11**;
- Pass 3 Batch 7 — **622–632 / printed 605–615 — COMPLETE 11/11**;
- Pass 3 Batch 8 — **633–643 / printed 616–626 — COMPLETE 11/11**;
- Pass 3 Batch 9 — **644–654 / printed 627–637 — COMPLETE 11/11**;
- Pass 3 Batch 10 — **655–665 / printed 638–648 — COMPLETE 11/11**;
- Pass 3 final remainder — **666 / unnumbered pictorial back cover — COMPLETE 1/1 / PASS**;
- final-remainder structural/visual corrections — **0**;
- final-remainder lexical/body-text changes — **0**;
- final-remainder page-layer compare — `c51b18d49513a78c26be806384875b0cf7ee9245` → same commit — **identical / 0 changed files**;
- Pass 3 structural/visual corrections overall — **2 page records / scans 611 and 631**;
- Pass 3 lexical/body-text changes overall — **0**;
- Pass 3 — **COMPLETE / PASS 111/111**;
- Part 006 audit — **PASS / COMPLETE**;
- audit record — `works/kuraloviyam/PART_006_AUDIT.md`;
- direct header audit — **111/111 canonical records / 0 gaps / 0 duplicates / 0 mapping anomalies**;
- page functions — **102 body-prose / 8 contents-index / 1 back-cover**;
- final metadata/status synchronization — **PASS / CLOSED**;
- status-sync record — `works/kuraloviyam/PART_006_FINAL_STATUS_SYNC.md`;
- status-sync base — `fec10c426518d8b5cb490db9bfab8b50f6d6a440`;
- page-layer endpoint — `6cdb3cdd18cc1ccf1b1f2071055e9a1fd7782db0`;
- exact compare — **11 commits / exactly 111 Part-006 page files / +2 -2 each / 0 non-page files**;
- final Part-006 Tamil status — **111 verified / 0 needs-review / 0 partial / 0 blocked / 0 source-limited**;
- final Part-006 visual fidelity — **111 verified / 0 needs-review**;
- documentation synchronization — **COMPLETE / PASS**;
- documentation-sync record — `works/kuraloviyam/PART_006_DOCUMENTATION_SYNC.md`;
- documentation-only page-layer changes — **0**;
- Tamil archival-ready checkpoint — **PASS / CLOSED**;
- archival-ready record — `works/kuraloviyam/PART_006_TAMIL_ARCHIVAL_READY.md`;
- Part 006 Tamil — **ARCHIVAL-READY / CLOSED — 111/111 textual verified + 111/111 visual verified / 0 exceptions**;
- Part-006 English inventory at Tamil closure — **0/111 page records**;
- current normal English batch size — **37 physical scans**;
- Draft D1 — **COMPLETE / PASS 37/37**;
- D1 range — **556–592 / printed 539–575**;
- D1 base → endpoint — `411fc0fdad71c2b94ef5c17f68dece42e744089d` → `8ca4baeb33a8a45d13df372dc97acc705c1398e3`;
- Draft D2 — **COMPLETE / PASS 37/37**;
- D2 range — **593–629 / printed 576–612**;
- D2 base → endpoint — `7961c8869685814e213b0a6e891b5da878b0c126` → `9c09dfe256eb72e75beccc4ff6ba0d8c87e922da`;
- D2 exact compare — **6 commits / exactly 37 new English page files / 0 non-page changes / 0 Tamil changes**;
- Draft D3 — **COMPLETE / PASS 37/37**;
- D3 range — **630–666 / printed 613–648 + unnumbered back cover**;
- D3 base → endpoint — `f88a79c563871669c96533c07d5d50f0f87d1e17` → `8a87fbe5cf0ee36858111f693805eb4ab64ad8b0`;
- D3 exact compare — **5 commits / exactly 37 new English page files / 0 non-page changes / 0 Tamil changes**;
- Part 006 English drafting — **COMPLETE / CLOSED 111/111**;
- English Source-Check SC1 — **COMPLETE / PASS 37/37**;
- English Source-Check SC2 — **COMPLETE / PASS 37/37**;
- English Source-Check SC3 — **COMPLETE / PASS 37/37**;
- SC3 base → endpoint — `ba1391558c55e0a2917af872b6fbc42c0af8f064` → `35f666f3ab3e904565c5c24deecbffc034133a39`;
- SC3 exact compare — **3 commits / exactly 37 modified English page files / 0 non-page changes / 0 Tamil changes**;
- SC3 source-fidelity/page-function repairs — **19 page files**;
- Part 006 English source-check — **COMPLETE / CLOSED 111/111**;
- English Glossary Reconciliation GR1 — **COMPLETE / PASS 37/37**;
- GR1 page-layer base → endpoint — `a230f74a9d027435a009cd3569dec70f5f907b9b` → `42d9df79adc7d4e2cf7f1ef42bbf3fa272fe60a4`;
- GR1 exact page compare — **1 commit / exactly 4 modified English page files / 0 non-page changes / 0 Tamil changes / 0 status changes**;
- GR1 terminology repairs — **scans 561–563 Alagan/Alagi; scan 579 Gandhi**;
- historical GR1 checkpoint state — **111 source-checked / 0 draft**;
- source endpoint handling — **658–665 contents exact / 666 pictorial back cover / 665→666 CLEAN / 666 no external continuation**;
- then-next stage at that historical checkpoint — **Part 006 English Glossary Reconciliation GR2 / scans 593–629 / printed 576–612 — 37 pages**.

## Kuraloviyam — FINAL MAINTAINED CLOSURE

The complete supplied `குறளோவியம்` six-Part source family is **CLOSED**.

Part 006 final state:

- scans **556–666**;
- Tamil — **ARCHIVAL-READY / CLOSED — 111/111 textual + visual verified**;
- English — **RELEASE COMPLETE / CLOSED — 111/111 release-ready**;
- durable Part review — `works/kuraloviyam/translations/en/reviews/PART_006_ENGLISH_REVIEW.md`;
- durable release report — `works/kuraloviyam/translations/en/reviews/PART_006_ENGLISH_RELEASE_REPORT.md`;
- final closure — `works/kuraloviyam/PART_006_FINAL_CLOSURE.md`;
- source endpoint — scan **666 / unnumbered pictorial back cover / no external continuation**.

Whole-work maintained disposition:

- physical scans — **1–666 complete**;
- Tamil — **662 verified + 4 partial/source-limited; 666/666 visual verified**;
- maintained English — **662 release-ready + 4 source-limited**;
- blocked — **0**;
- Parts **001–006** — all closed.

The four durable source limitations remain Part 001 scans **13, 14, 15, 19**.

## Kuraloviyam derived sections

The maintained archival/release workflow remains **fully closed**. A downstream navigation layer is now active under `works/kuraloviyam/sections/`.

S1 — **COMPLETE / PASS**:

- Book → Iyal → Adhikaram scaffold created;
- **120** source-evidenced Adhikaram files;
- exact contents entries **1–300** preserved;
- **0** Tamil/English page-layer changes.

## Kuraloviyam derived sections S2 — COMPLETE

The downstream section hierarchy is now:

**Book → Iyal → Adhikaram → Kuraloviyam contents entry**

S2 processed **300/300** source contents entries:
- **298 resolved**;
- **2 partial source metadata** — entries **46, 104**;
- **0 unresolved**;
- **121/133** source-evidenced Chapter numbers;
- **0** closed Tamil/English page-layer mutations.

## Kuraloviyam derived sections S3 — COMPLETE

The downstream navigation layer now includes **300/300 individual entry leaves**, machine-readable JSON/TSV indexes, Chapter-grouped navigation, and direct Adhikaram→entry links.

Closed Tamil/English page layers remain unchanged.

## Exact next activity — குறளோவியம்

**None required.**

Use `works/kuraloviyam/sections/entries/index.json` as the preferred structured input for any future website/search/API derivative.


# Sangath Tamil Gate F closure — 2026-09-16

- Gate F — **COMPLETE / PASS**
- F01–F20 — **497/497 scans**
- formal citation-provenance units — **115**
- standalone source-note-only provenance records — **4**
- unresolved provenance gaps — **0**
- canonical page-wording changes — **0**
- wording state — **Gemini-lexical-locked; not word-for-word scan verified**
- Historical checkpoint note — C2 had not yet been opened when Gate F closed; this is superseded by the current C2 state below.
- physical provenance endpoint — **scan 497 / back cover**
- Historical Gate-F next activity was Gate G; this is superseded by the current C2 state below.


# Sangath Tamil Gate G closure / Gate H handoff — 2026-09-16

- Gate C2 — **COMPLETE / APPLIED**
- C2 disposition coverage — **497/497 scans**
- historical Gate-C discrepancy records adjudicated — **140/140**
- C2-locked remainder — **0**
- whole-volume word-for-word scan verification — **NOT CLAIMED**
- post-C2 reconciliation R1 — **COMPLETE / PASS**
- R1 durable record — `works/sangatamil/POST_C2_RECONCILIATION.md`
- Gate G — **COMPLETE / PASS**
- Gate-G canonical records audited — **497/497**
- Gate-G missing-field repairs — **11 `visual_fidelity` fields**
- Gate-G unresolved inconsistencies — **0**
- Gate-G canonical wording changes — **0**
- Gate-G durable report — `works/sangatamil/GATE_G_METADATA_STATUS_AUDIT.md`
- Gate-G page-layer endpoint — `fd024e4c0b1d3f21a3849c360d509350ce808db5`
- Gate H — **COMPLETE / PASS — derived navigation built**
- Gate I — **COMPLETE / PASS — final closure**
- current state — **CLOSED / no pending archival gate**

