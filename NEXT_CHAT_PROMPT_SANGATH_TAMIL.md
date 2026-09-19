# NEXT CHAT PROMPT — சங்கத் தமிழ் / 20-PAGE RE-AUDIT R40+R41 scans 391–410

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Active workflow

Tamil word-for-word / historical-glyph re-audit uses the user's fixed cadence:

> **20 physical scans per user iteration**

Keep durable audit reports in **10-scan R batches** inside each 20-page iteration.

R01 through R39 are complete through physical scan **390**.

Latest frontier:

- R36 scans **351–360 — COMPLETE / PASS**
- R37 scans **361–370 — COMPLETE / PASS**
- R38 scans **371–380 — COMPLETE / PASS**
- R39 scans **381–390 — COMPLETE / PASS**

**Exact next user iteration: R40 + R41 = scans 391–410.**

Use only the user's supplied controlling split PDFs:

- scans **391–400** — `TVA_BOK_0042551_சங்கத்_தமிழ்_part_008_pages_351-400.pdf`, PDF pages **41–50**
- scans **401–410** — `TVA_BOK_0042551_சங்கத்_தமிழ்_part_009_pages_401-450.pdf`, PDF pages **1–10**

Do not substitute web copies.

## Read first — mandatory

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R38_SCANS_371_380.md`
3. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R39_SCANS_381_390.md`
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

## Durable state through R39

Current Tamil state:

- `verified` — **348**
- `needs-review` — **148**
- `partial` — **1**
- visual `verified` — **348**
- visual `needs-review` — **149**
- restart coverage — **390/497**

### Confirmed unresolved lexical holds — DO NOT CHANGE

WFV-002 through WFV-053 remain pending explicit user adjudication. WFV-001 remains rejected.

### R38 / R39 closure

R38 scans **371–380 — COMPLETE / PASS**:

- new WFV rows — **0**
- unresolved new pages — **0**
- lexical substitutions — **0**
- status promotions — **10**
- C15-010 and C16-001 preserved

R39 scans **381–390 — COMPLETE / PASS**:

- new WFV rows — **0**
- unresolved new pages — **0**
- lexical substitutions — **0**
- source-supported nonlexical correction — scan **383** dash/right-edge placement before `எனக்கு`
- status promotions — **10**
- C16-002/C16-003 preserved

## R40+R41 protected C17 rulings — scans 391–410

Preserve these exact prior user adjudications:

- **scan 402 / C17-001**
  - exact source wording/placement: `வஞ்சமின்றி வழங்கிடுவேன் உனக்காகக் கண்ணா! - உன்`
  - continuation: `மஞ்சத்து மயிலாக...`

- **scan 404 / C17-002**
  - exact source wording: `அருகில் வரமுடியாமல் ஏங்கத்தான் வேண்டும்!`

- **scan 410 / C17-003**
  - protected Gemini-correct quotation:
    `முலைவேதின் ஒற்றி முயங்கிப் பொதிவேம்`
    `கொலைஏறு சாடிய புண்ணை......`

Do not reopen these merely because an earlier Gemini/source comparison disagreed.

## Exact activity — 20 pages

### R40 — scans 391–400

1. source-check Part008 PDF pages **41–50** word-for-word;
2. apply historical-glyph review;
3. ledger every new lexical/glyph/material-placement difference starting with the next live WFV ID after WFV-053;
4. make **0 lexical substitutions** without user adjudication;
5. apply only source-supported nonlexical structure/punctuation/layout changes;
6. promote only clean fully audited pages;
7. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R40_SCANS_391_400.md`.

### R41 — scans 401–410

1. continue immediately using Part009 PDF pages **1–10**;
2. preserve C17-001 through C17-003 exactly;
3. ledger every new lexical/glyph/material-placement difference under the next live WFV ID;
4. make **0 lexical substitutions** without user adjudication;
5. promote only clean fully audited pages;
6. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R41_SCANS_401_410.md`.

At the end synchronize:

- `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
- `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
- `works/sangatamil/README.md`
- root `HANDOVER.md`
- `works/sangatamil/indexes/page-map.md`
- `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
- **`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`**

The maintained-English release-report gate remains **PAUSED**.

After R40+R41, the next user iteration is **R42+R43 — scans 411–430 (20 pages)** using Part009 PDF pages **11–30**.
