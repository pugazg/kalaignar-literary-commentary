# NEXT CHAT PROMPT — சங்கத் தமிழ் / RE-AUDIT R10 scans 91–100

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Active workflow

Tamil word-for-word / historical-glyph re-audit has been **restarted from scan 1 in 10-page iterations**.

R01 scans **1–10 — COMPLETE / PASS**.  
R02 scans **11–20 — COMPLETE / PASS**.  
R03 scans **21–30 — COMPLETE / PASS WITH LEXICAL HOLDS**.  
R04 scans **31–40 — COMPLETE / PASS**.  
R05 scans **41–50 — COMPLETE / PASS WITH LEXICAL HOLD**.  
R06 scans **51–60 — COMPLETE / PASS WITH LEXICAL HOLD**.  
R07 scans **61–70 — COMPLETE / PASS WITH LEXICAL HOLDS**.  
R08 scans **71–80 — COMPLETE / PASS**.  
R09 scans **81–90 — COMPLETE / PASS WITH LEXICAL HOLDS**.

**Exact next range: R10 scans 91–100.**

Use:

`TVA_BOK_0042551_சங்கத்_தமிழ்_part_002_pages_51-100.pdf`

## Read first — mandatory

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R08_SCANS_071_080.md`
3. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R09_SCANS_081_090.md`
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

1. keep current canonical wording unchanged;
2. record/reconfirm the difference in `LEXICAL_DISCREPANCY_LEDGER.md`;
3. keep/reopen the page as `needs-review` when unresolved;
4. wait for explicit user adjudication before lexical mutation.

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

## Durable state through R09

### Current confirmed unresolved holds — DO NOT CHANGE

- **WFV-002 / scan 62** — token-placement discrepancy for `தனது`
- **WFV-003 / scan 69** — `தலைமகனாம் என் கணவர்` vs source `தலைமகனும் என் கணவர்`
- **WFV-004 / scan 83** — `மாலையாவதில்ல - ஆழல்` vs source `மாலையாவதில்ல - ஆனால்`
- **WFV-006 / scan 25** — `பெற்றவனோ?` vs source `பெற்றவனே?`
- **WFV-007 / scan 30 quotation** — `ஆள்அன்று` vs source `ஆளன்று`
- **WFV-008 / scan 30 gloss** — `ஆள்அன்று` vs source `ஆளன்று`
- **WFV-009 / scan 49** — `திண்டோர்` vs source `திண்டேர்`
- **WFV-010 / scan 55** — `கூடிற்றாம்!` vs source `கூடிற்றும்!`
- **WFV-011 / scan 67** — `தேர்ஏறி!` vs source `தேரேறி!`
- **WFV-012 / scan 85** — source-visible `- அவர்கள்` missing from canonical
- **WFV-013 / scan 87** — source places `நல்ல` with the `அகில், மிளகு, முத்து` trade line; canonical places it before `இலக்கிய மேதைகள்`

### R09

- scans **81–90** — COMPLETE / PASS WITH LEXICAL HOLDS
- WFV-004 — reconfirmed
- new rows — WFV-012, WFV-013
- canonical lexical substitutions — **0**
- source-supported non-lexical body corrections — **1** (scan 88 punctuation)
- page-status promotions — **7**
- current Tamil state — **79 verified / 417 needs-review / 1 partial**
- current visual state — **79 verified / 418 needs-review**

## R10 pre-existing candidate — MUST RECONFIRM, NOT APPLY

R10 contains earlier interrupted-cadence candidate:

- **WFV-005 / scan 91 / printed 76**
  - canonical: `வாராத காரணம்தான்`
  - earlier source observation: `வராத காரணம்தான்`
  - status before R10: **PENDING RECONFIRMATION — do not change word**

Reinspect scan 91 at enlarged/native resolution. If confirmed, update the existing WFV-005 disposition to R10 confirmed / pending user adjudication. **Do not alter canonical wording automatically.**

## R10 exact activity — scans 91–100

Process exactly **10 physical scans: 91–100** from Part002.

For each page:

1. compare canonical Tamil word-for-word against the source scan;
2. inspect at enlarged/native resolution;
3. apply the historical-glyph checklist;
4. preserve prior explicit C2 rulings in scans 91–100;
5. reconfirm WFV-005 when scan 91 is reached;
6. record any additional lexical/glyph difference in the ledger;
7. **change 0 lexical words without explicit user adjudication**;
8. apply only source-supported non-lexical structure/punctuation/layout corrections;
9. promote clean fully audited pages to `verified` / visual `verified` where appropriate;
10. unresolved lexical pages stay `needs-review`;
11. do not alter the confirmed holds listed above.

At R10 close create:

`works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R10_SCANS_091_100.md`

Then synchronize:

- `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
- `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
- `works/sangatamil/README.md`
- root `HANDOVER.md`
- `works/sangatamil/indexes/page-map.md` if statuses change
- `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
- **`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`**

The English release-report gate stays paused.

After R10, exact next range becomes **R11 scans 101–110**, using Part003.
