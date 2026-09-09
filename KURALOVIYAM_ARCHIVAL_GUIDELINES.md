# Kuraloviyam — Archival Guidelines

This is the work-specific operating guide for `works/kuraloviyam/` in `pugazg/kalaignar-literary-commentary`.

It supplements `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`. The controlling scan and the stricter source-preservation rule always govern.

## 1. Controlling-source rule

> **The rendered source scan is the controlling source.**

The Markdown archive is a preservation layer, not a corrected or normalized edition.

Never silently:

- correct spelling, punctuation, sandhi, names or numbers because another edition differs;
- replace a printed Kural with a memorized, web or standard-edition reading;
- modernize historical forms;
- reconstruct unclear letters from context;
- treat OCR, parsed text or model memory as source authority;
- merge printed text with handwriting, library marks, bleed-through or scanner artefacts.

If a reading is uncertain, use `needs-review`, `partial` or `blocked` rather than guessing.

## 2. Source identity and split-PDF rule

The complete Kuraloviyam source is reported as **666 physical PDF pages**, manually split into **six parts of 111 pages each**.

| Part | Overall scans |
|---|---:|
| 001 | 1–111 |
| 002 | 112–222 |
| 003 | 223–333 |
| 004 | 334–444 |
| 005 | 445–555 |
| 006 | 556–666 |

Repository `scan_page` always means the **overall 1–666 physical scan number**. It never restarts inside a later split. `part_page` may record the local 1–111 position.

Do not infer a later Part's exact filename, printed-page boundary, text, illustrations or continuity until that source is supplied.

## 3. Source files are not stored in GitHub

Split PDFs are controlling working sources and are not committed unless the user explicitly changes that policy.

Archive transcription, metadata, indexes, verification/audit records and project-created translation layers in GitHub.

## 4. Image-only / no-text-layer handling

Parts 001–003 expose no usable parsed text layer in the supplied file environment.

- inspect rendered page images directly;
- OCR may be a disposable aid only, never authority;
- do not fill unclear print from language knowledge or context;
- final source verification must compare repository text against the rendered scan.

## 5. Page-aligned Tamil archive

Every physical scan must have one page record, including covers, publication matter, prefaces, facsimiles, photographs, illustrations, blank source-side pages and body pages.

Core status vocabulary:

- `not-started`
- `needs-review`
- `partial`
- `verified`
- `blocked`

Use textual `verified` only after the required direct source comparisons are complete. A genuine source-limited page may remain `partial` permanently rather than being guessed.

Meaningful visual fidelity is tracked separately through `visual_fidelity` and may be `verified` even when textual status remains `partial`, provided the source-visible organization has been directly checked.

## 6. Kuraloviyam-specific fidelity

Kuraloviyam combines prose, Kural quotations/references and substantial illustration/layout work. Preserve, when source-supported:

- section/vignette headings and hierarchy;
- prose paragraph boundaries and dialogue structure;
- quoted Kural wording and printed lineation;
- `அதிகாரம்` / chapter labels, numbers and song/Kural references exactly as printed;
- quotation marks, separators and deliberate block placement;
- running headers and printed page numbers as page furniture rather than body prose;
- captions or text directly associated with illustrations;
- illustration/text order and relationship;
- continuation across physical page boundaries;
- non-body handwriting/stamps separately from printed body text.

Do not substitute standard Thirukkural wording for what this edition actually prints. Pixel-perfect artwork recreation is not required; factual `visual_notes` are sufficient.

## 7. Mandatory per-part closure workflow

> **Finish the entire required workflow for the currently supplied Part before beginning the next Part.**

For each Part, in order:

1. **Source intake** — confirm actual local page count, overall scan range, source identity and visible boundaries.
2. **Pass 1: physical capture / transcription** — create the complete page-aligned Tamil record set.
3. **Pass 2A: direct textual verification** — compare wording, punctuation, paragraph boundaries, Kural text and metadata against the rendered scan.
4. **Pass 2B: independent lexical-fidelity re-read** — after Pass 2A covers the whole Part, re-read every source-visible printed word independently; this is not normalization.
5. **Pass 3: meaningful visual-text verification** — verify headings, lineation, block relationships, page furniture, illustration/text relationships and physical continuations.
6. **Part audit** — verify complete physical coverage, internal continuity, source limits and the supplied Part boundary.
7. **Final metadata/status synchronization** — assign final textual/visual statuses without changing Tamil body wording.
8. **Documentation synchronization** — update work overview, page map/current frontier, audit/closure record, handover and next-chat prompt.
9. **Tamil archival-ready checkpoint** — declare the Part closed only when the above gates pass.
10. **Project-created English workflow, when maintained** — translate only from audited Tamil records, perform required review/status synchronization, and record a closed English checkpoint.
11. **Final Part closure** — only then may the next Part begin, and only when that next Part's source is supplied.

