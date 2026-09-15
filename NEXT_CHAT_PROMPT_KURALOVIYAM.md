# NEXT CHAT PROMPT — குறளோவியம் / Part 006 English Source-Check SC3

Continue directly in `pugazg/kalaignar-literary-commentary`, branch `main`, active work `works/kuraloviyam/`. **LIVE MAIN IS AUTHORITATIVE.**

## Closed Parts

Parts **001–005 are fully closed**. Do not reopen them.

## Part 006 Tamil authority

Part 006 Tamil is:

**ARCHIVAL-READY / CLOSED — 111/111 textual verified + 111/111 visual verified / 0 exceptions.**

Normal English source-check authority is the audited Tamil page layer:

`works/kuraloviyam/pages/`

The controlling PDF is reopened only if a genuinely new provenance/fidelity issue appears.

## English workflow policy

Read and preserve:

- `works/kuraloviyam/translations/en/TRANSLATION_GUIDE.md`;
- `works/kuraloviyam/translations/en/GLOSSARY.md`;
- `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`;
- `works/kuraloviyam/translations/en/README.md`.

Translation identity:

**project-created English translation**

Permanent gate order:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**

Current user-directed normal batch size:

**37 physical scans per iteration**

## Part 006 drafting — COMPLETE / CLOSED 111/111

- D1 — scans **556–592 / printed 539–575** — **COMPLETE / PASS 37/37**;
- D2 — scans **593–629 / printed 576–612** — **COMPLETE / PASS 37/37**;
- D3 — scans **630–666 / printed 613–648 + unnumbered back cover** — **COMPLETE / PASS 37/37**.

## Part 006 Source-Check SC1 — COMPLETE / PASS 37/37

- scans **556–592 / printed 539–575**;
- page-layer base — `0b3d8a701d5db04164f969b15d1d0090622cc664`;
- endpoint — `8baca75a8efd00db5a05de425305f244c1c19120`;
- exact compare — **3 commits / exactly 37 modified English page files / 0 non-page changes / 0 Tamil changes**;
- fidelity repairs — **16 page files**;
- status-only promotions — **21 page files**.

## Part 006 Source-Check SC2 — COMPLETE / PASS 37/37

SC2 range:

**scans 593–629 / printed 576–612**

SC2 page-layer base:

`ce140cb9a2b23b860772ee649de473ffde8fc9dc`

SC2 page-layer endpoint:

`0c2d08993de3ba3d8b4df9c8bd5fe12b58ed22c0`

Exact SC2 compare:

- **3 commits ahead / non-divergent**;
- exactly **37 modified English page files**;
- scans **593–629** represented exactly once;
- missing scans — **0**;
- duplicate scans — **0**;
- Tamil page changes — **0**;
- non-English-page/control-file changes during the SC2 page layer — **0**;
- `source-checked` — **37/37**;
- `source_tamil_status: "verified"` — **37/37**;
- `translation_type: "project_translation"` — **37/37**.

SC2 source-fidelity repairs:

- **603–604** — restored audited physical split at `இப்போது மணவிழா / என்றைக்கென்று...`;
- **608–609** — restored audited physical split at `ஆணவமான சொற்களைத் தங்கு தடையின்றிப் / மொழிகிறாய்!`;
- **610–611** — restored audited physical split at `செய்தி குறுநில / மன்னன் செவிக்கு எட்டியது`;
- **615** — restored the source's `குறை / கறை` distinction by changing the premature “hands without stain” wording to **“faultless hands”**;
- **620** — direct rendered-source recheck confirmed `அவன் பாடியது! அவனும் இணைந்து பாடியது!`; English now follows the printed source rather than silently normalizing the apparent contextual inconsistency.

SC2 correction pages:

**603, 604, 608, 609, 610, 611, 615, 620**

The other **29** pages changed only by `draft` → `source-checked`.

SC2 boundaries:

- incoming **592→593 CLEAN** preserved;
- outgoing **629→630 GENUINE CONTINUATION** preserved.

Current Part-006 English state:

- `source-checked` — **74**;
- `draft` — **37**;
- `editorial-reviewed` — **0**;
- `release-ready` — **0**;
- `source-limited` — **0**;
- `blocked` — **0**.

## Exact next activity — Source-Check SC3

Process exactly:

**scans 630–666 — 37 physical scans**

Coverage:

- scans **630–665** = printed **613–648**;
- scan **666** = **unnumbered pictorial back cover**.

Incoming boundary:

- **629→630 GENUINE CONTINUATION**;
- scan 630 continues the lover-in-the-heart vignette begun on scan 629.

Backmatter/source endpoint:

- scans **658–665** = complete `பொருளடக்கம்` / contents-index run;
- scan **665** contains the fourth-edition orthography note plus a non-source library stamp;
- **665→666 CLEAN / PHYSICAL SOURCE ENDPOINT**;
- scan **666** = unnumbered pictorial back cover;
- **666 — NO EXTERNAL CONTINUATION**.

## Source-check discipline

For every page, compare the English record directly against its audited Tamil counterpart:

- paragraph-by-paragraph;
- dialogue turn by dialogue turn;
- Kural block by Kural block;
- metadata and glosses;
- factual visual/non-body material;
- contents/index structure;
- source/page-function notes where relevant;
- cross-page continuations.

Check specifically for:

- omissions;
- unsupported additions;
- meaning drift;
- lost rhetorical repetition;
- names and relationship terms;
- chapter labels and Kural numbers;
- quoted Kural lineation;
- source glosses;
- page alignment;
- continuity across physical page boundaries;
- index-entry completeness on scans **658–665**;
- no invented body prose on scan **666**.

A passing page may move only:

`status: "draft"` → `status: "source-checked"`

Do not promote any page with a remaining fidelity problem.

Source-check is not a stylistic rewrite gate. Make only corrections required for fidelity to the audited Tamil/source structure.

Do not import published, standard, web, or remembered English Kural wording.

## Required SC3 completion audit

After SC3:

- confirm **37/37** pages scans **630–666** have been directly source-checked;
- confirm all **111/111 Part-006 English pages** are now `source-checked`;
- confirm `draft` becomes **0**;
- record every wording/structure correction by scan;
- compare the pre-SC3 page-layer base to the SC3 endpoint;
- require changes only inside `works/kuraloviyam/translations/en/pages/`;
- confirm **0 Tamil page changes**;
- preserve **658–665 contents**, **665→666 CLEAN / PHYSICAL SOURCE ENDPOINT**, and **666 NO EXTERNAL CONTINUATION**;
- update `TRANSLATION_STATUS.md` and relevant control docs.

After SC3 closes, Part-006 English source-check is **COMPLETE / CLOSED 111/111**.

The next gate is **Part 006 English glossary reconciliation**, using the same **37-page** cadence unless live repository policy says otherwise.
