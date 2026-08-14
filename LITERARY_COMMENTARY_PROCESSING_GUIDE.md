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

தமிழ் மற்றும் அதிகாரப்பூர்வ/வெளியிடப்பட்ட ஆங்கில மொழிபெயர்ப்பு இரண்டும் கிடைக்கும் நூல்களுக்கு பின்னர்:

```text
  translations/en/
  BILINGUAL_ALIGNMENT.md
  TRANSLATION_REVIEW.md
```

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

Status:

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

## 6. Batch workflow

1. PDF scan identity மற்றும் page count உறுதி செய்.
2. Cover/title/publication/contents pages ஆய்வு செய்.
3. `metadata/source.md` புதுப்பி.
4. அனைத்து scan pages-க்கும் `indexes/page-map.md` manifest உருவாக்கு/புதுப்பி.
5. சிறிய batch-ஆக page transcription செய்.
6. தெளிவில்லாதவை `partial` அல்லது `needs-review` ஆக வைத்திரு.
7. batch முடிந்ததும் work README மற்றும் `HANDOVER.md` புதுப்பி.
8. இறுதி visual comparison முடிந்த பின் மட்டும் `verified` மாற்று.

## 7. Source-page marker

Verified page-ன் முடிவில்:

```html
<!-- மூல ஸ்கேன் பக்கம்: 1; அச்சுப் பக்கம்: — -->
```

## 8. தொடர்ச்சித் திட்டம்

இந்த repository முதலில் `திருக்குறள் — கலைஞர் உரை` மூலம் தொடங்குகிறது. பின்னர் `சங்கத்தமிழ்` மற்றும் `குறளோவியம்` தமிழ்/ஆங்கில பதிப்புகள் சேர்க்கப்படும். ஒவ்வொரு நூலின் source identity தனித்தனியாகக் காக்கப்பட வேண்டும்; இரண்டு பதிப்புகளின் உரையை ஒரே page transcription-ல் கலக்கக் கூடாது.
