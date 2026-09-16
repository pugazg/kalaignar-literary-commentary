# சங்கத் தமிழ் — Productive Completion Plan

## Purpose

This plan replaces the older open-ended eight-pass cadence with a **Kuraloviyam-style gated closure workflow**: one clearly bounded gate at a time, durable closure records, explicit exceptions, and no reopening of closed work without new evidence.

Controlling source:

`TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

Physical source boundary:

- **497 scans**;
- scan **497** — back cover;
- no scan 498+.

User-supplied lexical scaffold:

- `File1.md` … `File10.md`;
- together they cover the complete source sequence through the final Book Pages 414–484 / PDF scans 426–497 block;
- Gemini text remains the **locked lexical layer** unless the user explicitly authorizes lexical source correction.

## Authority split

1. **PDF scan** — physical page, structure, layout, headings, punctuation, lineation, page type, printed page number, continuation and provenance placement.
2. **Gemini File1–File10** — lexical/text wording lock.
3. **Repository** — preservation and derived navigation layer.

A scan/Gemini lexical disagreement is **recorded, not silently corrected**, while the lock remains active.

## Why this differs from the earlier workflow

The old plan mixed too many whole-volume passes and left several control files stale while page work advanced. The Kuraloviyam project succeeded because each gate had:

- a fixed scope;
- durable progress/closure records;
- explicit exceptions;
- status promotion only after the gate closed;
- derived sections only after the archival layer was stable.

Sangath Tamil will now use the same discipline.

# Gate A — Source bundle + repository hygiene

**Goal:** establish one clean physical record per scan before any new content gate.

Tasks:

1. confirm source boundary 1–497;
2. confirm all ten Gemini files are available;
3. inventory `pages/` by `scan_page`;
4. remove duplicate/stale page aliases so each physical scan has exactly one canonical page record;
5. confirm no missing scans;
6. record a durable hygiene report;
7. synchronize only the current control documents.

Closure condition:

- **497/497 unique canonical scan records**;
- **0 duplicate scan aliases**;
- **0 missing scans**.

# Gate B — Gemini-locked structural fidelity

**Goal:** make every canonical page structurally faithful to the PDF while preserving Gemini words.

Normal batch:

- **25 physical scans per iteration**;
- reduce only for unusually dense or damaged material;
- align naturally to the 50-scan Gemini blocks where practical.

For each scan:

- preserve Gemini lexical wording;
- correct physical page placement;
- correct paragraph order/boundaries;
- correct punctuation and quotation structure;
- correct headings/hierarchy;
- correct verse lineation/stanzas;
- correct speaker labels;
- correct citation / `பொருள் விளக்கம்` block placement;
- remove non-source OCR/stamp/handwriting garbage from body text;
- preserve illustration/divider/blank pages;
- record source-visible printed page number only.

Do **not** silently change legitimate lexical words.

Durable output:

`STRUCTURAL_FIDELITY_PROGRESS.md`

Closure:

- scans **1–497 structurally reviewed**;
- 0 unresolved structural placement issues, or explicit exceptions only.

# Gate C — Lexical discrepancy audit under the current lock

**Goal:** identify where the locked Gemini wording differs from the scan without changing it.

For each 25-scan batch:

- compare source-visible lexical text against Gemini/repository wording;
- record only substantive lexical discrepancies;
- distinguish:
  - likely Gemini error;
  - source-damaged/unclear;
  - old/uncommon form;
  - missing whole lexical block;
  - repository-only divergence.

Durable output:

`LEXICAL_DISCREPANCY_LEDGER.md`

Important:

**Gate C is an audit-only gate while the lexical lock is active.**

If the user later authorizes source correction, a separate **Gate C2 — lexical source correction** can promote the archive to true scan-word textual verification.

Without that authorization, final closure must say **Gemini-lexical-locked**, not “word-for-word scan verified.”

# Gate D — Physical / visual / continuity closure

Audit the complete 497-scan source for:

- one scan → one canonical record;
- covers/blanks/illustrations/dividers/end matter;
- printed pagination;
- running headers/footers;
- meaningful alignment;
- continuation relationships;
- cross-page sentence/verse continuity;
- shared-page or boundary anomalies.

Durable output:

`PHYSICAL_CONTINUITY_AUDIT.md`

# Gate E — Section reconstruction

Build the canonical source-order section layer only after Gate B/D are stable.

For every decorative/thematic section:

- exact printed heading;
- scan start/end;
- printed-page span;
- illustration placement;
- boundary evidence;
- direct links to page records.

Every scan 1–497 must be assigned to a section role:

- front matter;
- thematic section;
- illustration/divider;
- end matter/back cover.

Durable outputs:

- completed `indexes/section-register.md`;
- section READMEs;
- `SECTION_COVERAGE_AUDIT.md`.

# Gate F — Sangam provenance

Systematically verify source-visible:

- anthology/work name;
- பாடல் number/range;
- poet attribution;
- quoted Sangam verse block boundaries;
- `பொருள் விளக்கம்`;
- other printed source notes.

Do not silently replace this edition with another edition.

Durable outputs:

- completed `indexes/source-citation-register.md`;
- `PROVENANCE_AUDIT.md`.

# Gate G — Metadata/status closure

Audit all canonical page records for:

- `scan_page`;
- `printed_page`;
- `section`;
- `page_type`;
- status fields;
- continuation fields;
- source filename;
- transcription method;
- filename/path consistency.

Status rule:

- structural completion does not equal lexical scan verification;
- under the current lock, final wording state must remain explicitly **Gemini-lexical-locked**.

# Gate H — Derived navigation layer

After archival gates close, create Kuraloviyam-style downstream navigation without mutating page records.

Recommended hierarchy:

**Front matter / source collection or theme → section → Sangam citation unit → page span**

Then create:

- section-level navigation;
- citation/provenance crosswalk;
- individual leaf records where useful;
- JSON/TSV indexes for website/search/API use.

# Gate I — Final whole-volume closure

Synchronize:

- root/work README;
- HANDOVER;
- next-chat prompt;
- page map;
- section register;
- source citation register;
- all gate reports.

Final declaration must distinguish one of two outcomes:

### Outcome 1 — current lock retained

**STRUCTURAL / PHYSICAL / SECTION / PROVENANCE CLOSED — GEMINI-LEXICAL-LOCKED**

### Outcome 2 — user later authorizes Gate C2

**FULL TEXTUAL + VISUAL + STRUCTURAL + PROVENANCE CLOSED**

## Current active gate

**Gate C — lexical discrepancy audit under the current lock.**

Current durable state — **2026-09-16**:
- Gate A — COMPLETE / PASS
- canonical page records — 497/497
- duplicate aliases — 0
- missing scans — 0
- Gate B B01–B20 — **COMPLETE / PASS**
- structurally reviewed — **497/497**
- structurally remaining — **0**
- unresolved structural placement issues — **0**
- latest B20 page-layer endpoint — `e8919ea260fdc3c8a5e8fef643bdd1ff3691a49c`
- Gate-B closure / durable B20 progress commit — `90caaeb3bd92201a75d45f617727721b9c3e0df7`
- wording state — **Gemini-lexical-locked; not word-for-word scan verified**
- Gate C C01–C05 — **COMPLETE / PASS**
- Gate-C audited — **125/497**
- Gate-C remaining — **372**
- Gate-C frontier — **scan 126**
- latest Gate-C ledger commit — `4e942af8ef1330d1e924ff2c5d720595fad1fffb`
- C05 substantive discrepancy records — **4**
- cumulative Gate-C discrepancy records — **36**
- Gate C2 — **NOT STARTED / NOT AUTHORIZED**

Durable Gate-B extraction/mapping exceptions remain recorded in `STRUCTURAL_FIDELITY_PROGRESS.md`; do not reopen Gate B merely to source-correct lexical wording.

Exact next activity: **Gate C C06 — scans 126–150**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_003_pages_101-150.pdf`, split pages **26–50** / physical scans **126–150**;
- user-supplied `File3.md`, Pages **126–150**.

Gate C remains audit-only:
- append substantive discrepancies to `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`;
- **do not modify page wording**;
- do not start Gate C2 unless the user explicitly authorizes source correction.
