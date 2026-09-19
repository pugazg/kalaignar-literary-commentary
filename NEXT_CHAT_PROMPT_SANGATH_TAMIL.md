# NEXT CHAT PROMPT — சங்கத் தமிழ் / 20-PAGE RE-AUDIT R16+R17 scans 151–170

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Active workflow

Tamil word-for-word / historical-glyph re-audit now uses the user's fixed execution cadence:

> **20 physical scans per user iteration**

Keep durable audit reports in **10-scan R batches** inside each 20-page iteration.

R01 through R15 are complete through physical scan **150**.

Latest frontier:

- R12 scans **111–120 — COMPLETE / PASS**
- R13 scans **121–130 — COMPLETE / PASS**
- R14 scans **131–140 — COMPLETE / PASS**
- R15 scans **141–150 — COMPLETE / PASS**

**Exact next user iteration: R16 + R17 = scans 151–170.**

Preferred split source:

`TVA_BOK_0042551_சங்கத்_தமிழ்_part_004_pages_151-200.pdf`

Physical scans **151–170** correspond to Part004 PDF pages **1–20**. Use only the user's controlling source / attachment; do not substitute web copies.

## Read first — mandatory

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R14_SCANS_131_140.md`
3. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R15_SCANS_141_150.md`
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
2. record the difference in `LEXICAL_DISCREPANCY_LEDGER.md`;
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

## Durable state through R15

Current Tamil state:

- `verified` — **137**
- `needs-review` — **359**
- `partial` — **1**
- visual `verified` — **137**
- visual `needs-review` — **360**
- restart coverage — **150/497**

### Confirmed unresolved lexical holds — DO NOT CHANGE

WFV-002 through WFV-014 remain pending explicit user adjudication. No pending hold may be silently applied.

### R14 / R15 closure

R14 scans **131–140 — COMPLETE / PASS**:
- new WFV rows — **0**
- lexical substitutions — **0**
- status promotions — **10**
- Gate-B extraction exclusions on scans 131 and 137 remain supported
- C2-06 contains no discrepancy records

R15 scans **141–150 — COMPLETE / PASS**:
- new WFV rows — **0**
- lexical substitutions — **0**
- status promotions — **10**
- scan 143 two-page spread verified
- scan 148 two-page illustrated spread verified
- scan 149 `மன்னன்!` source placement preserved
- scan 150 physical boundary at `பட்டமும்` preserved
- C2-06 contains no discrepancy records

## R16+R17 protected C2 rulings — scans 151–170

C2-07 covers scans **151–175**. Within the next 20-page iteration, preserve:

- **scan 163 / C07-001**
  - source/user-authorized:
    `கொங்கர்க் குடகடல் ஓட்டிய ஞான்றைத்`
  - do not regress to `ஓடிய`.

- **scan 165 / C07-002**
  - exact decorative/source heading:
    `காடைப் போர் கண்டுவந்த கணவன்!`
  - preserve the corrected heading; do not restore malformed `இகண்டுவந்த`.

C07-003 scan 174 and C07-004 scan 175 belong to the **following** 20-page iteration and must not be pulled forward.

## Exact activity — 20 pages

Process physical scans **151–170** in one user iteration:

### R16 — scans 151–160

1. source-check all 10 scans word-for-word;
2. apply historical-glyph review;
3. ledger every new lexical/glyph difference;
4. make **0 lexical substitutions** without user adjudication;
5. apply only source-supported nonlexical structure/punctuation/layout changes;
6. promote clean audited pages to `verified`;
7. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R16_SCANS_151_160.md`.

### R17 — scans 161–170

1. continue immediately without stopping;
2. preserve C2 scan 163 and 165 rulings exactly;
3. ledger any new difference under the next live WFV ID;
4. make **0 lexical substitutions** without user adjudication;
5. promote only clean fully audited pages;
6. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R17_SCANS_161_170.md`.

At the end of the full 20-page iteration synchronize:

- `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
- `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
- `works/sangatamil/README.md`
- root `HANDOVER.md`
- `works/sangatamil/indexes/page-map.md`
- `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
- **`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`**

The maintained-English release-report gate remains **PAUSED**.

After R16+R17, the next user iteration is **R18+R19 — scans 171–190 (20 pages)**.