A page is not finally source-verified merely because Pass 2A completed. Pass 2B and Pass 3 must also close before final verification metadata is assigned.

## 8. Closed-Part source independence

After a Part reaches its closed checkpoint, repository records become the durable working layer for normal subsequent work.

Do **not** routinely require an older split PDF again while processing later Parts. Reopen an earlier Part source only when a newly discovered source/provenance/fidelity problem specifically requires an earlier scan to be checked.

The cross-Part boundary itself is checked only when the adjacent Part source becomes available; do not infer the missing side of a boundary.

## 9. Batch discipline

Default source-dependent work may use smaller batches when no user override exists. **Current user directive for Part 003 Pass 1 and Pass 2A page-batched work: 11 physical scans per normal iteration**, with a shorter final remainder when necessary.

For every source-dependent batch:

1. fetch live `main`;
2. resolve the exact split PDF;
3. inspect source images directly;
4. fetch existing target records before writing;
5. transcribe/correct only source-supported visible material;
6. preserve overall scan numbering;
7. commit sequentially;
8. inspect the changed-file set;
9. record the exact next frontier.

A workflow batch boundary never implies a narrative, quotation or Kural boundary. Inspect the first scan of the following batch only as a boundary witness when needed.

Pass 2B is performed only after Pass 2A reaches the end of the supplied Part so it functions as an independent second read.

## 10. English layers

If a published English Kuraloviyam source is supplied later, archive it separately as a source-controlled edition. Never mix it with a project-created translation.

A project-created English translation may be produced only from audited Tamil records and must declare:

```yaml
translation_type: "project_translation"
```

English translation must not silently alter or repair a source-limited Tamil reading. Where the Tamil archive explicitly marks unavailable/uncertain source text, the English layer must preserve that limitation rather than inventing a translation.

## 11. Current frontier

### Part 001 — overall scans 1–111

**Tamil + maintained English: CLOSED.**

English final state: **107 `release-ready` + 4 `source-limited`**.

### Part 002 — overall scans 112–222

**Tamil + maintained English: CLOSED.**

- Tamil: **111/111 textual verified + 111/111 visual verified / 0 exceptions**;
- English: **111/111 `release-ready`**;
- final Part checkpoint: **PASS / CLOSED**.

### Part 003 — overall scans 223–333

Controlling source: `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf`.

Source intake: **PASS / COMPLETE**.

- local pages: **111**;
- printed pages: **206–316**;
- file size: **93,488,924 bytes**;
- SHA-256: `f07e7cdb3a6e786b0378e00bbe699a241be41c9e099c004a4faa90fa82b4239f`;
- source text layer: no usable parsed text;
- **222→223: clean boundary** — Part 003 begins a new `பேதைமை` vignette;
- Pass 1: **COMPLETE — 111/111 captured, scans 223–333 / printed 206–316**;
- Pass 2A Batch 1: **COMPLETE — scans 223–233 / printed 206–216**;
- Pass 2A Batch 2: **COMPLETE — scans 234–244 / printed 217–227**;
- Pass 2A Batch 3: **COMPLETE — scans 245–255 / printed 228–238**;
- Pass 2A Batch 4: **COMPLETE — scans 256–266 / printed 239–249**;
- Pass 2A Batch 5: **COMPLETE — scans 267–277 / printed 250–260**;
- current Pass-2A frontier: **55/111 through scan 277 / printed 260**;
- **233→234 genuine continuation** reconfirmed during Pass 2A;
- **244→245 clean** reconfirmed from scan 245 boundary witness;
- **255→256 clean** reconfirmed from scan 256 boundary witness;
- **266→267 genuine continuation** reconfirmed from scan 267 boundary witness;
- **277→278 clean** reconfirmed from scan 278 boundary witness;
- scan 333 closes the final visible Part 003 unit with Chapter 57 / Kural 567;
- external **333→334** is deferred until Part 004 intake.

### Exact next content stage

Continue **Part 003 Pass 2A / Batch 6 — scans 278–288 / printed 261–271, 11 physical scans**. Begin after the confirmed clean **277→278** boundary, inspect scan **289 / printed 272** only as a boundary witness when necessary, preserve the known **288→289 genuine continuation**, correct only direct source-supported differences, preserve `needs-review` statuses, update the Pass-2A log, and audit the exact changed-file set before advancing.