# Thirukkural semantic-structure audit

## Scope

This audit checks the repository navigation layer under `works/thirukkural/structure/`. It does not replace the scan-faithful Tamil archive in `works/thirukkural/pages/` or the released English physical-page archive in `works/thirukkural/translations/en/pages/`.

Audit target:

- 3 பால்
- 13 இயல்
- 133 அதிகாரம்
- one semantic chapter directory per அதிகாரம்
- one chapter `README.md` per அதிகாரம்
- deterministic ten-Kural range per chapter
- no change to canonical Tamil or released English page records

## Expected hierarchy

### 01 — அறத்துப்பால்

- 01 பாயிரவியல் — அதிகாரம் 1–4 — குறள் 1–40
- 02 இல்லறவியல் — அதிகாரம் 5–24 — குறள் 41–240
- 03 துறவறவியல் — அதிகாரம் 25–37 — குறள் 241–370
- 04 ஊழியல் — அதிகாரம் 38 — குறள் 371–380

Total: **38 அதிகாரம் / 380 குறள்**.

### 02 — பொருட்பால்

- 01 அரசியல் — அதிகாரம் 39–63 — குறள் 381–630
- 02 அமைச்சியல் — அதிகாரம் 64–73 — குறள் 631–730
- 03 அரணியல் — அதிகாரம் 74–75 — குறள் 731–750
- 04 கூழியல் — அதிகாரம் 76 — குறள் 751–760
- 05 படையியல் — அதிகாரம் 77–78 — குறள் 761–780
- 06 நட்பியல் — அதிகாரம் 79–95 — குறள் 781–950
- 07 குடியியல் — அதிகாரம் 96–108 — குறள் 951–1080

Total: **70 அதிகாரம் / 700 குறள்**.

### 03 — இன்பத்துப்பால்

- 01 களவியல் — அதிகாரம் 109–115 — குறள் 1081–1150
- 02 கற்பியல் — அதிகாரம் 116–133 — குறள் 1151–1330

Total: **25 அதிகாரம் / 250 குறள்**.

## Range rule

For அதிகாரம் `n`, the semantic Kural range is:

- first Kural: `(n - 1) × 10 + 1`
- last Kural: `n × 10`

This gives continuous coverage from **குறள் 1 through குறள் 1330** with no semantic gap or overlap.

## Audit finding and correction

The audit found one duplicate semantic node created during chapter-metadata population for அதிகாரம் 28:

- established folder: `028-கூடா-ஒழுக்கம்/`
- accidental duplicate: `028-கூடாவொழுக்கம்/`

The accidental duplicate was removed. The established folder now contains the chapter README:

- அதிகாரம்: **28. கூடா ஒழுக்கம்**
- பால்: **அறத்துப்பால்**
- இயல்: **துறவறவியல்**
- குறள்: **271–280**

No canonical Tamil transcription or released English translation was changed by this correction.

## Source-controlled naming

Folder and chapter-title wording follows the project's established/source-controlled terminology rather than silently normalising to another Thirukkural naming convention. In particular, chapter 1 remains **`வழிபாடு`** in this project.

Hyphens in directory names are filesystem separators only; human-readable chapter titles in README files may restore spaces where appropriate.

## Archival separation

The semantic hierarchy is navigation metadata only. It must not invent physical scan boundaries. Exact scan/page provenance continues to live in the canonical page records and their audits.

## Result

**PASS WITH ONE CORRECTION APPLIED.**

The semantic hierarchy is ready for the next phase: mapping each அதிகாரம் node to the exact canonical Tamil page record(s) and corresponding released English page record(s), while retaining scan-level provenance.
