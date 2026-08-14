# Part 001 English Translation Release Report

## Release scope

This report closes the English project-translation workflow for Tamil Part 001, overall scans **1–20**.

- translation type: `project_translation`;
- controlling authority: supplied Tamil scans and their audited archival records;
- aligned English records: **20 / 20**;
- fully translatable pages: **19** — scans 1–7 and 9–20;
- source-limited page: **1** — scan 8 handwritten facsimile;
- external/published English Thirukkural translations used: **none**.

## Release-gate checks

### 1. Page alignment

**PASS.** One English record exists for every Part 001 overall scan **1–20**, with filenames aligned one-to-one to the Tamil archival records.

### 2. Review completion

**PASS.** Before release promotion, all 19 fully translatable pages had completed both source-check and the Part 001 editorial-consistency / glossary-reconciliation pass documented in [`PART_001_REVIEW.md`](PART_001_REVIEW.md).

Following this release gate, scans **1–7 and 9–20** are `status: "release-ready"`.

### 3. Scan 8 source limitation

**PASS WITH DOCUMENTED SOURCE LIMITATION.** Scan 8 remains `status: "source-limited"` because the controlling Tamil facsimile is itself `partial`.

The English record represents only the securely established material:

- title **An Introduction to the Preface!**;
- decorative divider presence;
- Kalaignar's signature presence;
- date **27/12/2007**;
- page-condition / reverse-side bleed-through description.

The continuous handwritten body remains untranslated and unreconstructed. Release does not override this limitation.

### 4. Terminology and glossary consistency

**PASS.** The release agrees with `GLOSSARY.md` and `PART_001_REVIEW.md` on the controlled Part 001 treatments, including:

- `முப்பால்` → **Muppaal**;
- verified source form `திருவிடம்` → **Tiruvidam**;
- `ஊழ்` → **Oozh** as a heading/concept title and *oozh* in running discussion where the Tamil term itself is named;
- `இயற்கை நிலை` → **natural condition** only where Professor Nannan explicitly attributes that meaning to Kalaignar;
- `வாயுறை` → **counsel**;
- `பெண்வழிச் சேறல்` → **Following a Woman's Lead**;
- `பிறிது மொழிதல்` → ***pirithu mozhithal*** with the gloss “saying one thing in order to convey another”;
- `பா நலம்` → **Poetic Quality**;
- `அணி நலம்` → **Excellence of Poetic Figure**;
- `அடை நலம்` → **Excellence of Epithets**.

The distinction between source title **Invocation to God** (`கடவுள் வாழ்த்து`) and Kalaignar's adopted title **Worship** (`வழிபாடு`) remains intentional.

### 5. Scan 19 retained Tamil phrase

**PASS WITH DOCUMENTED EDITORIAL RETENTION.** The phrase `அடுத்தூர்வது அஃதொப்பதில்` remains exactly in Tamil in the English scan-19 record.

The prior speculative English expansion was withdrawn during source-check. Editorial review confirmed that the immediate audited source does not establish a sufficiently secure English rendering and that importing an external Kural translation or another commentator would violate the source-controlled translation policy.

This is therefore an intentional, visible editorial retention rather than a hidden omission or blocked review item. Scan 19 remains eligible for `release-ready` status with that note preserved.

### 6. Quoted Kural examples on scan 20

**PASS.** Kurals **1101, 1098 and 17** and their adjacent Kalaignar explanations remain project translations based on this archived Tamil source. No published/external English Kural wording was substituted during source-check, editorial review or release.

### 7. Status integrity after release

**PASS.** Final Part 001 English status is:

- `release-ready`: **19** — scans 1–7 and 9–20;
- `source-limited`: **1** — scan 8;
- `editorial-reviewed`: **0**;
- `source-checked`: **0**;
- `draft`: **0**;
- `blocked`: **0**.

## Release decision

**RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS.**

The **19 fully translatable Part 001 English pages are release-ready**. Scan 8 is included in the aligned Part 001 English layer as a documented `source-limited` facsimile record and is not falsely promoted. Scan 19's retained Tamil phrase is explicitly documented and does not conceal an unresolved source-fidelity problem.

Part 001 has therefore completed the full English workflow:

**English first pass → source-check → editorial consistency review → release gate.**

## Next activity

Begin **Part 002 English first-pass translation**, starting with overall scans **21–27**:

- scans 21–26 — continuation and completion of Professor Ma. Nannan's `மதிப்புரை` / **Critical Appreciation**;
- scan 27 — `பதிப்புரை` / **Publisher's Note**.

Create one-to-one English files matching the existing Tamil filenames, initially as `draft`, and continue using the Part 001 controlled glossary unless the new source context requires a deliberately documented addition or revision.

Do not begin main-body Kural 1–40 translation until the Part 002 front-matter sequence is handled in order.
