# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–009 **ARCHIVAL-READY** continuously through overall scan 191 / printed page 158 / Kural 780; Part 010 Tamil first pass **COMPLETE 23/23**, verification pending |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–009 **released through Kural 780** |
| சங்கத்தமிழ் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Sangatamil | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |
| குறளோவியம் | தமிழ் | பின்னர் சேர்க்கப்படும் |
| Kuraloviyam | ஆங்கில வெளியிடப்பட்ட மொழிபெயர்ப்பு | source கிடைக்கும் போது தனித்த edition ஆக archive செய்யப்படும் |

## மூலக் கொள்கை

> **ஸ்கேன் தான் அதிகாரப்பூர்வ மூல ஆதாரம். Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது.

## English layers — published source vs project translation

1. **Published / official English source** — தனியாக வெளியிடப்பட்ட source கிடைத்தால், அதன் சொந்த pagination / wording / metadata-உடன் source-controlled edition ஆக archive செய்யப்படும்.
2. **Project-created English translation** — audited Tamil source-இலிருந்து உருவாக்கப்படும் மொழிபெயர்ப்பு; `translation_type: "project_translation"` என்று வெளிப்படையாகக் குறிக்கப்படும்.

The project translation follows an explicit fidelity rule: **retain Kalaignar's own language, images and interpretive direction; do not replace them with familiar standard Kural interpretations.**

## தற்போதைய நிலை — திருக்குறள்

Tamil Parts **001–009** are audited / archival-ready continuously through overall scan **191** / printed page **158** / Kural **780**.

English Parts **001–009** have completed their full release workflow continuously through Kural **780**.

Part 009 English covers scans **170–191 / printed pages 137–158 / Kural 671–780**. All **22 / 22** aligned English pages are `release-ready` after first pass, direct source-check, editorial consistency / glossary reconciliation and the separate release gate.

Editorial review: [`works/thirukkural/translations/en/reviews/PART_009_REVIEW.md`](works/thirukkural/translations/en/reviews/PART_009_REVIEW.md).

Release report: [`works/thirukkural/translations/en/reviews/PART_009_RELEASE_REPORT.md`](works/thirukkural/translations/en/reviews/PART_009_RELEASE_REPORT.md) — **PASS / RELEASE APPROVED**.

The released Part 009 section sequence is:

`அமைச்சியல்` → **Ministerial Affairs** → `அரணியல்` → **Fortification Affairs** → `கூழியல்` → **Wealth** → `படையியல்` → **Military Affairs**.

Chapter 71 `குறிப்பறிதல்` remains controlled as **Understanding Signs**. The project-added `(Porul)` disambiguator remains removed.

Protected source-check and source-sensitive decisions remain intact, including Kural 680, 691, 717, the unusual Kural 725 and 733 commentary bases, Kural 771's **memorial stones** image, and Kural 773's **great manliness / manliness** framing.

No substantive Kural/commentary body-text change was made during the Part 009 release gate.

## Part 010 Tamil — FIRST PASS COMPLETE

Controlling source: `திருக்குறள்_கலைஞர்_உரை_part_010_pages_192-214.pdf`.

All **23 / 23** supplied physical pages have first-pass Tamil records:

- overall scans **192–214**;
- printed pages **159–181**;
- Kural **781–895**;
- chapters **79–90**;
- source section throughout: `பொருள் — நட்பியல்`;
- chapter 90 `பெரியாரைப் பிழையாமை` begins on scan 214, with only Kural **891–895** present in this supplied part.

Every Part 010 page remains:

```yaml
status: "needs-review"
transcription_method: "manual transcription from source scan; direct visual verification pending"
```

Part 010 therefore has **23 `needs-review`, 0 `verified`, 0 `partial`, 0 `blocked`**. It is not archival-ready, and no Part 010 English work has begun.

Part 009 → Part 010 continuity is established at printed page **158 → 159** / Kural **780 → 781**.

## அடுத்த செயல்

Perform the separate **Part 010 Tamil direct visual verification** for all **23 pages**, scans **192–214 / printed pages 159–181 / Kural 781–895**.

Compare the complete first-pass records directly against the controlling scan and promote only passing pages to `verified`. Do not create the Part 010 audit, call the part archival-ready, or begin Part 010 English during the verification activity.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).
