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

Current state after R23 scans 221–230:

- `verified` — **203**
- `needs-review` — **293**
- `partial` — **1**
- visual `verified` — **203**
- visual `needs-review` — **294**
- blocked — **0**

R01–R23 changed **0 lexical words**. R03 discovered **3** lexical discrepancy rows on scans **25 and 30**; R05 discovered **1** on scan **49**; R06 discovered **1** on scan **55**; R07 reconfirmed WFV-002 and WFV-003 and discovered WFV-011 on scan **67**; R08 found **0** new discrepancies; R09 reconfirmed WFV-004 and discovered WFV-012 and WFV-013; R10 reconfirmed WFV-005 and discovered WFV-014; R11–R17 found **0** new discrepancies; R18 opened **WFV-015 through WFV-019**; R19 opened **WFV-020 through WFV-022**; R20 opened **WFV-023 and WFV-024**; R21 opened **WFV-025 and WFV-026**; R22 opened **WFV-027 through WFV-029**; R23 opened **WFV-030 through WFV-032**. All disputed lexical wording and material token placement remain unchanged pending user adjudication.

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

## R04 — scans 31–40

**COMPLETE / PASS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R04_SCANS_031_040.md`

Results:

- scans **31–40** — full restart audit completed at enlarged/native resolution;
- new lexical discrepancy rows — **0**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical page corrections — **0**;
- page-layer mutations — **0**;
- earlier explicit C2 rulings on scans **35, 39 and 40** — preserved and not relitigated;
- existing R03 WFV-006 through WFV-008 — unchanged / pending user adjudication;
- whole-volume state remains **47 verified / 449 needs-review / 1 partial**.

## R05 — scans 41–50

**COMPLETE / PASS WITH LEXICAL HOLD**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R05_SCANS_041_050.md`

Results:

- scans **41–50** — full restart audit completed at enlarged/native resolution;
- new lexical discrepancy rows — **1**: WFV-009;
- unresolved new lexical pages — **1**: scan **49**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical page corrections — **0**;
- page-layer lexical mutations — **0**;
- scan **49** — canonical quotation `திண்டோர் நள்ளி கானத் தண்டர்` held against source-visible `திண்டேர் நள்ளி கானத் தண்டர்`; page reopened to `needs-review`;
- prior C2 rulings on scan **47** preserved and not relitigated;
- whole-volume state now **46 verified / 450 needs-review / 1 partial**.

## R06 — scans 51–60

**COMPLETE / PASS WITH LEXICAL HOLD**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R06_SCANS_051_060.md`

Results:

- scans **51–60** — full restart audit completed at enlarged/native resolution;
- new lexical discrepancy rows — **1**: WFV-010;
- unresolved new lexical pages — **1**: scan **55**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical page corrections — **2 page files**: scans **51, 57**;
- page-status promotions — **9**: scans **51–54, 56–60**;
- scan **55** — canonical `கூடிற்றாம்!` held against source-visible `கூடிற்றும்!`; page remains `needs-review`;
- prior C2 rulings on scans **51, 53, 58 and 59** preserved;
- whole-volume state now **55 verified / 441 needs-review / 1 partial**.

## R07 — scans 61–70

**COMPLETE / PASS WITH LEXICAL HOLDS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R07_SCANS_061_070.md`

Results:

- scans **61–70** — full restart audit completed at enlarged/native resolution;
- reconfirmed pre-restart rows — **2**: WFV-002 and WFV-003;
- new lexical discrepancy rows — **1**: WFV-011;
- unresolved lexical pages in this batch — **3**: scans **62, 67, 69**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **0**;
- page-status promotions — **7**: scans **61, 63–66, 68, 70**;
- scan **62** — WFV-002 refined/reconfirmed as a `தனது` token-placement discrepancy; canonical wording/placement unchanged;
- scan **67** — canonical `தேர்ஏறி!` held against source-visible `தேரேறி!`;
- scan **69** — WFV-003 reconfirmed: canonical `தலைமகனாம் என் கணவர்` vs source `தலைமகனும் என் கணவர்`;
- prior C2 rulings on scans **64 and 70** preserved;
- whole-volume state now **62 verified / 434 needs-review / 1 partial**.

