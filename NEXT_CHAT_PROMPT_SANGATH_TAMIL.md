# NEXT CHAT PROMPT — சங்கத் தமிழ் / 20-PAGE RE-AUDIT R30+R31 scans 291–310

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Active workflow

Tamil word-for-word / historical-glyph re-audit uses the user's fixed cadence:

> **20 physical scans per user iteration**

Keep durable audit reports in **10-scan R batches** inside each 20-page iteration.

R01 through R29 are complete through physical scan **290**.

Latest frontier:

- R26 scans **251–260 — COMPLETE / PASS WITH LEXICAL HOLD**
- R27 scans **261–270 — COMPLETE / PASS WITH LEXICAL HOLDS**
- R28 scans **271–280 — COMPLETE / PASS**
- R29 scans **281–290 — COMPLETE / PASS WITH LEXICAL HOLDS**

**Exact next user iteration: R30 + R31 = scans 291–310.**

Use only the user's supplied controlling split PDFs:

- physical scans **291–300** → `TVA_BOK_0042551_சங்கத்_தமிழ்_part_006_pages_251-300.pdf`, PDF pages **41–50**;
- physical scans **301–310** → `TVA_BOK_0042551_சங்கத்_தமிழ்_part_007_pages_301-350.pdf`, PDF pages **1–10**.

Do not substitute web copies.

## Read first — mandatory

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R28_SCANS_271_280.md`
3. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R29_SCANS_281_290.md`
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

For every source/Gemini word, character, omitted phrase, historical-glyph difference, or materially meaningful token-placement difference:

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

## Durable state through R29

Current Tamil state:

- `verified` — **253**
- `needs-review` — **243**
- `partial` — **1**
- visual `verified` — **253**
- visual `needs-review` — **244**
- restart coverage — **290/497**

### Confirmed unresolved lexical holds — DO NOT CHANGE

WFV-002 through WFV-048 remain pending explicit user adjudication. WFV-001 remains rejected.

### R28 / R29 closure

R28 scans **271–280 — COMPLETE / PASS**:
- new WFV rows — **0**
- unresolved pages — **0**
- lexical substitutions — **0**
- status promotions — **10**
- C11-006 scan 274 preserved

R29 scans **281–290 — COMPLETE / PASS WITH LEXICAL HOLDS**:
- new WFV rows — **4**: WFV-045 through WFV-048
- unresolved pages — **281, 282, 290**
- lexical substitutions — **0**
- status promotions — **7**
- C12-001, C12-002 and C12-003 preserved

## R30+R31 protected C12/C13 rulings — scans 291–310

Preserve these exact prior user adjudications:

- **scan 292 / C12-004**
  - exact heading: `ஒல்லையூரில் / முல்லையோ?`

- **scan 294 / C12-005**
  - exact source wording: `ஒல்லையூர்ப் பகுதி எல்லையிலே`

- **scan 296 / C12-006**
  - exact heading: `மறு பிறப்பு / உண்டென்றால் / மறக்க / நேரிடுமோ?`

- **scan 304 / C13-001**
  - preserve restored quotation continuation:
    `தாள் தாமரை தோள் தமனியக் கயமலர்`
  - it follows `ஆயிதழ் உண்கண் அலர் முகத் தாமரை`.

- **scan 307 / C13-002**
  - exact source wording: `யாருக்கும் அடங்காமல் பிளிறிற்றங்கே!`

- **scan 309 / C13-003**
  - exact heading: `முரசு கட்டிலில் / மோசுகீரனார்!`

C13-004 begins at scan **312** and belongs to the following iteration; do not pull it forward.

## Exact activity — 20 pages

### R30 — scans 291–300

1. source-check Part006 PDF pages **41–50** word-for-word;
2. apply historical-glyph review;
3. preserve C12-004, C12-005 and C12-006 on scans 292, 294 and 296 exactly;
4. ledger every new lexical/glyph/material-placement difference starting with the next live WFV ID after WFV-048;
5. make **0 lexical substitutions** without user adjudication;
6. apply only source-supported nonlexical structure/punctuation/layout changes;
7. promote only clean fully audited pages;
8. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R30_SCANS_291_300.md`.

### R31 — scans 301–310

1. continue immediately using Part007 PDF pages **1–10**;
2. preserve C13-001, C13-002 and C13-003 on scans 304, 307 and 309 exactly;
3. ledger every new lexical/glyph/material-placement difference under the next live WFV ID;
4. make **0 lexical substitutions** without user adjudication;
5. promote only clean fully audited pages;
6. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R31_SCANS_301_310.md`.

At the end synchronize:

- `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
- `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
- `works/sangatamil/README.md`
- root `HANDOVER.md`
- `works/sangatamil/indexes/page-map.md`
- `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
- **`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`**

The maintained-English release-report gate remains **PAUSED**.

After R30+R31, the next user iteration is **R32+R33 — scans 311–330 (20 pages)** using Part007 PDF pages **11–30**.
