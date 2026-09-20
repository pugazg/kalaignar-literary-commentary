# English Translation Guide — Sangatamil

This guide governs the **project-created maintained English translation** of Kalaignar M. Karunanidhi's `சங்கத் தமிழ்`.

It models the maintained-English workflow used for Kuraloviyam while preserving Sangatamil's own archival state and its explicit Tamil-fidelity limitation.

## 1. Translation identity

This is a project translation, not a publisher-issued or official English edition.

Every English page must carry:

```yaml
translation_type: "project_translation"
```

A later published English source, if supplied, must be archived as a separate source-controlled edition. It must never silently replace this project translation.

## 2. Authority order

For normal translation/review work:

1. canonical Tamil page record under `works/sangatamil/pages/`;
2. user-adjudicated Gate-C2 decisions and post-C2 reconciliation;
3. closed Gate-E section and Gate-F provenance registers;
4. derived navigation under `works/sangatamil/navigation/`;
5. this guide and `GLOSSARY.md`;
6. `TRANSLATION_STATUS.md` and English review/release records.

The controlling scan remains ultimate source authority if a new fidelity problem is discovered.

Important: Gates A–I and the later dedicated Tamil WFV cycle are closed. Tamil WFV is **COMPLETE / PASS across 497/497 physical scans** with **496 verified / 0 needs-review / 1 source-limited partial (scan 8)**. English review/release status remains a separate workflow and must not alter Tamil source status.

## 3. Objective

Produce faithful, readable English preserving:

- Kalaignar's narrative and interpretive voice;
- imagery, rhetoric, dialogue and humour;
- paragraph movement and meaningful repetition;
- quoted Sangam verse as verse;
- poem/work/poet/provenance metadata;
- `பொருள் விளக்கம்` and other source-labelled explanatory blocks;
- source-supported visual descriptions;
- source-supported cross-page continuities.

Do not turn the translation into new commentary or ideological/literary harmonization.

## 4. Page alignment

Each English page mirrors its Tamil filename.

Example:

```text
Tamil:
works/sangatamil/pages/0017-malarmari-pozhiginren-01.md

English:
works/sangatamil/translations/en/pages/0017-malarmari-pozhiginren-01.md
```

Recommended front matter:

```yaml
---
source_scan_page: 17
source_tamil_file: "../../../pages/0017-malarmari-pozhiginren-01.md"
printed_page: "2"
work: "sangatamil"
section: "மலர்மாரி பொழிகின்றேன்!"
language: "en"
translation_type: "project_translation"
status: "draft"
source_tamil_status: "verified"
source_tamil_visual_fidelity: "verified"
translation_basis: "maintained canonical Tamil archival record after completed 497-scan WFV; controlling scan remains ultimate source authority; scan 8 remains source-limited"
---
```

Copy the Tamil status fields factually. Never promote a Tamil `needs-review` or `partial` record because an English page has passed review.

## 5. English statuses

- `draft` — complete first English rendering exists for safely translatable canonical Tamil content.
- `source-checked` — English has been compared paragraph-by-paragraph / block-by-block against the canonical Tamil record for omissions, additions and meaning drift.
- `editorial-reviewed` — readability, terminology, names, recurring phrasing, quoted verse, source labels and consistency have received a second review.
- `release-ready` — included in an approved English release report.
- `source-limited` — English is necessarily incomplete because the maintained Tamil record itself is partial or description-only.
- `blocked` — a documented source or interpretive problem prevents safe translation.

An English `release-ready` status certifies the maintained-English workflow only. Tamil WFV is separately and independently **COMPLETE / PASS**; English release status neither creates nor overrides that Tamil verification state.

## 6. Scan 8 permanent source limitation

Scan **8** contains the handwritten `முன்னுரை` facsimile retained as **description-only by explicit user direction**.

Its English record must:

- translate only the secure archival description / page function;
- not reconstruct or decipher the handwriting;
- remain `source-limited` unless the user explicitly changes the source policy.