## R08 — scans 71–80

**COMPLETE / PASS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R08_SCANS_071_080.md`

Results:

- scans **71–80** — full restart audit completed at enlarged/native resolution;
- new lexical discrepancy rows — **0**;
- unresolved new lexical pages — **0**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **0**;
- page-status promotions — **10**;
- prior C2 ruling on scan **77** preserved;
- earlier provisional suspicions on scans **73, 78 and 79** remain rejected after high-resolution review;
- whole-volume state now **72 verified / 424 needs-review / 1 partial**.

## R09 — scans 81–90

**COMPLETE / PASS WITH LEXICAL HOLDS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R09_SCANS_081_090.md`

Results:

- scans **81–90** — full restart audit completed at enlarged/native resolution;
- WFV-004 — **reconfirmed** on scan **83**;
- new lexical discrepancy rows — **2**: WFV-012 and WFV-013;
- unresolved lexical pages in this batch — **3**: scans **83, 85, 87**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **1 page file**: scan **88** punctuation only;
- page-status promotions — **7**: scans **81, 82, 84, 86, 88, 89, 90**;
- scan **85** — source-visible `- அவர்கள்` remains ledger-only / canonical body unchanged;
- scan **87** — source places `நல்ல` with the `அகில், மிளகு, முத்து` trade line; canonical token placement unchanged;
- prior C2 rulings on scans **83 and 87** preserved;
- whole-volume state now **79 verified / 417 needs-review / 1 partial**.

## R10 — scans 91–100

**COMPLETE / PASS WITH LEXICAL HOLDS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R10_SCANS_091_100.md`

Results:

- scans **91–100** — full restart audit completed;
- WFV-005 — **reconfirmed** on scan **91**;
- new lexical discrepancy row — **WFV-014** on scan **94**;
- unresolved lexical pages in this batch — **2**: scans **91, 94**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **0**;
- page-status promotions — **8**: scans **92, 93, 95–100**;
- prior C2 scan-96 heading and `சிவகெங்கைச் சீமை` rulings preserved;
- whole-volume state after R10 — **87 verified / 409 needs-review / 1 partial**.

## R11 — scans 101–110

**COMPLETE / PASS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R11_SCANS_101_110.md`

Results:

- scans **101–110** — full restart audit completed;
- new lexical discrepancy rows — **0**;
- unresolved new lexical pages — **0**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **0**;
- page-status promotions — **10**;
- no C2 user-adjudicated item falls inside scans **101–110**;
- whole-volume state now **97 verified / 399 needs-review / 1 partial**.

## R12 — scans 111–120

**COMPLETE / PASS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R12_SCANS_111_120.md`

Results:

- scans **111–120** — full restart audit completed;
- new lexical discrepancy rows — **0**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **0**;
- source-supported metadata alignments — **3** (scans 113–115 section metadata aligned to exact C2 heading);
- page-status promotions — **10**;
- protected C2 rulings on scans **112, 113 and 120** preserved;
- whole-volume state after R12 — **107 verified / 389 needs-review / 1 partial**.

## R13 — scans 121–130

**COMPLETE / PASS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R13_SCANS_121_130.md`

Results:

- scans **121–130** — full restart audit completed;
- new lexical discrepancy rows — **0**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **0**;
- page-status promotions — **10**;
- protected C2 scan-123 restored opening prose preserved;
- C2-06 scans 126–130 remain a no-discrepancy range;
- whole-volume state now **117 verified / 379 needs-review / 1 partial**.

## R14 — scans 131–140

**COMPLETE / PASS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R14_SCANS_131_140.md`

Results:

- scans **131–140** — full restart audit completed;
- new lexical discrepancy rows — **0**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **0**;
- page-status promotions — **10**;
- prior Gate-B extraction exclusions on scans 131 and 137 remain supported;
- C2-06 contains no discrepancy records for scans 131–140;
- whole-volume state after R14 — **127 verified / 369 needs-review / 1 partial**.

## R15 — scans 141–150

**COMPLETE / PASS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R15_SCANS_141_150.md`

