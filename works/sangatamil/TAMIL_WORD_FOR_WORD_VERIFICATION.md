# Sangatamil — Tamil Word-for-Word Verification Tracker

**Status: IN PROGRESS**

- started: **2026-09-19**
- controlling source: user-supplied split Tamil PDFs from `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`
- repository: `pugazg/kalaignar-literary-commentary`
- branch: `main`
- scope: pages whose canonical Tamil `status` is `needs-review`
- permanent exception: scan **8** remains `partial` / handwritten facsimile unless the user explicitly changes that policy

## Governing rule

This is a new source-first verification pass authorized by the user after Gate I and after the maintained-English whole-volume review.

For every page entering this pass:

1. the supplied PDF scan is the controlling authority for printed Tamil wording;
2. compare every printed word, punctuation mark, quotation boundary, heading, verse line, provenance/gloss block, visible page function and cross-page continuation;
3. correct canonical Tamil when the scan supports the correction;
4. promote only a fully checked page from `needs-review` to `verified`;
5. set `visual_fidelity: "verified"` only after the physical/visual presentation is checked;
6. do not reopen pages already `verified` unless the user expands scope or a new clear defect is discovered;
7. record any canonical correction for later English impact reconciliation before English release.

The historical Gemini lexical lock remains historical evidence but does **not** override the user-supplied scan for pages processed in this new pass.

## Volume state

Historical Gate-G baseline:

- `verified` — **43**
- `needs-review` — **453**
- `partial` — **1**
- visual `verified` — **43**
- visual `needs-review` — **454**

Current state after Part001:

- `verified` — **49**
- `needs-review` — **447**
- `partial` — **1**
- visual `verified` — **49**
- visual `needs-review` — **448**
- blocked — **0**

Whole-volume word-for-word verification is **IN PROGRESS**, not yet complete.

## Source-part progress

| Source part | Scans | Prior needs-review pages | Verified in this pass | Canonical corrections | Result |
|---|---:|---:|---:|---:|---|
| Part001 | 1–50 | 6 | 6 | 3 pages | **COMPLETE / PASS** |
| Part002 | 51–100 | pending source | — | — | **NEXT** |
| Part003 | 101–150 | pending source | — | — | pending |
| Part004 | 151–200 | pending source | — | — | pending |
| Part005 | 201–250 | pending source | — | — | pending |
| Part006 | 251–300 | pending source | — | — | pending |
| Part007 | 301–350 | pending source | — | — | pending |
| Part008 | 351–400 | pending source | — | — | pending |
| Part009 | 401–450 | pending source | — | — | pending |
| Part010 | 451–497 | pending source | — | — | pending |

## Part001 closure

Durable report: `TAMIL_WORD_FOR_WORD_PART001_REPORT.md`

Prior `needs-review` pages:

- scan **7**
- scan **31**
- scan **33**
- scan **34**
- scan **35**
- scan **36**

All six are now **verified / visual verified**.

Canonical corrections:

- scan **7** — restored source-visible `ராக்ஃபோர்ட்` publisher spelling and exact printed punctuation/spacing in the publication-details table;
- scan **31** — restored exact verse lineation around `அஃதேபோல்` and the printed dash in `கவிக்கோ - தமிழர்`;
- scan **34** — moved `அதுவரையில்` to its exact source position inside the closing speech, immediately before `காதல் எல்லை...`.

Scans **33, 35 and 36** required no canonical wording or structural correction after direct source verification.

Scan **8** remains `partial`; it was not in the user-requested `needs-review` scope.

## Exact next activity

Receive and process **Part002 — scans 51–100**, reviewing only the pages currently marked `needs-review` against the supplied source PDF.
