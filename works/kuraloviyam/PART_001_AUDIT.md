# குறளோவியம் — Part 001 audit

Controlling source: `TVA_BOK_0065733_குறளோவியம்_part_001_pages_1-111.pdf`

Audit base: live `main` after completion of Part 001 Pass 3 (`3af65e74adec056480d701356ff18be176888a04`).

This is the Part 001 gate defined by `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`: physical coverage, scan/printed-page continuity, verification-gate closure, status consistency, Part boundary and unresolved source limitations.

## Result

**PART 001 AUDIT: PASS FOR SOURCE COVERAGE / TEXTUAL FIDELITY / VISUAL-TEXT FIDELITY, WITH FINAL METADATA-STATUS SYNCHRONIZATION STILL REQUIRED.**

Part 001 is not yet declared fully archival-ready in page front matter because the page-level `status` / `visual_fidelity` fields have deliberately not been globally promoted during Pass 2A, Pass 2B or Pass 3. That synchronization is the exact next repository activity.

## 1. Physical coverage — PASS

- supplied split contains **111 physical scans**;
- canonical overall range is **1–111**;
- page-aligned Markdown records exist continuously for the Part 001 sequence;
- `scan_page` and `part_page` use the same 1–111 sequence in Part 001;
- the project page map records all physical pages, including cover, publication matter, handwritten facsimiles, photograph/illustration pages, body pages, the section-title leaf and the intentionally blank source-side page.

No physical scan is intentionally omitted.

## 2. Printed-page / structural continuity — PASS

Confirmed source boundaries:

- scan 1 — front cover;
- scans 2–3 — title/publication/edition matter;
- scans 4–17 — front matter, printed iii–xvi;
- scan 18 — main body begins at printed page 1 (`பேராசிரியர்`);
- scan 31 — printed page 14 (`கலைஞர் ஏற்புரை`);
- scan 32 — section-title leaf `கலைஞரின் குறளோவியம்`, with no printed page number claimed;
- scan 33 — intentionally blank source-side page, printed page 16; reverse-side bleed-through remains non-body material;
- scans 34–111 — main `கலைஞரின் குறளோவியம்` sequence through printed page 94;
- scan 111 — Part 001 final physical scan / printed page 94, closing the learned-speaker vignette with two `சொல்வன்மை` Kurals and the lower Valluvar statue motif.

The apparently missing printed page 15 is not manufactured: scan 32 is an unnumbered section-title leaf and scan 33 visibly carries printed page 16.

## 3. Verification gates — PASS

### Pass 1

**COMPLETE — 111 / 111 scans captured.**

### Pass 2A — direct textual verification

**COMPLETE — 111 / 111 scans.**

`PASS2_TEXTUAL_VERIFICATION_PART_001.md` records direct source comparison for the entire part. Source-supported wording, punctuation, paragraph, Kural and metadata corrections were applied during that pass without assigning final `verified` status.

### Pass 2B — independent lexical-fidelity re-read

**COMPLETE — 111 / 111 scans.**

`PASS2B_LEXICAL_FIDELITY_PART_001.md` records the independent second reading of every source-visible printed word, including character-level distinctions, joining/spacing, names, quotations, Kural text and punctuation.

### Pass 3 — meaningful visual-text verification

**COMPLETE — 111 / 111 scans.**

`PASS3_VISUAL_TEXT_VERIFICATION_PART_001.md` records heading hierarchy, block/quotation lineation, page furniture, image/text relationships and cross-page continuation. Source-supported illustration-order corrections were made where required.

No remaining ordinary printed page depends on Pass 3 as a lexical safety net.

## 4. Source-limited records — PRESERVED / NON-BLOCKING

The following limitations are genuine properties of the supplied scan and remain deliberately unresolved rather than reconstructed:

