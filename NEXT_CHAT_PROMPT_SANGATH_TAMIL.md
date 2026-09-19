# NEXT CHAT PROMPT — சங்கத் தமிழ் / 20-PAGE RE-AUDIT R18+R19 scans 171–190

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Active workflow

Tamil word-for-word / historical-glyph re-audit uses the user's fixed cadence:

> **20 physical scans per user iteration**

Keep durable audit reports in **10-scan R batches** inside each 20-page iteration.

R01 through R17 are complete through physical scan **170**.

Latest frontier:

- R14 scans **131–140 — COMPLETE / PASS**
- R15 scans **141–150 — COMPLETE / PASS**
- R16 scans **151–160 — COMPLETE / PASS**
- R17 scans **161–170 — COMPLETE / PASS**

**Exact next user iteration: R18 + R19 = scans 171–190.**

Preferred split source:

`TVA_BOK_0042551_சங்கத்_தமிழ்_part_004_pages_151-200.pdf`

Physical scans **171–190** correspond to Part004 PDF pages **21–40**. Use only the user's controlling source / attachment; do not substitute web copies.

## Read first — mandatory

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R16_SCANS_151_160.md`
3. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R17_SCANS_161_170.md`
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

## Durable state through R17

Current Tamil state:

- `verified` — **157**
- `needs-review` — **339**
- `partial` — **1**
- visual `verified` — **157**
- visual `needs-review` — **340**
- restart coverage — **170/497**

### Confirmed unresolved lexical holds — DO NOT CHANGE

WFV-002 through WFV-014 remain pending explicit user adjudication. No pending hold may be silently applied.

### R16 / R17 closure

R16 scans **151–160 — COMPLETE / PASS**:
- new WFV rows — **0**
- lexical substitutions — **0**
- status promotions — **10**
- scans 156 and 160 full-page illustrations verified
- C2-07 contains no adjudication records within scans 151–160

R17 scans **161–170 — COMPLETE / PASS**:
- new WFV rows — **0**
- lexical substitutions — **0**
- status promotions — **10**
- scan 163 `கொங்கர்க் குடகடல் ஓட்டிய ஞான்றைத்` preserved
- scan 165 heading `காடைப் போர் கண்டுவந்த கணவன்!` preserved
- scan 166 full-page illustration verified
- scan 170 historical `னா` identity in `கானாங் கோழி` confirmed with same-page `இளநாகனார்` evidence

## R18+R19 protected C2 rulings — scans 171–190

Preserve these exact prior user adjudications:

- **scan 174 / C07-003**
  - `சிறுயிலை நெல்லித் தீங்கனி குறியாது`
  - Gemini is correct; do not alter it.

- **scan 175 / C07-004**
  - exact heading: `நீலமலை நீரினும் குளிர்ந்த நெஞ்சம்!`
  - do not restore either historical incorrect heading candidate.

- **scan 180 / C08-001**
  - quotation contains `... வானி நீரினும் தீந்தன் சாயலன் ...`
  - Gemini is correct; preserve it.

- **scan 188 / C08-002**
  - exact decorative/source heading: `அவள் நிலமானாள்; அவன் மழையானான்!`
  - preserve corrected `மழையானான்!`; do not regress to `மழையானன்!`.

C08-003 scan 192 and later C08 rulings belong to the **following** 20-page iteration and must not be pulled forward.

## Exact activity — 20 pages

Process physical scans **171–190** in one user iteration:

### R18 — scans 171–180

1. source-check all 10 scans word-for-word;
2. apply historical-glyph review;
3. preserve C2 scans 174, 175 and 180 exactly;
4. ledger every new lexical/glyph difference;
5. make **0 lexical substitutions** without user adjudication;
6. apply only source-supported nonlexical structure/punctuation/layout changes;
7. promote only clean fully audited pages;
8. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R18_SCANS_171_180.md`.

### R19 — scans 181–190

1. continue immediately without stopping;
2. preserve C2 scan 188 exactly;
3. ledger any new difference under the next live WFV ID;
4. make **0 lexical substitutions** without user adjudication;
5. promote only clean fully audited pages;
6. create:
   `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R19_SCANS_181_190.md`.

At the end of the full 20-page iteration synchronize:

- `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
- `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
- `works/sangatamil/README.md`
- root `HANDOVER.md`
- `works/sangatamil/indexes/page-map.md`
- `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
- **`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`**

The maintained-English release-report gate remains **PAUSED**.

After R18+R19, the next user iteration is **R20+R21 — scans 191–210 (20 pages)**.
