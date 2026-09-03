# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை மூல ஸ்கேனை controlling source ஆகக் கொண்டு பக்கவாரியாக பாதுகாக்கும் பகுதி.

## Current source state

The user reports the original PDF as **666 physical pages** and has manually split it into **six parts of 111 pages each** for upload.

Canonical overall scan mapping:

| Part | Overall scans | Supplied state | Tamil archival state |
|---|---:|---|---|
| 001 | 1–111 | **supplied** — `TVA_BOK_0065733_குறளோவியம்_part_001_pages_1-111.pdf` | source intake complete; **Pass 1 captured through scan 30** |
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

New Pass-1 page records normally remain `needs-review`. Genuinely unreadable handwritten facsimiles may remain `partial` rather than being guessed.

## Part 001 Pass 1 progress

**Scans 1–30 are captured continuously as 30 page-aligned Markdown records.**

Current record sequence:

- scans **1–3** — cover / title-publisher / edition-imprint matter;
- scans **4–8 / printed iii–vii** — `முகப்புரை`;
- scans **9–12 / printed viii–xi** — `மதிப்புரை`, through its conclusion;
- scans **13–15 / printed xii–xiv** — handwritten/facsimile preface material; retained `partial` where word-for-word handwriting cannot safely be established;
- scan **16 / printed xv** — first-edition photograph and commemorative note;
- scan **17 / printed xvi** — `ஆறாம் பதிப்பின் பதிப்புரை`;
- scans **18–20 / printed 1–3** — `பேராசிரியர்`;
- scan **21 / printed 4** — `மகா வித்துவான் தண்டபாணி தேசிகர்`;
- scans **22–23 / printed 5–6** — `டாக்டர் வ.சுப.மாணிக்கம்`;
- scan **24 / printed 7** — `மதுரை யாதவர் கல்லூரி முதல்வர் தமிழ்க்குடிமகன்`;
- scan **25 / printed 8** — `காசி ஆனந்தன்`;
- scans **26–27 / printed 9–10** — `ஆட்சிமொழிக் காவலர் இராமலிங்கனார்`;
- scan **28 / printed 11** — `ஆசிரியர் சாவி`;
- scan **29 / printed 12** — `டாக்டர் மெ.சுந்தரம்`;
- scan **30 / printed 13** — `டாக்டர் மா.நன்னன்`.

Scans 1–12 and 16–30 remain `needs-review` / `visual_fidelity: needs-review` as required by Pass 1. Scans 13–15 are intentionally `partial` because the handwritten body is not safely legible word-for-word from the supplied scan; no handwriting was reconstructed from context.

## Batch audits

### Scans 1–10

The earlier page-batch audit confirmed 10 sequential page commits and exactly 10 page records for scans 1–10.

### Scans 11–20

Batch base → page-head:

`1700e1d93cf55830f3b477702b43852d33cca341` → `5b67f778ac6d1f45c2a6632a6546f115c04bea57`

GitHub comparison confirmed **10 sequential commits** adding exactly the expected page records for scans **11–20** and no unrelated files in the page batch.

### Scans 21–30

Batch base → page-head:

`32c71ef540509e881dcc5bb38ccdff92f7642c1d` → `1bea805eea734ad25941ebe5d19796507ebd6323`

GitHub comparison confirmed **10 sequential commits** adding exactly the expected page records for scans **21–30** and no unrelated files in the page batch.

## Current status

**Part 001 source intake: COMPLETE.**

**Part 001 Pass 1: scans 1–30 COMPLETE; scans 31–111 pending.**

No textual verification, meaningful visual verification, part audit or English translation is being claimed yet.

## Next activity

Continue **Part 001 Pass 1** with **overall scans 31–40**:

- continue directly from printed page 13 into the next source page/section;
- create exactly one Markdown record per physical scan;
- preserve source-visible wording only;
- preserve illustrations and their relationship to surrounding prose;
- preserve printed pagination only when visible;
- leave new records `needs-review` unless a genuine source limitation requires `partial` or `blocked`;
- audit the changed-file set before advancing to the next batch.
