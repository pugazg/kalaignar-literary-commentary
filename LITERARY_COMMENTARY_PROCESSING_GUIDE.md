# Literary Commentary Processing Guide

இந்த repository-யில் கலைஞரின் இலக்கிய உரை நூல்களை ஒரே விதமான source-first முறையில் மின்னாக்குவதற்கான நிரந்தர வழிகாட்டி.

## 1. அடிப்படை விதி

> **மூல ஸ்கேன் தான் controlling source.**

Markdown உரை மூலத்தைப் பாதுகாக்க வேண்டும்; புதிய பதிப்பை உருவாக்கக் கூடாது.

அமைதியாக செய்யக் கூடாதவை:

- எழுத்துப்பிழை என்று தோன்றுவதைத் திருத்துதல்;
- பழைய சொல்/எழுத்து வடிவங்களை நவீனப்படுத்துதல்;
- இலக்கணம், punctuation, sandhi, பெயர்கள், எண்களை standardize செய்தல்;
- குறள்/பாடல்/மேற்கோளை memory அல்லது இணையப் பதிப்பால் மாற்றுதல்;
- தெளிவில்லாத எழுத்தை sentence பொருளை வைத்து ஊகித்தல்.

## 2. ஒவ்வொரு நூலுக்கும் அமைப்பு

```text
works/<work>/
  README.md
  metadata/
    source.md
  indexes/
    page-map.md
  pages/
    0001-....md
  sections/
```

ஆங்கில அடுக்கு இரண்டு வகையாக இருக்கலாம்; அவை கலக்கப்படக் கூடாது.

### A. Published / official English source

தமிழ் நூலுக்குத் தனியாக வெளியிடப்பட்ட ஆங்கில மொழிபெயர்ப்பு scan/source கிடைத்தால், அது தனித்த source-controlled edition ஆக archive செய்யப்பட வேண்டும். அதன் pagination, wording, metadata அனைத்தும் அதன் சொந்த scan-ஆல் கட்டுப்படும்.

### B. Project-created English translation

அதிகாரப்பூர்வ ஆங்கில source இல்லாதபோது, audited Tamil transcription-ஐ அடிப்படையாகக் கொண்டு project translation உருவாக்கலாம். அது வெளிப்படையாக:

```yaml
translation_type: "project_translation"
```

எனக் குறிக்கப்பட வேண்டும். அதை publisher / official English translation என்று சொல்லக்கூடாது.

Project translation structure:

```text
works/<work>/
  translations/
    en/
      README.md
      TRANSLATION_GUIDE.md
      GLOSSARY.md
      TRANSLATION_STATUS.md
      pages/
      reviews/
```

Published English source பின்னர் கிடைத்தாலும் project translation-ஐ overwrite செய்யக்கூடாது; இரண்டையும் தனித்த source/translation layers ஆக வைத்துப் பின்னர் alignment செய்யலாம்.

## 3. பக்கவாரி பதிவு

ஒவ்வொரு scan page-க்கும் Markdown record கட்டாயம் — cover, blank, title page, handwritten facsimile, contents, body text எல்லாம் உட்பட.

பரிந்துரைக்கப்படும் front matter:

```yaml
---
scan_page: 1
printed_page: null
work: "thirukkural"
section: "..."
page_type: "cover"
status: "verified"
language: "ta"
source_filename: "...pdf"
---
```

Tamil archival status:

- `not-started`
- `partial`
- `needs-review`
- `verified`
- `blocked`

`verified` என்பது scan-ஐ நேரடியாகப் பார்த்து உறுதிப்படுத்திய பின்னரே பயன்படுத்த வேண்டும்.

## 4. Printed text vs non-text marks

தனித்தனியாகப் பதிவு செய்ய வேண்டும்:

- அச்சு உரை;
- கையெழுத்து;
- கையொப்பம்;
- library stamp / accession mark;
- bleed-through;
- scanner artefact;
- photograph / illustration.

ஒரு கையெழுத்து வாசிக்கத் தெளிவில்லையெனில் அதன் முழு உரையை ஊகிக்க வேண்டாம். `partial` எனக் குறித்துப் factual visual description மட்டும் தரலாம்.

## 5. இலக்கிய உரைகளுக்கான கூடுதல் விதிகள்

### குறள் / நூற்பா / பாடல்

- அச்சில் உள்ள வரி முறிவை பாதுகாக்கவும்.
- எண், தலைப்பு, உரை வரிசையை மாற்ற வேண்டாம்.
- source-ல் காணப்படும் quotation form-ஐ அதேபடி transcription செய்யவும்.

