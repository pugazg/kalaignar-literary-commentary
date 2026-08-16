# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–009 **ARCHIVAL-READY** continuously through overall scan 191 / printed page 158 / Kural 780 |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–008 **released through Kural 670**; Part 009 source-check **COMPLETE 22/22 `source-checked`** through Kural 780 |
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

Tamil Parts **001–009** are audited / archival-ready continuously through:

- overall scan **191**;
- printed page **158**;
- Kural **780**.

English Parts **001–008** have completed their full release workflow continuously through Kural **670**.

Part 009 English has completed **first-pass translation and direct source-check** across all **22 aligned pages**, scans **170–191 / printed pages 137–158 / Kural 671–780**.

Current Part 009 English state:

- `draft`: **0**;
- `source-checked`: **22 / 22**;
- `editorial-reviewed`: **0**;
- `release-ready`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

### Part 009 source-check outcome

Three substantive source-supported English corrections were made:

- Kural **680** — replaced the unsupported territorial “smaller domain” wording with **“those with little support ... the trembling among their own”**, following Kalaignar's commentary;
- Kural **691** — removed unsupported **“contentious”** from “kings”;
- Kural **717** — retained the supplied edition's unusual final `இழுக்கு` and made the English clause minimally complete as **“before those who discern / faultless words, there is a lapse.”**

The direct source-check also confirms that the unusual audited bases at Kural **717**, Kural **725 commentary**, Kural **733 commentary**, and Kural **771 commentary** remain protected rather than normalized. Kural 771 retains **“have become memorial stones”** from `நடுகல்லாய்ப் போனவர்கள்`; Kural 773 retains Kalaignar's **great manliness / manliness** wording.

Kalaignar's government/public-life vocabulary and direct source images remain preserved.

The source-visible structural sequence remains:

`அமைச்சியல்` → `அரணியல்` → `கூழியல்` → `படையியல்`.

`அமைச்சியல்` is already controlled as **Ministerial Affairs**. The current English forms **Fortification Affairs**, **Wealth**, and **Military Affairs** for the three later structural labels remain provisional until the next editorial/glossary gate.

Part 010 remains untranscribed; its first page was inspected previously only to establish continuity at printed page **159 / Kural 781 / chapter 79 `நட்பு`**.

## அடுத்த செயல்

Perform **Part 009 English editorial consistency / glossary reconciliation** for all **22 `source-checked` pages**, scans **170–191 / Kural 671–780**.

Finalize Part 009 chapter headings and the English controls for `அரணியல்`, `கூழியல்` and `படையியல்`; review recurring terminology and readability while preserving all source-check corrections and source-sensitive readings; update `GLOSSARY.md`; create `PART_009_REVIEW.md`; and promote only passing pages to `editorial-reviewed`.

Do not combine this with the Part 009 release gate, and do not begin Part 010 Tamil transcription during the same activity.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).
