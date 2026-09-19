# NEXT CHAT PROMPT — சங்கத் தமிழ் / RE-AUDIT R14 scans 131–140

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Active workflow

Tamil word-for-word / historical-glyph re-audit runs in **10-page physical-scan iterations**.

R01 through R13 are complete through physical scan **130**.

Recent frontier:

- R10 scans **91–100 — COMPLETE / PASS WITH LEXICAL HOLDS**
- R11 scans **101–110 — COMPLETE / PASS**
- R12 scans **111–120 — COMPLETE / PASS**
- R13 scans **121–130 — COMPLETE / PASS**

**Exact next range: R14 scans 131–140.**

Preferred split source:

`TVA_BOK_0042551_சங்கத்_தமிழ்_part_003_pages_101-150.pdf`

R14 physical scans 131–140 correspond to Part003 PDF pages **31–40**. The same user-supplied controlling full source `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf` may be used if needed.

## Read first — mandatory

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R12_SCANS_111_120.md`
3. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R13_SCANS_121_130.md`
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
- keep in scope:
  `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- compare same-edition evidence when uncertain;
- distinguish character identity from expected modern spelling;
- OCR is not lexical authority;
- never global-replace.

Even strongly supported glyph/source differences are **ledger-first**.

## Durable state through R13

Current Tamil state:

- `verified` — **117**
- `needs-review` — **379**
- `partial` — **1**
- visual `verified` — **117**
- visual `needs-review` — **380**
- restart coverage — **130/497**

### Confirmed unresolved lexical holds — DO NOT CHANGE

WFV-002 through WFV-014 remain pending explicit user adjudication. No pending hold may be silently applied.

### R12 / R13 closure

- R12 scans **111–120** — COMPLETE / PASS
  - new WFV rows — **0**
  - lexical substitutions — **0**
  - scans 113–115 section metadata aligned to exact user-adjudicated heading `புரிந்துகொண்டான்; பிரிந்துசென்றார்!`
  - protected C2 scans 112, 113, 120 preserved
- R13 scans **121–130** — COMPLETE / PASS
  - new WFV rows — **0**
  - lexical substitutions — **0**
  - protected C2 scan-123 restored opening prose preserved
  - C2-06 scans 126–130 — no discrepancy records

## R14 C2 control

C2-06 covers scans **126–150** and is **COMPLETE / NO DISCREPANCY RECORDS / NO PAGE ACTION**.

Therefore scans **131–140** have no pre-existing C2 discrepancy rulings to invent or apply. Audit the actual source page-by-page; if a new lexical/glyph difference is found, ledger it under the current WFV sequence and do not mutate the lexical body without user adjudication.

## R14 exact activity

Process exactly **physical scans 131–140**.

For each scan:

1. compare canonical Tamil word-for-word against the controlling source;
2. inspect the full page and difficult clusters at enlarged/native resolution;
3. apply the historical-glyph checklist;
4. ledger every new lexical/glyph difference;
5. **change 0 lexical words without explicit user adjudication**;
6. apply only source-supported non-lexical structure/punctuation/layout corrections;
7. promote clean fully audited pages to `verified` / visual `verified`;
8. unresolved lexical pages remain `needs-review`;
9. do not alter WFV-002 through WFV-014.

At R14 close create:

`works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R14_SCANS_131_140.md`

Then synchronize:

- `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
- `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
- `works/sangatamil/README.md`
- root `HANDOVER.md`
- `works/sangatamil/indexes/page-map.md`
- `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
- **`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`**

The maintained-English release-report gate remains **PAUSED**.

After R14, exact next range becomes **R15 scans 141–150**, completing Part003.
