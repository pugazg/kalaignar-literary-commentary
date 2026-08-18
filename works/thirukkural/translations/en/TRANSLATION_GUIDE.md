# English Translation Guide — Thirukkural: Kalaignar's Commentary

This guide governs the project-created English translation of the archived Tamil `திருக்குறள் — கலைஞர் உரை`.

## 1. Translation identity

The English produced here is a **project translation**, not an official English edition unless a separately published English source is later supplied and archived independently.

Every translated page must therefore carry:

```yaml
translation_type: "project_translation"
```

Do not describe these files as "Kalaignar's official English translation", "publisher translation", or equivalent.

## 2. Controlling source

The supplied Tamil scan remains the ultimate authority.

The verified Tamil Markdown page is the working translation basis because it has already undergone direct source comparison. If a conflict is noticed between English, Tamil Markdown and the scan, stop and resolve the Tamil/source issue first.

Never silently use:

- a web Thirukkural text;
- another printed Tamil edition;
- an established English Kural translation;
- another commentator's explanation;
- memory of a familiar Kural;
- a modernized version of the Tamil.

## 3. Translation objective

The goal is **faithful, clear English that preserves the source's meaning and Kalaignar's interpretive voice**.

The translation should not become:

- a new commentary;
- a literary adaptation;
- a modernization of Kalaignar's ideas;
- a doctrinal reinterpretation;
- an attempt to harmonize Kalaignar with other commentators.

Natural English syntax is allowed and expected, but meaning, scope, emphasis and paragraph relationships must remain source-controlled.

## 4. Kural and commentary are separate layers

For main-body pages, preserve this structure:

```markdown
# 1. Worship

**1. [English Kural line 1]  
[English Kural line 2]**

[English translation of Kalaignar's commentary.]
```

Rules:

1. Preserve the Kural number.
2. Preserve the two-line verse structure.
3. Translate the Kural itself; do not substitute a prose paraphrase of Kalaignar's commentary.
4. Translate Kalaignar's commentary separately and preserve its paragraph boundary.
5. When the Kural is genuinely compressed or ambiguous, Kalaignar's adjacent commentary is the first permitted interpretive aid.
6. If a choice materially depends on interpretation rather than direct lexical/syntactic translation, add a concise translation note during review.
7. Do not use another commentator to settle the reading unless the user explicitly requests comparative research.

## 5. Commentary translation

Kalaignar's commentary should read naturally in English while staying close to the Tamil meaning.

Preserve:

- examples;
- contrasts;
- repetitions that carry emphasis;
- quoted expressions;
- rhetorical questions;
- references to social roles and relationships;
- gender specificity where the Tamil is specific;
- moral/political/social vocabulary without softening it.

Do not add explanatory material that Kalaignar did not provide merely to make the passage easier for an English reader.

## 6. Source typography versus English typography

The Tamil archival layer preserves source-specific spacing, joins and punctuation. English translation is not required to reproduce Tamil typographical spacing mechanically.

For example, a source form such as a split sandhi or historical word join should remain untouched in the Tamil page, while the English page may use normal English word spacing.

However, if an unusual Tamil form changes or complicates meaning, document that in a translation note rather than silently choosing a normalized Tamil source form.

## 7. Titles and chapter headings

Translate the heading actually used in this edition. Do not silently replace it with the heading preferred by another Thirukkural edition.

Use the controlled glossary as the default editorial vocabulary, but treat glossary entries as **context-aware defaults**, not mechanically forced equivalents.

If a chapter-title translation changes after review, update the glossary and relevant review record before applying the change consistently to affected English pages.

## 8. Core Tamil concepts

Some Tamil concepts do not have one perfect English equivalent.

The main example is `அறம்`.

Policy:

- In structural/book-level labels, prefer **Aram** with a short English gloss on first significant use, e.g. `Book of Aram (Virtue / Right Conduct)`.
- In running prose, translate contextually as `virtue`, `right conduct`, `ethical conduct`, `moral duty`, or another source-supported expression when English requires it.
- Do not force one English word into every occurrence if Kalaignar's sentence clearly uses a different shade of meaning.
- When consistency and contextual accuracy conflict, preserve meaning and record the choice in the glossary/review notes.

The same principle applies to terms such as `ஒழுக்கம்`, `அடக்கம்`, `நடுவுநிலைமை`, and `நன்றி`.

## 9. Names, titles and transliteration

Use familiar established English forms where they are unambiguous:

- Kalaignar
- M. Karunanidhi
- Thiruvalluvar
- Thirukkural

For Tamil technical terms retained in English, use simple readable transliteration without adding academic diacritics unless a later editorial decision explicitly adopts a diacritic system.

Do not anglicize personal names beyond established usage.

Honorifics and role labels should be translated or retained according to function and context, not deleted automatically.

## 10. Gender and social specificity

Do not make the source more gender-neutral than it is.

If the Tamil commentary explicitly says `பிறன் மனைவி`, translate that specificity rather than replacing it with a generic "another's partner".

Likewise, if the Tamil is generic, do not insert gender that the source does not require.

## 11. Quotations and culturally embedded phrases

Translate quoted expressions in the commentary as quotations. If a phrase is a culturally recognizable expression and a literal translation would obscure the immediate point, use a clear English rendering and add a short note only when necessary.

Do not replace a Tamil quotation with a pre-existing published English quotation unless that published wording is itself part of a separately supplied source.

## 12. Front matter

