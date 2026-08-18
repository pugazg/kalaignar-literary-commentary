# Thirukkural — Kalaignar Commentary Archival Guidelines

This document is the work-specific operating guide for `works/thirukkural/` in `pugazg/kalaignar-literary-commentary`.

It supplements the repository-level `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`. If there is any ambiguity, the source scan and the stricter source-preservation rule govern.

Last synchronized with the completed supplied-volume baseline: **2026-08-18**.

## 1. Controlling-source rule

> **The supplied scan is the controlling source.**

The Markdown archive is a preservation layer, not a corrected, modernized or normalized edition.

Never silently:

- correct spelling because another edition differs;
- modernize historical spelling, sandhi, punctuation or grammar;
- replace a Kural with a memorized or internet version;
- standardize names, numbers or compounds;
- reconstruct unclear letters from context alone;
- treat OCR or parsed text as authoritative;
- merge printed text with stamps, handwriting, bleed-through or scanner artefacts.

If a reading is genuinely unclear, preserve uncertainty with `needs-review`, `partial` or `blocked` rather than guessing.

## 2. Source files are not stored in GitHub

The supplied PDFs are working/control sources and should not be committed to this repository unless the user explicitly changes that policy.

Archive the transcription, metadata, audit trail, translation and review artefacts in GitHub; keep the scan itself outside the repository.

## 3. Page-aligned Tamil archive

Every physical scan page must have one corresponding Markdown record, including covers, blanks, title pages, contents and body pages.

For body pages use front matter of this form:

```yaml
---
scan_page: 163
part: 8
part_page: 15
printed_page: "130"
work: "thirukkural"
section: "பொருள் — அமைச்சியல் — அமைச்சு"
page_type: "commentary"
status: "needs-review"
language: "ta"
source_filename: "திருக்குறள்_கலைஞர்_உரை_part_008_pages_149-169.pdf"
transcription_method: "manual transcription from source scan; direct visual verification pending"
---
```

Tamil status vocabulary:

- `not-started`
- `needs-review`
- `partial`
- `verified`
- `blocked`

Use `verified` only after a direct page-image comparison with the controlling scan.

## 4. Tamil transcription fidelity

For every Kural page preserve:

- chapter number and chapter title when printed;
- Kural number;
- the source-supported two-line verse structure;
- printed joins and spacing where they are meaningful;
- punctuation and quotation marks supported by the scan;
- Kalaignar commentary wording and paragraph boundaries;
- printed running-header structural distinctions such as `அரசியல்` and `அமைச்சியல்`.

Do not improve Kalaignar's prose. The purpose is to preserve his wording exactly as printed in this edition.

## 5. Tamil workflow — mandatory gates

For each supplied PDF part:

1. **Source intake** — inspect the actual scan, identify physical page count, printed-page range and Kural range.
2. **First-pass transcription** — create all page records with `status: "needs-review"`.
3. **Direct visual verification** — compare every Markdown record line-by-line with the scan and change passing pages to `verified`.
4. **Part audit** — only after every page is resolved, create `AUDIT_PART_XXX.md` and make an explicit archival-ready decision.
5. **English work may begin only after the Tamil part is archival-ready.**

Do not collapse transcription, verification and audit into a single gate merely to move faster.

### Verification requirements

Compare all of the following:

- Kural text letter-for-letter;
- Kural line breaks;
- joins and word spacing visible in the edition;
- punctuation;
- chapter heading;
- running header / structural section;
- Kalaignar commentary;
- printed-page metadata;
- scan-page metadata.

Every real correction discovered during verification must be documented in the handover/audit trail.

## 6. Part audit requirements

A part may be declared `ARCHIVAL-READY` only when:

- all expected physical scan pages have records;
- scan numbering is continuous;
- printed-page/Kural continuity is understood;
- all records are `verified`, except deliberately documented source-limited cases;
- no unresolved `needs-review` or `blocked` page remains;
- transitions between chapters/sections and adjacent PDF parts are checked;
- all corrections found during verification are documented.

The audit is a separate activity after verification. Do not call a part archival-ready merely because the final verification page passed.

## 7. English translation identity

The English in this repository is a **project-created translation**, not a publisher or official English edition.

Every English page should identify:

```yaml
translation_type: "project_translation"
```

The corresponding audited Tamil Markdown page is the working basis; the Tamil scan remains the ultimate source authority.

## 8. Retain Kalaignar's language and interpretation

This is a permanent project requirement.

Translate Kalaignar's actual wording, argument, images, social vocabulary and interpretive direction. Do not silently substitute a familiar conventional interpretation of the Thirukkural.

Important established examples:

- Chapter 38 `ஊழ்` remains **Oozh** as the chapter heading, while Kalaignar's repeated explanatory phrase `இயற்கை நிலை` is rendered **natural condition**. Do not replace his explanation with a generic fate/destiny doctrine.
- At Kural 543, Kalaignar explicitly explains `அந்தணர் நூற்கும்` through `அறவோர் நூல்களுக்கும்`. The English therefore follows his interpretation as **the books of the virtuous**. Do **not** automatically translate `அந்தணர்` as “Brahmin(s)” when Kalaignar's own commentary gives a different interpretive meaning.
- Preserve his government/administration, citizens, treasury, revenue, justice, public-resource and working-people vocabulary where the Tamil uses it.
- Preserve direct comparisons and images even when modern English might prefer to soften them.
- Preserve Kalaignar's rational/inquiry framing where he explicitly insists on examining what is true rather than accepting a claim because someone says it.

A smoother English sentence is acceptable only when it does not weaken, sanitize, doctrinally normalize or redirect the source.

## 9. English page structure

English pages mirror the Tamil filenames and page alignment.

Example:

