# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

Active work: `works/thirukkural/`

## Mandatory startup

Before making changes:

1. read `THIRUKKURAL_ARCHIVAL_GUIDELINES.md` completely;
2. read `LITERARY_COMMENTARY_PROCESSING_GUIDE.md` completely;
3. read this `HANDOVER.md` completely;
4. read `works/thirukkural/README.md`;
5. inspect existing target files before writing;
6. inspect the actual controlling source required by the active gate;
7. for English work additionally fresh-read:
   - `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`;
   - `works/thirukkural/translations/en/GLOSSARY.md`;
   - `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
   - latest relevant English review/release artefacts.

Repository state is authoritative.

## Source rule

The supplied Tamil scans are controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

Source PDFs are working/control sources and are not to be committed to GitHub unless the user explicitly requests that.

OCR/parsed text may assist but is never authoritative over direct inspection of the scan.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Keep these as separate gates.

Every project-created English page must identify:

```yaml
translation_type: "project_translation"
```

Released English material must not be revised merely to harmonize later vocabulary.

Permanent earlier protections remain binding, including:

- chapter 38 `ஊழ்` → **Oozh**;
- Kalaignar's `இயற்கை நிலை` → **natural condition**;
- Kural 543 `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**, not an automatic caste-specific conventional gloss;
- preservation of Kalaignar's governance, citizens, working-people, justice, public-resource and rational/inquiry vocabulary where the Tamil explicitly uses it.

# Established baseline

## Tamil

Parts **001–012 are audited / ARCHIVAL-READY continuously** through:

- overall scan **260**;
- printed page **227**;
- Kural **1115**.

Latest completed Tamil audit:

`works/thirukkural/AUDIT_PART_012.md` — **PASS / ARCHIVAL-READY**.

Part **013 has completed first-pass transcription only** through:

- overall scan **282**;
- printed page **249**;
- Kural **1225**.

All 22 Part 013 records remain `needs-review`. Part 013 is **not archival-ready**.

## English

Parts **001–012 are fully released continuously through Kural 1115**.

Latest English artefacts:

- `works/thirukkural/translations/en/reviews/PART_012_REVIEW.md`;
- `works/thirukkural/translations/en/reviews/PART_012_RELEASE_REPORT.md` — **PASS / RELEASE APPROVED**.

All 23 Part 012 English page records are `release-ready`.

Released Parts 001–012 must remain untouched during Part 013 Tamil work.

# Closed Part 012 baseline

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_012_pages_238-260.pdf`

Closed Part 012 scope:

- physical pages **23 / 23**;
- scans **238–260**;
- Part-local pages **1–23**;
- printed pages **205–218**, two unnumbered leaves, then **221–227**;
- Kural **1011–1115**;
- Tamil `verified`: **23 / 23**;
- English `release-ready`: **23 / 23**.

The Part 012 → Part 013 boundary is source-supported at printed page **227 → 228 / Kural 1115 → 1116**.

# Active Part 013 Tamil unit — FIRST PASS COMPLETE

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_013_pages_261-282.pdf`

Current supplied-file identity in the user's file library:

`file_0000000081a08208a863fa44b7c0e9b9`

Source inspection and first-pass transcription have been completed for **all 22 physical pages**.

Current state:

- physical source pages: **22 / 22**;
- overall scans: **261–282**;
- Part-local pages: **1–22**;
- printed pages: **228–249** continuously;
- Kural range: **1116–1225** continuously;
- page records present: **22 / 22**;
- `needs-review`: **22 / 22**;
- `verified`: **0 / 22**;
- Tamil direct verification: **not started**;
- `AUDIT_PART_013.md`: **not created**;
- English Part 013: **not started / not eligible**.

Every Part 013 first-pass record uses:

```yaml
status: "needs-review"
transcription_method: "manual transcription from source scan; direct visual verification pending"
```

## Part 013 page / chapter map

