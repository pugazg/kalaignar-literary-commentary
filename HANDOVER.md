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

Latest completed Tamil audit before the active part:

`works/thirukkural/AUDIT_PART_012.md` — **PASS / ARCHIVAL-READY**.

Part **013 direct visual verification is complete 22/22** through scan **282 / printed page 249 / Kural 1225**, but `AUDIT_PART_013.md` does not yet exist and Part 013 is therefore **not yet archival-ready**.

## English

Parts **001–012 are fully released continuously through Kural 1115**.

Latest English artefacts:

- `works/thirukkural/translations/en/reviews/PART_012_REVIEW.md`;
- `works/thirukkural/translations/en/reviews/PART_012_RELEASE_REPORT.md` — **PASS / RELEASE APPROVED**.

Released Parts 001–012 must remain untouched during Part 013 Tamil work.

# Part 013 verification baseline

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_013_pages_261-282.pdf`

Supplied-file identity:

`file_0000000081a08208a863fa44b7c0e9b9`

Verified scope:

- physical pages **22 / 22**;
- overall scans **261–282**;
- Part-local pages **1–22**;
- printed pages **228–249** continuously;
- Kural **1116–1225** continuously;
- Tamil `verified`: **22 / 22**;
- `needs-review`: **0**;
- `partial`: **0**;
- `blocked`: **0**;
- audit: **not started**;
- English Part 013: **not started**.

All passing records now use:

```yaml
status: "verified"
transcription_method: "direct visual comparison with source scan"
```

Incoming boundary already source-confirmed:

- Part 012 ends printed page **227 / Kural 1115**;
- Part 013 begins printed page **228 / Kural 1116** and completes chapter 112 through Kural 1120.

Verified chapter structure:

- scan 261 — ch.112 `நலம் புனைந்து உரைத்தல்`, K1116–1120;
- scans 262–263 — ch.113 `காதற் சிறப்புரைத்தல்`, K1121–1130;
- scans 264–265 — ch.114 `நாணுத் துறவுரைத்தல்`, K1131–1140;
- scans 266–267 — ch.115 `அலர் அறிவுறுத்தல்`, K1141–1150;
- scans 268–269 — ch.116 `பிரிவு ஆற்றாமை`, K1151–1160;
- scans 270–271 — ch.117 `படர்மெலிந்து இரங்கல்`, K1161–1170;
- scans 272–273 — ch.118 `கண் விதுப்பழிதல்`, K1171–1180;
- scans 274–275 — ch.119 `பசப்புறு பருவரல்`, K1181–1190;
- scans 276–277 — ch.120 `தனிப்படர் மிகுதி`, K1191–1200;
- scans 278–279 — ch.121 `நினைந்தவர் புலம்பல்`, K1201–1210;
- scans 280–281 — ch.122 `கனவுநிலை உரைத்தல்`, K1211–1220;
- scan 282 — ch.123 `பொழுதுகண்டு இரங்கல்`, K1221–1225, partial at this processing-unit boundary.

Verified structural transition:

1. scans **261–277** — `இன்பம் — களவியல்`;
2. scans **278–282** — `இன்பம் — கற்பியல்`.

## Direct-verification corrections — authoritative

Exactly three first-pass corrections were required:

1. scan **267 / Kural 1147 commentary**
   - first pass: `கொண்டு வளரும் தவிரக் கருகிப் போய்விடாது.`
   - verified: `கொண்டு வளருமே தவிரக் கருகிப் போய்விடாது.`
2. scan **268 / Kural 1152 commentary**
   - verified full sentence: `முன்பெல்லாம் அவரைக் கண்களால் தழுவிக் கொண்டதே இன்பமாக இருந்தது; ஆனால், இப்போது உடல் தழுவிக் களிக்கும்போதுகூடப் பிரிவை எண்ணும் அச்சத்தால் துன்பமல்லவா வந்துதிகிறது!`
3. scan **280 / Kural 1212 commentary**
   - first pass: `விழிகள் உறங்குமானால்`
   - verified: `விழிகள் உறங்கிடுமானால்`

## Protected source-sensitive readings

The next gate must preserve these direct confirmations:

- Kural **1152 commentary** ends with source-visible `வந்துதிகிறது!`; do not normalize it;
- Kural **1220** is printed in this supplied edition as:
  ```text
  நனவினான் நந்தத்தார் என்பர் கனவினான்
  காணார்கொல் இவ்வூ ரவர்.
  ```
  Do not replace this with a familiar external reading.

# Supplied later sources

- Part 014 — `திருக்குறள்_கலைஞர்_உரை_part_014_pages_283-302.pdf` — **20 pages** — source received, not started;
- Part 015 — `திருக்குறள்_கலைஞர்_உரை_part_015_pages_303-323.pdf` — **21 pages** — source received, not started.

# Exact next activity

**Part 013 Tamil audit / archival-ready gate.**

Required procedure:

1. fresh-read the mandatory startup files above;
2. inspect all 22 verified Part 013 page records on `main`;
3. confirm exactly one record for each overall scan **261–282** and Part-local page **1–22**;
4. confirm continuous printed pages **228–249** and Kural **1116–1225**;
5. confirm chapter 112 completes at Kural 1120, chapters 113–122 are complete, and chapter 123 is present only through Kural 1225 in Part 013;
6. confirm the incoming Part 012 → Part 013 boundary **printed 227 → 228 / Kural 1115 → 1116**;
7. confirm the source-visible `இன்பம் — களவியல்` → `இன்பம் — கற்பியல்` transition at scan **278 / printed page 245 / Kural 1201**;
8. confirm all 22 statuses are `verified`, all metadata/source markers align, and no unresolved `needs-review`, `partial`, `blocked`, or missing record remains;
9. confirm the three verification corrections above and the protected Kural 1152 / Kural 1220 readings remain intact;
10. inspect only the necessary first page of the supplied Part 014 source to establish the outgoing boundary after scan 282 / printed page 249 / Kural 1225; do not transcribe Part 014;
11. create `works/thirukkural/AUDIT_PART_013.md` with an explicit PASS / FAIL archival-ready decision;
12. synchronize root README, work README, English `TRANSLATION_STATUS.md`, and this handover after the audit;
13. stop after the audit gate;
14. do **not** begin Part 013 English in the same activity;
15. do **not** begin Parts 014–015 Tamil transcription in the same activity.

If the audit passes, the following separate activity is **Part 013 English project translation — first pass**, with all aligned English records created only as `status: "draft"`.