```text
Tamil:
works/thirukkural/pages/0163-porul-amaichu-02.md

English:
works/thirukkural/translations/en/pages/0163-porul-amaichu-02.md
```

Keep the Kural translation and Kalaignar commentary translation visibly separate.

English statuses:

- `draft`
- `source-checked`
- `editorial-reviewed`
- `release-ready`
- `source-limited`
- `blocked`

## 10. English workflow — mandatory gates

For each archival-ready Tamil part:

1. **English first pass** — create all aligned pages as `draft`.
2. **Direct source-check** — compare each English page against the audited Tamil record; promote passing pages to `source-checked`.
3. **Editorial consistency / glossary reconciliation** — review controlled headings, recurring terms, punctuation and readability while protecting Kalaignar's wording; create `reviews/PART_XXX_REVIEW.md`; promote passing pages to `editorial-reviewed`.
4. **Release gate** — perform final consistency/alignment review, create `reviews/PART_XXX_RELEASE_REPORT.md`, and only then promote pages to `release-ready`.

Do not combine source-check, editorial review and release into one activity.

## 11. Glossary and chapter headings

`works/thirukkural/translations/en/GLOSSARY.md` is the controlled terminology record for the project-created English translation.

Use the actual main-body context as authority for chapter heading decisions. An earlier contents/index page is useful evidence but does not overrule the main-body source.

When a deliberate term choice is introduced or refined, document it in the glossary and relevant review report.

Do not revise already released Parts merely because a later Part suggests an alternative phrasing. Any project-wide revision must be deliberate, source-supported and separately documented.

## 12. Repository-state discipline

At the beginning of every continuation session:

1. fetch `HANDOVER.md` fresh from `main`;
2. read this file completely;
3. read the relevant work README;
4. if English work is active, read `TRANSLATION_GUIDE.md`, `GLOSSARY.md`, `TRANSLATION_STATUS.md`, and the previous completed review/release report as the model;
5. if semantic/provenance work is active, read `structure/README.md`, `structure/CHAPTER_README_POLICY.md` and `structure/STRUCTURE_AUDIT.md`;
6. inspect the actual source pages needed for the current activity;
7. inspect existing target files before writing, and continue them rather than creating duplicates.

Repository state outranks conversational summaries. If a previous message and GitHub disagree, inspect the files and proceed from the repository's actual state.

## 13. Batch discipline

Work in sensible page batches, but do not arbitrarily limit activity to one page when a coherent multi-page batch can be safely completed.

At the end of each activity:

- update statuses only for pages actually completed;
- synchronize the work README and root README when project state changes materially;
- update `HANDOVER.md` with the exact next activity or explicit completed baseline;
- document corrections and protected translation decisions;
- stop at the requested gate.

Never claim a later gate is complete before its artefacts and page statuses exist in GitHub.

## 14. Permanent source/translation sequence

For a new source Part, the permanent sequence is:

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

Only after the current Part reaches the required gate should the next Part begin, unless the user explicitly instructs otherwise.

This sequence remains the rule for future new source material even though the currently supplied Parts 001–015 have completed it.

## 15. Semantic structure / provenance layer

The completed non-destructive semantic hierarchy is:

`works/thirukkural/structure/`

Hierarchy:

**பால் → இயல் → அதிகாரம்**

The semantic layer must remain separate from the physical-page archives.

Canonical physical layers:

- Tamil: `works/thirukkural/pages/`;
- released English: `works/thirukkural/translations/en/pages/`.

A semantic chapter README may record an exact physical boundary only after verification from actual canonical page records. It must capture the information required by `structure/CHAPTER_README_POLICY.md`, including exact scan(s), source Part(s), Part-local page(s), printed page(s), Kural coverage, Tamil/English paths, verification and any material source-sensitive notes.

Never:

- infer scan boundaries because most chapters use a similar physical pattern;
- move or duplicate page records into chapter folders;
- rewrite released English or canonical Tamil to make semantic labels uniform;
- create normalized duplicate chapter folders because spacing or joining differs;
- treat a source Part boundary as a semantic chapter break when Kural continuity is intact.

### Semantic / physical metadata discrepancies

If semantic classification and physical archive metadata differ, preserve both and document the discrepancy.

The completed controlling example is Inbam:

- semantic chapters **109–115** → `களவியல்`;
- semantic chapters **116–133** → `கற்பியல்`;
- physical archive retains `களவியல்` / `Clandestine Love` through scan **277**;
- scan **278** is the first physical `கற்பியல்` / `Wedded Love` page.

Chapters 116–121 document this transition. Do not normalize the physical archive retroactively.

### Cross-Part chapter continuity

A semantic chapter can span source Parts. Verified examples include:

- chapter 112: Part 012 → Part 013;
- chapter 123: Part 013 → Part 014;
- chapter 133: Part 014 → Part 015.

Record both physical records inside one semantic chapter node when chapter/Kural continuity is uninterrupted.

## 16. Completed supplied-volume baseline

As of **2026-08-18**, the supplied Thirukkural volume has completed all currently defined phases:

### Tamil

- Parts **001–015** archival-ready;
- scans **1–323** represented;
- commentary ends at printed page **270 / Kural 1330**;
- scans 304–321 are the first-word index;
- scan 322 blank;
- scan 323 back cover.

### English project translation

- Parts **001–015** released through the end of the supplied volume.

### Semantic provenance

- **3 / 3 பால்**;
- **13 / 13 இயல்**;
- **133 / 133 அதிகாரம்**;
- **1,330 / 1,330 குறள்**;
- final semantic audit: `works/thirukkural/structure/STRUCTURE_AUDIT.md` — **PASS**.

There is no unfinished current Part or semantic chapter to continue. Do not manufacture work after Kural 1330. A future activity must come from a newly supplied source or a separately defined enhancement/audit task.
