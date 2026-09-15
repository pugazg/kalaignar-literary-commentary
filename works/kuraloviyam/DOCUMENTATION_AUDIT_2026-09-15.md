# Kuraloviyam Documentation Audit — 2026-09-15

## Result

**CURRENT-CONTROL DOCUMENTATION: SYNCHRONIZED / PASS.**

Live-main base audited: `121eacebe2bcfa1dfd38e53d9200b005f0b8dacb`.

The audit distinguished:

1. **current control documents**, which must describe the present closed/S3 state; and
2. **historical progress/audit records**, which intentionally preserve earlier workflow checkpoints and are not rewritten as if they were current.

## Current-control documents checked

- root `HANDOVER.md`;
- `NEXT_CHAT_PROMPT_KURALOVIYAM.md`;
- `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`;
- `works/kuraloviyam/README.md`;
- `works/kuraloviyam/HANDOVER.md`;
- `works/kuraloviyam/indexes/page-map.md`;
- `works/kuraloviyam/metadata/source.md`;
- `works/kuraloviyam/metadata/transcription-policy.md`;
- maintained-English README/status/guide;
- section README/build-status/S3 completion report.

## Issues found and corrected

### 1. Superseded GR1/GR2 frontier wording

Several live control documents still contained embedded phrases such as:

- “current English state — 111 source-checked”;
- “exact next stage — GR2”.

Those statements described an earlier historical checkpoint but were not always labelled as historical. They are now explicitly marked as **historical / then-next** wherever they remain for provenance.

### 2. Source metadata table

Part 005 and Part 006 rows still described unfinished English work. They are now synchronized to the final state:

- Part 005 — Tamil + maintained English CLOSED;
- Part 006 — Tamil + maintained English CLOSED, S1–S3 complete, physical endpoint confirmed.

### 3. Page-map frontier

The page map still ended with the old Part 006 GR2 frontier. It now records:

- no active frontier;
- Tamil/English/S1/S2/S3 closed;
- explicit derived coverage for all **666/666** scans.

### 4. Section coverage clarity

The sections controls now explicitly state physical-source accounting:

- scans 1–33 — front matter / transition;
- scans 34–657 — 300 Kuraloviyam entry spans;
- scans 658–665 — source contents/index;
- scan 666 — unnumbered pictorial back cover / endpoint.

Therefore **666/666 physical scans are accounted for**.

## Historical documents intentionally left unchanged

Files whose names and purpose are historical checkpoints—such as `PART_*_PASS1_PROGRESS.md`, Pass 2/Pass 3 batch logs, audit records, documentation-sync records and English review/release reports—retain their original state descriptions.

They are evidence of what was true at that gate; rewriting them to today's state would damage the audit trail.

## Current authoritative state

- physical source — **1–666 complete**;
- Tamil — **662 verified + 4 explicit partial/source-limited; visual 666/666 verified**;
- maintained English — **662 release-ready + 4 source-limited**;
- S2 — **300/300 processed / 298 resolved / 2 partial-source-metadata / 0 unresolved**;
- S3 — **300/300 individual entry leaves + JSON/TSV/human/Chapter indexes**;
- required next Kuraloviyam activity — **none**.
