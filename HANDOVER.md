# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. Preserve source-specific Kural spelling, joining, spacing, punctuation, line breaks and Kalaignar commentary exactly as printed.

The English layer is a **project-created translation**, not an official/publisher English edition. It must retain Kalaignar's own language, images, emphases and interpretive direction and must not import external English Kural wording or another commentator's interpretation.

Permanent cadence:

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release report.**

# திருக்குறள் — established Tamil archival state

- Part 001 — scans 1–20: **ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**; 19 verified + scan 8 partial.
- Part 002 — scans 21–41: **ARCHIVAL-READY**, 21/21 verified.
- Part 003 — scans 42–62: **ARCHIVAL-READY**, 21/21 verified; printed pages 9–29; Kural 41–145.
- Part 004 — scans 63–84: **ARCHIVAL-READY**, 22/22 verified and audited; printed pages 30–51; Kural 146–255.
- Part 005 — scans 85–106: **ARCHIVAL-READY**, 22/22 verified and audited; printed pages 52–73; Kural 256–365.

The currently supplied Tamil source therefore reaches overall scan **106** / printed page **73** / Kural **365**.

Do not redo or renumber Parts 001–005.

## Part 005 audit

Audit file:

`works/thirukkural/AUDIT_PART_005.md`

Audit result: **ARCHIVAL-READY**.

The audit confirms:

- exactly **22/22** one-to-one page records for scans 85–106;
- local pages **1–22**;
- printed pages **52–73**;
- continuous Kural range **256–365**;
- Part 004→005 continuity at Kural **255→256**;
- all 22 records at `status: "verified"`;
- all 22 records use `transcription_method: "direct visual comparison with source scan"`;
- no remaining `needs-review`, partial, blocked or uncreated Part 005 record;
- chapter continuity from completion of `26. புலால் மறுத்தல்` through the supplied beginning of `37. அவா அறுத்தல்`;
- source-specific Tamil retained without standard/web substitution;
- scan 99 / Kural 329 commentary correction retained as **`பகுத்தறிவு இழந்து செயல்படும்`**.

Part 005 ends intentionally at Kural 365 because the supplied PDF ends there. Do not import Kural 366 onward from another source.

# English project translation state

Currently released:

- Part 001 — 19 `release-ready` + scan 8 `source-limited`;
- Part 002 — 21/21 `release-ready`;
- Part 003 — 21/21 `release-ready`, through Kural 145.

Tamil Parts **004 and 005 are now archival-ready**, so both are eligible for the existing English project-translation workflow.

The controlling translation rule remains:

> **Retain Kalaignar's own language, images, emphases and interpretive direction. Do not replace his reading with familiar standard Thirukkural interpretations or copy a published external English Kural translation.**

Preserve the established separation between:

- the Kural itself;
- Kalaignar's commentary;
- any project editorial/glossary layer.

# Exact next activity

Begin **Part 004 English first-pass translation** from audited Tamil source.

Initial batch:

- overall scans **63–69**;
- printed pages **30–36**;
- Kural **146–180**;
- completion of `15. பிறனில் விழையாமை`;
- `16. பொறையுடைமை`;
- `17. அழுக்காறாமை`;
- `18. வெஃகாமை`.

Follow the same English record structure and metadata conventions used in released Parts 001–003.

For every new English record:

1. use the corresponding audited Tamil Markdown page as the working basis, with the scan remaining the ultimate source authority;
2. translate both Kural and Kalaignar commentary without importing an external standard translation;
3. retain Kalaignar's distinctive wording, imagery, social framing and interpretive choices;
4. keep Kural and commentary clearly separate;
5. use `translation_type: "project_translation"`;
6. begin at `status: "draft"`;
7. preserve one-to-one scan/page correspondence and source metadata;
8. do not begin source-check in the same first-pass activity.

After scans 63–69 are drafted, synchronize the English translation status/README files and this handover, then stop.

For further Tamil archival work, wait for the next supplied source beginning after overall scan **106** / printed page **73** / Kural **365**.
