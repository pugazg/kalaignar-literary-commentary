# Next Chat Prompt — குறளோவியம் archival / bilingual project

Continue directly in `pugazg/kalaignar-literary-commentary`, branch `main`, active work `works/kuraloviyam/`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work. Do not reopen closed Part 001 work unless a genuinely new source/provenance issue appears.

## Mandatory startup

Read completely before changing anything:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this prompt
5. `works/kuraloviyam/HANDOVER.md`
6. `works/kuraloviyam/README.md`
7. `works/kuraloviyam/PART_002_PASS1_PROGRESS.md`
8. `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_002.md`
9. `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_002.md`
10. `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_002.md`
11. `works/kuraloviyam/PART_002_AUDIT.md`
12. `works/kuraloviyam/indexes/page-map.md`
13. `works/kuraloviyam/metadata/source.md`
14. `works/kuraloviyam/metadata/transcription-policy.md`

## Part 001 — CLOSED

Tamil scans **1–111** are archival-ready. English Part 001 is closed with **107 release-ready + 4 source-limited** records (13, 14, 15, 19).

## Part 002 source

Controlling source:

`TVA_BOK_0065733_குறளோவியம்_part_002_pages_112-222.pdf`

Recorded identity:

- **111 physical pages**;
- overall scans **112–222**;
- printed pages **95–205**;
- size **93,279,161 bytes**;
- SHA-256 `4397caf9ba405ba65f50865c85e24461ea56bd2efa3dd589d31469877c9a4bda`;
- no usable parsed text layer; rendered source is authority when a source recheck is genuinely needed.

## Completed Part 002 gates

- source intake — **COMPLETE**
- Pass 1 — **COMPLETE, 111/111**
- Pass 2A — **COMPLETE, 111/111**
- Pass 2B — **COMPLETE, 111/111**
- Pass 3 — **COMPLETE, 111/111 scans 112–222 / printed 95–205**
- Part audit — **PASS**
- final metadata/status synchronization — **NEXT / not started**

All Part 002 records still remain `status: "needs-review"` / `visual_fidelity: "needs-review"`; the Part audit deliberately made no status promotion.

## Part 002 audit closure

Durable audit: `works/kuraloviyam/PART_002_AUDIT.md`.

The audit confirms:

- complete physical coverage **111/111**, scans **112–222**, local pages **1–111**, printed **95–205**;
- continuous page mapping and one durable record per physical scan as established by the Pass 1/page-map controls;
- source-verification gates Pass 2A, Pass 2B and Pass 3 all closed **111/111**;
- illustration-only continuations **176→177→178** and **202→203→204** are coherent;
- **221→222** is a genuine continuation and scan **222 / printed 205** is the supplied Part 002 endpoint;
- identified library stamps remain non-body material;
- no blocked/source-limited/partial Tamil condition requires an audit HOLD.

The audit made **no Tamil body-text change** and **no status change**.

## Exact next activity — Part 002 final metadata/status synchronization

Synchronize final metadata across **all 111 Part 002 page records, scans 112–222 / printed 95–205**.

Use the completed source intake, Pass 1, Pass 2A, Pass 2B, Pass 3 and Part-audit records as the evidence base. This is a metadata/status gate, not a fresh transcription pass.

Requirements:

1. fetch live `main` first and preserve newer durable state;
2. determine the final textual and visual status distribution from the closed verification/audit evidence rather than assuming a result in advance;
3. update each Part 002 page record's `status` and `visual_fidelity` consistently;
4. **do not change Tamil body wording** during synchronization;
5. preserve page types, visual-material blocks, non-body stamp notes and source-continuation comments established during Pass 3;
6. create a durable `PART_002_FINAL_STATUS_SYNC.md` report recording counts, exceptions, evidence and the exact post-sync gate;
7. audit the starting-head→final-head changed-file set;
8. after the status result is known, synchronize README, HANDOVER, page map and this prompt;
9. do not declare Part 002 Tamil archival-ready until final metadata/status synchronization and the required documentation synchronization close;
10. do not begin Part 003 before Part 002 is fully closed.

If the evidence exposes any genuine unresolved source limitation during synchronization, preserve it explicitly rather than forcing `verified`.
