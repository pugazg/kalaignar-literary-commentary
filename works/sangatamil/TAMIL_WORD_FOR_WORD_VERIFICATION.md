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

Current state after R01 scans 1–10:

- `verified` — **49**
- `needs-review` — **447**
- `partial` — **1**
- visual `verified` — **49**
- visual `needs-review` — **448**
- blocked — **0**

R01 changed **0 lexical words**.

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
| R02 | 11–20 | **NEXT** |
| R03 | 21–30 | pending |
| R04 | 31–40 | pending |
| R05 | 41–50 | pending |
| R06 | 51–60 | pending |
| R07 | 61–70 | pending |
| R08 | 71–80 | pending |
| R09 | 81–90 | pending |
| R10 | 91–100 | pending |
| R11–R49 | 101–490 | pending in 10-scan cadence |
| R50 | 491–497 | final 7-scan remainder |

## Exact next activity

Process **R02 — scans 11–20** from the supplied Part001 PDF.

At R02 close:

- inspect all 10 scans at enlarged/native resolution;
- apply the historical-glyph guide;
- check all 13 known families where present;
- preserve prior explicit C2 adjudications;
- record every new lexical/glyph difference in the discrepancy ledger;
- change **0 lexical words without user adjudication**;
- apply only non-lexical source-supported structure/punctuation/layout changes;
- synchronize this tracker, README, HANDOVER, English-release pause state and `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`.