Results:

- scans **141–150** — full restart audit completed;
- new lexical discrepancy rows — **0**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **0**;
- page-status promotions — **10**;
- scan 143 and scan 148 spread structures verified;
- scan 149 `மன்னன்!` placement and scan 150 `பட்டமும்` physical boundary preserved;
- C2-06 contains no discrepancy records for scans 141–150;
- whole-volume state now **137 verified / 359 needs-review / 1 partial**.

## R16 — scans 151–160

**COMPLETE / PASS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R16_SCANS_151_160.md`

Results:

- scans **151–160** — full restart audit completed;
- new lexical discrepancy rows — **0**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **0**;
- page-status promotions — **10**;
- scans 156 and 160 full-page illustrations verified;
- C2-07 contains no adjudication records within scans 151–160;
- whole-volume state after R16 — **147 verified / 349 needs-review / 1 partial**.

## R17 — scans 161–170

**COMPLETE / PASS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R17_SCANS_161_170.md`

Results:

- scans **161–170** — full restart audit completed;
- new lexical discrepancy rows — **0**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **0**;
- page-status promotions — **10**;
- scan 163 C07-001 `கொங்கர்க் குடகடல் ஓட்டிய ஞான்றைத்` preserved;
- scan 165 C07-002 heading `காடைப் போர் கண்டுவந்த கணவன்!` preserved;
- scan 170 historical `னா` identity in `கானாங் கோழி` confirmed by same-page edition evidence; no discrepancy row opened;
- whole-volume state now **157 verified / 339 needs-review / 1 partial**.

## R18 — scans 171–180

**COMPLETE / PASS WITH LEXICAL HOLDS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R18_SCANS_171_180.md`

Results:

- scans **171–180** — full restart audit completed;
- new lexical discrepancy rows — **5**: WFV-015 through WFV-019;
- unresolved lexical pages — **3**: scans **174, 177, 179**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **1**: scan 174 punctuation/spacing only;
- source-supported section-metadata alignments — **5**: scans 176–180;
- page-status promotions — **7**;
- protected C2 rulings on scans 174, 175 and 180 preserved;
- whole-volume state after R18 — **164 verified / 332 needs-review / 1 partial**.

## R19 — scans 181–190

**COMPLETE / PASS WITH LEXICAL HOLDS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R19_SCANS_181_190.md`

Results:

- scans **181–190** — full restart audit completed;
- new lexical discrepancy rows — **3**: WFV-020 through WFV-022;
- unresolved lexical pages — **2**: scans **183, 189**;
- canonical lexical substitutions — **0**;
- source-supported section-metadata alignments — **1**: scan 181;
- page-status promotions — **8**;
- protected C2 ruling on scan 188 preserved;
- whole-volume state now **172 verified / 324 needs-review / 1 partial**.

## R20 — scans 191–200

**COMPLETE / PASS WITH LEXICAL HOLDS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R20_SCANS_191_200.md`

Results:

- scans **191–200** — full restart audit completed;
- new lexical discrepancy rows — **2**: WFV-023 and WFV-024;
- unresolved lexical pages — **2**: scans **192, 195**;
- canonical lexical substitutions — **0**;
- page-status promotions — **8**;
- C08-003, C08-004 and C08-005..007 protected;
- whole-volume state after R20 — **180 verified / 316 needs-review / 1 partial**.

## R21 — scans 201–210

**COMPLETE / PASS WITH LEXICAL HOLDS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R21_SCANS_201_210.md`

Results:

- scans **201–210** — full restart audit completed;
- new lexical discrepancy rows — **2**: WFV-025 and WFV-026;
- unresolved lexical pages — **2**: scans **205, 209**;
- canonical lexical substitutions — **0**;
- page-status promotions — **8**;
- C09-001 scan-208 heading protected;
- whole-volume state now **188 verified / 308 needs-review / 1 partial**.

## R22 — scans 211–220

