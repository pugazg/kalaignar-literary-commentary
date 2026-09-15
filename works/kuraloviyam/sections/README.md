# Kuraloviyam — Derived Section Navigation

This directory is a **derived navigation layer** built after the six-Part archival and English workflows were fully closed.

It does **not** replace, rewrite or reopen:

- `../pages/` — audited Tamil page records;
- `../translations/en/pages/` — maintained English page records;
- the Part-level review/release/final-closure records.

## Hierarchy

The navigation hierarchy is:

**Book → Iyal → Adhikaram (Chapter) → Kuraloviyam contents entry**

Current directories:

- `00-front-matter/` — front matter and pre-main-body material;
- `01-aram/` — அறத்துப்பால்;
- `02-porul/` — பொருட்பால்;
- `03-inbam/` — இன்பத்துப்பால்;
- `04-contents/` — exact source-keyed 300-entry contents index from scans 658–665.

## Evidence model

Two evidence layers are deliberately distinguished:

1. **Source-derived**
   - front-matter scan roles from the audited page map;
   - Chapter numbers/Tamil labels/controlled English labels from the maintained glossary and audited Chapter/Kural metadata;
   - the 300 contents entries and printed-page locators from scans 658–665.

2. **Derived navigation scaffold**
   - Book/Iyal directory placement follows the conventional Thirukkural chapter-range organization solely to make navigation practical.
   - These Iyal directory boundaries are **not claimed as headings transcribed from the Kuraloviyam contents pages**.

No source text is normalized to make it fit the scaffold.

## Source-number anomaly preserved

The maintained source contains two distinct Chapter-title records carrying source Chapter number **26**:

- `அருளுடைமை` / **Possession of Compassion** — scan 365 / printed 348;
- `புலால் மறுத்தல்` / **Abstaining from Flesh** — scan 642 / printed 625.

The derived chapter file preserves both records and does **not** silently correct or reconcile the source numbering.

## Coverage

Source-evidenced Chapter numbers represented by maintained glossary controls: **120/133**.

Chapter numbers with no maintained source-evidenced Chapter-label control:

**1, 18, 22, 25, 44, 52, 70, 71, 76, 86, 91, 106, 107**

Absence here means only that the maintained source metadata/glossary does not currently evidence that Chapter number; it is not filled from an outside edition.

## Entry crosswalk

The exact 300-entry source index is available under `04-contents/`.

This first structural pass creates the full Book/Iyal/Adhikaram scaffold and preserves the exact source contents. A later crosswalk pass may attach each contents entry to its source-evidenced Chapter/Kural closure by reading the audited page records; it must not infer assignments from an external Kural edition.
