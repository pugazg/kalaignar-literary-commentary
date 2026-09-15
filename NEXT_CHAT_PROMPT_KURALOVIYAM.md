# NEXT CHAT PROMPT — குறளோவியம் / Part 006 Final Metadata-Status Synchronization

Continue directly in `pugazg/kalaignar-literary-commentary`, branch `main`, active work `works/kuraloviyam/`. **LIVE MAIN IS AUTHORITATIVE.**

## Closed Parts

Parts **001–005 are fully closed**. Do not reopen them.

## Part 006 controlling source

`TVA_BOK_0065733_குறளோவியம்_part_006_pages_556-666.pdf`

Durable Part-006 verification and audit records:

- `works/kuraloviyam/SOURCE_INTAKE_PART_006.md`
- `works/kuraloviyam/PART_006_PASS1_PROGRESS.md`
- `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_006.md`
- `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_006.md`
- `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_006.md`
- `works/kuraloviyam/PART_006_AUDIT.md`

## Durable Part 006 state

- Source intake — **PASS / COMPLETE**;
- Pass 1 — **COMPLETE 111/111**;
- Pass 2A — **COMPLETE / PASS 111/111**;
- Pass 2B — **COMPLETE / PASS 111/111**;
- Pass 3 — **COMPLETE / PASS 111/111**;
- Part 006 audit — **PASS / COMPLETE**;
- audit commit — `84710e8bdb06418a16ca2c84ee7495f86d9711d4`;
- audit creation compare — `6738303e704eb3a3669137fb9f016b55f3e2b57f` → `84710e8bdb06418a16ca2c84ee7495f86d9711d4` — **1 commit / exactly one added file: `works/kuraloviyam/PART_006_AUDIT.md` / 0 Part-006 page-file changes**;
- direct page inventory — **111/111 canonical records**;
- scans — **556–666**, continuous, **0 gaps / 0 duplicates**;
- local pages — **1–111**, continuous;
- printed mapping — **539–648**, plus scan 666 `unnumbered`;
- exact source identity — **111/111 records**;
- page functions — **102 body-prose / 8 contents-index / 1 back-cover**;
- scans **658–665** — complete `பொருளடக்கம்` run;
- scan **666** — unnumbered pictorial back cover / physical source endpoint;
- **665→666 CLEAN / PHYSICAL SOURCE ENDPOINT**;
- unresolved Tamil exceptions — **0**;
- current status distribution:
  - Tamil textual status — **111 needs-review / 0 verified / 0 partial-blocked-source-limited**;
  - visual fidelity — **111 needs-review / 0 verified**.

## Exact next activity — final metadata/status synchronization

Follow the closed Part-005 precedent in:

`works/kuraloviyam/PART_005_FINAL_STATUS_SYNC.md`

Perform a **metadata-only promotion across all 111 Part-006 page records / scans 556–666**.

For every Part-006 record, change only:

- `status: "needs-review"` → `status: "verified"`;
- `visual_fidelity: "needs-review"` → `visual_fidelity: "verified"`.

Do **not** change:

- Tamil body wording;
- Kural wording or lineation;
- paragraph/dialogue structure;
- `page_type`;
- `visual_notes`;
- source-page comments;
- source filename;
- transcription method;
- scan/local/printed-page mapping;
- contents/back-cover function.

## Required execution audit

Use the audit-closed state as the status-sync base.

After all 111 page records are promoted, compare the base to the page-layer status endpoint and verify:

- exactly **111 Part-006 page files** changed;
- scans **556–666** are all represented exactly once;
- each changed page file has only the two status-token replacements;
- expected per-file diff is **2 additions / 2 deletions**;
- **0 non-page files** changed during the metadata-only page promotion;
- final textual status — **111 verified / 0 needs-review / 0 partial / 0 blocked / 0 source-limited**;
- final visual fidelity — **111 verified / 0 needs-review**.

Create:

`works/kuraloviyam/PART_006_FINAL_STATUS_SYNC.md`

recording the starting checkpoint, status commits, exact page-layer endpoint, compare result and final distribution.

After the final status synchronization closes, the exact next gate is **Part 006 documentation synchronization**.

Do not start English translation in this activity.
