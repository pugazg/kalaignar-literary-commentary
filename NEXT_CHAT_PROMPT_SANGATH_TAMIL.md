# Next Chat Prompt — சங்கத் தமிழ் archival project

Continue the **சங்கத் தமிழ் — Kalaignar source-first archival / provenance project** directly in `pugazg/kalaignar-literary-commentary` on `main`.

Active path: `works/sangatamil/`

## Mandatory startup

Read completely before any repository change:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. `works/sangatamil/README.md`
5. `works/sangatamil/MULTI_PASS_WORKFLOW.md`
6. `works/sangatamil/metadata/source.md`
7. `works/sangatamil/metadata/transcription-policy.md`
8. `works/sangatamil/indexes/page-map.md`
9. `works/sangatamil/indexes/section-register.md`
10. `works/sangatamil/indexes/source-citation-register.md`

Then inspect current `main` and the actual source scan required for the active pass.

## Source authority

The scan is authoritative. Do not silently modernize, normalize, correct from another edition, replace quoted Sangam text, alter printed anthology/poem/poet labels, reconstruct hidden text, or infer pagination/source content.

## Source boundary

The supplied PDF is independently confirmed as **497 scans**; scan **497 is the back cover**. Canonical range: **1–497**. The retired 150-page preview count must not be used as a source boundary.

# Canonical workflow — do not revert to mixed per-page verification

Sangath Tamil now uses the full-volume multi-pass workflow defined in:

`works/sangatamil/MULTI_PASS_WORKFLOW.md`

The pass order is:

1. Pass 1 — transcription / physical capture only through scan 497;
2. Pass 2 — textual verification, scan 1 → 497;
3. Pass 3 — visual-text fidelity verification, scan 1 → 497;
4. Pass 4 — physical-page and continuity audit, scan 1 → 497;
5. Pass 5 — section-structure audit, scan 1 → 497;
6. Pass 6 — Sangam source / provenance audit, scan 1 → 497;
7. Pass 7 — metadata / status consistency audit, scan 1 → 497;
8. Pass 8 — whole-volume synchronization and final audit.

**Only Pass 1 is active now.**

## Pass 1 rules

For each scan:

- inspect once;
- create the physical Markdown record;
- transcribe visible text;
- preserve obvious printed line/paragraph breaks and immediately visible headings;
- create a concise factual record for illustration/blank/non-text pages;
- record printed pagination only if visible;
- leave uncertain readings for later review rather than spending extended time resolving them;
- normally set `status: needs-review` and `visual_fidelity: needs-review`;
- commit and move to the next scan.

Do **not** perform routine:

- second source reading;
- character-by-character verification;
- textual verification;
- visual-fidelity verification;
- repeated crop/zoom forensic work;
- provenance verification;
- external-edition comparison;
- section-end investigation;
- continuity audit;
- metadata/status audit;
- per-page README/index/HANDOVER synchronization.

If a word is genuinely unreadable for basic capture, mark it uncertain or use the appropriate `partial`/`blocked` status rather than stopping the entire pass for forensic reconstruction.

## Current state

Physical page records exist through **scan 53**.

- scan 50 / printed 35 — `மாதரின் கண்ட மலர்கள்` opening; earlier verified cadence;
- scan 51 / printed 36 — transcription-only, `needs-review`;
- scan 52 — illustration capture, `needs-review`;
- scan 53 / printed 38 — fast transcription-only, `needs-review`.

Earlier completed/verified material through scan 49 remains preserved. Existing verified pages are not downgraded, but later whole-volume passes will still run scan 1 → 497 for systematic final coverage.

Scans 7–8 remain `partial`.

## Existing verified Sangam provenance

- scan 19 — `பத்துப்பாட்டு (குறிஞ்சிப்பாட்டு)` / `61 முதல் 95 முடிய` / `கபிலர்`;
- scan 24 — `புறநானூறு - பாடல் : 192` / `கணியன் பூங்குன்றன்`;
- scan 30 — `புறநானூறு : பாடல்: 74` / `சேரமான் கணைக்கால் இரும்பொறை`;
- scan 36 — `ஐங்குறுநூறு : பாடல் : 180` / `அம்மூவனார்`;
- scan 41 — `புறநானூறு : பாடல் : 286` / source-visible `ஒளவையார்`;
- scan 46 — `அகநானூறு : பாடல் : 248` / `கபிலர்`;
- scan 49 — `குறுந்தொகை : பாடல் : 210` / `காக்கைப்பாடினியார் நச்செள்ளையார்`.

Do not stop Pass 1 to verify newly encountered provenance; Pass 6 is the systematic provenance pass.

## Current provisional section context

`மாதரின் கண்ட மலர்கள்` begins at scan **50 / printed 35** and has page records through scan 53. Its canonical end boundary is intentionally deferred to Pass 5.

## Exact next activity

**Process scan 54 only as Pass-1 fast transcription / physical capture.**

Create the page record, normally leave it `needs-review`, commit it, and stop. Do not perform any Pass 2–8 activity in the same iteration.