- scan **261** / local 1 / printed **228** — continuation and completion of chapter 112 `நலம் புனைந்து உரைத்தல்`, Kural **1116–1120**;
- scans **262–263** / printed **229–230** — chapter 113 `காதற் சிறப்புரைத்தல்`, Kural **1121–1130**;
- scans **264–265** / printed **231–232** — chapter 114 `நாணுத் துறவுரைத்தல்`, Kural **1131–1140**;
- scans **266–267** / printed **233–234** — chapter 115 `அலர் அறிவுறுத்தல்`, Kural **1141–1150**;
- scans **268–269** / printed **235–236** — chapter 116 `பிரிவு ஆற்றாமை`, Kural **1151–1160**;
- scans **270–271** / printed **237–238** — chapter 117 `படர்மெலிந்து இரங்கல்`, Kural **1161–1170**;
- scans **272–273** / printed **239–240** — chapter 118 `கண் விதுப்பழிதல்`, Kural **1171–1180**;
- scans **274–275** / printed **241–242** — chapter 119 `பசப்புறு பருவரல்`, Kural **1181–1190**;
- scans **276–277** / printed **243–244** — chapter 120 `தனிப்படர் மிகுதி`, Kural **1191–1200**;
- scans **278–279** / printed **245–246** — chapter 121 `நினைந்தவர் புலம்பல்`, Kural **1201–1210**;
- scans **280–281** / printed **247–248** — chapter 122 `கனவுநிலை உரைத்தல்`, Kural **1211–1220**;
- scan **282** / local 22 / printed **249** — chapter 123 `பொழுதுகண்டு இரங்கல்`, Kural **1221–1225**; chapter continues beyond this supplied Part 013 unit.

Thus chapter 112 is completed in Part 013, chapters 113–122 are complete, and chapter 123 is partial through Kural 1225.

## Part 013 source hierarchy

The source-visible hierarchy must not be flattened:

1. scans **261–277** — `இன்பம் — களவியல்`;
2. scan **278 / printed page 245 / Kural 1201** begins `இன்பம் — கற்பியல்`;
3. scans **278–282** remain `இன்பம் — கற்பியல்`.

This `களவியல் → கற்பியல்` transition is already represented in first-pass page metadata and must be directly rechecked during verification.

## Part 013 first-pass source-sensitive items

These were retained exactly as read during first-pass source inspection and must be checked directly in the next gate rather than normalized from another edition:

### Scan 268 / Kural 1152 commentary

The source-visible commentary includes:

```text
... ‘பிரிவு’ என்னும் அச்சத்தால் துன்பமல்லவா வந்துதிகிறது!
```

The unusual-looking `வந்துதிகிறது!` is intentionally retained pending verification.

### Scan 281 / Kural 1220

The source was read as:

```text
நனவினான் நந்தத்தார் என்பர் கனவினான்
காணார்கொல் இவ்வூ ரவர்.
```

Do not replace this with a familiar external Kural wording. Verify this supplied-edition reading directly from the scan.

Other unusual joins, punctuation, sandhi and commentary forms across scans 261–282 remain source-controlled and should be corrected only when the separate direct visual comparison demonstrates a real first-pass error.

# Supplied later sources

- Part 014 — `திருக்குறள்_கலைஞர்_உரை_part_014_pages_283-302.pdf` — **20 pages** — source received, not started;
- Part 015 — `திருக்குறள்_கலைஞர்_உரை_part_015_pages_303-323.pdf` — **21 pages** — source received, not started.

Do not begin either during Part 013 verification.

# Exact next activity

**Part 013 Tamil direct visual verification — all 22 physical pages / overall scans 261–282.**

Required procedure:

1. fresh-read the mandatory startup files above;
2. inspect all 22 current Part 013 first-pass records before editing;
3. inspect the actual controlling Part 013 source scan directly;
4. compare every page line-by-line for:
   - Kural number and exact Tamil text;
   - source-supported two-line Kural structure;
   - joins / spacing / sandhi visible in this edition;
   - punctuation and quotation marks;
   - chapter heading;
   - running-header hierarchy;
   - Kalaignar commentary wording and paragraph boundary;
   - printed-page, scan-page and Part-local-page metadata;
   - source marker;
5. recheck the source-visible `இன்பம் — களவியல்` → `இன்பம் — கற்பியல்` transition at scan 278;
6. explicitly recheck Kural 1152 commentary `வந்துதிகிறது!` and the supplied Kural 1220 reading above;
7. document every real first-pass correction found during verification;
8. promote each passing page from `needs-review` to `verified` and set:
   ```yaml
   transcription_method: "direct visual comparison with source scan"
   ```
9. leave any genuinely unresolved page at `needs-review`, `partial` or `blocked` rather than guessing;
10. synchronize status documentation after the complete verification gate;
11. stop after direct visual verification.

Do **not** create `AUDIT_PART_013.md` during this verification activity. The audit is the following separate gate only after every page is resolved.

Do **not** begin Part 013 English translation during verification.

Do **not** alter released English Parts 001–012.

Do **not** begin Parts 014–015 in the same activity.

After successful verification of all Part 013 records, the next separate activity is **Part 013 Tamil audit / archival-ready decision**.