## 7. Sangam verse handling

When Kalaignar quotes or presents a Sangam poem or fragment:

- translate the exact Tamil wording preserved in the canonical page record;
- preserve verse/block separation and source order;
- retain work name, poem number/range and poet attribution where present;
- preserve fragments as fragments;
- do not substitute a published English Sangam rendering;
- do not normalize the Tamil source through another edition;
- use Kalaignar's adjacent explanation / `பொருள் விளக்கம்` as the first interpretive aid when the classical phrase is compressed;
- if a material ambiguity remains, document it for review rather than invent certainty.

Source-printed Tamil incipits may be retained as source keys when useful for provenance/navigation.

## 8. Prose and dialogue

Translate narrative, commentary, dialogue, rhetorical questions, repeated emphasis and meaningful paragraph boundaries in source order.

Natural English syntax is expected, but additions unsupported by the Tamil are not permitted merely to make the passage smoother.

## 9. Titles and section headings

The 104 Gate-E section-role entries are authoritative for source-order identity.

English section titles may be translated for readability, but the Tamil printed heading remains the controlling identifier in metadata/navigation. Do not alter canonical Tamil slugs or section ranges to improve an English title.

## 10. Provenance

Gate F is closed at **115 formal provenance units + 4 source-note-only records**.

English translation must preserve the substance of:

- anthology/work name;
- poem number/range;
- poet attribution;
- quotation boundaries;
- source-labelled explanatory notes such as `பொருள் விளக்கம்`;
- other printed provenance notes.

Do not create new provenance from external editions.

## 11. Visual and non-body material

Translate factual archival descriptions of covers, illustrations, facsimiles and other non-body matter when they help preserve page meaning.

Do not invent captions or convert inferred imagery into printed text.

## 12. Controlled terminology

Use `GLOSSARY.md` as a context-aware editorial control, not a mechanical substitution table.

Names, Sangam work titles, literary terms and recurring source labels should remain consistent. Context may require different English renderings; record such decisions rather than forcing one word everywhere.

## 13. Permanent workflow

1. English page-aligned first-pass draft;
2. source-check against canonical Tamil record;
3. glossary / recurring terminology reconciliation;
4. editorial consistency review;
5. whole active release-unit review;
6. release report;
7. page promotion to `release-ready` only after approval;
8. final synchronization.

No English gate may silently modify canonical Tamil files.

## 14. Iteration discipline

Normal page-batched cadence: **37 consecutive physical scans**.

For drafting:
- use consecutive `scan_page` records;
- preserve section and cross-page continuities even when a batch cuts across them;
- source-limited pages count toward the batch.

For source-check:
- compare English to canonical Tamil paragraph-by-paragraph / block-by-block;
- check omissions, additions, meaning drift, names, titles, quotations, verse blocks, page function, provenance and continuity;
- do not use this gate for unrelated stylistic rewriting.

For glossary reconciliation:
- reconcile recurring names, Sangam work titles, literary terms, provenance labels and repeated English renderings;
- update the glossary only for terms actually evidenced in Sangatamil;
- do not import terminology from published translations or web sources.

For editorial review:
- improve readability only where source meaning remains intact;
- consult canonical Tamil whenever an edit could alter meaning;
- passing `source-checked` pages may move to `editorial-reviewed`.

For release:
- review the active release unit as a whole;
- preserve source-limited/blocked states;
- promotion to `release-ready` must not alter approved wording.

For every gate, fetch live `main` first, preserve newer state, update `TRANSLATION_STATUS.md`, and audit the exact changed-file set before advancing.

## 15. Final closed state

The maintained-English workflow is **RELEASE COMPLETE / CLOSED**:

- English records — **497/497**;
- `release-ready` — **496**;
- `source-limited` — **1** (scan 8);
- `blocked` — **0**;
- release report — `reviews/WHOLE_VOLUME_ENGLISH_RELEASE_REPORT.md`;
- exact next activity — **none required** unless new source evidence or an explicit correction reopens the work.
