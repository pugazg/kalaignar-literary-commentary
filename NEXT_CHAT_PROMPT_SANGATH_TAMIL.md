# NEXT CHAT PROMPT — சங்கத் தமிழ் / 20-PAGE RE-AUDIT R26+R27 scans 251–270

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Active workflow

Tamil word-for-word / historical-glyph re-audit uses the user's fixed cadence:

> **20 physical scans per user iteration**

Keep durable audit reports in **10-scan R batches** inside each 20-page iteration.

R01 through R25 are complete through physical scan **250**.

Latest frontier:

- R22 scans **211–220 — COMPLETE / PASS WITH LEXICAL HOLDS**
- R23 scans **221–230 — COMPLETE / PASS WITH LEXICAL HOLDS**
- R24 scans **231–240 — COMPLETE / PASS WITH LEXICAL HOLDS**
- R25 scans **241–250 — COMPLETE / PASS WITH LEXICAL HOLD**

**Exact next user iteration: R26 + R27 = scans 251–270.**

Use only the user's supplied controlling:

`TVA_BOK_0042551_சங்கத்_தமிழ்_part_006_pages_251-300.pdf`

Physical scans **251–270** correspond to Part006 PDF pages **1–20**. Do not substitute web copies.

## Read first — mandatory

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R24_SCANS_231_240.md`
3. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R25_SCANS_241_250.md`
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
- distinguish historical glyph identity from expected modern spelling;
- OCR is not lexical authority;
- never global-replace.

Even strongly supported glyph/source differences are **ledger-first**.

## Durable state through R25

Current Tamil state:

- `verified` — **220**
- `needs-review` — **276**
- `partial` — **1**
- visual `verified` — **220**
- visual `needs-review` — **277**
- restart coverage — **250/497**

### Confirmed unresolved lexical holds — DO NOT CHANGE

WFV-002 through WFV-040 remain pending explicit user adjudication. WFV-001 remains rejected.

### R24 / R25 closure

R24 scans **231–240 — COMPLETE / PASS WITH LEXICAL HOLDS**:
- new WFV rows — **7**: WFV-033 through WFV-039
- unresolved pages — **231, 233**
- lexical substitutions — **0**
- status promotions — **8**
- C10-003 and C10-004 protected

R25 scans **241–250 — COMPLETE / PASS WITH LEXICAL HOLD**:
- new WFV row — **1**: WFV-040
- unresolved page — **248**
- lexical substitutions — **0**
- status promotions — **9**
- C10-005 protected
- WFV-040 records source glossary continuation `மகன்.`; canonical remains unchanged

## R26+R27 protected C11 rulings — scans 251–270

Preserve these exact prior user adjudications:

- **scan 254 / C11-001**
  - retain only one `இந்தச்`, after `சிற்றூர் முதல் பேரூர் நகரங்கள் வரை -`;
  - do not reintroduce the removed duplicate.

- **scan 257 / C11-002**
  - exact poem term: `காம ஒள்எரி`.

- **scan 257 / C11-003**
  - quotation: `என்புஉற நலியினும்`.

- **scan 257 / C11-004**
  - quotation: `பிரித்துஇடை களையார்`.

- **scan 257 / C11-005**
  - glossary: `காம ஒள்எரி = காமமெனும் ஒளிபொருந்திய தீ.`

C11-006 is on scan **274** and belongs to a later iteration; do not pull it forward.

## Exact activity — 20 pages

Process physical scans **251–270** in one user iteration:

### R26 — scans 251–260

1. source-check all 10 scans word-for-word;
2. apply historical-glyph review;
3. preserve C11 scans 254 and 257 exactly;
4. ledger every new lexical/glyph/material-placement difference starting with the next live WFV ID after WFV-040;
5. make **0 lexical substitutions** without user adjudication;
6. apply only source-supported nonlexical structure/punctuation/layout changes;
7. promote only clean fully audited pages;
8. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R26_SCANS_251_260.md`.

### R27 — scans 261–270

1. continue immediately without stopping;
2. ledger every new lexical/glyph/material-placement difference under the next live WFV ID;
3. make **0 lexical substitutions** without user adjudication;
4. promote only clean fully audited pages;
5. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R27_SCANS_261_270.md`.

At the end synchronize:

- `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
- `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
- `works/sangatamil/README.md`
- root `HANDOVER.md`
- `works/sangatamil/indexes/page-map.md`
- `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
- **`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`**

The maintained-English release-report gate remains **PAUSED**.

After R26+R27, the next user iteration is **R28+R29 — scans 271–290 (20 pages)**.
