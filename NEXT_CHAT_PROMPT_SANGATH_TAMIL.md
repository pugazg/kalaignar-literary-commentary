# NEXT CHAT PROMPT — சங்கத் தமிழ் / 20-PAGE RE-AUDIT R22+R23 scans 211–230

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Active workflow

Tamil word-for-word / historical-glyph re-audit uses the user's fixed cadence:

> **20 physical scans per user iteration**

Keep durable audit reports in **10-scan R batches** inside each 20-page iteration.

R01 through R21 are complete through physical scan **210**.

Latest frontier:

- R18 scans **171–180 — COMPLETE / PASS WITH LEXICAL HOLDS**
- R19 scans **181–190 — COMPLETE / PASS WITH LEXICAL HOLDS**
- R20 scans **191–200 — COMPLETE / PASS WITH LEXICAL HOLDS**
- R21 scans **201–210 — COMPLETE / PASS WITH LEXICAL HOLDS**

**Exact next user iteration: R22 + R23 = scans 211–230.**

Use only the user's supplied controlling:

`TVA_BOK_0042551_சங்கத்_தமிழ்_part_005_pages_201-250.pdf`

Physical scans **211–230** correspond to Part005 PDF pages **11–30**. Do not substitute web copies.

## Read first — mandatory

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R20_SCANS_191_200.md`
3. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R21_SCANS_201_210.md`
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

For every source/Gemini word, character, omitted phrase, or materially meaningful token-placement difference:

1. keep current canonical wording/placement unchanged;
2. record the difference in `LEXICAL_DISCREPANCY_LEDGER.md` under the next live WFV ID;
3. keep/reopen the page as `needs-review`;
4. wait for explicit user adjudication before lexical mutation.

Earlier explicit C2 user adjudications remain controlling.

## Historical-glyph rule

For every printed page:

- inspect the whole page;
- use enlarged/native pixels for difficult clusters;
- explicitly keep in scope:
  `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- compare same-edition evidence when uncertain;
- distinguish character identity from expected modern spelling;
- OCR is not lexical authority;
- never global-replace.

Even strongly supported glyph/source differences are **ledger-first**.

## Durable state through R21

Current Tamil state:

- `verified` — **188**
- `needs-review` — **308**
- `partial` — **1**
- visual `verified` — **188**
- visual `needs-review` — **309**
- restart coverage — **210/497**

### Confirmed unresolved lexical holds — DO NOT CHANGE

WFV-002 through WFV-026 remain pending explicit user adjudication. WFV-001 remains rejected.

### R20 / R21 closure

R20 scans **191–200 — COMPLETE / PASS WITH LEXICAL HOLDS**:
- new WFV rows — **2**: WFV-023, WFV-024
- unresolved pages — **192, 195**
- lexical substitutions — **0**
- status promotions — **8**
- protected C2 scans 192, 195 and 199 preserved

R21 scans **201–210 — COMPLETE / PASS WITH LEXICAL HOLDS**:
- new WFV rows — **2**: WFV-025, WFV-026
- unresolved pages — **205, 209**
- lexical substitutions — **0**
- status promotions — **8**
- C09-001 scan 208 heading preserved

## R22+R23 protected C2 rulings — scans 211–230

Preserve these exact prior user adjudications:

- **scan 221 / C09-002**
  - source/user-authorized: `தனக்கு இரிந்தானைப் பெயர்புறம் நகுமே`
  - do not regress to `இரித்தானைப்`.

- **scan 223 / C09-003**
  - source/user-authorized carryover `எனை` belongs before `நாணம் வந்து தடுப்பதாலே`
  - preserve the adjudicated placement.

- **scan 226 / C10-001**
  - exact source heading: `பாரி மகளிர் பாடிய செய்யுள்`
  - do not regress to malformed `பாபி மகளிர்`.

- **scan 230 / C10-002**
  - source/user-authorized: `அந்துவன் சாத்தனையும் ஆதன் அழிசையையும்`
  - do not regress to `இழிசையையும்`.

C10-003 scan 237 and later C10 rulings belong to the following iteration and must not be pulled forward.

## Exact activity — 20 pages

Process physical scans **211–230** in one user iteration:

### R22 — scans 211–220

1. source-check all 10 scans word-for-word;
2. apply historical-glyph review;
3. ledger every new lexical/glyph/material-placement difference;
4. make **0 lexical substitutions** without user adjudication;
5. apply only source-supported nonlexical structure/punctuation/layout changes;
6. promote only clean fully audited pages;
7. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R22_SCANS_211_220.md`.

### R23 — scans 221–230

1. continue immediately without stopping;
2. preserve C2 scans 221, 223, 226 and 230 exactly;
3. ledger every new lexical/glyph/material-placement difference under the next live WFV ID;
4. make **0 lexical substitutions** without user adjudication;
5. promote only clean fully audited pages;
6. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R23_SCANS_221_230.md`.

At the end synchronize:

- `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
- `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
- `works/sangatamil/README.md`
- root `HANDOVER.md`
- `works/sangatamil/indexes/page-map.md`
- `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
- **`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`**

The maintained-English release-report gate remains **PAUSED**.

After R22+R23, the next user iteration is **R24+R25 — scans 231–250 (20 pages)**.
