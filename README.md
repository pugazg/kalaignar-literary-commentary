# கலைஞர் இலக்கிய உரைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் இலக்கிய உரை / விளக்க நூல்களை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## திட்டமிட்ட நூல்கள்

| நூல் | மொழி | நிலை |
|---|---|---|
| திருக்குறள் — கலைஞர் உரை | தமிழ் | Parts 001–011 **ARCHIVAL-READY continuously through overall scan 237 / printed page 204 / Kural 1010** |
| Thirukkural — Kalaignar's Commentary | English project translation | Parts 001–010 **RELEASED through Kural 895**; Part 011 **SOURCE-CHECKED 23/23 through Kural 1010** |
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

Tamil Parts **001–011** are audited / archival-ready continuously through overall scan **237** / printed page **204** / Kural **1010**.

Part 011 Tamil audit: [`works/thirukkural/AUDIT_PART_011.md`](works/thirukkural/AUDIT_PART_011.md) — **PASS / ARCHIVAL-READY**.

The Part 010 → Part 011 boundary passes at printed page **181 → 182 / Kural 895 → 896**. Part 011 preserves the source-visible transition from `பொருள் — நட்பியல்` on scans **215–225** to `பொருள் — குடியியல்` from scan **226 / printed page 193 / chapter 96 குடிமை**.

English Parts **001–010** have completed the full translation workflow continuously through Kural **895**. Released Part 010 protections remain unchanged, including **women for hire** at Kural 813/822, Kural 835's **seven periods**, Kural 850's evidence/“ghosts” framing, Kalaignar's supplied Kural 861 interpretation, Kural 869's repeated **“cowards who are afraid, and ignorant cowards”**, Kural 876's enemy/friendship nuance, and Kural 895's **ruler / government** distinction.

Part 011 English first pass and **direct source-check are now complete 23 / 23** for scans **215–237 / printed pages 182–204 / Kural 896–1010**. Every Part 011 English record is now `status: "source-checked"`; editorial/glossary review and release remain pending.

Six substantive source-fidelity corrections/refinements were made during source-check: Kural **911** now says **bring suffering** rather than “bring ruin”; Kural **926** restores the sleepers/dead and liquor/poison line relationships; Kural **953** follows Kalaignar's **truthful citizens** interpretation; Kural **961** removes an unsupported qualification from “indispensable”; Kural **989** keeps the all-seas-overturning image in commentary rather than importing it into the Kural; and Kural **1006** correctly makes the miser a disease upon his great wealth.

The source-check also retains Kalaignar's **oppressive government** framing at Kural 899, **social disease** at 948, rationalist **nonexistent heaven** question at 966, explicit **Everyone is equal by birth** formulation at 972, and the unusual audited Kural 971 basis and source images.

`நட்பியல்` remains controlled as **Friendship**. `குடியியல்` → **Civic Life** and chapter headings 91–101 remain provisional until the next editorial/glossary gate.

No Kural **1011** onward has been inferred or created.

## அடுத்த செயல்

Perform **Part 011 English editorial consistency / glossary reconciliation** for all **23 `source-checked` pages**. Finalize `குடியியல்` and chapter headings 91–101, update `GLOSSARY.md`, create `PART_011_REVIEW.md`, and promote passing pages only to `editorial-reviewed`.

Do not combine that gate with release. Do not modify released Parts 001–010 merely to harmonize later wording.

Detailed status: [`works/thirukkural/README.md`](works/thirukkural/README.md), [`works/thirukkural/translations/en/TRANSLATION_STATUS.md`](works/thirukkural/translations/en/TRANSLATION_STATUS.md), and [`HANDOVER.md`](HANDOVER.md).
