# NEXT CHAT PROMPT — குறளோவியம் / Part 004 final metadata-status synchronization

Continue directly in `pugazg/kalaignar-literary-commentary`, branch `main`, active work `works/kuraloviyam/`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve any newer durable work. Do not roll back or overwrite newer repository state because this prompt has become stale.

Operational checkpoint immediately before this prompt synchronization:

`df429102652cd36c29246684e5a9067ee67fa4d4` — `kuraloviyam: Advance archival guide after Part 004 audit`

Parts **001–003 are fully CLOSED**. Do not reopen them unless genuinely new source/provenance/fidelity evidence appears.

## Controlling Part 004 source

`TVA_BOK_0065733_குறளோவியம்_part_004_pages_334-444.pdf`

Identity:

- physical pages: **111**;
- overall scans: **334–444**;
- local pages: **1–111**;
- printed pages: **317–427**;
- SHA-256: `5b7fcc65f19dc3d2a57bebb13cdfb02d0c83f70a5ccc9e537886790908674581`;
- no usable parsed text layer;
- rendered source scans were the controlling authority during the completed verification chain.

Do **not** commit the controlling PDF.

## Mandatory startup reading

Read completely before changing Part-004 status fields:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this `NEXT_CHAT_PROMPT_KURALOVIYAM.md`
5. `works/kuraloviyam/HANDOVER.md`
6. `works/kuraloviyam/README.md`
7. `works/kuraloviyam/indexes/page-map.md`
8. `works/kuraloviyam/SOURCE_INTAKE_PART_004.md`
9. `works/kuraloviyam/PART_004_PASS1_PROGRESS.md`
10. `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_004.md`
11. `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_004.md`
12. `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_004.md`
13. `works/kuraloviyam/PART_004_AUDIT.md`

## Durable Part 004 state

- source intake — **PASS / COMPLETE**;
- Pass 1 — **COMPLETE 111/111**;
- Pass 2A — **COMPLETE / PASS 111/111**;
- Pass 2B — **COMPLETE / PASS 111/111**;
- Pass 3 — **COMPLETE / PASS 111/111**;
- Part audit — **PASS / COMPLETE**;
- direct audit inventory — **111/111 records, no scan/local-page/printed-page gaps or duplicates**;
- carried `partial` / `blocked` / source-limited Tamil exceptions — **0**;
- audit Tamil/body-text changes — **0**;
- audit page-status promotions — **0**;
- current textual status distribution — **111 `needs-review`, 0 partial, 0 blocked, 0 verified**;
- current visual status distribution — **111 `needs-review`, 0 verified**;
- final metadata/status synchronization — **NEXT / UNBLOCKED**;
- external **444→445 remains DEFERRED / UNRESOLVED** until actual Part 005 source intake.

## Exact next activity — final metadata/status synchronization

Process **all 111 Part-004 page records, scans 334–444 / printed 317–427**, as a metadata-only gate.

Before writing, confirm live `main` still matches the audit evidence and that all 111 eligible records remain:

- `status: "needs-review"`;
- `visual_fidelity: "needs-review"`.

Then promote each eligible record:

- `status: "needs-review"` → `status: "verified"`;
- `visual_fidelity: "needs-review"` → `visual_fidelity: "verified"`.

### Strict change boundary

For each of the 111 page records, change **only those two fields**.

Do **not** change:

- Tamil body wording;
- Kural wording or lineation;
- paragraph/dialogue structure;
- `page_type`;
- `visual_notes`;
- source filename or transcription method;
- scan/local/printed-page mapping;
- source comments / continuation comments;
- any source-visible punctuation, joining or spacing.

Preserve the external source-limit condition:

**444→445 DEFERRED / UNRESOLVED** until Part 005 is supplied.

## Required durable close-out

After status promotion:

1. verify all **111/111** page records now carry `status: "verified"`;
2. verify all **111/111** carry `visual_fidelity: "verified"`;
3. verify **0** Part-004 records remain `needs-review`, `partial` or `blocked`;
4. compare the pre-sync checkpoint to the clean status-sync endpoint and confirm the page-record diff is metadata-only;
5. create `works/kuraloviyam/PART_004_FINAL_STATUS_SYNC.md`;
6. synchronize `PART_004_PASS1_PROGRESS.md`, work handover, root handover, README, page-map, archival guide and this next-chat prompt to the subsequent **documentation synchronization** gate;
7. audit the exact changed-file set and fetch final live `main`.

Do **not** begin documentation synchronization itself in the same iteration unless separately instructed. Do **not** begin Part 005.
