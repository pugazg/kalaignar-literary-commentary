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
6. for English work also read:
   - `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`;
   - `works/thirukkural/translations/en/GLOSSARY.md`;
   - `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
   - `works/thirukkural/translations/en/reviews/PART_008_REVIEW.md`;
   - `works/thirukkural/translations/en/reviews/PART_008_RELEASE_REPORT.md`;
   - `works/thirukkural/AUDIT_PART_009.md`.

Repository state is authoritative.

## Source rule

The supplied Tamil scans are controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

Source PDFs are working/control sources and are not to be committed to GitHub unless the user explicitly requests that.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Keep these as separate gates.

# Established state

## Tamil

Parts **001–009 are audited / ARCHIVAL-READY continuously** through:

- overall scan **191**;
- printed page **158**;
- Kural **780**.

Latest Tamil audit: `works/thirukkural/AUDIT_PART_009.md`.

## English project translation

Parts **001–008 are fully released** continuously through Kural **670**.

Part 009 English **first-pass translation is complete 22/22** through Kural **780**. All Part 009 English pages remain `draft`; direct source-check has not yet begun.

Every English page must identify:

```yaml
translation_type: "project_translation"
```

Released Parts 001–008 must not be revised merely to harmonize later vocabulary.

Permanent earlier protections remain binding, including chapter 38 `ஊழ்` → **Oozh**, `இயற்கை நிலை` → **natural condition**, and Kural 543's Kalaignar-directed `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**.

# Part 009 Tamil — ARCHIVAL-READY

Controlling source: `திருக்குறள்_கலைஞர்_உரை_part_009_pages_170-191.pdf`

Final Tamil scope:

- physical pages: **22**;
- scans **170–191**;
- printed pages **137–158**;
- Kural **671–780**;
- chapters **68–78**;
- `verified`: **22 / 22**;
- `needs-review`: **0**;
- `partial`: **0**;
- `blocked`: **0**;
- audit decision: **PASS / ARCHIVAL-READY**.

Chapter map:

- 68 `வினை செயல்வகை` — 671–680;
- 69 `தூது` — 681–690;
- 70 `மன்னரைச் சேர்ந்து ஒழுகல்` — 691–700;
- 71 `குறிப்பறிதல்` — 701–710;
- 72 `அவை அறிதல்` — 711–720;
- 73 `அவை அஞ்சாமை` — 721–730;
- 74 `நாடு` — 731–740;
- 75 `அரண்` — 741–750;
- 76 `பொருள் செயல்வகை` — 751–760;
- 77 `படை மாட்சி` — 761–770;
- 78 `படைச் செருக்கு` — 771–780.

Source-visible section sequence:

`அமைச்சியல்` → `அரணியல்` → `கூழியல்` → `படையியல்`.

Do not flatten these distinctions in English.

## Protected Tamil readings

These were directly verified and must remain the translation basis:

- Kural **717**: `கற்றறிந்தார் கல்வி விளங்கும் கசடறச் / சொற்றெரிதல் முன்னர் இழுக்கு.`
- Kural **725 commentary**: `தருக்கமென்படும் அளவைக் திறமும்`
- Kural **733 commentary**: `மளவுக்கு வளம்`
- Kural **771 commentary**: corrected/verified `நடுகல்லாய்ப் போனவர்கள்`.

## Adjacent continuity

Part 008 printed page **136** / Kural **670** continues into Part 009 printed page **137** / Kural **671**.

The supplied Part 010 first page has been inspected for boundary continuity only: printed page **159**, chapter `79. நட்பு`, Kural **781**. Part 010 remains untranscribed.

# Part 009 English — FIRST-PASS COMPLETE / SOURCE-CHECK PENDING

All **22 / 22** aligned Part 009 English page records exist under `works/thirukkural/translations/en/pages/`.

Scope:

- scans **170–191**;
- printed pages **137–158**;
- Kural **671–780**;
- chapters **68–78**.

Current status:

- `draft`: **22 / 22**;
- `source-checked`: **0**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

Every Part 009 English page currently uses:

```yaml
translation_type: "project_translation"
status: "draft"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

No page has been advanced to a later English gate.

## Part 009 English files

- `0170-porul-vinai-seyalvagai-01.md`
- `0171-porul-vinai-seyalvagai-02.md`
- `0172-porul-thoothu-01.md`
- `0173-porul-thoothu-02.md`
- `0174-porul-mannarai-sernthu-ozhugal-01.md`
- `0175-porul-mannarai-sernthu-ozhugal-02.md`
- `0176-porul-kuripparithal-01.md`
- `0177-porul-kuripparithal-02.md`
- `0178-porul-avai-arithal-01.md`
- `0179-porul-avai-arithal-02.md`
- `0180-porul-avai-anjaamai-01.md`
- `0181-porul-avai-anjaamai-02.md`
- `0182-porul-naadu-01.md`
- `0183-porul-naadu-02.md`
- `0184-porul-aran-01.md`
- `0185-porul-aran-02.md`
- `0186-porul-porul-seyalvagai-01.md`
- `0187-porul-porul-seyalvagai-02.md`
- `0188-porul-padai-maatchi-01.md`
- `0189-porul-padai-maatchi-02.md`
- `0190-porul-padai-serukku-01.md`
- `0191-porul-padai-serukku-02.md`

## First-pass chapter headings

- 68 `வினை செயல்வகை` → **The Method of Action**;
- 69 `தூது` → **The Envoy**;
- 70 `மன்னரைச் சேர்ந்து ஒழுகல்` → **Conduct in the Presence of Kings**;
- 71 `குறிப்பறிதல்` → **Understanding Signs (Porul)**;
- 72 `அவை அறிதல்` → **Knowing the Assembly**;
- 73 `அவை அஞ்சாமை` → **Fearlessness in the Assembly**;
- 74 `நாடு` → **The Country**;
- 75 `அரண்` → **Fortress**;
- 76 `பொருள் செயல்வகை` → **The Way of Acquiring Wealth**;
- 77 `படை மாட்சி` → **Excellence of the Army**;
- 78 `படைச் செருக்கு` → **Martial Pride**.

These are first-pass choices. Do not treat them as final released controls before editorial/glossary review.

## First-pass structural vocabulary

The already controlled Part 008 term continues:

- `அமைச்சியல்` → **Ministerial Affairs**.

New Part 009 structural labels are provisionally represented as:

- `அரணியல்` → **Fortification Affairs**;
- `கூழியல்` → **Wealth**;
- `படையியல்` → **Military Affairs**.

These three new terms are **provisional only**. Do not add them to the controlled glossary as final decisions during source-check; glossary reconciliation is a later separate gate.

## First-pass source-sensitive treatments

### Kural 717 — scan 179

The draft deliberately translates the supplied edition's verified unusual Tamil rather than substituting familiar external wording. The page carries a clearly marked `Draft source note` recording the exact Tamil basis. Source-check must determine whether the English can be made more faithful/clear without changing the Tamil reading.

### Kural 725 commentary — scan 180

The audited phrase `தருக்கமென்படும் அளவைக் திறமும்` is retained as the basis. The current draft renders the key idea as **“the skill of measure called logic”** and includes a draft source note. Verify directly against the audited Tamil; do not repair the Tamil.

### Kural 733 commentary — scan 182

The audited `மளவுக்கு வளம்` is retained. The draft currently uses **“possesses wealth to that measure”** and records the source phrase in a draft note. Verify fidelity without normalizing the Tamil.

### Kural 771 commentary — scan 190

The verified `நடுகல்லாய்ப் போனவர்கள்` is translated using the direct image **“have become memorial stones.”** Preserve the source image unless source-check shows a clearer equally faithful English rendering.

## Other fidelity points carried into first pass

Kalaignar's institutional/public vocabulary is deliberately retained where explicit: government, tax/revenue, customs duties, tribute, country, fortification, wealth, army, ruler/leader and public responsibility.

Direct images have been retained, including one elephant capturing another, warming by fire, the cashew-nut comparison in commentary, nectar in an unclean courtyard, love/compassion/nurse-material-resources, elephants fighting viewed from a hill, rats/the sea/cobra breath, victory garland, memorial stones, a spear pulled from a warrior's chest, honourable battle wounds and the warrior's anklet.

Kural 773 currently retains Kalaignar's explicit `பெரும் ஆண்மை` / `ஆண்மையின் உச்சம்` framing as **great manliness / manliness** rather than sanitizing it in the first pass. Review only for fidelity/clarity at source-check; do not replace Kalaignar's emphasis merely for modern stylistic preference.

# Exact next activity

Perform the separate **Part 009 English direct source-check** for all **22 `draft` pages**, scans **170–191 / printed pages 137–158 / Kural 671–780**.

## Required source-check procedure

1. fresh-read this handover, the translation guide, glossary, translation status, Part 008 review/release artefacts and Part 009 Tamil audit;
2. inspect all 22 current Part 009 English pages and confirm each begins at `status: "draft"`;
3. compare every English Kural line directly with the corresponding audited Tamil Kural;
4. compare every English Kalaignar commentary paragraph directly with the audited Tamil commentary;
5. verify Kural/commentary separation, two-line verse structure, page alignment, source-Tamil path, printed page, chapter heading and section metadata;
6. preserve Kalaignar's institutional/social vocabulary and direct images rather than importing a conventional Kural gloss;
7. explicitly source-check Kural 717, Kural 725 commentary, Kural 733 commentary and Kural 771 commentary against their protected audited Tamil readings;
8. document every substantive English correction made during source-check;
9. promote only passing pages from `draft` to `source-checked`;
10. synchronize `TRANSLATION_STATUS.md`, English README, work README, root README and this handover at the end of the source-check gate;
11. stop after direct source-check.

## Do not start alongside source-check unless explicitly requested

Do **not**:

- perform Part 009 editorial consistency / glossary reconciliation;
- create `PART_009_REVIEW.md`;
- perform the Part 009 release gate or create a release report;
- promote any Part 009 page beyond `source-checked`;
- begin Part 010 Tamil transcription;
- alter released English Parts 001–008 merely for harmonization.

# After Part 009 English source-check

If all 22 pages pass source-check, the next separate activity is **Part 009 English editorial consistency / glossary reconciliation**, including deliberate final decisions for Part 009 chapter headings and the new section terms `அரணியல்`, `கூழியல்` and `படையியல்`.
