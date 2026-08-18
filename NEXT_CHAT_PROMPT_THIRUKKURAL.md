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

1. `NEXT_CHAT_PROMPT_THIRUKKURAL.md`
2. `THIRUKKURAL_ARCHIVAL_GUIDELINES.md`
3. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
4. root `HANDOVER.md`
5. `works/thirukkural/README.md`
6. `works/thirukkural/structure/README.md`
7. `works/thirukkural/structure/CHAPTER_README_POLICY.md`
8. `works/thirukkural/structure/STRUCTURE_AUDIT.md`
9. `works/thirukkural/translations/en/TRANSLATION_STATUS.md`
10. `works/thirukkural/AUDIT_PART_013.md`

Then inspect current GitHub `main` and fetch the live HEAD. Repository state is authoritative over stale SHAs or historical status paragraphs.

Do not answer with only a plan after startup. Proceed with the actual repository work.

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

The canonical scan-faithful Tamil remains under `works/thirukkural/pages/` and released English remains under `works/thirukkural/translations/en/pages/`.

The semantic structure must point to those physical-page records; it must not replace, move, duplicate, or rewrite them.

## CURRENT EXACT MAPPING BOUNDARY

Exact canonical physical-page provenance mapping is complete through:

- **அதிகாரம் 112 — நலம் புனைந்துரைத்தல்**;
- **குறள் 1120**;
- **scan 261**;
- **Part 013 local page 1**;
- **printed page 228**.

Therefore **அதிகாரங்கள் 1–112 / குறள் 1–1120** are semantically mapped.

Chapter 112 crosses the Part boundary:

- scan 260 / Part 012 local page 23 / printed page 227 / Kurals 1111–1115;
- scan 261 / Part 013 local page 1 / printed page 228 / Kurals 1116–1120.

The Part 012 → Part 013 sequence is continuous with no textual gap.

Do not restart or rewrite chapters 1–112.

## CRITICAL INBAM HIERARCHY

The live semantic tree and `AUDIT_PART_013.md` establish the next sequence exactly.

### Still under `இன்பத்துப்பால் → களவியல்`

113. `காதற் சிறப்புரைத்தல்` — Kurals 1121–1130
114. `நாணுத் துறவுரைத்தல்` — Kurals 1131–1140
115. `அலர் அறிவுறுத்தல்` — Kurals 1141–1150

### Beginning `இன்பத்துப்பால் → கற்பியல்`

116. `பிரிவு ஆற்றாமை` — Kurals 1151–1160
117. `படர்மெலிந்து இரங்கல்` — Kurals 1161–1170

**The `களவியல் → கற்பியல்` transition occurs at chapter 116 / Kural 1151.**

Do not misclassify chapter 116 as `களவியல்`. Chapter 115 remains the final `களவியல்` chapter.

## EXACT LIVE SEMANTIC FOLDER PATHS

Use these existing folders; do not create normalized duplicates:

- `works/thirukkural/structure/03-இன்பத்துப்பால்/01-களவியல்/113-காதற்சிறப்புரைத்தல்/`
- `works/thirukkural/structure/03-இன்பத்துப்பால்/01-களவியல்/114-நாணுத்துறவுரைத்தல்/`
- `works/thirukkural/structure/03-இன்பத்துப்பால்/01-களவியல்/115-அலரறிவுறுத்தல்/`
- `works/thirukkural/structure/03-இன்பத்துப்பால்/02-கற்பியல்/116-பிரிவாற்றாமை/`
- `works/thirukkural/structure/03-இன்பத்துப்பால்/02-கற்பியல்/117-படர்மெலிந்திரங்கல்/`

The audit may render chapter labels with spaces while semantic folder slugs omit them. Preserve the existing live folder spelling.

## EXACT NEXT ACTIVITY

Map the next **5 அதிகாரங்கள்: 113–117 / குறள் 1121–1170**.

The continuous Part 013 sequence indicates that the relevant working scan window is expected to be **262–271**, immediately after the verified chapter-112 endpoint at scan 261.

However, **do not infer individual chapter/page boundaries arithmetically**. Before writing anything, fetch the actual canonical records and establish the exact mapping from their metadata/content.

### Gate A — Tamil provenance verification

Fetch the ten canonical Tamil page records covering the chapter 113–117 sequence from:

`works/thirukkural/pages/`

For every record, verify:

- `status: verified`;
- source Part;
- Part-local page;
- overall scan;
- printed page;
- exact Kural coverage;
- section / chapter heading;
- any source-sensitive punctuation, spelling or direct-verification correction.

Do not use remembered or external Thirukkural wording to override these records.

### Gate B — English release verification

Fetch the ten corresponding records from:

`works/thirukkural/translations/en/pages/`

For every record, verify:

- `status: release-ready`;
- `source_tamil_status: verified`;
- matching source scan / Kural coverage;
- chapter/section naming used by the released translation.

Do not revise released English body text during this semantic task.

### Gate C — Semantic node inspection

Fetch the five live semantic chapter `README.md` files / skeletons at the exact folder paths listed above.

Do not guess path spellings and do not create parallel folders.

### Gate D — Write the five mappings

Update only the five semantic chapter READMEs for chapters 113–117.

Each mapped README must include:

- **Section** / பால்;
- **Chapter group** / இயல்;
- **Status**: `mapped`;
- exact Kural range;
- source Part(s);
- exact source scans;
- physical provenance for each page: scan / Part-local page / printed page / Kural range;
- canonical Tamil record links;
- released English record links;
- verification state;
- source-sensitive notes where warranted;
- statement that the semantic node does not replace, move, duplicate or rewrite the canonical Tamil or released English physical-page archive.

Preserve the `களவியல் → கற்பியல்` transition explicitly:

- chapter 115 closes `களவியல்`;
- chapter 116 begins `கற்பியல்` at Kural 1151.

If the live records reveal a source-sensitive form or correction, record it accurately in the relevant semantic README. Do not silently normalize it.

Use sequential commits on `main` if the GitHub Contents API requires one commit per README. Report the actual final commit boundary; do not claim a single multi-file commit if one was not created.

## SOURCE-SENSITIVE PROTECTIONS

All direct-verification corrections and unusual source-supported forms already present in the canonical archive, audits and mapped chapter READMEs remain binding.

Examples include:

- Kural 771 commentary `நடுகல்லாய்ப் போனவர்கள்`;
- Kural 911 commentary `பொருள் திரட்டுவதையே`;
- Kural 912 `பாகுமொழிபேசும்`;
- Kural 931 commentary `கெளவிக் கொண்டு போவதாகிவிடும்`;
- Kural 948 commentary `உடல் நோய்க்கு மட்டுமின்றிச் சமுதாய நோய்க்கும் இது பொருந்தும்.`;
- Kural 1018 corrected wording ending `அகன்றுவிட்டதாகக் கருத வேண்டும்.`;
- Kural 1035 `ஊதியம் பெற்று உண்ணும் இயல்புடையவர்`;
- Kural 1048 `கொலை செய்வதுபோல நேற்று...`.

These examples are not a substitute for checking the active source pages directly.

## DO NOT CHANGE DURING THIS BATCH

Do not modify:

- canonical Tamil body records unless a genuinely separate source-correction task is explicitly opened;
- released English body records;
- root `HANDOVER.md`;
- root status/audit documents;
- archival Part audits;
- already mapped chapters 1–112.

The handover/prompt documents have already been synchronized to this boundary. Ordinary chapter mapping should not rewrite them again unless the user requests it or the workflow itself changes.

## FINAL VERIFICATION AND STOP CONDITION

After all five chapters have been genuinely verified and written:

1. read back all five semantic READMEs from live `main`;
2. verify their section/group placement, Kural ranges, paths and physical provenance;
3. fetch the new live `main` HEAD;
4. report the exact completed boundary;
5. STOP after chapter 117.

If the expected Part 013 page pattern is confirmed by the actual canonical records, the anticipated endpoint is approximately:

- **chapter 117 / Kural 1170**;
- **scan 271**;
- **Part 013 local page 11**;
- **printed page 238**.

This endpoint is an **expectation, not authoritative provenance, until the live page records confirm it**.

The following batch should be **chapters 118–122 / Kurals 1171–1220**, subject to repository inspection after chapter 117 is complete.

## PROVENANCE RULE

Never infer that a chapter occupies two pages merely because earlier chapters did. Verify the actual physical-page records. If a page contains material from adjacent chapters, record partial coverage precisely.

Repository state and the controlling source records outrank memory, external editions and stale historical prompts.

Proceed with actual repository work after startup.

---
