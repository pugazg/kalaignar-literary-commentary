# Literary Commentary Processing Guide

இந்த repository-யில் கலைஞரின் இலக்கிய உரை நூல்களை source-first முறையில் மின்னாக்குவதற்கான நிரந்தர வழிகாட்டி.

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
status: "needs-review"
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

`verified` என்பது scan-ஐ நேரடியாகப் பார்த்து required textual fidelity மற்றும் meaningful visual text fidelity gates முடிந்த பின்னரே பயன்படுத்த வேண்டும்.

Meaningful page structure உள்ள works-க்கு optional fields பயன்படுத்தலாம்:

```yaml
visual_fidelity: "needs-review"
visual_notes: "centered heading; verse block; illustration between text blocks"
```

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

Source crop, binding shadow, damage அல்லது scan loss காரணமாக text/layout மறைந்திருந்தாலும் context வைத்து reconstruct செய்யக்கூடாது; `partial` அல்லது `blocked` நிலை பயன்படுத்த வேண்டும்.

## 5. இலக்கிய உரைகளுக்கான கூடுதல் விதிகள்

### குறள் / நூற்பா / பாடல்

- அச்சில் உள்ள வரி முறிவை final archival state-ல் பாதுகாக்கவும்.
- எண், தலைப்பு, உரை வரிசையை மாற்ற வேண்டாம்.
- source-ல் காணப்படும் quotation form-ஐ அதேபடி transcription செய்யவும்.

### Commentary

Commentary paragraph boundaries மற்றும் emphasis-ஐ final archival state-ல் source-supported அளவில் பாதுகாக்கவும். Markdown line wrapping மாற்றலாம்; paragraph boundary மாற்றக்கூடாது.

### Editorial/front matter

முகவுரை, அணிந்துரை, மதிப்புரை, பதிப்புரை, உள்ளுறை/contents போன்றவை body commentary-யிலிருந்து தனித்த section-ஆகப் பதிவு செய்யப்பட வேண்டும்.

### Visual text fidelity

Text transcription என்பது characters மட்டும் அல்ல; final archive source-இன் **meaningful visual organization**-ஐயும் பாதுகாக்க வேண்டும்.

Dedicated visual verification-ல் source-supported அளவில் பின்வருவன சரிபார்க்கப்பட வேண்டும்:

- verse line breaks மற்றும் stanza grouping;
- prose paragraph boundaries;
- indentation / hanging indentation;
- centered, right-aligned அல்லது deliberate alignment கொண்ட heading/line;
- decorative heading hierarchy;
- தனி quotation / citation / gloss blocks;
- numbered or lettered list grouping;
- asterisks, rules, ornamental separators மற்றும் section breaks;
- structural meaning கொண்ட bold / underline / enlarged emphasis;
- running headers, printed page numbers மற்றும் footers ஆகியவற்றை body text-ல் அமைதியாக கலக்காமல் page furniture ஆகப் பதிவு செய்தல்;
- captions மற்றும் image-க்கு உடனான text relationship;
- physical page boundary-ஐ கடந்து தொடரும் sentence / paragraph / poem continuity.

Exact font face, point size, colour, kerning அல்லது decorative artwork-ஐ pixel-perfect ஆக reproduce செய்ய வேண்டியதில்லை. நோக்கம் **semantic visual fidelity**, facsimile recreation அல்ல.

Markdown meaningful structure-ஐ காக்க முடியாத இடத்தில் limited HTML பயன்படுத்தலாம். Exact spatial placement reproduce செய்ய முடியாவிட்டால் text-ஐ faithful-ஆகப் பாதுகாத்து factual `visual_notes` அல்லது HTML comment மூலம் arrangement-ஐ பதிவு செய்யவும்.

Source-ல் இல்லாத alignment, stanza break, emphasis அல்லது decorative grouping உருவாக்கக்கூடாது.

ஒரு page-ல் characters சரியாக இருந்தாலும் meaningful lineation/block structure தவறாக இருந்தால் அது final `verified` state அல்ல.

## 6. Tamil source processing workflow

### 6.1 Default gate logic

Every work must ultimately pass these conceptual gates:

1. source identity / page count;
2. physical page capture / transcription;
3. textual verification;
4. meaningful visual-text verification;
5. physical-page / continuity audit;
6. structure / section audit where applicable;
7. provenance / citation audit where applicable;
8. metadata / status consistency audit;
9. whole-volume or supplied-part final synchronization/audit.

A work may execute these gates in small batches **or** as whole-volume passes, but it must document the chosen cadence explicitly in that work's own guide/handover.

### 6.2 Work-specific cadence takes precedence

If a work-specific archival guide or workflow document defines a deliberate staged cadence, that cadence overrides the generic batching order here **without overriding the source-fidelity rules**.

In particular, `works/sangatamil/` uses:

[`works/sangatamil/MULTI_PASS_WORKFLOW.md`](works/sangatamil/MULTI_PASS_WORKFLOW.md)

Its canonical sequence is:

1. Pass 1 — transcription / physical capture only through the entire source;
2. Pass 2 — textual verification across the entire source;
3. Pass 3 — visual-text fidelity verification across the entire source;
4. Pass 4 — physical-page / continuity audit;
5. Pass 5 — section-structure audit;
6. Pass 6 — Sangam provenance audit;
7. Pass 7 — metadata / status audit;
8. Pass 8 — whole-volume synchronization / final audit.

During a transcription-only pass, new records may remain `needs-review`; the workflow must not falsely promote them to `verified`.

### 6.3 General status rule

- first-pass capture may use `needs-review`;
- source defect may require `partial` or `blocked`;
- `verified` only after the work's required verification gates are actually complete;
- documentation synchronization cadence follows the work-specific plan rather than being forced after every page or small batch.

## 7. Project-created English translation workflow

Project translation ஒரு Tamil PDF part **audited / archival-ready** ஆன பிறகே தொடங்க வேண்டும். முழு நூலும் முடியும் வரை காத்திருக்க வேண்டியதில்லை unless the work-specific plan requires full-volume completion first.

நிரந்தர cadence:

1. Tamil transcription complete;
2. Tamil direct textual + visual verification complete;
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

Tamil page-ன் முடிவில் source-page marker பயன்படுத்தலாம்:

```html
<!-- மூல ஸ்கேன் பக்கம்: 1; அச்சுப் பக்கம்: — -->
```

English project translation page-ல் source identity front matter-ல் explicit Tamil page path / scan page reference ஆக இருக்க வேண்டும்.

## 9. தொடர்ச்சித் திட்டம்

இந்த repository முதலில் `திருக்குறள் — கலைஞர் உரை` மூலம் தொடங்கியது. `சங்கத் தமிழ்` active source-first work ஆக உள்ளது; பின்னர் `குறளோவியம்` தமிழ்/ஆங்கில பதிப்புகள் சேர்க்கப்படும்.

ஒவ்வொரு நூலின் source identity தனித்தனியாகக் காக்கப்பட வேண்டும். இரண்டு published editions-ன் உரையை ஒரே transcription-ல் கலக்கக்கூடாது; project-created English translation-ஐ published English source என்று காட்டக்கூடாது.