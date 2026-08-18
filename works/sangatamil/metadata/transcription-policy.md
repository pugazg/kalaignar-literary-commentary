# மின்னாக்கக் கொள்கை — சங்கத் தமிழ்

## அடிப்படை விதி

**மூல ஸ்கேன் தான் controlling source.**

ஒவ்வொரு usable scan page-க்கும் தனி Markdown record உருவாக்கப்படும். அட்டை, வெற்றுப் பக்கம், கையெழுத்துப் facsimile, ஓவியம், தொடர்ச்சியான உரை அனைத்தும் இதில் அடங்கும்.

## நிலைகள்

- `not-started` — page record/metadata exists but continuous source text has not yet been transcribed;
- `partial` — only securely readable portions have been recorded;
- `needs-review` — full first pass exists but direct character-level comparison remains;
- `verified` — directly compared with the scan;
- `blocked` — source defect prevents safe completion.

## source-fragment boundary

Current work is limited to scans 1–150 of the supplied fragment. No 151+ record may be invented.

## செய்யக் கூடாதவை

- பழைய/வழக்கத்திற்கு மாறான சொல் வடிவத்தை அமைதியாகச் சீர்திருத்துதல்;
- சங்கப் பாடலை web/மற்ற பதிப்பிலிருந்து மாற்றிப் பதித்தல்;
- poem number அல்லது poet attribution-ஐ வெளிப்புற அறிவால் அமைதியாகத் திருத்துதல்;
- தெளிவில்லாத கையெழுத்தை context வைத்து நிரப்புதல்;
- ஓவியத்தில் source label இல்லாத நபரை appearance மூலம் அடையாளப்படுத்துதல்;
- printed page number தெரியாத இடத்தில் arithmetic வைத்து எண்ணை உருவாக்குதல்.

## கவிதை / மேற்கோள் / பொருள் விளக்கம்

- அச்சு verse lineation பாதுகாக்க வேண்டும்;
- quotation punctuation பாதுகாக்க வேண்டும்;
- source anthology, பாடல் எண், பாடியவர் ஆகியவை source-ல் இருப்பதுபோல பதிவு செய்ய வேண்டும்;
- `பொருள் விளக்கம்` தனி source block ஆக வைக்க வேண்டும்;
- Kalaignar explanation மற்றும் quoted Sangam verse ஒன்றாகக் கலக்கக் கூடாது.

## ஓவியப் பக்கங்கள்

Printed caption இருந்தால் verbatim transcription. Caption இல்லையெனில் factual visual description மட்டும்.

## section README

Decorative heading மூலம் தொடங்கும் thematic units `sections/` கீழ் source-order navigation nodes ஆக map செய்யப்படும். Repository sequence source-authored chapter number அல்ல.

## verification gate

`verified` status requires direct visual comparison with the scan. OCR/search snippets are never sufficient.
