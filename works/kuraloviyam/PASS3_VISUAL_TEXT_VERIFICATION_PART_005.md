# Kuraloviyam — Part 005 Pass 3 Visual/Text Verification

## Scope

- Source: `TVA_BOK_0065733_குறளோவியம்_part_005_pages_445-555.pdf`
- Overall scans: **445–555**
- Printed pages: **428–538**
- Physical scans: **111**
- Gate: **Pass 3 — meaningful visual/text fidelity verification**
- Initial cadence: **11 physical scans per normal iteration unless the user changes the cadence**
- Status: **NOT STARTED — next Batch 1 / scans 445–455**

## Preconditions

- Source intake — **PASS / COMPLETE**
- Pass 1 — **COMPLETE 111/111**
- Pass 2A — **COMPLETE / PASS 111/111**
- Pass 2B — **COMPLETE / PASS 111/111**
- Pass-2B correction endpoint — `892d3273ddf04f6b1a0364d0b77e9e4eb58d0c93`
- All 111 records remain `status: "needs-review"` / `visual_fidelity: "needs-review"`
- Incoming Part boundary **444→445 — GENUINE CONTINUATION / source-resolved**
- Outgoing Part boundary **555→556 — CLEAN / source-resolved**

## Method

Follow `PASS3_VISUAL_TEXT_VERIFICATION_PART_004.md` as precedent. For each physical scan, compare the current canonical page record directly with the rendered source scan and verify semantically meaningful visual organization:

- illustration/text order and relationship;
- heading hierarchy;
- Kural and quotation lineation/block placement;
- prose/quotation relationships;
- page furniture versus body text;
- source/non-source separation;
- physical-page continuation;
- source-size legibility.

This is **not another lexical reread**. Settled wording is not normalized or rewritten during Pass 3 unless a genuinely new direct-source issue is separately established. A page record changes only when the source requires a structural/visual-description correction. Exact artwork, font and colour recreation are outside this gate.

No final status promotion occurs during Pass 3. All Part-005 page records remain `needs-review` / visual `needs-review` until the later Part audit and final status synchronization.

## Exact next activity — Batch 1

Process scans **445–455 / printed 428–438**.

Preserve incoming **444→445 GENUINE CONTINUATION / source-resolved**. Inspect scan **456 / printed 439** only as the outgoing boundary witness when required. Record per-page Pass-3 structural/visual results, commit only source-required record changes, compare the batch base→head changed-file set, and keep all review flags unchanged.
