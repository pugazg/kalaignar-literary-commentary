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
- commentary: through printed page 270 / Kural 1330;
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

## CURRENT MAPPING BOUNDARY

Exact canonical physical-page provenance mapping is complete for **அதிகாரங்கள் 1–12 / குறள் 1–120**.

Completed mapped chapters:

1. வழிபாடு
2. வான் சிறப்பு
3. நீத்தார் பெருமை
4. அறன் வலியுறுத்தல்
5. இல்வாழ்க்கை
6. வாழ்க்கைத் துணைநலம்
7. மக்கட்பேறு
8. அன்புடைமை
9. விருந்தோம்பல்
10. இனியவை கூறல்
11. செய்ந்நன்றியறிதல்
12. நடுவு நிலைமை

Each completed chapter README contains:

- பால்;
- இயல்;
- அதிகார number/title;
- deterministic 10-Kural range;
- exact source scan(s);
- source Part and Part-page number;
- printed-page number;
- exact Kural coverage per physical page;
- canonical verified Tamil archival path;
- corresponding released English path;
- statement preserving the canonical physical-page layers.

Important duplicate-folder corrections already made include the source-controlled chapter nodes for அதிகாரம் 11 and 12. Do not recreate obsolete variants.

## BATCH SIZE

The user requested **5 அதிகாரம் per iteration** when 10 cannot be processed safely.

Do not claim a larger batch than was actually verified and committed.

## EXACT NEXT ACTIVITY

Map the next **5 அதிகாரங்கள்: 13–17 / குறள் 121–170**:

13. அடக்கம் உடைமை
14. ஒழுக்கம் உடைமை
15. பிறனில் விழையாமை
16. பொறையுடைமை
17. அழுக்காறாமை

For each chapter:

1. inspect the actual canonical Tamil page records first;
2. establish exact physical scan boundaries from repository records, not arithmetic assumptions;
3. confirm each Tamil record is `verified`;
4. inspect the corresponding English physical-page record and confirm it is `release-ready`;
5. record source scan, Part, Part page, printed page and exact Kural coverage;
6. update only the correct semantic chapter README;
7. preserve source-controlled chapter naming and existing folder spelling;
8. if duplicate/incorrect semantic folders are encountered, reconcile them carefully and document the correction rather than silently leaving parallel nodes;
9. do not alter canonical Tamil or released English body text.

After all five chapters are genuinely verified and updated, commit the batch to `main` and report the new exact mapping boundary.

Then STOP. The following batch should be அதிகாரங்கள் 18–22 unless repository inspection reveals a structural issue that must be corrected first.

## PROVENANCE RULE

Never infer that a chapter occupies two pages merely because earlier chapters did. Verify the actual page records. If a physical page contains material from adjacent chapters, document the partial coverage precisely.

Do not use external/memorized Thirukkural text to override the source-controlled repository edition.

Proceed with actual repository work after startup; do not respond with only a plan.

---
