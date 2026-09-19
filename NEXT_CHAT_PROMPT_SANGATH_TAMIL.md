# NEXT CHAT PROMPT — சங்கத் தமிழ் / 20-PAGE RE-AUDIT R20+R21 scans 191–210

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Active workflow

Tamil word-for-word / historical-glyph re-audit uses the user's fixed cadence:

> **20 physical scans per user iteration**

Keep durable audit reports in **10-scan R batches** inside each 20-page iteration.

R01 through R19 are complete through physical scan **190**.

Latest frontier:

- R16 scans **151–160 — COMPLETE / PASS**
- R17 scans **161–170 — COMPLETE / PASS**
- R18 scans **171–180 — COMPLETE / PASS WITH LEXICAL HOLDS**
- R19 scans **181–190 — COMPLETE / PASS WITH LEXICAL HOLDS**

**Exact next user iteration: R20 + R21 = scans 191–210.**

Use only the user's supplied controlling split PDFs:

- scans **191–200** → `TVA_BOK_0042551_சங்கத்_தமிழ்_part_004_pages_151-200.pdf`, PDF pages **41–50**;
- scans **201–210** → `TVA_BOK_0042551_சங்கத்_தமிழ்_part_005_pages_201-250.pdf`, PDF pages **1–10**.

Do not substitute web copies.

## Read first — mandatory

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R18_SCANS_171_180.md`
3. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R19_SCANS_181_190.md`
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

## Durable state through R19

Current Tamil state:

- `verified` — **172**
- `needs-review` — **324**
- `partial` — **1**
- visual `verified` — **172**
- visual `needs-review` — **325**
- restart coverage — **190/497**

### Confirmed unresolved lexical holds — DO NOT CHANGE

WFV-002 through WFV-022 remain pending explicit user adjudication. WFV-001 remains rejected. No pending hold may be silently applied.

### R18 / R19 closure

R18 scans **171–180 — COMPLETE / PASS WITH LEXICAL HOLDS**:
- new WFV rows — **5**: WFV-015 through WFV-019
- unresolved pages — **174, 177, 179**
- lexical substitutions — **0**
- status promotions — **7**
- metadata aligned to exact `நீலமலை நீரினும் குளிர்ந்த நெஞ்சம்!` on scans 176–180
- C07-003, C07-004 and C08-001 protected

R19 scans **181–190 — COMPLETE / PASS WITH LEXICAL HOLDS**:
- new WFV rows — **3**: WFV-020 through WFV-022
- unresolved pages — **183, 189**
- lexical substitutions — **0**
- status promotions — **8**
- scan-181 section metadata aligned
- C08-002 heading protected

## R20+R21 protected C2 rulings — scans 191–210

Preserve these exact prior user adjudications:

- **scan 192 / C08-003**
  - source/user-authorized: `அறிந்திட விரும்பாமலே அறிமுகமானோம்!`
  - do not regress to malformed `விருமபாமலே`.

- **scan 195 / C08-004**
  - source/user-authorized: `முடி புனைந்த மூத்தோர் மறைந்து; அவர்`
  - do not regress to `முத்தோர்`.

- **scan 199 / C08-005**
  - source/user-authorized: `கிழங்குகளின் குறும்புதான் என்னே...`
  - preserve the corrected form.

- **scan 199 / C08-006**
  - Purananuru 109 quotation: `தீஞ்சுனைப் பலவின் பழம்`
  - Gemini is correct; preserve it.

- **scan 199 / C08-007**
  - `கலைஉளமும் பெற்றதாலே கபிலர்க்கு உயிரே ஆனான்`
  - Gemini is correct; preserve it.

- **scan 208 / C09-001**
  - exact decorative/source heading: `காவிரிநாடன் கரிகாலன்!`
  - preserve corrected `கரிகாலன்!`; do not regress to `கபிகாலன்!`.

C09-002 scan 221 and C09-003 scan 223 belong to a later iteration and must not be pulled forward.

## Exact activity — 20 pages

Process physical scans **191–210** in one user iteration:

### R20 — scans 191–200

1. source-check all 10 scans word-for-word;
2. apply historical-glyph review;
3. preserve C2 scans 192, 195 and 199 exactly;
4. ledger every new lexical/glyph/material-placement difference;
5. make **0 lexical substitutions** without user adjudication;
6. apply only source-supported nonlexical structure/punctuation/layout changes;
7. promote only clean fully audited pages;
8. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R20_SCANS_191_200.md`.

### R21 — scans 201–210

1. continue immediately without stopping;
2. switch to Part005 at physical scan 201 / PDF page 1;
3. preserve C2 scan 208 exactly;
4. ledger any new lexical/glyph/material-placement difference under the next live WFV ID;
5. make **0 lexical substitutions** without user adjudication;
6. promote only clean fully audited pages;
7. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R21_SCANS_201_210.md`.

At the end of the full 20-page iteration synchronize:

- `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
- `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
- `works/sangatamil/README.md`
- root `HANDOVER.md`
- `works/sangatamil/indexes/page-map.md`
- `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
- **`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`**

The maintained-English release-report gate remains **PAUSED**.

After R20+R21, the next user iteration is **R22+R23 — scans 211–230 (20 pages)**.
