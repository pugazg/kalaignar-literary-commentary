# குறளோவியம்

கலைஞர் மு. கருணாநிதியின் **குறளோவியம்** நூலை மூல ஸ்கேனை controlling source ஆகக் கொண்டு பக்கவாரியாகவும் பின்னர் bilingual archival layer ஆகவும் பாதுகாக்கும் பகுதி.

## Source family and split plan

The user reports the original source as **666 physical PDF pages**, manually split into **six 111-page parts** for upload.

| Part | Overall scans | Supplied state | Current archival state |
|---|---:|---|---|
| 001 | 1–111 | supplied — `TVA_BOK_0065733_குறளோவியம்_part_001_pages_1-111.pdf` | **Tamil archival-ready / closed**; English project translation active — drafts through scan 8 |
| 002 | 112–222 | not yet supplied | not-started |
| 003 | 223–333 | not yet supplied | not-started |
| 004 | 334–444 | not yet supplied | not-started |
| 005 | 445–555 | not yet supplied | not-started |
| 006 | 556–666 | not yet supplied | not-started |

Repository `scan_page` always follows the **overall 1–666 sequence**. It never restarts at 1 for a later split.

## Controlling rule

The rendered scan is the source authority for source-dependent Tamil work. The repository is a preservation layer, not a normalized edition.

Do not silently correct printed wording from a standard Kural edition, memory, web text, OCR or contextual expectation. Genuine source limitations remain explicit rather than reconstructed.

Use [`../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md`](../../KURALOVIYAM_ARCHIVAL_GUIDELINES.md) for the complete operating policy.

## Mandatory per-part closure cadence

Each supplied Part is completed before the next Part begins:

1. source intake;
2. Pass 1 physical capture/transcription;
3. Pass 2A direct textual verification;
4. Pass 2B independent lexical-fidelity re-read;
5. Pass 3 meaningful visual-text verification;
6. Part audit;
7. final page metadata/status synchronization;
8. documentation synchronization;
9. Tamil archival-ready checkpoint;
10. project-created English translation/review closure when the bilingual layer is maintained;
11. final Part checkpoint;
12. only then begin the next supplied Part.

Once a Part is closed, normal later work uses the durable repository records; the earlier split PDF should not routinely be required again unless a new source/provenance issue specifically requires a recheck.

# Part 001 — Tamil archival layer

## Source boundary

Confirmed from the supplied 111-page split:

- scan **1** — front cover, `குறளோவியம்`, author `கலைஞர் மு. கருணாநிதி`;
- scans **2–3** — title/publication/edition matter;
- scans **4–17** — front matter;
- scan **18** — main body begins at printed page **1**, heading `பேராசிரியர்`;
- scan **31** — printed page 14, `கலைஞர் ஏற்புரை`;
- scan **32** — unnumbered section-title leaf `கலைஞரின் குறளோவியம்`;
- scan **33** — intentionally blank source-side page, printed page **16**;
- scans **34–111** — main `கலைஞரின் குறளோவியம்` sequence;
- scan **111** — printed page **94**, closing the learned-speaker vignette with two `சொல்வன்மை` Kurals and the lower Valluvar statue motif.

Part 001 has no usable parsed text layer in the supplied environment; all source-dependent verification was performed against rendered scans.

## Completed Tamil gates

**Part 001 Tamil is CLOSED / ARCHIVAL-READY.**

- physical/page-aligned capture: **111 / 111**;
- Pass 1: **COMPLETE — 111 / 111**;
- Pass 2A: **COMPLETE — 111 / 111**;
- Pass 2B: **COMPLETE — 111 / 111**;
- Pass 3: **COMPLETE — 111 / 111**;
- Part audit: **PASS**;
- final metadata/status synchronization: **PASS**;
- visual fidelity: **111 / 111 `verified`**.

Final textual-status distribution:

- **107** records — `verified`;
- **4** records — `partial`: scans **13, 14, 15, 19**.

The four `partial` records are intentional source limitations:

- scans 13–15: handwritten/facsimile bodies cannot safely be established word-for-word;
- scan 19 / printed page 2: physically washed-out/faint central printed material cannot safely be recovered.

Do not infer or reconstruct those missing readings.

## Durable Part 001 Tamil records

- `SOURCE_INTAKE_PART_001.md`
- `PASS2_TEXTUAL_VERIFICATION_PART_001.md`
- `PASS2B_LEXICAL_FIDELITY_PART_001.md`
- `PASS3_VISUAL_TEXT_VERIFICATION_PART_001.md`
- `PART_001_AUDIT.md`
- `PART_001_FINAL_STATUS_SYNC.md`
- `metadata/source.md`
- `metadata/transcription-policy.md`
- `indexes/page-map.md`
- `pages/` — 111 page-aligned Tamil records.

The final page-status change-set covered exactly the 111 Part 001 page records. Commit-level review of the three apparent extra diff lines on scans 10, 11 and 35 confirmed that they were only end-of-file newline changes; no Tamil body wording was altered by final status synchronization.

## Part boundary rule

Scan 111 closes the supplied Part 001 unit. The **111 → 112** adjacent-Part continuity check remains deferred until Part 002 is supplied. Nothing is inferred for overall scan 112.

# Part 001 — English project translation

The English layer is under:

`works/kuraloviyam/translations/en/`

It is explicitly a **project translation**, not a publisher/official English edition.

Durable English control files:

- `translations/en/README.md`;
- `translations/en/TRANSLATION_GUIDE.md`;
- `translations/en/GLOSSARY.md`;
- `translations/en/TRANSLATION_STATUS.md`.

English Batch 1 is complete as a first-pass draft:

- scans **1–3** — cover / title-publisher / edition-imprint;
- scans **4–8 / printed iii–vii** — complete Preface.

Current English draft coverage: **8 / 111**.

These eight pages remain `draft`; no source-check, editorial-review or release-ready status is claimed yet.

# Current frontier

**Tamil Part 001: archival-ready / closed.**

**English Part 001: first-pass drafting active through scan 8.**

Exact next activity: **English Batch 2 — scans 9–17**, closing the remaining front matter. Scans **13–15** must be English `source-limited` records and their unreadable handwriting must not be reconstructed.

Part 002 is not started. Do not begin it until the required Part 001 English/final closure checkpoint is complete and the Part 002 source is supplied.
