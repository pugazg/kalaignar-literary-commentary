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
6. inspect the actual controlling source scan needed for the activity;
7. for English work additionally fresh-read:
   - `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`;
   - `works/thirukkural/translations/en/GLOSSARY.md`;
   - `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
   - latest completed review/release artefacts, currently `PART_009_REVIEW.md` and `PART_009_RELEASE_REPORT.md`;
   - `works/thirukkural/AUDIT_PART_010.md`.

Repository state is authoritative.

## Source rule

The supplied Tamil scans are controlling sources. Do not silently modernize, normalize, correct, reconstruct or replace their wording from memory, the web or another edition.

Source PDFs are working/control sources and are not to be committed to GitHub unless the user explicitly requests that.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Keep these as separate gates.

# Established state

## Tamil

Parts **001–010 are audited / ARCHIVAL-READY continuously** through:

- overall scan **214**;
- printed page **181**;
- Kural **895**.

Latest Tamil audit: `works/thirukkural/AUDIT_PART_010.md` — **PASS / ARCHIVAL-READY**.

## English project translation

Parts **001–009 are fully released continuously** through Kural **780**.

Part 010 English first-pass translation is now **COMPLETE 23 / 23** through Kural **895**. All Part 010 English pages remain `draft`; direct source-check has not begun.

Every English page must identify:

```yaml
translation_type: "project_translation"
```

Released Parts 001–009 must not be revised merely to harmonize later vocabulary.

Permanent earlier protections remain binding, including chapter 38 `ஊழ்` → **Oozh**, `இயற்கை நிலை` → **natural condition**, Kural 543's Kalaignar-directed `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**, and all Part 009 release decisions documented in its review/release report.

# Part 010 Tamil — ARCHIVAL-READY

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_010_pages_192-214.pdf`

Audit:

`works/thirukkural/AUDIT_PART_010.md`

Decision: **PASS / ARCHIVAL-READY**.

Audited scope:

- physical pages: **23**;
- overall scans: **192–214**;
- Part-local pages: **1–23**;
- printed pages: **159–181**;
- Kural range present: **781–895**;
- source section throughout: `பொருள் — நட்பியல்`;
- chapters visible: **79–90**;
- `verified`: **23 / 23**;
- `needs-review`: **0**;
- `partial`: **0**;
- `blocked`: **0**.

Part 009 → Part 010 continuity passed at printed page **158 → 159** / Kural **780 → 781**.

Direct visual verification found **no first-pass Tamil body-text correction requiring a change**.

The source-sensitive scan **209 / Kural 869 commentary** was directly confirmed as:

`அஞ்சிடும் கோழைகளாகவும், அறிவில்லாக் கோழைகளாகவும் பகைவர்கள் இருப்பின் அவர்களை எதிர்ப்போரை விட்டு வெற்றியெனும் இன்பம் விலகாமலே நிலைத்து நிற்கும்.`

Do not silently smooth, deduplicate or normalize that Tamil basis.

The supplied source ends at printed page **181 / Kural 895**, halfway through chapter 90 `பெரியாரைப் பிழையாமை`. Do not infer Kural 896 onward without the next controlling source.

# Part 010 English — FIRST PASS COMPLETE

All **23 / 23** aligned English pages now exist under `works/thirukkural/translations/en/pages/` and remain:

```yaml
translation_type: "project_translation"
status: "draft"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

Current Part 010 English state:

- `draft`: **23 / 23**;
- `source-checked`: **0**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

## Part 010 English page files

- `0192-porul-natpu-01.md`
- `0193-porul-natpu-02.md`
- `0194-porul-natpaaraaythal-01.md`
- `0195-porul-natpaaraaythal-02.md`
- `0196-porul-pazhaimai-01.md`
- `0197-porul-pazhaimai-02.md`
- `0198-porul-thee-natpu-01.md`
- `0199-porul-thee-natpu-02.md`
- `0200-porul-koodaa-natpu-01.md`
- `0201-porul-koodaa-natpu-02.md`
- `0202-porul-pethaimai-01.md`
- `0203-porul-pethaimai-02.md`
- `0204-porul-pullarivaanmai-01.md`
- `0205-porul-pullarivaanmai-02.md`
- `0206-porul-igal-01.md`
- `0207-porul-igal-02.md`
- `0208-porul-pagai-maatchi-01.md`
- `0209-porul-pagai-maatchi-02.md`
- `0210-porul-pagaithiram-therithal-01.md`
- `0211-porul-pagaithiram-therithal-02.md`
- `0212-porul-utpagai-01.md`
- `0213-porul-utpagai-02.md`
- `0214-porul-periyaaraip-pizhaiyaamai-01.md`.

