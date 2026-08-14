# English Translation Status — Thirukkural: Kalaignar's Commentary

## Translation identity

- type: **project-created English translation**
- official/publisher English source supplied: **no**
- controlling source: supplied Tamil scans
- working basis: audited Tamil archival page records
- translation framework established: **yes**

## Current source readiness

| Tamil part | Overall scans | Tamil state | English state |
|---|---:|---|---|
| Part 001 | 1–20 | archival-ready; scan 8 documented partial | **12 English records created: 11 drafts + 1 source-limited** |
| Part 002 | 21–41 | archival-ready | not started |
| Part 003 | 42–62 | archival-ready | not started |

## Current English counts

- English page files: **12**
- `draft`: **11** — scans 1–7 and 9–12
- `source-checked`: **0**
- `editorial-reviewed`: **0**
- `release-ready`: **0**
- `source-limited`: **1** — scan 8 handwritten facsimile
- `blocked`: **0**

## Part 001 progress

### Completed first-pass drafts — scans 1–7

Matching English files exist for the cover, title page, blank-page record, publication details, edition details, contents, and Kalaignar's Preface.

### Source-limited record — scan 8

`0008-handwritten-note.md` uses `status: "source-limited"` because the controlling Tamil archival record is itself `partial`. It translates only securely established elements and does not reconstruct the unreadable continuous handwriting.

### Completed first-pass drafts — scans 9–12

Matching English files now exist for all four pages of `பேராசிரியரின் அணிந்துரை` / **The Professor's Foreword**:

- scan 9 / printed viii — `0009-aninthurai-01.md`;
- scan 10 / printed ix — `0010-aninthurai-02.md`;
- scan 11 / printed x — `0011-aninthurai-03.md`;
- scan 12 / printed xi — `0012-aninthurai-04.md`.

All four remain `draft`. The first pass preserves the poem-like line structure, source quotations and emphatic lines rather than converting the foreword into prose.

Source-sensitive translation choices recorded in this batch include:

- `முப்பால்` retained as **Muppaal** pending part-level review;
- source form `திருவிடம்` retained as **Tiruvidam** rather than silently replacing it with a different Tamil form;
- `ஊழ்` retained as **oozh** in the foreword where the source explicitly discusses the term;
- names and political/cultural honorifics such as Periyar, Anna and Anbazhagan retained in source-supported form.

No English page has yet completed the separate source-check or editorial-review stages.

### Remaining Part 001 first-pass work

1. scans 13–20 — `மதிப்புரை` / Critical Appreciation and related literary-analysis front matter;
2. source-check pass for all translatable Part 001 English pages;
3. editorial consistency review and glossary reconciliation;
4. `PART_001_RELEASE_REPORT.md`.

## Part 002 plan

After Part 001 English release review:

1. scans 21–33 — remaining front matter, indexes, section title and blank verso;
2. scans 34–41 — Kural 1–40 + Kalaignar commentary;
3. source-check and editorial review;
4. Part 002 translation release report.

## Part 003 plan

After Part 002 English release review:

1. scans 42–62 — Kural 41–145 + Kalaignar commentary;
2. source-check and editorial review;
3. Part 003 translation release report.

## Future cadence

For every newly supplied Tamil PDF after Part 003:

**Tamil transcription → Tamil verification → Tamil audit → English draft → English source check → editorial review → translation release report.**

Do not wait until all 1,330 Kurals are archived before translating newly audited parts.

## Next exact activity

Create Part 001 English first-pass `draft` files for **scans 13–20**, covering `மதிப்புரை` and the literary-analysis front matter.

Rules:

- mirror Tamil filenames exactly under `translations/en/pages/`;
- translate only the audited Tamil source content;
- preserve headings, quotations, Kural citations, paragraph structure and source-supported emphasis;
- keep all new files `draft` during first-pass creation;
- add translation notes only where a source-specific form materially affects interpretation;
- do not source-check or editorially promote the pages in the same activity.
