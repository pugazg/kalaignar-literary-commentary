# Kuraloviyam Derived Sections — S3 Completion Report

## Decision

**S3 — COMPLETE / PASS.**

S3 adds one stable leaf record per Kuraloviyam contents entry and a web-ready navigation/index layer without reopening the closed archival or maintained-English page layers.

S2 closed base:

`93a9f80ce93cb4a15be5537767ba89fc800d067f`

S3 content endpoint before documentation sync:

`30c700ba8a76165550b12b989b0d4aa608089065`

## S3 outputs

Under `works/kuraloviyam/sections/entries/`:

- individual entry leaf records — **300/300**;
- `README.md` — human-readable entry index;
- `index.json` — structured web/API index;
- `index.tsv` — compact tabular index;
- `BY_CHAPTER.md` — Chapter-grouped entry navigation.

Each entry leaf records:

- exact contents key;
- printed-page span;
- overall scan span;
- S2 status;
- source-evidenced Adhikaram/Kural assignment(s);
- direct Book/Iyal/Adhikaram navigation link(s);
- direct links to every audited Tamil page in the entry span;
- direct links to every maintained English page in the same span.

## Chapter-link integration

All **121 source-evidenced Adhikaram files** were refreshed so their entry tables now link directly to the S3 leaf records.

Relative navigation links to the S2 crosswalk and S3 entry index were also normalized at this gate.

## Preserved S2 evidence limitations

S3 does not alter S2 evidence decisions.

- entry **46** — **PARTIAL-SOURCE-METADATA**;
- entry **104** — **PARTIAL-SOURCE-METADATA**;
- entry **202** — source-proven shared-page overlap through printed page **435 / scan 452**;
- unresolved entries — **0**;
- source-evidenced Chapter numbers — **121/133**;
- non-evidenced Chapter numbers — **1, 18, 22, 25, 44, 52, 70, 76, 86, 91, 106, 107**.

No outside Kural numbering was inferred.

## Exact S3 change audit

S3 consists of four content commits:

1. `a093335adaeb62fb150913f0c64906a41bb25adb` — **100** entry leaves, entries 001–100;
2. `bb85f4206b6e93a426953a491b7f68f5e830695d` — **100** entry leaves, entries 101–200;
3. `40a06ec079fdd2924fc96b8f3d15c21ca63ccf1b` — **100** entry leaves, entries 201–300;
4. `30c700ba8a76165550b12b989b0d4aa608089065` — **125** section files: 4 entry-index files + 121 Adhikaram files.

Per-commit compare audits:

- each commit — **1 ahead / 0 behind**;
- changed files — **100 / 100 / 100 / 125**;
- changed files outside `works/kuraloviyam/sections/` — **0**;
- Tamil archival page files changed — **0**;
- maintained English page files changed — **0**.

Total S3 file writes — **425**, all within the derived `sections/` layer.

## Final decision

**S3 COMPLETE / PASS.**

The section/navigation layer now supports both human reading and machine consumption while preserving all closed source-fidelity decisions.

There is no required next section stage.
