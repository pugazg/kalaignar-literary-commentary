# Thirukkural semantic-structure completion audit

Last audited against live `main`: **2026-08-18**.

## Scope

This audit checks the completed semantic navigation/provenance layer under `works/thirukkural/structure/` after mapping through chapter 133. It does not replace the scan-faithful Tamil archive in `works/thirukkural/pages/` or the released English physical-page archive in `works/thirukkural/translations/en/pages/`.

Audit target:

- 3 பால்;
- 13 இயல்;
- 133 அதிகாரம்;
- continuous semantic Kural coverage from 1 through 1330;
- one semantic chapter node per அதிகாரம்;
- source-verified physical provenance recorded at chapter level;
- links to canonical Tamil and released English physical-page records;
- explicit preservation of source/archive discrepancies rather than silent normalization;
- no semantic-phase rewrite of canonical Tamil or released English body records.

## Hierarchy result

### 01 — அறத்துப்பால்

- பாயிரவியல் — அதிகாரம் 1–4 — குறள் 1–40
- இல்லறவியல் — அதிகாரம் 5–24 — குறள் 41–240
- துறவறவியல் — அதிகாரம் 25–37 — குறள் 241–370
- ஊழியல் — அதிகாரம் 38 — குறள் 371–380

Total: **38 அதிகாரம் / 380 குறள்**.

### 02 — பொருட்பால்

- அரசியல் — அதிகாரம் 39–63 — குறள் 381–630
- அமைச்சியல் — அதிகாரம் 64–73 — குறள் 631–730
- அரணியல் — அதிகாரம் 74–75 — குறள் 731–750
- கூழியல் — அதிகாரம் 76 — குறள் 751–760
- படையியல் — அதிகாரம் 77–78 — குறள் 761–780
- நட்பியல் — அதிகாரம் 79–95 — குறள் 781–950
- குடியியல் — அதிகாரம் 96–108 — குறள் 951–1080

Total: **70 அதிகாரம் / 700 குறள்**.

### 03 — இன்பத்துப்பால்

- களவியல் — அதிகாரம் 109–115 — குறள் 1081–1150
- கற்பியல் — அதிகாரம் 116–133 — குறள் 1151–1330

Total: **25 அதிகாரம் / 250 குறள்**.

Overall: **3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள்**.

## Continuity rule and result

For அதிகாரம் `n`, the semantic Kural range remains:

- first Kural: `(n - 1) × 10 + 1`;
- last Kural: `n × 10`.

The live பால் and இயல் parent READMEs were rechecked after chapter 133 was mapped. Their ranges join continuously from Kural **1** through **1330**, with no parent-level gap or overlap.

The semantic mapping therefore closes at:

- அதிகாரம் **133 — ஊடலுவகை**;
- குறள் **1330**;
- overall scan **303** for the final commentary page;
- printed page **270**.

## Provenance controls checked

Representative and boundary-sensitive chapter nodes were read back from live `main`, including:

- chapter 1 `வழிபாடு` — opening mapped node;
- chapter 28 `கூடா ஒழுக்கம்` — previously reconciled duplicate-folder control;
- chapter 38 `ஊழ்` — end of அறத்துப்பால்;
- chapter 112 `நலம் புனைந்து உரைத்தல்` — crosses Part 012 → Part 013;
- chapter 113 — confirms continuation after the former handover boundary;
- chapters 116, 120 and 121 — preserve the semantic/physical `களவியல்` / `கற்பியல்` discrepancy correctly;
- chapter 123 `பொழுதுகண்டு இரங்கல்` — crosses Part 013 → Part 014;
- chapter 133 `ஊடலுவகை` — crosses Part 014 → Part 015 and completes the work.

These controls confirm that scan, Part-local-page, printed-page and Kural boundaries are being recorded from actual canonical page records rather than inferred arithmetically.

## Important semantic / physical hierarchy discrepancy

The semantic hierarchy places:

- chapters 109–115 under `இன்பத்துப்பால் → களவியல்`;
- chapters 116–133 under `இன்பத்துப்பால் → கற்பியல்`.

The canonical physical-page metadata does not switch at chapter 116. It retains `களவியல்` through scan **277**; scan **278** is the first physical Tamil record explicitly labelled `கற்பியல்`. Released English mirrors this, retaining `Clandestine Love` through scan 277 and switching to `Wedded Love` at scan 278.

This is **not treated as an error to be normalized**. Chapters 116–120 document the discrepancy as provenance; chapter 121 records the source-visible physical transition. The canonical Tamil and released English physical-page records remain unchanged.

## Chapter README representation

Mapped chapter nodes exist in two compatible presentation styles created during the project:

1. earlier nodes use a `Canonical physical-page mapping` table containing scan, Part, Part-local page, printed page, Kural coverage and Tamil/English paths, followed by verification and archival-separation statements;
2. later nodes use explicit labelled fields such as `Status: mapped`, `Source part(s)`, `Source scans`, `Physical provenance`, record links, verification and notes.

This formatting difference is not a semantic defect. Both layouts preserve the required provenance. No bulk cosmetic rewrite of already-correct chapter nodes is required.

## Historical correction retained

The earlier duplicate node for chapter 28 was already reconciled:

- retained: `028-கூடா-ஒழுக்கம்/`;
- removed historical duplicate: `028-கூடாவொழுக்கம்/`.

The live `துறவறவியல்` tree still contains the retained canonical semantic folder only. No source body was changed by that correction.

## Archival separation

The semantic layer is navigation/provenance metadata only.

It must not:

- move or duplicate the canonical Tamil pages;
- rewrite released English pages;
- invent scan or printed-page boundaries;
- normalize a source/archive discrepancy merely to make semantic labels uniform.

Canonical authority remains:

1. controlling source scan;
2. verified Tamil physical-page record and completed Tamil audit;
3. released English physical-page record and completed English review/release report;
4. semantic navigation/provenance README.

## Result

**PASS — SEMANTIC PROVENANCE MAPPING COMPLETE.**

Completion status:

- **3 / 3 பால்**;
- **13 / 13 இயல்**;
- **133 / 133 அதிகாரம்**;
- **1,330 / 1,330 குறள்**;
- final semantic boundary: chapter **133 / Kural 1330 / scans 302–303**.

There is no remaining chapter-provenance mapping work for the supplied Thirukkural volume. Future work should begin only from a separately defined enhancement task or from a newly supplied source/work; released Tamil and English layers must not be reopened merely for stylistic harmonization.
