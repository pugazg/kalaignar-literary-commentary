# NEXT CHAT PROMPT — சங்கத் தமிழ் / RE-AUDIT R12 scans 111–120

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Active workflow

Tamil word-for-word / historical-glyph re-audit runs in **10-page physical-scan iterations**.

R01 through R11 are complete through physical scan **110**.

Recent frontier:

- R08 scans **71–80 — COMPLETE / PASS**
- R09 scans **81–90 — COMPLETE / PASS WITH LEXICAL HOLDS**
- R10 scans **91–100 — COMPLETE / PASS WITH LEXICAL HOLDS**
- R11 scans **101–110 — COMPLETE / PASS**

**Exact next range: R12 scans 111–120.**

Preferred split source when available:

`TVA_BOK_0042551_சங்கத்_தமிழ்_part_003_pages_101-150.pdf`

R12 physical scans 111–120 correspond to Part003 PDF pages **11–20**. The same user-supplied controlling full source `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf` may be used for those physical scans if needed.

## Read first — mandatory

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R10_SCANS_091_100.md`
3. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R11_SCANS_101_110.md`
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

## Durable state through R11

Current Tamil state:

- `verified` — **97**
- `needs-review` — **399**
- `partial` — **1**
- visual `verified` — **97**
- visual `needs-review` — **400**
- restart coverage — **110/497**

### Confirmed unresolved lexical holds — DO NOT CHANGE

All **WFV-002 through WFV-014** are confirmed / pending explicit user adjudication.

Most recent:

- **WFV-005 / scan 91** — `வாராத காரணம்தான்` vs source `வராத காரணம்தான்`
- **WFV-012 / scan 85** — source-visible `- அவர்கள்` missing from canonical
- **WFV-013 / scan 87** — `நல்ல` token-placement discrepancy
- **WFV-014 / scan 94** — quotation `என் உயிர்ஒம் புநனே` vs source `என் உயிர்ஓம் புநனே`

No pending hold may be silently applied.

## R12 protected C2 rulings — scans 111–120

Preserve these exact prior user adjudications:

- **scan 112 / C05-001** — exact heading:
  `புரிந்துகொண்டான்; பிரிந்துசென்றார்!`
- **scan 113 / C05-002** — source opening quotation stanza after the prose is a true missing whole lexical block and was user-authorized/restored; preserve that restored block.
- **scan 120 / C05-003** — note `ஊன்பொழிப் பசுங்குடையார்` — **Gemini is correct**; preserve.

Do not reopen these unless the user explicitly does so.

## R12 exact activity

Process exactly **physical scans 111–120**.

For each scan:

1. compare canonical Tamil word-for-word against the controlling source;
2. inspect the full page and enlarged/native details;
3. apply the historical-glyph checklist;
4. preserve C2 rulings above;
5. ledger every new lexical/glyph difference;
6. **change 0 lexical words without explicit user adjudication**;
7. apply only source-supported non-lexical structure/punctuation/layout corrections;
8. promote clean fully audited pages to `verified` / visual `verified`;
9. unresolved lexical pages remain `needs-review`;
10. do not alter WFV-002 through WFV-014.

At R12 close create:

`works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R12_SCANS_111_120.md`

Synchronize:

- `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
- `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
- `works/sangatamil/README.md`
- root `HANDOVER.md`
- `works/sangatamil/indexes/page-map.md`
- `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
- **`NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`**

The maintained-English release-report gate remains **PAUSED**.

After R12, exact next range becomes **R13 scans 121–130**.