## Provisional Part 010 first-pass terminology

The section-level rendering currently used is:

- `நட்பியல்` → **Friendship** — **provisional**.

First-pass chapter headings:

- 79 `நட்பு` → **Friendship**;
- 80 `நட்பாராய்தல்` → **Examining Friendship**;
- 81 `பழைமை` → **Long-Standing Friendship**;
- 82 `தீ நட்பு` → **Harmful Friendship**;
- 83 `கூடா நட்பு` → **False Friendship**;
- 84 `பேதைமை` → **Folly**;
- 85 `புல்லறிவாண்மை` → **Possession of Little Understanding**;
- 86 `இகல்` → **Discord**;
- 87 `பகை மாட்சி` → **The Character of Enmity**;
- 88 `பகைத்திறம் தெரிதல்` → **Discerning Enmity**;
- 89 `உட்பகை` → **Internal Enmity**;
- 90 `பெரியாரைப் பிழையாமை` → **Not Offending the Great**.

These are first-pass choices only. `GLOSSARY.md` was deliberately **not** updated at this gate because the project has previously finalized new structural controls during the later editorial consistency / glossary reconciliation gate. Do not treat these provisional forms as released controls yet.

## Part 010 first-pass fidelity points

1. Kural/commentary separation and two-line English Kural structure are present on all aligned pages.
2. Kalaignar's direct language and images are retained rather than replaced by a standard English Thirukkural translation.
3. Kural **850** commentary retains Kalaignar's evidence/truth framing and the quoted **“ghosts”** image.
4. Kural **813** commentary retains the source's explicit comparison involving **women for hire** and thieves rather than neutralizing the social/gender specificity.
5. Kural **835** uses the source commentary's **seven periods** without importing an external doctrinal “seven births” explanation.
6. Scan **209 / Kural 869 commentary** preserves the repetition in English as **“cowards who are afraid, and ignorant cowards”** rather than silently repairing it.
7. Kural **895** retains the distinction between the Kural's ruler language and Kalaignar commentary's government framing.
8. No Kural **896** or later English text has been created.

# Exact next activity

Perform the separate **Part 010 English direct source-check** for all **23 `draft` pages**, scans **192–214 / printed pages 159–181 / Kural 781–895**.

## Required Part 010 English source-check procedure

1. fresh-read all mandatory English startup files above;
2. inspect `AUDIT_PART_010.md`, all 23 verified Tamil Part 010 records, and all 23 English draft records;
3. compare each translated Kural against the verified Tamil Kural for number, two-line structure, omissions, additions and meaning drift;
4. compare every Kalaignar commentary paragraph directly against the corresponding verified Tamil commentary;
5. preserve Kalaignar's actual interpretive direction rather than substituting a standard Kural gloss;
6. verify `source_scan_page`, `source_tamil_file`, `printed_page`, section/chapter metadata, `translation_type`, `source_tamil_status`, translation basis and source marker for all 23 pages;
7. pay special attention to first-pass interpretive risk points, including Kural 813, 835, 849, 850, 861, 869, 876 and 895;
8. specifically retain the source-supported Kural 869 repetition rather than smoothing it away;
9. document every substantive correction made during source-check;
10. promote only pages that pass to:

```yaml
status: "source-checked"
```

11. keep provisional section/chapter terminology provisional; do not perform the later glossary/editorial gate during source-check;
12. synchronize `TRANSLATION_STATUS.md`, English README, work README, root README and this handover after the complete source-check;
13. stop after source-check.

## Do not combine with source-check

Do **not**:

- create `PART_010_REVIEW.md` during this activity;
- finalize `நட்பியல்` or chapter-heading glossary controls during this activity;
- promote pages to `editorial-reviewed` or `release-ready`;
- create `PART_010_RELEASE_REPORT.md`;
- begin unsupplied Tamil or English continuation after Kural 895;
- alter released English Parts 001–009 merely for harmonization.

If all 23 pages pass source-check with no blocker, the next separate activity will be **Part 010 English editorial consistency / glossary reconciliation**.
