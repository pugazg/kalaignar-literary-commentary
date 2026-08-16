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

Part 009 English has completed its first-pass and **direct source-check 22/22** through Kural **780**. All 22 Part 009 English pages are now `source-checked`; editorial consistency / glossary reconciliation has not yet begun.

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

These were directly verified and remain the translation basis:

- Kural **717**: `கற்றறிந்தார் கல்வி விளங்கும் கசடறச் / சொற்றெரிதல் முன்னர் இழுக்கு.`
- Kural **725 commentary**: `தருக்கமென்படும் அளவைக் திறமும்`
- Kural **733 commentary**: `மளவுக்கு வளம்`
- Kural **771 commentary**: corrected/verified `நடுகல்லாய்ப் போனவர்கள்`.

## Adjacent continuity

Part 008 printed page **136** / Kural **670** continues into Part 009 printed page **137** / Kural **671**.

The supplied Part 010 first page has been inspected for boundary continuity only: printed page **159**, chapter `79. நட்பு`, Kural **781**. Part 010 remains untranscribed.

# Part 009 English — SOURCE-CHECK COMPLETE / EDITORIAL REVIEW PENDING

All **22 / 22** aligned Part 009 English page records exist under `works/thirukkural/translations/en/pages/` and are now `source-checked`.

Scope:

- scans **170–191**;
- printed pages **137–158**;
- Kural **671–780**;
- chapters **68–78**.

Current status:

- `draft`: **0**;
- `source-checked`: **22 / 22**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

Every Part 009 English page now uses:

```yaml
translation_type: "project_translation"
status: "source-checked"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

No page has been advanced beyond the direct source-check gate.

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

## Substantive source-check corrections

Exactly three substantive English body-text corrections were required:

1. **scan 171 / Kural 680 verse**
   - first pass: “When those of a smaller domain fear the trembling within ...”
   - source-checked: **“When those with little support fear the trembling among their own ...”**
   - reason: Kalaignar's commentary gives `தம்முடன் இருப்பவர்களே அஞ்சும்போது`; the earlier territorial “domain” framing was unsupported.
2. **scan 174 / Kural 691 verse**
   - first pass: “Those who live in the company of contentious kings ...”
   - source-checked: **“Those who live in the company of kings ...”**
   - reason: Kalaignar's commentary gives `முடிமன்னருடன் பழகுவோர்`; “contentious” added a characterization not present in his explanation.
3. **scan 179 / Kural 717 verse**
   - first pass ended fragmentarily with “faultless words, a lapse.”
   - source-checked: **“The learning of those who have learned and understood shines; before those who discern / faultless words, there is a lapse.”**
   - reason: retain the supplied edition's unusual verified `இழுக்கு` while making the English minimally complete. No external Kural text was substituted.

No other substantive body-text change was required during source-check.

## Protected source-sensitive treatments after source-check

### Kural 717 — scan 179

The source-checked English remains based on the verified supplied-edition Tamil:

`கற்றறிந்தார் கல்வி விளங்கும் கசடறச் / சொற்றெரிதல் முன்னர் இழுக்கு.`

The page carries a `Source-check note` making clear that the final `இழுக்கு` is preserved rather than replaced by a familiar external reading.

### Kural 725 commentary — scan 180

The audited `தருக்கமென்படும் அளவைக் திறமும்` remains the basis. English remains **“the skill of measure called logic”** and the page now carries a `Source-check note`; do not repair the Tamil during editorial review.

### Kural 733 commentary — scan 182

The audited `மளவுக்கு வளம்` remains the basis. English remains **“possesses wealth to that measure”** and the page carries a `Source-check note`; do not normalize the Tamil basis.

### Kural 771 commentary — scan 190

The verified `நடுகல்லாய்ப் போனவர்கள்` remains represented through the direct image **“have become memorial stones.”**

Kural **773** continues to retain Kalaignar's explicit `பெரும் ஆண்மை` / `ஆண்மையின் உச்சம்` framing as **great manliness / manliness**. Do not sanitize the source merely for modern stylistic preference.

## Other fidelity points confirmed

Kalaignar's institutional/public vocabulary remains where explicit: government, tax/revenue, customs duties, tribute, country, fortification, wealth, army, ruler/leader and public responsibility.

Direct images remain preserved, including one elephant capturing another, warming by fire, the cashew-nut comparison, nectar in an unclean courtyard, love/compassion/nurse/material-resources, elephants fighting viewed from a hill, rats/sea/cobra breath, victory garland, memorial stones, the spear pulled from a warrior's chest, honourable battle wounds and the warrior's anklet.

# Terminology entering editorial review

Current Part 009 chapter headings are provisional until this next gate:

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

The already controlled term remains:

- `அமைச்சியல்` → **Ministerial Affairs**.

New Part 009 structural labels remain **provisional** and must be deliberately reconciled during the next gate:

- `அரணியல்` → **Fortification Affairs**;
- `கூழியல்` → **Wealth**;
- `படையியல்` → **Military Affairs**.

They have not yet been entered as final controlled glossary vocabulary.

# Exact next activity

Perform the separate **Part 009 English editorial consistency / glossary reconciliation** for all **22 `source-checked` pages**, scans **170–191 / printed pages 137–158 / Kural 671–780**.

## Required editorial-review procedure

1. fresh-read this handover, the translation guide, glossary, translation status, Part 008 review/release artefacts and Part 009 Tamil audit;
2. inspect all 22 Part 009 English pages and confirm each begins at `status: "source-checked"`;
3. reconcile all Part 009 chapter headings against the supplied main-body Tamil context;
4. make deliberate final decisions for `அரணியல்`, `கூழியல்` and `படையியல்`, preserving their source-visible distinction from `அமைச்சியல்` and from one another;
5. review recurring vocabulary, readability, punctuation, names, institutional/social terminology and direct images without weakening Kalaignar's language;
6. preserve all three source-check corrections and the Kural 717 / 725 / 733 / 771 protected readings;
7. update `works/thirukkural/translations/en/GLOSSARY.md` with controlled Part 009 decisions;
8. create `works/thirukkural/translations/en/reviews/PART_009_REVIEW.md` documenting heading/term decisions and every substantive editorial body-text refinement;
9. promote only passing pages from `source-checked` to `editorial-reviewed`;
10. synchronize `TRANSLATION_STATUS.md`, English README, work README, root README and this handover;
11. stop after editorial/glossary review.

## Do not start alongside editorial review unless explicitly requested

Do **not**:

- perform the Part 009 release gate;
- create `PART_009_RELEASE_REPORT.md`;
- promote any Part 009 page to `release-ready`;
- begin Part 010 Tamil transcription;
- alter released English Parts 001–008 merely for harmonization.

# After Part 009 English editorial review

If all 22 pages pass, the next separate activity is the **Part 009 English release gate**.