### Commentary

Commentary paragraph boundaries மற்றும் emphasis-ஐ சாத்தியமான வரை பாதுகாக்கவும். Markdown line wrapping மாற்றலாம்; paragraph boundary மாற்றக்கூடாது.

### Editorial/front matter

முகவுரை, அணிந்துரை, மதிப்புரை, பதிப்புரை, உள்ளுறை/contents போன்றவை body commentary-யிலிருந்து தனித்த section-ஆகப் பதிவு செய்யப்பட வேண்டும்.

## 6. Tamil source batch workflow

1. PDF scan identity மற்றும் page count உறுதி செய்.
2. Cover/title/publication/contents pages ஆய்வு செய்.
3. `metadata/source.md` புதுப்பி.
4. அனைத்து scan pages-க்கும் `indexes/page-map.md` manifest உருவாக்கு/புதுப்பி.
5. சிறிய batch-ஆக page transcription செய்.
6. தெளிவில்லாதவை `partial` அல்லது `needs-review` ஆக வைத்திரு.
7. batch முடிந்ததும் work README மற்றும் `HANDOVER.md` புதுப்பி.
8. இறுதி visual comparison முடிந்த பின் மட்டும் `verified` மாற்று.
9. ஒரு supplied part முழுவதும் review ஆன பிறகு audit file உருவாக்கி archival release decision பதிவு செய்.

## 7. Project-created English translation workflow

Project translation ஒரு Tamil PDF part **audited / archival-ready** ஆன பிறகே தொடங்க வேண்டும். முழு நூலும் முடியும் வரை காத்திருக்க வேண்டியதில்லை.

நிரந்தர cadence:

1. Tamil transcription complete;
2. Tamil direct visual verification complete;
3. Tamil part audit complete;
4. English page-aligned first-pass translation;
5. English source-check against verified Tamil record;
6. glossary / recurring terminology review;
7. editorial consistency review;
8. part-level English release report.

ஒவ்வொரு English page-மும் corresponding Tamil page filename-ஐ mirror செய்ய வேண்டும்.

Example:

```text
Tamil:
works/thirukkural/pages/0034-aram-vazhipadu-01.md

English project translation:
works/thirukkural/translations/en/pages/0034-aram-vazhipadu-01.md
```

English translation statuses Tamil archival statuses-இலிருந்து தனித்தவை:

- `draft`
- `source-checked`
- `editorial-reviewed`
- `release-ready`
- `source-limited`
- `blocked`

Tamil page `verified` என்பதால் English page தானாக `verified` அல்லது `release-ready` ஆகாது.

### Kural / commentary translation rule

- Kural number மற்றும் இரண்டு-line verse structure பாதுகாக்கப்பட வேண்டும்.
- Kural translation மற்றும் Kalaignar commentary translation தனித்தனியாக இருக்க வேண்டும்.
- commentary prose-ஐ Kural translation ஆக மாற்றக்கூடாது.
- compressed Kural reading-க்கு தேவைப்பட்டால் முதலில் Kalaignar-ன் adjacent commentary-யையே interpretive aid ஆகப் பயன்படுத்தவும்.
- வேறு commentator / web English translation-ஐ அமைதியாக இறக்குமதி செய்யக்கூடாது.

### Partial source rule

Tamil source partial என்றால் English completeness அதைவிட அதிகமாக இருக்கக் கூடாது. உதாரணமாக unreadable handwriting-ஐ English-ல் reconstruct செய்யாமல் `source-limited` ஆக வைத்திருக்க வேண்டும்.

## 8. Source-page marker

Verified Tamil page-ன் முடிவில்:

```html
<!-- மூல ஸ்கேன் பக்கம்: 1; அச்சுப் பக்கம்: — -->
```

English project translation page-ல் source identity front matter-ல் explicit Tamil page path / scan page reference ஆக இருக்க வேண்டும்.

## 9. தொடர்ச்சித் திட்டம்

இந்த repository முதலில் `திருக்குறள் — கலைஞர் உரை` மூலம் தொடங்குகிறது. பின்னர் `சங்கத்தமிழ்` மற்றும் `குறளோவியம்` தமிழ்/ஆங்கில பதிப்புகள் சேர்க்கப்படும்.

ஒவ்வொரு நூலின் source identity தனித்தனியாகக் காக்கப்பட வேண்டும். இரண்டு published editions-ன் உரையை ஒரே transcription-ல் கலக்கக்கூடாது; project-created English translation-ஐ published English source என்று காட்டக்கூடாது.