| Scan | Printed page | Status to retain | Limitation |
|---:|---|---|---|
| 13 | xii | `partial` | handwritten/facsimile body is not safely readable word-for-word; printed heading/date/layout were checked |
| 14 | xiii | `partial` | handwritten/facsimile body is not safely readable word-for-word; printed heading/layout were checked |
| 15 | xiv | `partial` | handwritten/facsimile body is not safely readable word-for-word; printed heading/layout were checked |
| 19 | 2 | `partial` | physically washed-out/faint central printed region cannot be safely recovered from the controlling scan |

These pages must **not** be promoted to textual `verified` while their source-visible wording remains incomplete. Their Pass 3 visual organization has nevertheless been directly checked.

## 5. Part boundary — PASS WITH ADJACENT-PART CHECK DEFERRED

Scan 111 is a complete supplied physical scan and the current Part 001 boundary. Its page record captures the learned-speaker conclusion, two `சொல்வன்மை` Kurals, authority/song metadata and the lower Valluvar statue motif.

No source for overall scan 112 / Part 002 has yet been supplied in this project state, so the external **111 → 112 cross-part visual/content continuity check is deferred until Part 002 is attached**. Nothing is inferred or invented for scan 112.

This deferred adjacent-part check does not alter the integrity of the supplied 111-page Part 001 source unit.

## 6. Status / metadata consistency — ACTION REQUIRED

The source-verification gates are complete, but page front matter was intentionally left in pre-final states during the staged passes. The final status synchronization has not yet been performed globally.

Expected synchronization rule:

- ordinary fully source-checked pages: `status: "verified"`;
- scans **13–15 and 19**: retain `status: "partial"`;
- all 111 pages whose meaningful visual-text gate is complete: `visual_fidelity: "verified"`;
- do not alter Tamil body wording during metadata-only synchronization;
- do not remove or weaken the explicit source-limit notes on scans 13–15 and 19.

Because there are 111 physical records and four genuine `partial` records, the expected final textual-status distribution after synchronization is **107 `verified` + 4 `partial`**.

Until that page-level synchronization is committed and audited, do not claim that every page front matter is archival-ready and do not begin English translation.

## 7. Documentation drift found

`works/kuraloviyam/README.md`, `works/kuraloviyam/indexes/page-map.md`, root `HANDOVER.md` and `NEXT_CHAT_PROMPT_KURALOVIYAM.md` contain older workflow-frontier language from Pass 1 / Pass 2B stages. Live verification logs are newer and authoritative.

These documentation files should be synchronized after (or together with) the page-status synchronization so the next-chat frontier does not reopen completed Pass 2A / Pass 2B / Pass 3 work.

## Final audit disposition

- physical coverage: **PASS — 111 / 111**;
- internal scan continuity: **PASS**;
- printed-page/source-structure continuity: **PASS**;
- Pass 2A: **COMPLETE — 111 / 111**;
- Pass 2B: **COMPLETE — 111 / 111**;
- Pass 3: **COMPLETE — 111 / 111**;
- unresolved source limitations: **4 documented `partial` pages (13–15, 19), no contextual reconstruction permitted**;
- adjacent Part 002 boundary: **deferred until scan 112 source is supplied**;
- final page-front-matter synchronization: **PENDING**.

## Exact next activity

Perform **Part 001 final metadata/status synchronization**:

1. update ordinary Part 001 page records to `status: "verified"`;
2. retain `status: "partial"` on scans 13–15 and 19;
3. set `visual_fidelity: "verified"` on all 111 Part 001 page records now covered by Pass 3;
4. make no Tamil lexical/body-text edits during this synchronization;
5. audit the resulting distribution as **107 verified + 4 partial**, with 111/111 visual-fidelity verified;
6. synchronize `README.md`, `indexes/page-map.md`, root `HANDOVER.md` and `NEXT_CHAT_PROMPT_KURALOVIYAM.md` to the new durable frontier;
7. only after that synchronization is clean may Part 001 be declared archival-ready and an English project-translation layer be considered.

Do not begin Part 002 until its source is supplied.