# சங்கத் தமிழ் — கலைஞர் மு. கருணாநிதி

This directory is the source-first archival workspace for **சங்கத் தமிழ்** by **கலைஞர் மு. கருணாநிதி**.

The methodology follows the repository's source-first archival discipline, with a dedicated printed Sangam-provenance layer and a full-volume multi-pass execution model.

## Controlling source

`TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

The actual mounted PDF has been independently confirmed as a **complete 497-scan source**. Scan **497 is the back cover**. The earlier 150-page figure came from a preview-service limit and is retired.

Canonical source range: **1–497**. Do not create scan 498+ records or infer printed pagination from scan arithmetic.

See [`metadata/source.md`](metadata/source.md).

## Canonical workflow

The active execution plan is:

[`MULTI_PASS_WORKFLOW.md`](MULTI_PASS_WORKFLOW.md)

The project no longer mixes transcription, textual verification, visual-fidelity verification, section mapping, provenance review and metadata synchronization in the same routine page iteration.

The canonical pass order is:

1. **Pass 1 — transcription / physical capture only, through scan 497**;
2. **Pass 2 — textual verification, scan 1 → 497**;
3. **Pass 3 — visual-text fidelity verification, scan 1 → 497**;
4. **Pass 4 — physical-page and continuity audit, scan 1 → 497**;
5. **Pass 5 — section-structure audit, scan 1 → 497**;
6. **Pass 6 — Sangam source / provenance audit, scan 1 → 497**;
7. **Pass 7 — metadata / status consistency audit, scan 1 → 497**;
8. **Pass 8 — whole-volume synchronization and final audit**.

## Archival layers

1. `pages/` — canonical physical scan-page records.
2. `sections/` — non-destructive navigation by decorative thematic headings.
3. `indexes/page-map.md` — physical scan/status map.
4. `indexes/section-register.md` — source-order section boundaries.
5. `indexes/source-citation-register.md` — printed Sangam anthology / poem-number / poet provenance.
6. future English source/alignment — separate from the Tamil archive.

The section layer never replaces page records.

## Current Pass 1 rules

Pass 1 is **capture only**.

For each new scan:

- read the page once;
- create the physical Markdown record;
- transcribe visible text;
- preserve obvious printed line/paragraph breaks and directly visible headings;
- create concise physical records for illustration/blank/non-text pages;
- record printed pagination only when visible;
- leave uncertain readings for later review instead of spending extended time resolving them;
- normally use `status: needs-review` and `visual_fidelity: needs-review`;
- commit and move forward.

Do **not** perform routine second-pass verification, provenance verification, section-end research, visual-fidelity audit, continuity audit, metadata audit or broad documentation synchronization during Pass 1.

## Current physical extent

Physical Markdown records now exist through **scan 53**.

Current immediate state:

- scan 50 / printed 35 — `மாதரின் கண்ட மலர்கள்` opening, completed under the earlier verified-page cadence;
- scan 51 / printed 36 — transcription-only, `needs-review`;
- scan 52 — illustration-only capture, `needs-review`;
- scan 53 / printed 38 — fast transcription-only, `needs-review`;
- **next Pass-1 page: scan 54**.

Earlier completed/verified work remains preserved:

- scans **9–14 / printed IV–IX** — front-matter text gate;
- `மலர்மாரி பொழிகின்றேன்!` — scans **17–19**;
- `யாதும் ஊரே; யாவரும் கேளிர்!` — scans **20–24**;
- `மானங்காத்த மறவன்!` — scans **25–30**;
- `துணை நின்றார் தோழி!` — scans **31–36**;
- `சுமந்தவன் சுமந்த சோகம்!` — scans **37–41**;
- `பாவை புகழ்ந்த பன்றி` — scans **42–46**;
- `காக்கைக்கு நன்றி காட்ட...` — scans **47–49**.

Scans **7–8** remain `partial`.

Existing `verified` pages are not downgraded, but the later systematic full-volume passes may still revisit them so that final coverage is uniform from scan 1 through scan 497.

## Verified printed Sangam provenance already preserved

- scan 19 — `பத்துப்பாட்டு (குறிஞ்சிப்பாட்டு)` / `61 முதல் 95 முடிய` / `கபிலர்`;
- scan 24 — `புறநானூறு - பாடல் : 192` / `கணியன் பூங்குன்றன்`;
- scan 30 — `புறநானூறு : பாடல்: 74` / `சேரமான் கணைக்கால் இரும்பொறை`;
- scan 36 — `ஐங்குறுநூறு : பாடல் : 180` / `அம்மூவனார்`;
- scan 41 — `புறநானூறு : பாடல் : 286` / source-visible `ஒளவையார்`;
- scan 46 — `அகநானூறு : பாடல் : 248` / `கபிலர்`;
- scan 49 — `குறுந்தொகை : பாடல் : 210` / `காக்கைப்பாடினியார் நச்செள்ளையார்`.

These remain valid records. New provenance encountered during Pass 1 does not need immediate verification/register synchronization; the systematic provenance sweep is Pass 6.

## Permanent fidelity rule

Do not substitute a familiar Sangam poem from another edition for what is printed in this book. Preserve Kalaignar's wording, arrangement, quotations, poem labels, poet attributions, word explanations and meaningful visual organization exactly as source-supported.

First-pass capture is not final verification. `verified` remains reserved for pages that have passed the required later textual and visual-fidelity gates.

## Exact next activity

**Pass 1 only: transcribe/capture scan 54, commit it as a first-pass physical record, then continue sequentially toward scan 497.**

Do not mix Pass 2–8 work into routine Pass-1 page capture.