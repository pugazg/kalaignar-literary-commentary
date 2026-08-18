# அதிகாரம் README policy

Last synchronized with the completed semantic mapping: **2026-08-18**.

Each of the 133 அதிகாரம் directories in `works/thirukkural/structure/` is a semantic navigation/provenance node. The semantic layer points back to the physical-page archives; it never replaces them.

## Required semantic content

A completed chapter README must identify, either as explicit labelled fields or in an equivalent provenance table/prose layout:

- பால் / Section;
- இயல் / Chapter group;
- அதிகாரம் number and source-controlled title;
- the deterministic ten-Kural range: `(chapter − 1) × 10 + 1` through `chapter × 10`;
- exact source Part(s) used by the chapter;
- exact overall scan page(s);
- Part-local page number(s);
- printed-page number(s), where the source has printed pagination;
- precise Kural coverage on each physical page;
- canonical Tamil physical-page record path(s);
- corresponding released English physical-page record path(s);
- verification state: canonical Tamil `verified` (or a documented source-limited exception) and English release state;
- source-sensitive or boundary notes where they materially affect provenance;
- a statement preserving the separation between semantic navigation and the physical-page archives.

Later chapter mappings use an explicit `Status: mapped` field. Earlier completed mappings use a `Canonical physical-page mapping` table plus verification prose. Both representations are compliant when all required provenance is present; already-correct early nodes do not need a cosmetic rewrite solely to match the later layout.

## Archival boundary

The chapter-to-Kural range is semantic metadata. Exact scan/page provenance may be recorded only after it has been independently verified from the canonical physical-page records and, where relevant, completed Part audits.

Canonical layers remain:

- Tamil: `works/thirukkural/pages/`;
- released English: `works/thirukkural/translations/en/pages/`.

A chapter README must not:

- infer a two-page pattern merely because nearby chapters use two pages;
- invent printed pagination for unnumbered leaves;
- move or duplicate physical-page records into the semantic tree;
- revise canonical Tamil or released English wording;
- silently normalize source/archive metadata to agree with the semantic hierarchy.

If a semantic classification and physical archive metadata differ, document the discrepancy explicitly and preserve both layers. The completed `களவியல்` / `கற்பியல்` transition is the controlling example: semantic chapter 116 begins `கற்பியல்`, while the physical archive retains `களவியல்` through scan 277 and first shows `கற்பியல்` at scan 278.

## Source-controlled naming

Use the existing live semantic folder spelling. Do not create normalized duplicate folders because a chapter title can be written with different spacing or joins.

Chapter-title terminology follows this project's established/source-controlled structure, including chapter 1 `வழிபாடு` and the retained chapter-28 folder `028-கூடா-ஒழுக்கம்`.

## Completion state

All **133 / 133** chapter nodes are provenance-mapped through Kural **1330**. See [`STRUCTURE_AUDIT.md`](STRUCTURE_AUDIT.md) for the completed semantic audit.
