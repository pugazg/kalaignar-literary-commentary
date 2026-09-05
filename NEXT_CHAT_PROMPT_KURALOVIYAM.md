# Next Chat Prompt — குறளோவியம் archival / bilingual project

Continue directly in:

`pugazg/kalaignar-literary-commentary`

Branch: `main`

Active work: `works/kuraloviyam/`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve any newer durable state. Do not reset, repeat or reopen completed Tamil work, completed first-pass English drafting, completed Part 001 English source-check, or completed glossary-reconciliation batches because a copied prompt or root multi-work handover contains an older checkpoint.

## Mandatory startup

Read completely before any Kuraloviyam change:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this `NEXT_CHAT_PROMPT_KURALOVIYAM.md`
5. `works/kuraloviyam/HANDOVER.md`
6. `works/kuraloviyam/README.md`
7. `works/kuraloviyam/PART_001_AUDIT.md`
8. `works/kuraloviyam/PART_001_FINAL_STATUS_SYNC.md`
9. `works/kuraloviyam/metadata/source.md`
10. `works/kuraloviyam/metadata/transcription-policy.md`
11. `works/kuraloviyam/indexes/page-map.md`
12. `works/kuraloviyam/translations/en/README.md`
13. `works/kuraloviyam/translations/en/TRANSLATION_GUIDE.md`
14. `works/kuraloviyam/translations/en/GLOSSARY.md`
15. `works/kuraloviyam/translations/en/TRANSLATION_STATUS.md`

Normal Part 001 English work uses audited Tamil repository page records. Do not reopen the Part 001 PDF unless a newly discovered source/provenance issue specifically requires it.

## Source / split identity

Complete source reported by user: **666 physical pages**, split into six 111-page Parts: 1–111, 112–222, 223–333, 334–444, 445–555, 556–666. Repository `scan_page` never restarts per split.

Part 002 has not been supplied or started.

## Part 001 Tamil state — CLOSED

Part 001 Tamil is **ARCHIVAL-READY**: scans 1–111; source intake and Passes 1/2A/2B/3 complete; Part audit PASS; final status sync PASS; **107 `verified` + 4 `partial`**; partial scans **13, 14, 15, 19**; visual fidelity **111/111 `verified`**.

Do not reconstruct the handwritten/facsimile bodies on scans 13–15 or the faint/washed-out material on scan 19.

## Mandatory per-part closure rule

Finish one supplied Part completely before the next:

Tamil source intake → Pass 1 → Pass 2A → Pass 2B → Pass 3 → Part audit → final status/documentation sync → Tamil archival-ready → English translation/review closure → final Part checkpoint → next supplied Part.

## English project translation controls

English layer: `works/kuraloviyam/translations/en/`.

It is a **project-created translation**, not an official/publisher-issued English edition. Every English page carries `translation_type: "project_translation"`.

Permanent review cadence:

**draft → source-check → glossary reconciliation → editorial review → Part review → release report → release-ready**.

Do not import standard Thirukkural wording, published English translations, web text, another commentator or memory.

The user-directed normal iteration size is **15 consecutive physical scan pages**; a final Part remainder may be shorter.

## English first-pass state — COMPLETE

All **111/111** Part 001 English page records exist.

## English source-check state — COMPLETE

All **111/111 physical scans** have been source-reviewed.

Final source-check totals:

- page records: **111/111**;
- `source-checked`: **107**;
- `source-limited`: **4** — scans 13–15, 19; all four reviewed within available evidence;
- `draft`: **0**;
- editorial-reviewed: **0**;
- release-ready: **0**;
- unreadable source material reconstructed: **none**;
- external/standard Kural English wording imported: **none**.

## Glossary / recurring-terminology reconciliation

**GR1 — scans 1–15 — COMPLETE.**

- controlled source-supported terms/names were reconciled and added to `GLOSSARY.md`;
- no English page wording correction was required solely for GR1 consistency;
- scans 13–15 remain source-limited and no handwritten body terminology was inferred.

**GR2 — scans 16–30 — COMPLETE.**

- `பதிப்புரை` → **Publisher's Note** is explicitly distinct from `பதவுரை` → **word-by-word explanation** and `முகப்புரை` → **Preface**;
- the user-confirmed `பதவுரை` clarification was applied to its existing English occurrences on scans 4–5;
- scan 17 now uses the controlled structural sequence **the Book of Aram, the Book of Porul and the Book of Love** for `அறத்துப்பால், பொருட்பால், காமத்துப்பால்`;
- scan 30 now preserves **Puratchi Kavignar Bharathidasan**, consistent with the explicit source honorific and scan 19;
- context-sensitive `உரை` and `புதுக் கவிதை` renderings were retained rather than flattened;
- scan 19 remains source-limited; nothing was inferred from its washed-out gap.

**GR3 — scans 31–45 — COMPLETE.**

- all fifteen records were reconciled against audited Tamil context and the expanded glossary;
- English page wording corrections required solely for GR3 consistency: **none**;
- scan 31 `முன்னுரை` / `ஏற்புரை` were recorded as **preface / Response**, retaining the distinction from printed `முகப்புரை` headings where needed;
- **Muthamizh** and **yaazh** were recorded from scans 39–40;
- scan 35's explicit lexical contrast `இறைவன் / இறை / கடவுள் / தெய்வம்` is preserved contextually as **Iraivan / Irai / Kadavul / Deivam** when the source distinguishes the terms;
- **Primordial Being**, **Vaal-arivan**, `அதிகாரம் / பாடல்` → **Chapter / Kural**, and the source-supported chapter labels encountered through scan 44 were added to the glossary;
- no standard/published/web English Kural translation wording was imported.

Glossary-reconciliation coverage: **45/111 scans**. Page statuses remain unchanged; glossary review does not itself create `editorial-reviewed` status.

## Exact next activity

If live `main` has not advanced beyond this frontier, execute **Part 001 glossary / recurring-terminology reconciliation GR4 — scans 46–60**.

1. process exactly **15 consecutive pages**;
2. fetch matching audited Tamil and English records for scans **46–60** as needed;
3. compare recurring names, controlled literary terms, chapter labels, publication/work names and repeated English renderings against the expanded `works/kuraloviyam/translations/en/GLOSSARY.md` and their Tamil context;
4. add or refine glossary entries only where Part 001 evidence supports them;
5. do not mechanically force one English equivalent where context requires a different rendering;
6. do not import terminology from standard Thirukkural editions, web sources, published translations, another commentator or memory;
7. this glossary gate does **not** itself promote pages to `editorial-reviewed`;
8. record any terminology corrections transparently in affected English page records and `GLOSSARY.md`;
9. update `TRANSLATION_STATUS.md`, English/work README, `works/kuraloviyam/HANDOVER.md`, and this prompt;
10. audit the exact pre-batch base→head changed-file set before advancing to GR5.

Do not begin Part 002 until Part 001 English/final closure is complete and the Part 002 source is supplied.