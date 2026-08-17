# Next Chat Prompt — Continue Thirukkural Kalaignar Commentary Structure Mapping

Copy/paste the prompt below into a new chat window.

---

Continue the **Thirukkural — Kalaignar Commentary semantic structure / provenance-mapping project** directly in:

`pugazg/kalaignar-literary-commentary`

Work on `main`.

Active work path:

`works/thirukkural/structure/`

## MANDATORY STARTUP

Before making any repository change, read these files completely:

1. `THIRUKKURAL_ARCHIVAL_GUIDELINES.md`
2. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
3. root `HANDOVER.md`
4. `works/thirukkural/README.md`
5. `works/thirukkural/structure/README.md`
6. `works/thirukkural/structure/CHAPTER_README_POLICY.md`
7. `works/thirukkural/structure/STRUCTURE_AUDIT.md`
8. `works/thirukkural/translations/en/TRANSLATION_STATUS.md`

Then inspect current GitHub `main`. Repository state is authoritative over stale SHAs or historical status paragraphs.

## COMPLETED SOURCE WORK — DO NOT RESTART

The supplied Thirukkural volume is complete:

- Tamil Parts 001–015: **ARCHIVAL-READY** through scan 323;
- commentary through printed page 270 / Kural 1330;
- English Parts 001–015: **RELEASED** through the same complete volume;
- scans 304–321: index back matter;
- scan 322: blank leaf;
- scan 323: back cover.

Do not retranscribe or retranslate released material merely to support semantic navigation.

## SEMANTIC STRUCTURE

A non-destructive literary navigation layer exists under:

`works/thirukkural/structure/`

Hierarchy:

**பால் → இயல் → அதிகாரம்**

Target structure:

- 3 பால்;
- 13 இயல்;
- 133 அதிகாரம்;
- 1,330 குறள்.

The canonical scan-faithful Tamil remains under `works/thirukkural/pages/` and released English remains under `works/thirukkural/translations/en/pages/`. The semantic structure must point to those records; it must not replace, move, duplicate, or rewrite them.

## CURRENT EXACT MAPPING BOUNDARY

Exact canonical physical-page provenance mapping is complete through:

- **அதிகாரம் 77 — படைமாட்சி**;
- **குறள் 770**;
- **scan 189**;
- **Part 009 local page 20**;
- **printed page 156**.

Therefore **அதிகாரங்கள் 1–77 / குறள் 1–770** are complete.

The most recent mapped batch is 73–77:

- 73. அவையஞ்சாமை — scans 180–181 / printed 147–148 — final `அமைச்சியல்` chapter;
- 74. நாடு — scans 182–183 / printed 149–150 — begins `அரணியல்`;
- 75. அரண் — scans 184–185 / printed 151–152;
- 76. பொருள் செயல்வகை — scans 186–187 / printed 153–154 — begins `கூழியல்`;
- 77. படைமாட்சி — scans 188–189 / printed 155–156 — begins `படையியல்`.

Each completed semantic chapter README records exact source scans, Part/local-page numbers, printed pages, physical-page Kural coverage, canonical `verified` Tamil record paths and corresponding `release-ready` English paths.

## SOURCE-SENSITIVE PROTECTIONS

Do not normalize source-verified unusual readings from memory or another edition. Important examples already encountered include:

- scan 179 / Kural 717 source reading;
- scan 180 / Kural 725 commentary: `தருக்கமென்படும் அளவைக் திறமும்`;
- scan 182 / Kural 733 commentary: `மளவுக்கு வளம்`.

The next chapter also contains a verified correction that must be preserved:

- scan **190 / printed page 157 / Kural 771 commentary**: **`நடுகல்லாய்ப் போனவர்கள்`**.

Do not revert it to the earlier first-pass form `நடுகல்லைப் போனவர்கள்`.

## BATCH SIZE

Process **5 அதிகாரம் per iteration** when 10 cannot be processed safely.

Do not claim a larger batch than was actually verified and committed/written to `main`.

The GitHub Contents API may create one linear commit for each README update. If that happens, report the final commit boundary accurately instead of claiming a single multi-file commit.

## EXACT NEXT ACTIVITY

Map the next **5 அதிகாரங்கள்: 78–82 / குறள் 771–820**:

78. படைச் செருக்கு
79. நட்பு
80. நட்பாராய்தல்
81. பழைமை
82. தீ நட்பு

Repository-controlled semantic nodes include:

- `works/thirukkural/structure/02-பொருட்பால்/05-படையியல்/078-படைச்செருக்கு/`
- `works/thirukkural/structure/02-பொருட்பால்/06-நட்பியல்/079-நட்பு/`
- `works/thirukkural/structure/02-பொருட்பால்/06-நட்பியல்/080-நட்பாராய்தல்/`
- `works/thirukkural/structure/02-பொருட்பால்/06-நட்பியல்/081-பழைமை/`
- `works/thirukkural/structure/02-பொருட்பால்/06-நட்பியல்/082-தீ-நட்பு/`

The source-backed expected ranges, which must still be verified from the individual live page records before writing, are:

- **78. படைச் செருக்கு** — scans 190–191 / Part 009 pp.21–22 / printed 157–158 / Kurals 771–780 / `படையியல்`;
- **79. நட்பு** — scans 192–193 / Part 010 pp.1–2 / printed 159–160 / Kurals 781–790 / starts `நட்பியல்`;
- **80. நட்பாராய்தல்** — scans 194–195 / Part 010 pp.3–4 / printed 161–162 / Kurals 791–800;
- **81. பழைமை** — scans 196–197 / Part 010 pp.5–6 / printed 163–164 / Kurals 801–810;
- **82. தீ நட்பு** — scans 198–199 / Part 010 pp.7–8 / printed 165–166 / Kurals 811–820.

This batch contains two critical source-supported transitions:

1. **Part 009 → Part 010** between scans 191 and 192: printed page 158 / Kural 780 → printed page 159 / Kural 781;
2. **படையியல் → நட்பியல்**: chapter 78 closes `படையியல்`; chapter 79 `நட்பு` opens `நட்பியல்`.

For each chapter:

1. inspect the actual canonical Tamil page records first;
2. establish exact physical scan boundaries from repository records, not arithmetic assumptions;
3. confirm each Tamil record is `verified`;
4. inspect the corresponding English physical-page record and confirm it is `release-ready` with `source_tamil_status: verified`;
5. record source scan, Part, Part page, printed page and exact Kural coverage;
6. update only the correct semantic chapter README;
7. preserve source-controlled chapter naming and existing folder spelling;
8. if duplicate/incorrect semantic folders are encountered, reconcile them carefully and document the correction rather than silently leaving parallel nodes;
9. document the Part 009 → 010 and படையியல் → நட்பியல் transitions where appropriate;
10. preserve the scan-190 / Kural-771 verified source correction exactly;
11. do not alter canonical Tamil or released English body text.

After all five chapters are genuinely verified and updated, report the exact new mapping boundary and STOP.

The following batch should be **அதிகாரங்கள் 83–87 / குறள் 821–870**, subject to repository inspection.

## PROVENANCE RULE

Never infer that a chapter occupies two pages merely because earlier chapters did. Verify the actual page records. If a physical page contains material from adjacent chapters, document the partial coverage precisely.

Do not use external or memorized Thirukkural text to override the source-controlled repository edition.

Proceed with actual repository work after startup; do not respond with only a plan.

---
