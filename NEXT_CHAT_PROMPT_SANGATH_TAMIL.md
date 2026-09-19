# NEXT CHAT PROMPT — சங்கத் தமிழ் / RE-AUDIT R07 scans 61–70

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Active workflow

Tamil word-for-word / historical-glyph re-audit has been **restarted from scan 1 in 10-page iterations**.

R01 scans **1–10 — COMPLETE / PASS**.  
R02 scans **11–20 — COMPLETE / PASS**.  
R03 scans **21–30 — COMPLETE / PASS WITH LEXICAL HOLDS**.  
R04 scans **31–40 — COMPLETE / PASS**.  
R05 scans **41–50 — COMPLETE / PASS WITH LEXICAL HOLD**.  
R06 scans **51–60 — COMPLETE / PASS WITH LEXICAL HOLD**.

**Exact next range: R07 scans 61–70.**

Use the already supplied:

`TVA_BOK_0042551_சங்கத்_தமிழ்_part_002_pages_51-100.pdf`

## Read first — mandatory

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R05_SCANS_041_050.md`
3. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R06_SCANS_051_060.md`
4. `works/sangatamil/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
5. `works/sangatamil/GEMINI_TEXT_LOCK.md`
6. `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
7. `works/sangatamil/C2_SOURCE_CORRECTION_PROGRESS.md`
8. `works/sangatamil/README.md`
9. root `HANDOVER.md`
10. `works/sangatamil/indexes/page-map.md`
11. `works/sangatamil/indexes/section-register.md`
12. `works/sangatamil/indexes/source-citation-register.md`

## Highest-priority lexical rule

> **Do not correct any words directly.**

For every source/Gemini word or character difference:

1. keep the current Gemini/canonical word unchanged;
2. record/reconfirm the difference in `LEXICAL_DISCREPANCY_LEDGER.md`;
3. keep/reopen the page as `needs-review` when unresolved;
4. wait for explicit user adjudication before any lexical mutation.

Earlier explicit C2 user adjudications remain controlling.

## Historical-glyph rule

For every printed page:

- inspect the whole page first;
- use enlarged/native pixels for difficult clusters;
- check:
  `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- compare same-edition evidence when uncertain;
- distinguish character identity from expected modern spelling;
- OCR is not lexical authority;
- never global-replace.

Even strongly supported glyph differences are **ledger-first**.

## Durable state through R06

### Current unresolved holds — DO NOT CHANGE

- **WFV-006 / scan 25** — canonical `பெற்றவனோ?` vs source `பெற்றவனே?`
- **WFV-007 / scan 30 quotation** — canonical `ஆள்அன்று` vs source `ஆளன்று`
- **WFV-008 / scan 30 gloss** — canonical `ஆள்அன்று` vs source `ஆளன்று`
- **WFV-009 / scan 49** — canonical `திண்டோர்` vs source `திண்டேர்`
- **WFV-010 / scan 55** — canonical `கூடிற்றாம்!` vs source `கூடிற்றும்!`

### R06

- scans **51–60** — COMPLETE / PASS WITH LEXICAL HOLD
- new lexical discrepancy rows — **1**: WFV-010
- canonical lexical substitutions — **0**
- source-supported non-lexical corrections — scans **51, 57**
- page-status promotions — **9**
- prior C2 rulings on scans **51, 53, 58, 59** preserved
- current Tamil state — **55 verified / 441 needs-review / 1 partial**
- current visual state — **55 verified / 442 needs-review**

## R07 pre-existing candidate rows — MUST RECONFIRM, NOT APPLY

R07 contains two earlier interrupted-cadence candidates:

- **WFV-002 / scan 62 / printed 47**  
  canonical proceeds from `படர்ந்துள்ள கொடியுதிர் மலர்களில்` to `பாதம் படுகின்ற...`  
  earlier source observation: intervening token `தனது`  
  status before R07: **PENDING RECONFIRMATION — do not add word**

- **WFV-003 / scan 69 / printed 54**  
  canonical: `தலைமகனாம் என் கணவர்`  
  earlier source observation: `தலைமகனும் என் கணவர்`  
  status before R07: **PENDING RECONFIRMATION — do not change word**

Reinspect both at native/enlarged resolution. If confirmed, update their ledger disposition to R07 confirmed / pending user adjudication; **do not modify canonical wording**.

## R07 exact activity — scans 61–70

Process exactly **10 physical scans: 61–70** from Part002.

For each page:

1. compare canonical Tamil word-for-word against the source scan;
2. inspect at enlarged/native resolution;
3. apply the historical-glyph checklist;
4. preserve prior explicit C2 rulings;
5. reconfirm WFV-002 and WFV-003 where reached;
6. record any additional lexical/glyph difference in the ledger;
7. **change 0 lexical words without explicit user adjudication**;
8. apply only source-supported non-lexical structure/punctuation/layout corrections;
9. promote clean fully audited pages to `verified` / visual `verified` where appropriate;
10. unresolved lexical pages stay `needs-review`;
11. do not alter WFV-006 through WFV-010.

At R07 close create:

`works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R07_SCANS_061_070.md`

Then synchronize:

- `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
- `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
- `works/sangatamil/README.md`
- root `HANDOVER.md`
- `works/sangatamil/indexes/page-map.md` if statuses change
- `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
- **`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`**

The English release-report gate stays paused.

After R07, exact next range becomes **R08 scans 71–80**.
