# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil.

The English layer is a **project-created translation**, not an official/publisher English edition. It must retain Kalaignar's own language, images, emphases and interpretive direction and must not import external English Kural wording or another commentator's interpretation.

Permanent cadence:

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release report.**

Do not collapse these stages.

# Established completed state

## Tamil

Parts **001–007 are audited / archival-ready** through overall scan **148** / printed page **115** / Kural **565**.

Part 007 audit: [`works/thirukkural/AUDIT_PART_007.md`](works/thirukkural/AUDIT_PART_007.md).

## English project translation

Parts **001–006 are released** through Kural **460**. Do not revise those released entries during Part 007 work.

# Part 007 English — SOURCE-CHECK COMPLETE

Scope:

- scans **128–148**;
- local pages **1–21**;
- printed pages **95–115**;
- Kural **461–565**;
- chapters **47–57**.

Current state:

- aligned English files: **21 / 21**;
- `source-checked`: **21 / 21**;
- `draft`: **0**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

Every Part 007 English page was compared directly against its audited Tamil archival record. Kural and Kalaignar commentary were checked as separate layers for omissions, additions, meaning drift, source imagery and imported interpretation.

## Source-check correction recorded

One substantive source-fidelity refinement was made:

- scan **128 / Kural 464**:
  - first pass: **“Those who fear the disgrace of failure / do not begin what has not been made clear.”**
  - source-checked: **“Those who fear the blemish of disgrace / do not begin an action whose consequences are unclear.”**
  - reason: Kalaignar's commentary centres `களங்கம்`; the first-pass phrase “failure” added a specificity not present in his explanation.

No other Part 007 page required a source-fidelity wording correction during this pass.

## Protected Kalaignar-language / interpretation decisions

These remain binding for editorial review:

1. **Kural 543** — Kalaignar explains `அந்தணர் நூற்கும்` through `அறவோர் நூல்களுக்கும்`; the English remains **“the books of the virtuous”**. Do not replace this with a caste-specific conventional gloss.
2. **Kural 520** — retain Kalaignar's explicit focus on **working people** and the obligation of those who govern to examine their condition daily and act accordingly.
3. **Chapters 55–57** — preserve Kalaignar's framing through **government, citizens, good governance, justice, tyranny, public resources, productive work, punishment and fear** rather than importing another commentator's vocabulary.
4. Preserve source-supported images: ram drawing back before charging; crane waiting and striking; crocodile leaving water; elephant trapped in mire and killed by foxes; timely rain and harvest; weeds removed from crops; citizens' tears becoming a weapon against oppressive rule.
5. Preserve direct social/political language rather than smoothing it into generic moral prose merely for elegance.

# Part 008 intake

Part 008 is supplied as:

`திருக்குறள்_கலைஞர்_உரை_part_008_pages_149-169.pdf`

Its first page is printed page **116** and contains Kural **566–570**, directly continuing chapter 57 `வெருவந்த செய்யாமை`. Part 008 remains intake-only during the Part 007 English workflow unless a later activity explicitly changes scope.

# Exact next activity

Perform **Part 007 English editorial consistency / glossary-reconciliation review only** across all **21 / 21 source-checked pages**.

Required procedure:

1. fresh-fetch this `HANDOVER.md`;
2. read `works/thirukkural/translations/en/TRANSLATION_GUIDE.md` and the full `GLOSSARY.md`;
3. inspect `reviews/PART_006_REVIEW.md` as the completed review model;
4. review all Part 007 English pages for readability, controlled chapter headings, recurring terms, repeated phrasing, punctuation and accidental interpretation drift;
5. preserve Kalaignar's language, imagery, political/governance framing and interpretive direction;
6. specifically protect the Kural 543 `அந்தணர்` → `அறவோர்` decision and Kural 520 working-people framing;
7. establish / confirm controlled Part 007 chapter headings 47–57 from actual context;
8. update `GLOSSARY.md` with deliberate Part 007 terminology decisions and any documented index/main-body refinements;
9. create `works/thirukkural/translations/en/reviews/PART_007_REVIEW.md` documenting scope, decisions and any actual editorial changes;
10. after a page passes editorial review, promote it from `source-checked` to `editorial-reviewed`;
11. synchronize `TRANSLATION_STATUS.md`, work README, root README and this handover;
12. stop after editorial review.

Do **not** in that activity:

- create `PART_007_RELEASE_REPORT.md`;
- promote pages to `release-ready`;
- begin Part 008 Tamil transcription;
- modify released English Parts 001–006.

After all 21 Part 007 English pages are `editorial-reviewed`, the next separate activity is the **Part 007 English release gate**.