Prefaces, forewords, reviews, publisher's notes and other prose should be translated paragraph-by-paragraph from the verified Tamil record.

For contents and indexes:

- preserve entry order;
- preserve page/authority numbers as source metadata;
- translate labels consistently;
- do not harmonize distinct source spellings before translation.

## 13. Handwriting and partial Tamil sources

A project translation can never be more certain than its controlling Tamil source.

For Part 001 scan 8:

- create an English page only from the securely established Tamil heading/date/signature description;
- mark it `status: "source-limited"`;
- explicitly state that the continuous handwritten body was not safely readable in the controlling scan;
- do not infer or reconstruct its English content.

## 14. File alignment and front matter

Every English page mirrors the Tamil filename.

Example:

```text
Tamil:
works/thirukkural/pages/0056-aram-naduvu-nilaimai-01.md

English:
works/thirukkural/translations/en/pages/0056-aram-naduvu-nilaimai-01.md
```

Recommended front matter:

```yaml
---
source_scan_page: 56
source_tamil_file: "../../../pages/0056-aram-naduvu-nilaimai-01.md"
work: "thirukkural"
section: "Aram — Domestic Life — Impartiality"
language: "en"
translation_type: "project_translation"
status: "draft"
source_tamil_status: "verified"
translation_basis: "verified Tamil archival transcription; controlling scan remains authoritative"
---
```

Do not copy the Tamil `status: verified` into English. Tamil source verification and English translation review are separate states.

## 15. Translation statuses

### `draft`

A complete first English rendering exists for the translatable source content.

### `source-checked`

The English file has been compared against the verified Tamil page line-by-line / paragraph-by-paragraph for omissions, additions and meaning drift.

### `editorial-reviewed`

A second review has checked:

- English readability;
- consistent chapter titles;
- glossary terms;
- repeated phrasing;
- names and honorifics;
- punctuation and quotation handling;
- accidental interpretation drift.

### `release-ready`

The page is included in a completed part-level translation release review/report.

### `source-limited`

The English translation is necessarily incomplete because the Tamil source itself is partial.

### `blocked`

A documented source or interpretive problem prevents safe translation.

## 16. Review workflow for each source part

For every Tamil PDF part:

1. Tamil transcription complete.
2. Tamil direct visual verification complete.
3. Tamil part audit complete / archival-ready.
4. English first-pass translation created page-by-page.
5. English source-check pass.
6. Glossary updated/reconciled for new recurring terms.
7. Editorial consistency review.
8. Part-level translation release report.
9. Pages promoted to `release-ready` only after the report.

This means English translation proceeds **after each audited Tamil PDF part**, not after the entire book has been supplied.

## 17. Part-level review artefacts

Maintain:

```text
translations/en/
  README.md
  TRANSLATION_GUIDE.md
  GLOSSARY.md
  TRANSLATION_STATUS.md
  pages/
  reviews/
    PART_001_REVIEW.md
    PART_001_RELEASE_REPORT.md
    PART_002_REVIEW.md
    PART_002_RELEASE_REPORT.md
    ...
```

Create review/release files only when the relevant English page batch exists; do not create empty ceremonial reports.

## 18. External English editions discovered later

If the user later supplies a published English translation of this same work:

- archive it as a **separate source-controlled English edition**;
- inspect its own scan, metadata, pagination and wording;
- do not overwrite the project translation;
- do not silently retrofit the project translation to match it;
- create a separate alignment/comparison layer if desired.

Published English versions of other works such as `Sangatamil` or `Kuraloviyam` likewise retain their own source authority and must not be treated as project translations.

## 19. Repository-state discipline

Current progress is not defined by historical snapshots embedded in older guides or saved prompts.

When progress documents disagree, use this precedence:

1. actual page files on `main` and their metadata;
2. completed Tamil audits and English review/release reports;
3. `TRANSLATION_STATUS.md`;
4. completed semantic structure audit where relevant;
5. current handover/READMEs;
6. older status snapshots.

Permanent fidelity rules remain binding even when an old document's progress section is stale.

## 20. Current workflow point — COMPLETE BASELINE

Last synchronized with live `main`: **2026-08-18**.

Tamil Parts **001–015 are audited / ARCHIVAL-READY continuously** through the end of the supplied volume:

- scans **1–323**;
- commentary through printed page **270 / Kural 1330**;
- back matter through printed page **288**;
- scan 322 blank;
- scan 323 back cover.

English Parts **001–015 are RELEASED continuously** through the end of the same supplied volume.

The final commentary translation boundary is scan **303 / printed page 270 / Kural 1330**. Part 015's review and release reports are complete, and `TRANSLATION_STATUS.md` records no unreleased Thirukkural material.

The semantic navigation/provenance layer is also complete for **3 பால் / 13 இயல் / 133 அதிகாரம் / 1,330 குறள்**.

There is therefore **no active translation gate** for the supplied volume. Do not restart Part 014 source-check, Part 015 drafting/review/release, or earlier released Parts merely for stylistic harmonization.

The reviewed structural terminology remains controlled for future comparable work. In particular, where the physical source uses `இன்பம் — கற்பியல்`, the released project translation uses **Inbam — Wedded Love**; chapter 133 `ஊடலுவகை` is released as **Joy of Lovers' Quarrel**.

If a new source is supplied, begin a new source-specific workflow after direct inspection. A published English edition must be archived separately and must not overwrite this completed project translation.
