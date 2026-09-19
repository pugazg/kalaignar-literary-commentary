# Sangatamil — Tamil Word-for-Word / Historical-Glyph Re-Audit Tracker

**Status: IN PROGRESS — RESTARTED FROM SCAN 1 IN 10-PAGE ITERATIONS**

- restart date: **2026-09-19**
- repository: `pugazg/kalaignar-literary-commentary`
- branch: `main`
- cadence: **10 physical scans per iteration**
- comparison source: user-supplied split PDFs from `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`
- lexical authority: **Gemini/canonical wording + exact prior user adjudications**
- structural/visual authority: **PDF scan**
- lexical discrepancy ledger: `LEXICAL_DISCREPANCY_LEDGER.md`
- historical-glyph control: `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
- permanent exception: scan **8** remains `partial` / handwritten facsimile unless the user explicitly changes that policy

## Highest-priority user rule

> **Do not correct any words directly.**

The review is word-for-word and glyph-aware, but a source/Gemini lexical difference is **ledger evidence**, not automatic permission to mutate the page.

For every scan:

1. inspect the whole page first;
2. use enlarged/native pixels for difficult text;
3. explicitly check the 13 historical/reform-sensitive families:
   `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
4. use same-edition examples when a glyph is uncertain;
5. separate historical glyph identity from expected modern spelling;
6. never use OCR as lexical authority;
7. **do not substitute a lexical word or character directly** when source and Gemini/canonical wording differ;
8. append every such lexical/glyph difference to `LEXICAL_DISCREPANCY_LEDGER.md`;
9. preserve exact prior user C2 adjudications unless the user explicitly reopens them;
10. structural/punctuation/layout corrections may be applied only when they do not change lexical wording;
11. unresolved lexical pages stay `needs-review`;
12. clean fully audited pages may remain/become `verified`;
13. no global replacements.

The attached historical-glyph guide says to read character identity rather than modern visual resemblance. For **this Sangatamil project**, its general glyph-decoding method is used for detection and evidence gathering, while the user's stricter Gemini-lock rule controls mutation: **ledger first, user adjudication before any lexical edit**.

## Restart status

Historical Gate-G baseline:

- `verified` — **43**
- `needs-review` — **453**
- `partial` — **1**

Current state after R03 scans 21–30:

- `verified` — **47**
- `needs-review` — **449**
- `partial` — **1**
- visual `verified` — **47**
- visual `needs-review` — **450**
- blocked — **0**

R01–R03 changed **0 lexical words**. R03 discovered **3 new lexical discrepancy rows** on scans **25 and 30**, left all disputed lexical wording unchanged, and applied only source-supported non-lexical corrections on scans **21, 25 and 29**.

## R01 — scans 1–10

**COMPLETE / PASS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R01_SCANS_001_010.md`

Results:

- scans **1–7, 9–10** — full restart audit completed;
- scan **8** — description-only handwritten facsimile; permanent special handling;
- new lexical discrepancies — **0**;
- WFV-001 scan 7 — **REJECTED** after high-resolution/same-edition comparison;
- scan 7 — promoted back to `verified` after lexical hold cleared; only punctuation/spacing synchronized;
- protected earlier C2 adjudications on scans 5 and 9 — preserved;
- historical-glyph guide — applied page-by-page;
- canonical lexical substitutions — **0**.

## R02 — scans 11–20

**COMPLETE / PASS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R02_SCANS_011_020.md`

Results:

- scans **11–20** — full restart audit completed at enlarged/native resolution;
- new lexical discrepancies — **0**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical page corrections — **0**;
- page-layer mutations — **0**;
- earlier explicit C2 rulings on scans **11, 13 and 19** — preserved and not relitigated;
- scan **20** old-type `கூறாக` cluster — confirmed as historical `றா` identity, not a new lexical discrepancy;
- all ten pages retain their existing appropriate `verified` / visual `verified` states;
- whole-volume state remains **49 verified / 447 needs-review / 1 partial**.

## R03 — scans 21–30

**COMPLETE / PASS WITH LEXICAL HOLDS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R03_SCANS_021_030.md`

Results:

- scans **21–30** — full restart audit completed at enlarged/native resolution;
- new lexical discrepancy rows — **3**: WFV-006 through WFV-008;
- unresolved lexical pages — **2**: scans **25, 30**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical page corrections — **3 page files**: scans **21, 25, 29**;
- page files mutated — **4**: scans **21, 25, 29, 30**;
- scan **25** — canonical `பெற்றவனோ?` held against source `பெற்றவனே?`; final two lines restored to source order;
- scan **30** — canonical `ஆள்அன்று` held against source `ஆளன்று` in quotation and gloss;
- prior C2 rulings on scans **21, 28 and 29** preserved and not relitigated;
- whole-volume state now **47 verified / 449 needs-review / 1 partial**.

## Pre-restart Part002 candidate rows

The earlier interrupted Part002 review is **not counted as completed restart coverage**.

WFV-002 through WFV-005 remain ledger-only candidate holds and must be **reconfirmed when their 10-page restart batches are reached**:

- WFV-002 — scan 62
- WFV-003 — scan 69
- WFV-004 — scan 83
- WFV-005 — scan 91

Do not change those words before re-audit + user adjudication.

## 10-page iteration plan

| Iteration | Scans | State |
|---|---:|---|
| R01 | 1–10 | **COMPLETE / PASS** |
| R02 | 11–20 | **COMPLETE / PASS** |
| R03 | 21–30 | **COMPLETE / PASS WITH LEXICAL HOLDS** |
| R04 | 31–40 | **NEXT** |
| R05 | 41–50 | pending |
| R06 | 51–60 | pending |
| R07 | 61–70 | pending |
| R08 | 71–80 | pending |
| R09 | 81–90 | pending |
| R10 | 91–100 | pending |
| R11–R49 | 101–490 | pending in 10-scan cadence |
| R50 | 491–497 | final 7-scan remainder |

## Exact next activity

Process **R04 — scans 31–40** from the supplied Part001 PDF.

At R04 close:

- inspect all 10 scans at enlarged/native resolution;
- apply the historical-glyph guide;
- check all 13 known families where present;
- preserve prior explicit C2 adjudications;
- record every new lexical/glyph difference in the discrepancy ledger;
- change **0 lexical words without user adjudication**;
- apply only non-lexical source-supported structure/punctuation/layout changes;
- synchronize this tracker, README, HANDOVER, English-release pause state and `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`.
