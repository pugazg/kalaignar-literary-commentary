# திருக்குறள் — பால் → இயல் → அதிகாரம் அமைப்பு

This directory is the completed semantic navigation/provenance hierarchy for the archived `திருக்குறள் — கலைஞர் உரை`.

**Hierarchy:** பால் → இயல் → அதிகாரம்.

## Completion state

Semantic provenance mapping is complete for:

- **3 / 3 பால்**;
- **13 / 13 இயல்**;
- **133 / 133 அதிகாரம்**;
- **1,330 / 1,330 குறள்**.

The final semantic node is chapter **133 — ஊடலுவகை**, spanning scans **302–303** and completing Kural **1330** on printed page **270**.

## Canonical archival separation

The existing `works/thirukkural/pages/` directory remains the canonical scan-faithful Tamil archival layer. The existing `works/thirukkural/translations/en/pages/` directory remains the released English physical-page layer.

Nothing in those audited/released layers is moved, duplicated or rewritten by this hierarchy. Semantic chapter nodes record verified physical provenance and links back to those archives.

## பால்

1. `01-அறத்துப்பால்` — அதிகாரம் 1–38 — குறள் 1–380
2. `02-பொருட்பால்` — அதிகாரம் 39–108 — குறள் 381–1080
3. `03-இன்பத்துப்பால்` — அதிகாரம் 109–133 — குறள் 1081–1330

The 13 இயல் parent ranges join continuously with no semantic gap or overlap.

## Physical provenance rule

Each அதிகாரம் contains exactly ten Kurals semantically, but its physical scan boundary is never inferred from that fact. Chapter provenance is taken from the actual canonical page records: overall scan, source Part, Part-local page, printed page, Kural coverage and matching English release record.

Where semantic hierarchy and physical archive metadata differ, the difference is documented rather than normalized. In particular:

- semantic chapters **109–115** are under `களவியல்`;
- semantic chapters **116–133** are under `கற்பியல்`;
- physical Tamil/English metadata retains `களவியல்` / `Clandestine Love` through scan **277**;
- scan **278** is the first physical `கற்பியல்` / `Wedded Love` record.

## Structural controls

- [`CHAPTER_README_POLICY.md`](CHAPTER_README_POLICY.md) — completed chapter-provenance requirements and archival-boundary policy.
- [`STRUCTURE_AUDIT.md`](STRUCTURE_AUDIT.md) — final audit of the **3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள்** semantic hierarchy and provenance mapping.

The semantic mapping phase is complete. There is no remaining chapter node to map for the supplied volume.
