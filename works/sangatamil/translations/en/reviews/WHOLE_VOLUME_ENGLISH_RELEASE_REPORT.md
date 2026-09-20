# Sangatamil — Whole-Volume English Release Report

**Status: PASS / APPROVED — MAINTAINED-ENGLISH RELEASE AUTHORIZED**

- date: **2026-09-20**
- repository: `pugazg/kalaignar-literary-commentary`
- branch: `main`
- active release unit: **physical scans 1–497**
- release-review base: `50183b35efb1ec013301f5c169bf37613c1a5480`

## Scope

This report is the release-approval gate required by `TRANSLATION_GUIDE.md` after completion of first-pass drafting, source-check, glossary reconciliation, editorial review, whole-volume / section-level review, and the completed Tamil word-for-word verification (WFV) adjudication cycle.

It approves the maintained project-created English layer for release relative to the maintained canonical Tamil archive. It does not reopen canonical Tamil wording and does not convert the scan-8 handwritten facsimile into fully source-verified text.

## Preconditions — PASS

The live release unit satisfies all required preconditions:

- English page records — **497/497 present**
- drafting D1–D14 — **497/497 COMPLETE / CLOSED**
- source-check SC1–SC14 — **497/497 COMPLETE / CLOSED**
- glossary reconciliation GR1–GR14 — **497/497 COMPLETE / CLOSED**
- editorial review ER1–ER14 — **497/497 COMPLETE / CLOSED**
- whole-volume / section-level English review — **PASS / CLOSED**
- unresolved whole-work English consistency blockers — **0**
- blocked English pages — **0**

## Tamil WFV closure carried into release

The completed fresh physical-source WFV coverage is:

- source coverage — **497/497 COMPLETE**
- Tamil — **496 verified / 0 needs-review / 1 source-limited partial**
- visual — **496 verified / 1 needs-review**
- scan **8** — permanent handwritten-facsimile / source-limited partial
- WFV-001 — **REJECTED / canonical retained**
- WFV-002 through WFV-056 — **55/55 USER ADJUDICATED / CLOSED**
- cumulative affected pages cleared — **44**
- repository/Gemini readings retained — **20**
- user-authorized corrections applied — **35**
- pending WFV rows — **0**
- targeted English impact reconciliation — **COMPLETE**

No canonical Tamil wording is reopened by this release gate.

## Pre-promotion English inventory

Immediately before release-ready promotion:

- `editorial-reviewed` — **496**
- `source-limited` — **1** (scan 8)
- `release-ready` — **0**
- `source-checked` — **0**
- `draft` — **0**
- `blocked` — **0**

## Release decision

**APPROVED.**

The **496 eligible `editorial-reviewed` English pages** are approved for status-token-only promotion to `release-ready`.

Scan **8** is explicitly excluded from promotion and must remain:

- `status: "source-limited"`
- `source_tamil_status: "partial"`
- description-only for the handwritten `முன்னுரை` facsimile
- not deciphered, reconstructed, or represented as fully source-verified

This scan-8 limitation is an intentional source-policy exception and does not block release of the maintained-English volume.

## Promotion constraints

The release-ready promotion must:

1. change only the English page-level `status` token from `editorial-reviewed` to `release-ready` on the 496 eligible pages;
2. preserve all approved English wording exactly;
3. preserve scan 8 as `source-limited`;
4. change **0 canonical Tamil page files**;
5. change **0 glossary wording**;
6. preserve all source-Tamil status/fidelity metadata;
7. synchronize `TRANSLATION_STATUS.md`, the Sangatamil README, and root handover after promotion.

## Release interpretation

`release-ready` certifies completion of the maintained-English workflow against the maintained canonical Tamil archive and the source-controlled review evidence accumulated by that workflow.

It does **not** mean that scan 8 has been deciphered or fully source-verified. The permanent source-limited exception remains part of the released archival record.

## Approved endpoint

The active release unit closes at:

- scan **496** — narrative ending plus final quoted/gloss unit
- scan **497** — physical back cover

There is no deferred continuation and no unresolved English release blocker.

## Final decision

**SANGATAMIL MAINTAINED ENGLISH RELEASE: PASS / APPROVED**

Authorized next step: promote the **496 eligible English pages** to `release-ready` by status-token-only changes, retain scan 8 as `source-limited`, then perform final control/documentation synchronization and exact changed-file-set audit.

## Final promotion and synchronization result

**COMPLETE / CLOSED**

- release promotion commit — `522923deb6ae1bcfdedd024ddf4439c0cf4a7868`
- post-WFV English metadata synchronization commit — `5a9b877a7b315a466ffe1067b60a0a04de3d356d`
- final English inventory — **496 `release-ready` + 1 `source-limited` (scan 8)**
- scan 8 status — **unchanged / permanent source-limited exception**
- approved English body wording changes during promotion/synchronization — **0**
- canonical Tamil page changes during promotion/synchronization — **0**
- glossary wording changes during promotion/synchronization — **0**
- unresolved release blockers — **0**

The English frontmatter source-status/fidelity snapshot was synchronized to the completed WFV state: all non-scan-8 pages now record verified Tamil/source-fidelity status, while scan 8 remains `partial / needs-review` by source policy.

**SANGATAMIL MAINTAINED ENGLISH: RELEASE COMPLETE / CLOSED.**

