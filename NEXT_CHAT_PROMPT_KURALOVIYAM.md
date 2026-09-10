# Next Chat Prompt — குறளோவியம் archival / bilingual project

Continue directly in `pugazg/kalaignar-literary-commentary`, branch `main`, active work `works/kuraloviyam/`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work. Do not reopen closed Part 001 or Part 002 unless a genuinely new source/provenance/fidelity issue appears.

## Mandatory startup

Read completely before changing anything:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this prompt
5. `works/kuraloviyam/HANDOVER.md`
6. `works/kuraloviyam/README.md`
7. `works/kuraloviyam/metadata/source.md`
8. `works/kuraloviyam/metadata/transcription-policy.md`
9. `works/kuraloviyam/indexes/page-map.md`
10. `works/kuraloviyam/SOURCE_INTAKE_PART_003.md`
11. `works/kuraloviyam/PART_003_PASS1_PROGRESS.md`
12. `works/kuraloviyam/PASS2_TEXTUAL_VERIFICATION_PART_003.md`
13. `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_003.md`
14. `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_003.md`
15. `works/kuraloviyam/PART_002_AUDIT.md` as audit precedent
16. `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_002.md`
17. `works/kuraloviyam/PART_002_TAMIL_ARCHIVAL_READY.md`
18. `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`
19. `works/kuraloviyam/translations/en/reviews/PART_002_ENGLISH_RELEASE_REPORT.md`

## Durable state

- Part 001: **CLOSED**.
- Part 002 Tamil: **ARCHIVAL-READY / CLOSED — 111/111 textual + visual verified**.
- Part 002 English: **RELEASE COMPLETE / CLOSED — 111/111 release-ready**.
- Part 003 source intake: **PASS / COMPLETE**.
- Part 003 Pass 1: **COMPLETE — 111/111, scans 223–333 / printed 206–316**.
- Part 003 Pass 2A: **COMPLETE — 111/111, scans 223–333 / printed 206–316**.
- Part 003 Pass 2B: **COMPLETE — 111/111 independently re-read through scan 333 / printed 316**.
- Part 003 Pass 3: **COMPLETE — 111/111 through scan 333 / printed 316**.
- Part 003 audit: **NEXT / not-started**.
- Part 003 final metadata/status synchronization and Tamil archival-ready: **not-started**.
- English remains **blocked until Tamil closure**.

## Part 003 controlling source

`TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf`

Confirmed identity:

- local PDF pages: **111**;
- overall scans: **223–333**;
- printed pages: **206–316**;
- file size: **93,488,924 bytes**;
- SHA-256: `f07e7cdb3a6e786b0378e00bbe699a241be41c9e099c004a4faa90fa82b4239f`;
- no usable parsed text layer; rendered source scans control.

All Part-003 page records intentionally remain:

- `status: "needs-review"`
- `visual_fidelity: "needs-review"`

Do **not** promote records during the audit. A separate final metadata/status synchronization follows only after an audit PASS.

## Pass 2B closure

Part 003 Pass 2B is **COMPLETE — 111/111**.

- Batches 1–9: **90/111 through scan 312**;
- Batch 10: **313–322 — 10/10**, corrections on **314, 316, 320, 322**;
- Batch 11: **323–332 — 10/10**, correction on **326**;
- final remainder: **scan 333 / printed 316 — 1/1**, with source restorations `இறுதியான` → `இறுதி யான` and `தலைமை ஏற்று` → `தலைமைபெற்று`.

The final scan independently reconfirmed Kural 567 wording/lineation and Chapter 57 — `வெருவந்த செய்யாமை` metadata. Internal **332→333 genuine continuation is closed**. External **333→334 remains deferred until Part 004 source intake**.

Durable cumulative record: `works/kuraloviyam/PASS2B_LEXICAL_FIDELITY_PART_003.md`.

## Pass 3 closure

Part 003 Pass 3 is **COMPLETE — 111/111 through scan 333 / printed 316**.

Pass 3 remained a meaningful visual-text verification gate rather than another lexical reread. It made **0 lexical body-text changes** and **0 status promotions**.

Structural/visual corrections during Pass 3:

- scan **223**;
- scan **260**;
- scans **267, 274, 277**;
- scan **292**;
- scans **302, 303**;
- scan **311**;
- scans **330, 332**;
- final remainder scan **333**.

Final remainder — **scan 333 / printed 316 — COMPLETE 1/1**:

- direct **332→333 genuine continuation** reconfirmed and closed internally;
- the source-displayed highlighted Kural 567 is preserved as a distinct **two-line Markdown set-out block** above Chapter 57 metadata;
- `visual_notes` records the side vertical title and footer as source page furniture excluded from body text;
- lexical wording unchanged;
- record remains `needs-review` / `visual_fidelity: needs-review`;
- external **333→334 remains deferred** until Part 004 source intake.

Durable Pass-3 record: `works/kuraloviyam/PASS3_VISUAL_TEXT_VERIFICATION_PART_003.md`.

## Exact next activity — Part 003 audit

Audit **all 111 Part-003 page records / scans 223–333 / printed 206–316** in one Part-level audit, following `works/kuraloviyam/PART_002_AUDIT.md` as precedent.

Requirements:

1. fetch live `main` first;
2. read the mandatory startup set completely;
3. reconcile the exact Part-003 inventory — **111 page records, scans 223–333, printed 206–316**;
4. reconcile controlling-source identity and provenance against `SOURCE_INTAKE_PART_003.md`;
5. reconcile Pass 1 / Pass 2A / Pass 2B / Pass 3 coverage, frontiers, correction claims and closure state against their durable records;
6. reconcile the complete internal boundary/continuation chain, including the closed **332→333 genuine continuation**; keep external **333→334 deferred** until Part 004 intake;
7. check for unresolved source holds, uncertainty markers, missing records, duplicate records, metadata inconsistencies, stale frontier claims and contradictory documentation;
8. verify all 111 page records still intentionally carry `status: "needs-review"` / `visual_fidelity: "needs-review"` before final synchronization;
9. do **not** repeat lexical transcription or visual rereading unless the audit exposes a specific contradiction requiring targeted source inspection;
10. create `works/kuraloviyam/PART_003_AUDIT.md` (or update it if live main already contains a newer audit record) and record each audit gate and the final PASS/HOLD result;
11. synchronize `works/kuraloviyam/README.md`, `works/kuraloviyam/HANDOVER.md`, root `HANDOVER.md`, `works/kuraloviyam/indexes/page-map.md` and this prompt to the audit result;
12. audit the exact changed-file set before advancing;
13. if and only if the Part audit is **PASS**, make the **separate final metadata/status synchronization** the next activity; do not perform that promotion inside the audit itself;
14. English remains blocked until Tamil archival closure.
