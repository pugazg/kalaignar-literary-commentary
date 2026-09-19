# Sangatamil — Tamil Word-for-Word Audit / Verification Tracker

**Status: IN PROGRESS**

- started: **2026-09-19**
- controlling source for comparison: user-supplied split PDFs from `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`
- lexical authority: **Gemini-locked canonical wording + prior explicit user adjudications**
- structural/visual authority: **PDF scan**
- discrepancy ledger: `LEXICAL_DISCREPANCY_LEDGER.md`
- scope: canonical Tamil pages currently marked `needs-review`
- permanent exception: scan **8** remains `partial` / handwritten facsimile unless the user explicitly changes that policy

## Governing rule — user corrected 2026-09-19

This pass is **word-for-word comparison, not automatic source correction**.

For every page entering this pass:

1. compare every printed word against the supplied source scan;
2. **do not replace, normalize, modernize or source-correct Gemini/canonical words directly**;
3. any newly discovered lexical/word discrepancy must be appended to `LEXICAL_DISCREPANCY_LEDGER.md`;
4. lexical wording changes require a later explicit user adjudication;
5. source-supported structure may still be corrected: page placement, paragraph order, punctuation, quotation structure, headings, speaker labels, poetry lineation, spacing, separators, continuation placement, illustration/divider/blank classification and provenance/gloss layout;
6. a page with an unresolved lexical discrepancy remains `needs-review`;
7. a clean page may be promoted to `verified` only after its full word-by-word comparison plus structural/visual audit passes;
8. `visual_fidelity` follows the physical/visual audit independently;
9. do not reopen pages already `verified` unless the user expands scope or a clear new problem is discovered.

The historical Gemini lock is therefore **active for lexical wording during this pass**. The PDF is used to detect discrepancies and to control structure; it does not silently overrule Gemini words.

## Policy repair after Part001

The earlier Part001 closure mistakenly treated the source scan as direct lexical authority on scan 7.

That unauthorized lexical change has been **reverted**. Scan 7 returns to its pre-pass canonical wording/state and the newly noticed publisher-name difference is now recorded in the lexical discrepancy ledger instead.

Part001 now stands:

- prior `needs-review` pages examined — **6: scans 7, 31, 33, 34, 35, 36**
- promoted to `verified` — **5: scans 31, 33, 34, 35, 36**
- unresolved lexical hold — **1: scan 7**
- direct new lexical substitutions retained — **0**
- structural-only changes retained — **scans 31 and 34**
- scan 8 — remains `partial`

Part001 state:

- `verified` — **48**
- `needs-review` — **1** (scan 7)
- `partial` — **1** (scan 8)

Whole-volume state after policy repair:

- `verified` — **48**
- `needs-review` — **448**
- `partial` — **1**
- blocked — **0**

## New discrepancy additions from this pass

Newly detected lexical differences are **ledger-only until user adjudication**.

Current new rows:

- scan **7** — canonical `ராக்போர்ட்` vs source-visible `ராக்ஃபோர்ட்`;
- scan **62** — source contains lexical token `தனது` before `பாதம் படுகின்ற...`, absent from canonical wording;
- scan **69** — canonical `தலைமகனாம்` vs source-visible `தலைமகனும்`;
- scan **83** — canonical `ஆழல்` vs source-visible `ஆனால்`;
- scan **91** — canonical `வாராத` vs source-visible `வராத`.

These rows do **not** authorize page-wording changes.

## Part002 progress

Source supplied:

`TVA_BOK_0042551_சங்கத்_தமிழ்_part_002_pages_51-100.pdf`

All **50 scans 51–100** are currently `needs-review` and therefore belong to this audit unit.

Durable progress at this checkpoint:

- scans **51–96** — source comparison performed;
- new lexical discrepancies confirmed — **4 pages: 62, 69, 83, 91**;
- those lexical differences — **ledger-only / no direct page wording mutation**;
- structural observations may be applied only if they do not alter lexical wording;
- scans **97–100** — exact next comparison range;
- Part002 page-status promotions — **not yet committed**.

Earlier provisional suspicions on scans **59, 73, 78 and 79** were rejected after higher-resolution source review and must **not** be turned into lexical corrections or ledger rows.

## Source-part progress

| Source part | Scans | State |
|---|---:|---|
| Part001 | 1–50 | **AUDIT COMPLETE — 5 verified / 1 lexical hold / scan8 partial** |
| Part002 | 51–100 | **IN PROGRESS — scans51–96 compared; 97–100 next** |
| Part003 | 101–150 | pending source |
| Part004 | 151–200 | pending source |
| Part005 | 201–250 | pending source |
| Part006 | 251–300 | pending source |
| Part007 | 301–350 | pending source |
| Part008 | 351–400 | pending source |
| Part009 | 401–450 | pending source |
| Part010 | 451–497 | pending source |

## Exact next activity

Continue **Part002 scans 97–100**.

At Part002 closure:

1. do not change any lexical word merely because the scan differs;
2. append every newly confirmed lexical difference to `LEXICAL_DISCREPANCY_LEDGER.md`;
3. apply only source-supported non-lexical structural/punctuation/layout corrections;
4. promote only clean fully audited pages to `verified`;
5. leave pages with unresolved lexical discrepancies as `needs-review`;
6. create/update the Part002 audit report;
7. synchronize `README.md`, `HANDOVER.md`, `NEXT_CHAT_PROMPT_SANGATH_TAMIL.md`, tracker and English-release pause controls.
