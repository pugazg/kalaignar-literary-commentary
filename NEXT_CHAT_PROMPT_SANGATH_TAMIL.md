# NEXT CHAT PROMPT — சங்கத் தமிழ் / RE-AUDIT R03 scans 21–30

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Active workflow

Tamil word-for-word / historical-glyph re-audit has been **restarted from scan 1 in 10-page iterations**.

R01 scans **1–10 — COMPLETE / PASS**.  
R02 scans **11–20 — COMPLETE / PASS**.

**Exact next range: R03 scans 21–30.**

Use the already supplied:

`TVA_BOK_0042551_சங்கத்_தமிழ்_part_001_pages_1-50.pdf`

## Read first — mandatory

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R01_SCANS_001_010.md`
3. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R02_SCANS_011_020.md`
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
2. record the difference in `LEXICAL_DISCREPANCY_LEDGER.md`;
3. keep/reopen the page as `needs-review` when unresolved;
4. wait for explicit user adjudication before any lexical mutation.

Earlier explicit C2 user adjudications remain controlling and must not be casually relitigated.

## Historical-glyph rule

The historical-glyph guide is mandatory for every printed page.

For each scan:

- inspect the whole page first;
- use enlarged/native pixels for difficult clusters;
- check the known minimum set:
  `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- compare same-edition evidence when uncertain;
- distinguish character identity from expected modern spelling;
- do not trust OCR as lexical authority;
- never global-replace.

For this Sangatamil project, even a strongly supported historical-glyph difference must be **ledgered first**, not directly applied.

## R01 durable state

Scans **1–10**:

- new lexical discrepancies — **0**;
- WFV-001 scan7 — **REJECTED**;
- scan7 canonical `ராக்போர்ட்` confirmed by high-resolution + same-edition evidence;
- scan7 punctuation/spacing only synchronized;
- scan8 — `partial`, description-only handwritten `முன்னுரை`;
- canonical lexical substitutions — **0**.

## R02 durable state

Scans **11–20**:

- reviewed — **10/10**;
- new lexical discrepancies — **0**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical page corrections — **0**;
- page-layer mutations — **0**;
- scan11 C2 ruling `ஆண்பாலர் பதினால்வர்` — preserved;
- scan13 C2 rulings `அதனைக் களைகின்ற திறல் மிக்க` and `சொல் நயத்தை மற்றாரும் நுகரும் வண்ணம்` — preserved;
- scan19 C2 ruling `அரும்பு, அமர் ஆத்தி` — preserved;
- scan20 `கூறாக` — old-type cluster confirmed as historical `றா` identity, **not** a new lexical discrepancy;
- all ten scans retain their existing appropriate `verified` / visual `verified` states.

Current Tamil state remains **49 verified / 447 needs-review / 1 partial**.  
Current visual-fidelity state remains **49 verified / 448 needs-review**.

The earlier interrupted Part002 findings WFV-002 through WFV-005 remain ledger-only candidates and are **not counted as restart coverage**. Reconfirm them only when their new 10-page batches are reached.

## R03 exact activity — scans 21–30

Process exactly **10 physical scans: 21–30**.

For each page:

1. compare canonical Tamil word-for-word against the source scan;
2. inspect at enlarged/native resolution;
3. apply the historical-glyph checklist;
4. preserve explicit prior C2 rulings;
5. record every newly confirmed lexical/glyph difference in the ledger;
6. **change 0 lexical words without explicit user adjudication**;
7. apply only source-supported non-lexical structure/punctuation/layout corrections;
8. mark clean fully audited pages `verified` / visual `verified` only when appropriate;
9. unresolved lexical pages remain `needs-review`;
10. scan-level historical-glyph ambiguity must not be guessed from context.

At R03 close create:

`works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R03_SCANS_021_030.md`

Then synchronize:

- `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
- `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
- `works/sangatamil/README.md`
- root `HANDOVER.md`
- `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
- **`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`**

The English release-report gate stays paused.

After R03, exact next range becomes **R04 scans 31–40**.
