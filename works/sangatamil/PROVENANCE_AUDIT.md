# சங்கத் தமிழ் — Gate F Sangam Provenance Audit

**Status: IN PROGRESS — F01 COMPLETE / PASS**

- date: **2026-09-16**
- repository: `pugazg/kalaignar-literary-commentary`
- branch: `main`
- F01 base: `c2576f5ae148b6c4b200b5107f3c71b03dacfac9`
- F01 physical scans: **1–25**
- scans inspected: **25/25**
- formal provenance units verified: **2**
- citation-anchor scans: **19, 24**
- canonical page files changed: **0**
- canonical page-wording changes: **0**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**
- next provenance frontier: **scan 26**

## Governing method

Gate F verifies **source-visible provenance only** against the supplied scan images:

- anthology / source-work label;
- பாடல் number or range;
- poet attribution;
- quoted Sangam verse block boundaries;
- `பொருள் விளக்கம்`;
- other printed source notes.

The supplied edition controls these labels and their placement. External editions and concordances are not used to overwrite the printed source. The Gemini lexical lock remains in force; Gate F does not source-correct canonical page wording.

## F01 findings

### Provenance unit 1 — scans 17–19

Section: **`மலர்மாரி பொழிகின்றேன்!`**

Citation anchor: **scan 19**.

Exact printed provenance block:

> (பத்துப்பாட்டு (குறிஞ்சிப்பாட்டு)  
> (61 முதல் 95 முடிய)  
> (பாடியவர் : கபிலர்)

Block structure:

- the quoted Sangam verse begins on **scan 17** after the printed lead-in `இதோ; கபிலர் காட்டும் மலர்கள் காண்க:`;
- **scan 18** is a full-page illustration and does not terminate the quotation;
- the quotation resumes and closes on **scan 19**;
- the printed provenance block follows the closing separator on scan 19;
- no `பொருள் விளக்கம்` block is printed for this citation unit.

Register link: [source-citation-register.md](indexes/source-citation-register.md).

### Provenance unit 2 — scan 24

Section: **`யாதும் ஊரே; யாவரும் கேளிர்!`**

Citation anchor: **scan 24**.

Exact printed provenance block:

> (புறநானூறு - பாடல் : 192  
> பாடியவர் : கணியன் பூங்குன்றன்)

Block structure:

- the Sangam quotation begins and closes on **scan 24**;
- a centered separator follows the quoted verse;
- the provenance block follows;
- the printed heading **`பொருள் விளக்கம் :`** then introduces the gloss block;
- a final separator and floral ornament close the page.

Register link: [source-citation-register.md](indexes/source-citation-register.md).

## F01 non-citation/source-context review

- scans **1–16** contain front matter and no formal Sangam citation/provenance unit;
- scans **20–21** contain narrative references to `புறநானூற்றுக் குறிப்பில்` and `நற்றிணையில் வருகின்ற காதல் பாட்டொன்றைக்`, but no standalone printed source-note block; these are not separate canonical citation entries;
- scan **22** is a full-page illustration;
- scan **25** starts `மானங்காத்த மறவன்!`; its formal Sangam citation lies beyond this batch boundary.

## Mutation audit

F01 updates only derived provenance/control documentation.

- canonical files under `works/sangatamil/pages/`: **0 changed**
- canonical page wording: **0 changed**
- Gate C2 corrections: **0**
- external-edition substitutions: **0**

## F01 closure

**F01 — COMPLETE / PASS**

- scans **1–25** inspected;
- **2** formal source-visible provenance units verified;
- exact printed labels preserved in the provenance register;
- quote boundaries and `பொருள் விளக்கம்` presence/absence recorded;
- **0 canonical page-wording changes**.

## Exact next activity

Continue **Gate F** from **scan 26** using the closed physical and section layers. Preserve this edition's printed provenance labels exactly and do not start Gate C2.
