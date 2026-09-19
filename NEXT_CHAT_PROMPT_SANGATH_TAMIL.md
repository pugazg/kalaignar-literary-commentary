# NEXT CHAT PROMPT — சங்கத் தமிழ் / RE-AUDIT R06 scans 51–60

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Active workflow

Tamil word-for-word / historical-glyph re-audit has been **restarted from scan 1 in 10-page iterations**.

R01 scans **1–10 — COMPLETE / PASS**.  
R02 scans **11–20 — COMPLETE / PASS**.  
R03 scans **21–30 — COMPLETE / PASS WITH LEXICAL HOLDS**.  
R04 scans **31–40 — COMPLETE / PASS**.  
R05 scans **41–50 — COMPLETE / PASS WITH LEXICAL HOLD**.

**Exact next range: R06 scans 51–60.**

Use the already supplied:

`TVA_BOK_0042551_சங்கத்_தமிழ்_part_002_pages_51-100.pdf`

## Read first — mandatory

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R03_SCANS_021_030.md`
3. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R04_SCANS_031_040.md`
4. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R05_SCANS_041_050.md`
5. `works/sangatamil/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
6. `works/sangatamil/GEMINI_TEXT_LOCK.md`
7. `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
8. `works/sangatamil/C2_SOURCE_CORRECTION_PROGRESS.md`
9. `works/sangatamil/README.md`
10. root `HANDOVER.md`
11. `works/sangatamil/indexes/page-map.md`
12. `works/sangatamil/indexes/section-register.md`
13. `works/sangatamil/indexes/source-citation-register.md`

## Highest-priority lexical rule

> **Do not correct any words directly.**

For every source/Gemini word or character difference:

1. keep the current Gemini/canonical word unchanged;
2. record the difference in `LEXICAL_DISCREPANCY_LEDGER.md`;
3. keep/reopen the page as `needs-review` when unresolved;
4. wait for explicit user adjudication before any lexical mutation.

Earlier explicit C2 user adjudications remain controlling and must not be casually relitigated.

## Historical-glyph rule

For every printed page:

- inspect the whole page first;
- use enlarged/native pixels for difficult clusters;
- check the minimum set:
  `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- compare same-edition evidence when uncertain;
- distinguish character identity from expected modern spelling;
- OCR is not lexical authority;
- never global-replace.

Even strongly supported historical-glyph differences are **ledger-first**.

## Durable restart state through R05

### R03 unresolved holds — DO NOT CHANGE

- **WFV-006 / scan 25** — canonical `பெற்றவனோ?` vs source `பெற்றவனே?`
- **WFV-007 / scan 30 quotation** — canonical `ஆள்அன்று` vs source `ஆளன்று`
- **WFV-008 / scan 30 gloss** — canonical `ஆள்அன்று` vs source `ஆளன்று`

### R04

- scans **31–40** — COMPLETE / PASS
- new lexical discrepancies — **0**
- canonical lexical substitutions — **0**
- page-layer mutations — **0**

### R05

- scans **41–50** — COMPLETE / PASS WITH LEXICAL HOLD
- new lexical discrepancy rows — **1**: WFV-009
- scan **49** — canonical quotation `திண்டோர் நள்ளி கானத் தண்டர்`
- source-visible — `திண்டேர் நள்ளி கானத் தண்டர்`
- canonical lexical substitutions — **0**
- scan 49 remains `needs-review` / visual `needs-review`
- scan 47 prior C2 heading and `அப்படியொரு காகம் கரைந்திற்றாங்கே!` rulings preserved.

### Unresolved current holds — DO NOT CHANGE

WFV-006 through **WFV-009** remain pending explicit user adjudication.

Current Tamil state:

- `verified` — **46**
- `needs-review` — **450**
- `partial` — **1**

Current visual-fidelity state:

- `verified` — **46**
- `needs-review` — **451**

## Pre-restart Part002 candidate

WFV-002 on scan **62** remains an earlier ledger-only candidate and is **not** restart-confirmed yet. Do not mutate it during R06 because scan 62 belongs to R07 (61–70), not R06.

## R06 exact activity — scans 51–60

Process exactly **10 physical scans: 51–60** from Part002.

For each page:

1. compare canonical Tamil word-for-word against the source scan;
2. inspect at enlarged/native resolution;
3. apply the historical-glyph checklist;
4. preserve prior explicit C2 rulings;
5. record every newly confirmed lexical/glyph difference in the ledger;
6. **change 0 lexical words without explicit user adjudication**;
7. apply only source-supported non-lexical structure/punctuation/layout corrections;
8. mark clean fully audited pages `verified` / visual `verified` only when appropriate;
9. unresolved lexical pages remain `needs-review`;
10. do not alter WFV-006 through WFV-009.

At R06 close create:

`works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R06_SCANS_051_060.md`

Then synchronize:

- `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
- `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
- `works/sangatamil/README.md`
- root `HANDOVER.md`
- `works/sangatamil/indexes/page-map.md` if statuses change
- `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
- **`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`**

The English release-report gate stays paused.

After R06, exact next range becomes **R07 scans 61–70**.
