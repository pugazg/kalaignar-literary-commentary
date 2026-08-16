# Part 009 English Translation Release Report

## Scope

This release gate covers the complete project-created English translation for **Part 009**, overall scans **170–191**, printed pages **137–158**, containing Kural **671–780** and Kalaignar's commentary.

The English layer is a **project translation**, not an official or publisher-supplied English edition.

## Source authority

The supplied Tamil scans remain the ultimate authority. The working translation basis is the verified Tamil archival transcription for Part 009, whose Tamil audit decision is **ARCHIVAL-READY**.

Release prerequisites completed before this gate:

- Tamil transcription: complete;
- Tamil direct visual verification: **22 / 22**;
- Tamil audit: **ARCHIVAL-READY**;
- English first-pass: **22 / 22**;
- English direct source-check: **22 / 22**;
- English editorial consistency / glossary reconciliation: **22 / 22**;
- editorial review artefact: `PART_009_REVIEW.md`.

## Release-gate checks

The Part 009 English set was checked as one continuous release unit for:

- exact page alignment with scans **170–191**;
- printed-page continuity **137–158**;
- Kural continuity **671–780**;
- exact English/Tamil filename alignment and `source_tamil_file` references;
- `translation_type: "project_translation"` on all aligned pages;
- `source_tamil_status: "verified"` throughout;
- chapter-heading consistency across chapters **68–78**;
- the controlled section sequence **Ministerial Affairs → Fortification Affairs → Wealth → Military Affairs**;
- Kural/commentary separation and page-local source markers;
- preservation of the Part 009 source-check corrections and protected source-sensitive readings;
- preservation of Kalaignar's institutional/public vocabulary and direct images;
- absence of `draft`, `source-checked`, `source-limited`, or `blocked` records before release.

All **22 / 22** Part 009 page records were confirmed at `editorial-reviewed` before this release report was created. No unresolved release blocker was found.

## Controlled Part 009 headings released

| No. | Tamil | Released English |
|---:|---|---|
| 68 | வினை செயல்வகை | **The Method of Action** |
| 69 | தூது | **The Envoy** |
| 70 | மன்னரைச் சேர்ந்து ஒழுகல் | **Conduct in the Presence of Kings** |
| 71 | குறிப்பறிதல் | **Understanding Signs** |
| 72 | அவை அறிதல் | **Knowing the Assembly** |
| 73 | அவை அஞ்சாமை | **Fearlessness in the Assembly** |
| 74 | நாடு | **The Country** |
| 75 | அரண் | **Fortress** |
| 76 | பொருள் செயல்வகை | **The Way of Acquiring Wealth** |
| 77 | படை மாட்சி | **Excellence of the Army** |
| 78 | படைச் செருக்கு | **Martial Pride** |

Chapter 71 is released as **Understanding Signs**. The earlier project-added `(Porul)` disambiguator was removed during editorial review because it is not present in the Tamil heading.

## Released structural vocabulary

The source-visible sequence is released in English metadata as:

- `அமைச்சியல்` → **Ministerial Affairs**;
- `அரணியல்` → **Fortification Affairs**;
- `கூழியல்` → **Wealth**;
- `படையியல்` → **Military Affairs**.

These labels preserve the supplied main body's section hierarchy rather than flattening the source-visible distinctions.

## Source-check corrections confirmed at release

The release gate confirms that all three substantive Part 009 source-check corrections remain intact:

1. Kural **680** retains **“those with little support ... the trembling among their own”**, not the unsupported territorial “smaller domain” wording;
2. Kural **691** retains **“kings”** without the unsupported adjective “contentious”;
3. Kural **717** retains the minimally complete English clause ending **“there is a lapse”**, grounded in this supplied edition's verified final `இழுக்கு`.

No source-check correction has been reverted during editorial review or release.

## Protected source-sensitive readings confirmed at release

The release deliberately retains the source-controlled treatments established by the Tamil audit and English review:

- Kural **717** remains based on the supplied-edition Tamil `கற்றறிந்தார் கல்வி விளங்கும் கசடறச் / சொற்றெரிதல் முன்னர் இழுக்கு.` and retains its source-check note;
- Kural **725 commentary** remains grounded in `தருக்கமென்படும் அளவைக் திறமும்`, with **“the skill of measure called logic”** and no repair of the Tamil basis;
- Kural **733 commentary** remains grounded in `மளவுக்கு வளம்`, with **“possesses wealth to that measure”** and no normalization of the Tamil basis;
- Kural **771 commentary** retains `நடுகல்லாய்ப் போனவர்கள்` through the direct image **“have become memorial stones”**;
- Kural **773** retains Kalaignar's explicit `பெரும் ஆண்மை` / `ஆண்மையின் உச்சம்` framing as **great manliness / manliness**.

## Kalaignar-language and image protections released

The release confirms preservation of Kalaignar's institutional and public-life vocabulary where explicit, including government, tax/revenue, customs duties, tribute, country, fortification, wealth, army, ruler/king/leader and public responsibility.

Direct images remain intact, including:

- one elephant capturing another;
- warming oneself by fire;
- the cashew-nut comparison;
- nectar spilled in an unclean courtyard;
- love as mother, compassion as child, material resources as nurse;
- watching elephants fight from a hill;
- rats roaring like the sea before the cobra's breath;
- the victory garland;
- memorial stones;
- the spear pulled from a warrior's chest;
- honourable battle wounds;
- the warrior's anklet.

No substantive Kural or Kalaignar-commentary body-text change was made during this release gate.

## Alignment result

The release unit is continuous and one-to-one:

- scan **170** / printed page **137** begins Kural **671**;
- scan **191** / printed page **158** ends Kural **780**;
- every intervening scan and printed page is represented exactly once;
- every English filename mirrors its Tamil archival filename;
- every `source_tamil_file` points to the corresponding verified Tamil record;
- chapter 68 begins at scan 170 and chapter 78 concludes at scan 191;
- the section transitions occur at the controlled source-supported boundaries: scan **182** → Fortification Affairs, scan **186** → Wealth, scan **188** → Military Affairs.

## Release decision

**PASS — PART 009 ENGLISH RELEASE APPROVED.**

All **22 / 22** aligned Part 009 English page records are eligible for promotion from `editorial-reviewed` to `release-ready`.

After promotion, the released project translation extends continuously through Kural **780**.

## Boundary after release

This report closes the English workflow for Part 009.

It does **not** begin Part 010 Tamil transcription. The next separate activity is **Part 010 Tamil first-pass transcription**, beginning at overall scan **192 / printed page 159 / Kural 781 / chapter 79 `நட்பு`**, using the supplied Part 010 scan as the controlling source.
