# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை மூல ஸ்கேனை controlling source ஆகக் கொண்டு பக்கவாரியாக பாதுகாக்கும் பகுதி.

## Current source state

The user reports the original PDF as **666 physical pages** and has manually split it into **six parts of 111 pages each** for upload.

Canonical overall scan mapping:

| Part | Overall scans | Supplied state | Tamil archival state |
|---|---:|---|---|
| 001 | 1–111 | **supplied** — `TVA_BOK_0065733_குறளோவியம்_part_001_pages_1-111.pdf` | source intake complete; **Pass 1 captured through scan 10** |
| 002 | 112–222 | not yet supplied | not-started |
| 003 | 223–333 | not yet supplied | not-started |
| 004 | 334–444 | not yet supplied | not-started |
| 005 | 445–555 | not yet supplied | not-started |
| 006 | 556–666 | not yet supplied | not-started |

Repository scan numbering always follows the **overall 1–666 sequence**. It never restarts for a split PDF.

## Part 001 source intake

Confirmed from the supplied 111-page Part 001:

- scan **1** — front cover, title `குறளோவியம்`, author `கலைஞர் மு. கருணாநிதி`;
- scan **2** — title/publisher page with `பாரதி பதிப்பகம்`;
- scan **3** — edition/imprint page; the printed edition list runs from First Edition February 1985 through Tenth Edition September 2018; visible price `ரூ.1200.00`;
- scans **4–17** — front matter, including `முகப்புரை`, `மதிப்புரை`, handwritten/facsimile preface material, later-edition preface material and a photograph page;
- scan **18** — main body begins, printed page **1**, heading `பேராசிரியர்`;
- scan **111** — printed page **94**;
- Part 001 contains **111/111 physical pages** in the supplied split.

The file environment exposes no usable parsed text layer for this PDF. Direct rendered-page inspection is therefore mandatory.

## Workflow

Use [`../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md`](../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md).

Part cadence:

1. source intake;
2. Pass 1 physical capture/transcription across all 111 scans;
3. Pass 2 textual verification;
4. Pass 3 meaningful visual-text verification;
5. Part audit;
6. optional English layer only after Tamil archival readiness.

New Pass-1 page records normally remain `needs-review`.

## Part 001 Pass 1 progress

**Scans 1–10 are captured as 10/10 page-aligned Markdown records.**

Current records:

- scans **1–3** — cover / title-publisher / edition-imprint matter;
- scans **4–8 / printed iii–vii** — `முகப்புரை`;
- scans **9–10 / printed viii–ix** — `மதிப்புரை` opening and continuation.

All ten records remain `needs-review` / `visual_fidelity: needs-review`, as required by the Pass-1 gate. Scan 3 preserves the handwritten numeric mark separately from printed text; scan 4 separately records the library stamp; scan 8 separately records the handwritten signature mark.

Batch audit from the source-intake checkpoint confirmed **10 sequential Pass-1 commits and exactly 10 page records** under `pages/`.

## Current status

**Part 001 source intake: COMPLETE.**

**Part 001 Pass 1: scans 1–10 COMPLETE; scans 11–111 pending.**

No textual verification, meaningful visual verification, part audit or English translation is being claimed yet.

## Next activity

Continue **Part 001 Pass 1** with **overall scans 11–20**:

- continue `மதிப்புரை` through its source boundary and preserve the remaining front-matter transitions;
- create exactly one Markdown record per physical scan;
- preserve source-visible wording only;
- distinguish printed text from handwriting/stamps/illustrations;
- preserve roman/Arabic printed pagination only when visible;
- leave new records `needs-review` unless a genuine source limitation requires `partial` or `blocked`;
- audit the changed-file set before advancing to the next batch.
