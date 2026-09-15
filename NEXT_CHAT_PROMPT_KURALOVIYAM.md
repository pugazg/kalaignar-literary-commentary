# NEXT CHAT PROMPT — குறளோவியம் / Part 006 Documentation Synchronization

Continue directly in `pugazg/kalaignar-literary-commentary`, branch `main`, active work `works/kuraloviyam/`. **LIVE MAIN IS AUTHORITATIVE.**

## Closed Parts

Parts **001–005 are fully closed**. Do not reopen them.

## Part 006 controlling source

`TVA_BOK_0065733_குறளோவியம்_part_006_pages_556-666.pdf`

## Durable Part 006 state

The Tamil verification chain through final status promotion is closed:

- Source intake — **PASS / COMPLETE**;
- Pass 1 — **COMPLETE 111/111**;
- Pass 2A — **COMPLETE / PASS 111/111**;
- Pass 2B — **COMPLETE / PASS 111/111**;
- Pass 3 — **COMPLETE / PASS 111/111**;
- Part 006 audit — **PASS / COMPLETE**;
- final metadata/status synchronization — **PASS / CLOSED**.

Durable records:

- `works/kuraloviyam/SOURCE_INTAKE_PART_006.md`
- `works/kuraloviyam/PART_006_PASS1_PROGRESS.md`
- `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_006.md`
- `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_006.md`
- `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_006.md`
- `works/kuraloviyam/PART_006_AUDIT.md`
- `works/kuraloviyam/PART_006_FINAL_STATUS_SYNC.md`

Final status-sync execution:

- starting checkpoint — `fec10c426518d8b5cb490db9bfab8b50f6d6a440`;
- page-layer endpoint — `6cdb3cdd18cc1ccf1b1f2071055e9a1fd7782db0`;
- commits — **11**;
- changed files — **exactly 111 Part-006 page files / scans 556–666**;
- per-file diff — **2 additions + 2 deletions**;
- non-page changes during page promotion — **0**;
- final Tamil textual status — **111 verified / 0 needs-review / 0 partial / 0 blocked / 0 source-limited**;
- final visual fidelity — **111 verified / 0 needs-review**;
- unresolved Tamil exceptions — **0**.

Source/page structure remains:

- scans **556–657** — **102 body-prose** records;
- scans **658–665** — **8 contents-index** records / complete `பொருளடக்கம்`;
- scan **666** — **1 back-cover** record / unnumbered pictorial back cover;
- **665→666 CLEAN / PHYSICAL SOURCE ENDPOINT**.

## Exact next activity — Part 006 documentation synchronization

Perform the dedicated **documentation synchronization** gate.

Reconcile the current Part-006 state across at least:

- `works/kuraloviyam/README.md`;
- `works/kuraloviyam/HANDOVER.md`;
- root `HANDOVER.md`;
- `works/kuraloviyam/indexes/page-map.md`;
- `works/kuraloviyam/metadata/source.md`;
- `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`;
- `NEXT_CHAT_PROMPT_KURALOVIYAM.md`;
- any other Part-006 control/status file that still carries a stale live frontier.

Use the closed Part-005 documentation-sync precedent if present.

The documentation-sync record should state that:

- Source Intake / Pass 1 / Pass 2A / Pass 2B / Pass 3 / Part audit / final status sync are all closed;
- Part 006 is **111/111 textual verified + 111/111 visual verified / 0 exceptions**;
- scans **658–665** are the complete `பொருளடக்கம்`;
- scan **666** is the physical source endpoint;
- there are **0 unresolved Tamil exceptions**;
- no page-layer changes occur during documentation sync.

Create:

`works/kuraloviyam/PART_006_DOCUMENTATION_SYNC.md`

with a durable inventory of the synchronized control files and the exact pre/post documentation checkpoints.

## Discipline

This gate is documentation/control-plane only.

Do **not** modify:

- Tamil body text;
- page frontmatter status fields;
- `visual_notes`;
- Kural wording;
- page types;
- source comments;
- scan/local/printed mapping.

After documentation synchronization closes, the exact next gate is the separate:

**Part 006 Tamil archival-ready checkpoint**.

Do not start English translation during documentation synchronization.
