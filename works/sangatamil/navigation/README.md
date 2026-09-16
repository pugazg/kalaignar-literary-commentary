# சங்கத் தமிழ் — Derived Navigation Layer

**Gate H — COMPLETE / PASS**

This directory is a **derived navigation / search / API layer** built from the already-closed canonical archive. It does not replace source authority and does not modify page wording.

## Hierarchy

**Volume → source-order section → formal Sangam provenance unit → canonical anchor page**

Source-note-only records are preserved alongside the formal units without inflating the formal citation count.

## Inputs

- `../indexes/section-register.md` — Gate E, **104** source-order section-role entries / **497/497** scans assigned exactly once;
- `../indexes/source-citation-register.md` — Gate F, **115** formal provenance units + **4** source-note-only records;
- `../GATE_G_METADATA_STATUS_AUDIT.md` — Gate G metadata/status closure.

## Outputs

- `SECTIONS.md` — human section navigation;
- `sections.json` / `sections.tsv` — machine-readable 104-section index;
- `provenance/index.json` / `provenance/index.tsv` — **115 formal + 4 note-only** records;
- `provenance/BY_SECTION.md` — section-grouped crosswalk;
- `provenance/unit-001.md` … `unit-115.md` — formal provenance leaves;
- `provenance/note-001.md` … `note-004.md` — source-note-only leaves.

## Safeguards

- canonical pages under `../pages/` are source-preservation records and are not mutated by this layer;
- section ranges/headings come from the closed Gate-E register;
- provenance labels come from the closed Gate-F register;
- composite printed rows are split into stable derived unit IDs only where Gate F explicitly counted multiple formal units;
- the original composite printed block and boundary note are retained on each derived leaf;
- no missing poem number, poet, section relation, or quotation span is supplied from an external edition or memory;
- whole-volume word-for-word scan verification is **not claimed**.

## Coverage

- sections — **104/104**
- physical scans represented by section layer — **497/497**
- formal provenance units — **115/115**
- source-note-only records — **4/4**
- provenance records mapped to a Gate-E section — **119/119**
- provenance anchor scans resolved to canonical page paths — **119/119**
