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

Part 010 English:

- first pass: **COMPLETE 23 / 23**;
- direct source-check: **COMPLETE 23 / 23**;
- current status: **23 / 23 `source-checked`**;
- editorial consistency / glossary reconciliation: **not started**;
- release gate: **not started**.

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

# Part 010 English — SOURCE-CHECK COMPLETE

All **23 / 23** aligned English pages now exist under `works/thirukkural/translations/en/pages/` and use:

```yaml
translation_type: "project_translation"
status: "source-checked"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
```

Current Part 010 English state:

- `draft`: **0**;
- `source-checked`: **23 / 23**;
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

## Direct source-check corrections

The full comparison of all 23 English pages against the verified Tamil records produced **seven source-fidelity corrections/refinements across six English files**.

1. **Kural 813 — scan 198 / `0198-porul-thee-natpu-01.md`**
   - first pass: `women who sell intimacy`
   - source-checked: **`women for hire`**
   - reason: Kalaignar's commentary explicitly uses `விலைமகளிரும்`; “sell intimacy” added wording not supplied by him.

2. **Kural 822 — scan 200 / `0200-porul-koodaa-natpu-01.md`**
   - first pass Kural expanded the comparison as `women who merely appear to possess virtue`;
   - source-checked Kural uses **`women for hire`**;
   - Kalaignar's fuller explanation about lacking the good qualities expected of women while acting as if possessing them remains in the separate commentary, where the source places it.

3. **Kural 842 commentary — scan 204 / `0204-porul-pullarivaanmai-01.md`**
   - removed unsupported **`earned`** from the recipient's good fortune;
   - source-checked commentary now follows `பெறுகிறவன் பெற்றபேறு` without adding a theory of how that fortune was earned.

4. **Kural 849 — scan 205 / `0205-porul-pullarivaanmai-02.md`**
   - first pass had subject drift in the compressed Kural;
   - source-check used Kalaignar's adjacent commentary as the permitted interpretive aid;
   - source-checked Kural now states that **one who tries to make an unseeing person see becomes unseeing himself, while the unseeing person thinks he has seen in the way he himself sees**.

5. **Kural 850 — scan 205 / same file**
   - first pass inserted the commentary's evidence clause into the Kural itself;
   - source-checked Kural now stays with the Kural's own statement that one who denies what the world says exists is placed among the “ghosts”;
   - Kalaignar's explicit evidence/truth framing remains in the separate commentary, where the Tamil places it.

6. **Kural 867 commentary — scan 209 / `0209-porul-pagai-maatchi-02.md`**
   - removed unsupported added phrase **`and harmful to us`**;
   - source-checked wording follows `தனக்குப் பொருந்தாத காரியங்களை` as acts that do not befit one.

7. **Kural 887 — scan 213 / `0213-porul-utpagai-02.md`**
   - removed unsupported material qualifier **`metal`** from `செப்பு`;
   - source-checked Kural says a lid fitting its container, while commentary retains the source term *seppu* without inventing a material.

## Part 010 source-sensitive protections after source-check

The source-check deliberately retained these Kalaignar-specific or source-sensitive treatments:

1. **Kural 813** — explicit comparison involving **women for hire** and thieves remains, without neutralizing the social/gender specificity.
2. **Kural 835** — Kalaignar commentary's `ஏழு காலத்திலும்` remains **seven periods**; do not import an external “seven births” explanation.
3. **Kural 850 commentary** — retain Kalaignar's evidence/truth framing and quoted **“ghosts”** image.
4. **Kural 861** — retain Kalaignar's supplied interpretation: `மெலியோரை விடுத்து, வலியோரை எதிர்த்துப் போரிட விரும்புவதே பகைமாட்சி எனப் போற்றப்படும்.` Do not replace it with a familiar conventional Kural interpretation.
5. **Kural 869 commentary** — retain **“cowards who are afraid, and ignorant cowards”**. The repetition is source-confirmed and must not be silently smoothed.
6. **Kural 876** — retain the nuance of neither becoming too close to the enemy in friendship nor separating completely while maintaining hostility when danger arises.
7. **Kural 895** — retain the distinction between the Kural's **ruler** and Kalaignar commentary's **government** framing.
8. No Kural **896** or later English text exists.

## Provisional terminology — still not controlled

The section-level rendering remains:

- `நட்பியல்` → **Friendship** — **provisional**.

Current source-checked chapter headings remain provisional:

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

`GLOSSARY.md` was deliberately **not** updated during source-check. Finalizing these belongs to the next gate.

# Exact next activity

Perform the separate **Part 010 English editorial consistency / glossary reconciliation** for all **23 `source-checked` pages**, scans **192–214 / printed pages 159–181 / Kural 781–895**.

## Required editorial procedure

1. fresh-read all mandatory startup files above;
2. inspect `AUDIT_PART_010.md`, all 23 verified Tamil pages and all 23 source-checked English pages;
3. review the source-checked English as one continuous Part 010 unit for readability and consistency without weakening source fidelity;
4. deliberately finalize a project rendering for source structural term `நட்பியல்` based on the supplied main-body context;
5. deliberately finalize chapter headings **79–90** from the supplied main-body context;
6. update `works/thirukkural/translations/en/GLOSSARY.md` with the controlled section/chapter decisions and any recurring terminology decisions that genuinely need a project control;
7. preserve every source-check correction listed above;
8. preserve the source-sensitive Kural **835, 850, 861, 869, 876 and 895** treatments and other Kalaignar-specific language/images;
9. check recurring friendship/enmity vocabulary, social specificity, government/ruler distinctions, punctuation and readability without importing an external Thirukkural translation;
10. create `works/thirukkural/translations/en/reviews/PART_010_REVIEW.md` documenting the editorial/glossary decisions and any body-text changes made;
11. promote only passing Part 010 English pages to:

```yaml
status: "editorial-reviewed"
```

12. synchronize `TRANSLATION_STATUS.md`, English README, work README, root README and this handover;
13. stop after the editorial consistency / glossary-reconciliation gate.

## Do not combine with editorial review

Do **not**:

- create `PART_010_RELEASE_REPORT.md` in this activity;
- promote Part 010 pages to `release-ready`;
- alter released English Parts 001–009 merely for harmonization;
- infer or create Kural 896 onward without the next controlling Tamil source.

If all 23 pages pass editorial review, the next separate activity will be **Part 010 English release gate**.
