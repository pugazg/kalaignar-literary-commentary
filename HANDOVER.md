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
   - the current Tamil audit, now `works/thirukkural/AUDIT_PART_010.md`.

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

Part 010 English has **not started** and is now eligible for first-pass translation.

Every English page must identify:

```yaml
translation_type: "project_translation"
```

Released Parts 001–009 must not be revised merely to harmonize later vocabulary.

Permanent earlier protections remain binding, including chapter 38 `ஊழ்` → **Oozh**, `இயற்கை நிலை` → **natural condition**, Kural 543's Kalaignar-directed `அறவோர் நூல்களுக்கும்` → **the books of the virtuous**, and all Part 009 release decisions documented in its review/release report.

# Part 009 English — RELEASE COMPLETE

Scope:

- scans **170–191**;
- printed pages **137–158**;
- Kural **671–780**;
- chapters **68–78**;
- aligned English records: **22 / 22**;
- final status: **22 / 22 `release-ready`**.

Release artefacts:

- `works/thirukkural/translations/en/reviews/PART_009_REVIEW.md`
- `works/thirukkural/translations/en/reviews/PART_009_RELEASE_REPORT.md`

Released structural vocabulary through Part 009:

- `அமைச்சியல்` → **Ministerial Affairs**;
- `அரணியல்` → **Fortification Affairs**;
- `கூழியல்` → **Wealth**;
- `படையியல்` → **Military Affairs**.

Do not flatten source-visible structural distinctions in later work.

# Part 010 Tamil — ARCHIVAL-READY

Controlling source:

`திருக்குறள்_கலைஞர்_உரை_part_010_pages_192-214.pdf`

Audit:

`works/thirukkural/AUDIT_PART_010.md`

Decision: **PASS / ARCHIVAL-READY**.

Final audited scope:

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

Part 010 chapter / page map:

- scans **192–193** / pp. **159–160** — `79. நட்பு` — Kural **781–790**;
- scans **194–195** / pp. **161–162** — `80. நட்பாராய்தல்` — **791–800**;
- scans **196–197** / pp. **163–164** — `81. பழைமை` — **801–810**;
- scans **198–199** / pp. **165–166** — `82. தீ நட்பு` — **811–820**;
- scans **200–201** / pp. **167–168** — `83. கூடா நட்பு` — **821–830**;
- scans **202–203** / pp. **169–170** — `84. பேதைமை` — **831–840**;
- scans **204–205** / pp. **171–172** — `85. புல்லறிவாண்மை` — **841–850**;
- scans **206–207** / pp. **173–174** — `86. இகல்` — **851–860**;
- scans **208–209** / pp. **175–176** — `87. பகை மாட்சி` — **861–870**;
- scans **210–211** / pp. **177–178** — `88. பகைத்திறம் தெரிதல்` — **871–880**;
- scans **212–213** / pp. **179–180** — `89. உட்பகை` — **881–890**;
- scan **214** / p. **181** — `90. பெரியாரைப் பிழையாமை` — **891–895** in this supplied part.

## Part 010 audit findings to preserve

1. complete **23 / 23** page coverage and continuous metadata passed;
2. Part 009 → Part 010 boundary passed at printed page **158 → 159** / Kural **780 → 781**;
3. direct visual verification found **no first-pass body-text correction requiring a change**;
4. scan **209 / Kural 869 commentary** was rechecked and the source confirms the repetition:

   `அஞ்சிடும் கோழைகளாகவும், அறிவில்லாக் கோழைகளாகவும் பகைவர்கள் இருப்பின் அவர்களை எதிர்ப்போரை விட்டு வெற்றியெனும் இன்பம் விலகாமலே நிலைத்து நிற்கும்.`

   Do not silently smooth, deduplicate or normalize this Tamil basis;
5. the supplied Part 010 source ends at printed page **181 / Kural 895**, halfway through chapter 90. The next source part is not supplied; **do not infer Kural 896 onward**.

# Exact next activity

Perform **Part 010 English project translation — first pass** for all **23 aligned archival-ready Tamil pages**, scans **192–214 / printed pages 159–181 / Kural 781–895**.

## Required Part 010 English first-pass procedure

1. fresh-read all mandatory English startup files listed above;
2. inspect `works/thirukkural/AUDIT_PART_010.md` and all 23 verified Part 010 Tamil records;
3. inspect the Part 010 English target directory first and continue existing work rather than creating duplicates; expected current state is no Part 010 English page records;
4. create one aligned English page for each Tamil filename under `works/thirukkural/translations/en/pages/`;
5. every new Part 010 English page must use:

```yaml
translation_type: "project_translation"
status: "draft"
```

6. preserve Kural number and a two-line translated Kural structure;
7. keep the Kural translation and Kalaignar commentary translation visibly separate;
8. translate Kalaignar's actual wording, reasoning, images and social vocabulary rather than substituting a familiar standard Kural gloss;
9. preserve the source-supported `பொருள் — நட்பியல்` hierarchy rather than flattening it;
10. determine first-pass English chapter headings for chapters **79–90** and a provisional project rendering for structural term `நட்பியல்` from the actual Tamil context and existing glossary/style; do not revise released Parts 001–009 merely to harmonize terminology;
11. protect scan **209 / Kural 869 commentary** as a source-sensitive basis and do not silently repair its repetition in the Tamil basis;
12. stop at Kural **895**; do not create or infer Kural 896 onward;
13. create exactly **23** Part 010 English records as `draft` if no source blocker arises;
14. update `TRANSLATION_STATUS.md`, English README, work README, root README and this handover after the first-pass gate; update `GLOSSARY.md` during first pass only if consistent with the project's prior practice for introducing provisional/controlled terms;
15. stop after the complete English first pass.

## Do not combine with Part 010 English first pass

Do **not**:

- promote any Part 010 English page to `source-checked` in the same activity;
- perform editorial consistency / glossary reconciliation as a later-gate substitute;
- create `PART_010_REVIEW.md` or `PART_010_RELEASE_REPORT.md` during first pass;
- begin any unsupplied Tamil continuation after Kural 895;
- alter released English Parts 001–009 merely for harmonization.

If all 23 English first-pass records are completed, the next separate activity will be **Part 010 English direct source-check**.