**COMPLETE / PASS WITH LEXICAL HOLDS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R22_SCANS_211_220.md`

Results:

- scans **211–220** — full restart audit completed;
- new lexical discrepancy rows — **3**: WFV-027 through WFV-029;
- unresolved lexical pages — **3**: scans **213, 215, 219**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **0**;
- page-status promotions — **7**;
- scans **216** and **220** full-page illustrations verified;
- whole-volume state after R22 — **195 verified / 301 needs-review / 1 partial**.

## R23 — scans 221–230

**COMPLETE / PASS WITH LEXICAL HOLDS**

Durable report: `TAMIL_WORD_FOR_WORD_REAUDIT_R23_SCANS_221_230.md`

Results:

- scans **221–230** — full restart audit completed;
- new lexical discrepancy rows — **3**: WFV-030 through WFV-032;
- unresolved lexical pages — **2**: scans **227, 230**;
- canonical lexical substitutions — **0**;
- source-supported non-lexical body corrections — **0**;
- page-status promotions — **8**;
- protected C2 rulings on scans **221, 223, 226 and 230** preserved;
- whole-volume state now **203 verified / 293 needs-review / 1 partial**.

## Pre-restart Part002 candidate rows

The earlier interrupted Part002 review is **not counted as completed restart coverage**.

WFV-002 and WFV-003 were **R07 reconfirmed / pending user adjudication**, WFV-004 was **R09 reconfirmed**, and WFV-005 was **R10 reconfirmed**. There are now **no unreconfirmed pre-restart Part002 candidate rows**.

Do not change any pending lexical wording before explicit user adjudication.

## 10-page iteration plan

| Iteration | Scans | State |
|---|---:|---|
| R01 | 1–10 | **COMPLETE / PASS** |
| R02 | 11–20 | **COMPLETE / PASS** |
| R03 | 21–30 | **COMPLETE / PASS WITH LEXICAL HOLDS** |
| R04 | 31–40 | **COMPLETE / PASS** |
| R05 | 41–50 | **COMPLETE / PASS WITH LEXICAL HOLD** |
| R06 | 51–60 | **COMPLETE / PASS WITH LEXICAL HOLD** |
| R07 | 61–70 | **COMPLETE / PASS WITH LEXICAL HOLDS** |
| R08 | 71–80 | **COMPLETE / PASS** |
| R09 | 81–90 | **COMPLETE / PASS WITH LEXICAL HOLDS** |
| R10 | 91–100 | **COMPLETE / PASS WITH LEXICAL HOLDS** |
| R11 | 101–110 | **COMPLETE / PASS** |
| R12 | 111–120 | **COMPLETE / PASS** |
| R13 | 121–130 | **COMPLETE / PASS** |
| R14 | 131–140 | **COMPLETE / PASS** |
| R15 | 141–150 | **COMPLETE / PASS** |
| R16 | 151–160 | **COMPLETE / PASS** |
| R17 | 161–170 | **COMPLETE / PASS** |
| R18 | 171–180 | **COMPLETE / PASS WITH LEXICAL HOLDS** |
| R19 | 181–190 | **COMPLETE / PASS WITH LEXICAL HOLDS** |
| R20 | 191–200 | **COMPLETE / PASS WITH LEXICAL HOLDS** |
| R21 | 201–210 | **COMPLETE / PASS WITH LEXICAL HOLDS** |
| R22 | 211–220 | **COMPLETE / PASS WITH LEXICAL HOLDS** |
| R23 | 221–230 | **COMPLETE / PASS WITH LEXICAL HOLDS** |
| R24–R49 | 231–490 | pending in 10-scan cadence |
| R50 | 491–497 | final 7-scan remainder |

## Exact next activity

Process **R24 + R25 — scans 231–250** as the next **20-page iteration** using Part005 PDF pages **31–50**.

At R25 close:

- inspect all scans at enlarged/native resolution;
- apply the historical-glyph guide and check all 13 known families where present;
- preserve explicit C2 adjudications on scans **237, 240 and 248**;
- record every new lexical/glyph/material-placement difference in the discrepancy ledger;
- change **0 lexical words without user adjudication**;
- apply only source-supported non-lexical structure/punctuation/layout changes;
- synchronize this tracker, README, HANDOVER, English-release pause state and `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`.
