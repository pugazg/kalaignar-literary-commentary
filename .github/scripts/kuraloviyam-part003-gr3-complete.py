from pathlib import Path
import re

ROOT=Path('works/kuraloviyam')
EN=ROOT/'translations/en'


def must_replace(text,old,new,label,count=None):
    n=text.count(old)
    if n==0: raise SystemExit(f'{label}: missing expected text: {old[:80]!r}')
    if count is not None and n!=count: raise SystemExit(f'{label}: expected {count} occurrences, found {n}: {old[:80]!r}')
    return text.replace(old,new)

def write(path,text): Path(path).write_text(text,encoding='utf-8')

# 1) Terminology correction required by the existing controlled proper-name form.
for scan,printed,expected in [(313,296,5),(314,297,3)]:
    p=EN/'pages'/f'{scan:04d}-kuraloviyam-{printed}.md'
    s=p.read_text(encoding='utf-8')
    n=s.count('Kaarmegam')
    if n!=expected: raise SystemExit(f'{p}: expected {expected} Kaarmegam occurrences, found {n}')
    s=s.replace('Kaarmegam','Karmegam')
    if s.count('status: "source-checked"')!=1: raise SystemExit(f'{p}: status drift')
    p.write_text(s,encoding='utf-8')

# 2) Glossary: source-evidenced chapter variants, controls, narrative names, and printed glosses.
gp=EN/'GLOSSARY.md'; g=gp.read_text(encoding='utf-8')
if '## Part 003 GR3 reconciliation record — scans 289–321' in g: raise SystemExit('GR3 glossary record already exists')
g=must_replace(g,'## Thirukkural chapter labels first encountered in Part 003 through GR2','## Thirukkural chapter labels first encountered in Part 003 through GR3','glossary heading',1)
g=must_replace(g,'| அவர்வயின்விதும்பல் | Longing for His Return |','| அவர்வயின்விதும்பல் / அவர் வயின் விதும்பல் | Longing for His Return |','chapter 127 variant',1)
g=must_replace(g,'| கனவு நிலையுரைத்தல் / கனவுநிலையுரைத்தல் / கனவுநிலை உரைத்தல் | Speaking of the Dream State |','| கனவு நிலையுரைத்தல் / கனவுநிலையுரைத்தல் / கனவுநிலை உரைத்தல் / கனவு நிலை உரைத்தல் | Speaking of the Dream State |','chapter 122 variant',1)
g=must_replace(g,'| ஆள்வினையுடைமை | Diligent Effort |','| ஆள்வினையுடைமை / ஆள்வினை உடைமை | Diligent Effort |','chapter 62 variant',1)
anchor='| பெரியாரைத் துணைக்கோடல் | Seeking the Support of the Great | Chapter 45 label on scan 285. |'
addition=anchor+'\n| துறவு | Renunciation | Chapter 35 label on scan 289. |\n| சுற்றந் தழால் | Cherishing Kindred | Chapter 53 label on scan 293. |'
g=must_replace(g,anchor,addition,'new GR3 chapter controls',1)

review='## Review rule\n\nNew recurring terms should be added only when actually encountered in audited Tamil records. Do not pre-populate the glossary from external editions or general Thirukkural terminology.'
gr3='''## Part 003 GR3 additional narrative/name controls

| Tamil | Default English form | Editorial note |
|---|---|---|
| பொன்னி | Ponni | Waiting-for-lover vignette across scans 290–291. |
| தாமரை | Thamarai | Ponni's companion across scans 290–291. |
| முகிலன் | Mukilan | Fisher/lover across scans 298–299. |
| முல்லைக்கொடி | Mullai-kodi | Mukilan's wife/lover across scans 298–299. |
| திருமகள் | Thirumagal | Named divinity/figure in the labour-and-idleness discussion across scans 300–302. |
| மூதேவி | Moodevi | Named counterpart to Thirumagal across scans 300–302. |
| திங்கள் | Thingal | Woman's personal name in scans 303–304; keep distinct from ordinary moon/day senses. |
| செவ்வாய் | Sevvai | Woman's personal name in scans 303–304; keep distinct from ordinary weekday/planet senses. |
| எழினி | Ezhini | Poet/character across scans 305–306. |
| கொல்லி நாடு | Kolli | Country/place reference in the Ezhini betrayal vignette across scans 305–306. |
| வஞ்சிக்கொடி | Vanchikkodi | Named woman at the opening of the harvest-field vignette across scans 307–308. |
| காளி | Kaali | Woman named in the harvest-field vignette across scans 307–308. |
| கடம்பன் | Kadamban | Kaali's lover across scans 307–308. |
| சேயிழை | Seyizhai | Woman in the pallor/separation vignette across scans 315–316. |

The already controlled `கார்மேகம்` → **Karmegam** form is reused for the distinct field/idleness character on scans **313–314**. GR3 reconciles the two English page files from **Kaarmegam** to **Karmegam**; this is a terminology/transliteration consistency correction only and does not alter Tamil or page status.

## Part 003 GR3 source-printed lexical glosses

These are page-specific source glosses and should not be generalized beyond their audited contexts without new evidence.

| Tamil source expression | Source-supported English | Evidence |
|---|---|---|
| பற்றற்ற கண்ணும் | even when one has fallen low | Scan 293 altered-Kural explanation. |
| பகைமை பாராட்டுதல் | cherishing enmity / acting with hostile feeling | Scan 293 altered-Kural explanation. |
| சுற்றத்தார் கண்ணேயுள | is found among one's kindred | Scan 293 altered-Kural explanation. |
| அதர்வினாய் | asking the way | Scan 310 printed gloss `வழிகேட்டு`. |
| உழை | place | Scan 310 printed gloss `இடம்`. |
| பகடு | ox | Scan 310 printed gloss `எருது`. |
| மடுத்தவாய் | obstructed place | Scan 310 printed gloss `தடைப்பட்ட இடம்`. |
| செறாது | not joined with hostility | Scan 321 printed gloss `பகையோடு பொருந்தாத`. |
| செற்றார் | enemy | Scan 321 printed gloss `பகைவர்`. |
| உறாஅர் | outsider | Scan 321 printed gloss `அயலார்`. |

## Part 003 GR3 reconciliation record — scans 289–321

GR3 processed **33 consecutive pages: scans 289–321 / printed 272–304**.

- scans **289–321** — glossary / recurring-terminology reconciliation **PASS, 33/33**;
- all **17** Chapter/Kural metadata records in the range were checked against their audited Tamil counterparts with **0 chapter-number, Kural-number, or controlled-label mismatches**;
- Part-003-first chapter controls added in this gate: **Renunciation** (`துறவு`) and **Cherishing Kindred** (`சுற்றந் தழால்`);
- source-form variants `அவர் வயின் விதும்பல்`, `கனவு நிலை உரைத்தல்`, and `ஆள்வினை உடைமை` are mapped to the established controls **Longing for His Return**, **Speaking of the Dream State**, and **Diligent Effort** rather than creating duplicate English chapter titles;
- recurring narrative/name controls were recorded for **Ponni, Thamarai, Mukilan, Mullai-kodi, Thirumagal, Moodevi, Thingal, Sevvai, Ezhini, Kolli, Vanchikkodi, Kaali, Kadamban,** and **Seyizhai**;
- the existing `கார்மேகம்` → **Karmegam** control required one terminology correction locus across English scans **313–314**: **Kaarmegam → Karmegam**; both pages remain `source-checked`;
- context review confirmed scan **298** `கேள்வி` is the common noun **question**, not Chapter 42 **Listening**; scan **303** `மாங்கனி` is the descriptive **mango**, not the personal name Maangani; scan **310** `செங்கோல்` is naturally the sceptre/justice image; scan **312** `ஏந்திழை` is descriptive **slender maiden**, not a forced proper name; and scan **318** `உரை` / `வீரன்` are ordinary **speech** / **warrior** uses;
- source-printed lexical glosses on scans **293, 310, and 321** are recorded above without importing external meanings;
- English page wording changes during GR3: **2 files — scans 313 and 314, proper-name transliteration only**;
- page status changes during GR3: **0**; all 33 pages remain `source-checked`;
- Tamil page / metadata changes during GR3: **0**;
- no external/published/web English terminology or remembered Kural wording was imported.

'''
g=must_replace(g,review,gr3+review,'insert GR3 record',1)
gp.write_text(g,encoding='utf-8')

# 3) Translation status: advance durable frontier.
sp=EN/'TRANSLATION_STATUS.md'; s=sp.read_text(encoding='utf-8')
s=s.replace('- glossary reconciliation: **IN PROGRESS — GR1 COMPLETE 33/111**;','- glossary reconciliation: **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**;')
s=must_replace(s,'- cumulative glossary reconciliation: **66/111**;','- cumulative glossary reconciliation: **99/111**;','status cumulative',1)
s=must_replace(s,'- remaining glossary-reconciliation pages: **45**;','- remaining glossary-reconciliation pages: **12**;','status remaining',1)
s=must_replace(s,'- English page wording changes during GR1+GR2: **0**;','- English page wording changes during GR1+GR2: **0**; GR3: **2 page files (scans 313–314), `Kaarmegam` → `Karmegam` only**;','status wording',1)
s=must_replace(s,'- page status changes during GR1+GR2: **0**;','- page status changes during GR1+GR2+GR3: **0**;','status page status',1)
s=must_replace(s,'- Tamil page / metadata changes during GR1+GR2: **0**.','- Tamil page / metadata changes during GR1+GR2+GR3: **0**.','status Tamil',1)
old='GR2 checked all **16** Chapter/Kural metadata records in scans **256–288** with **0 numeric or controlled-label mismatches**. Six Part-003-first chapter controls were added: **Poverty**, **Self-Control**, **Renouncing Modesty**, **Good Conduct**, **Knowing One\'s Strength**, and **Seeking the Support of the Great**. Existing controls were extended to the source forms `காதற்சிறப்புரைத்தல்`, `கனவுநிலை உரைத்தல்`, and `அவர்வயின்விதும்பல்`. Contextual controls were refined for `பாவம்`, `தேன்மொழி`, and descriptive `புணர்ச்சி மகிழ்தல்`, and recurring GR2 narrative/literary names were recorded. No English page wording required correction.'
new=old+'\n\nGR3 checked all **17** Chapter/Kural metadata records in scans **289–321** with **0 numeric or controlled-label mismatches**. It added **Renunciation** and **Cherishing Kindred**, mapped three source-form variants to established chapter controls, recorded recurring GR3 names and the source-printed lexical glosses on scans **293, 310, and 321**, and reconciled `கார்மேகம்` to the existing **Karmegam** spelling on English scans **313–314**. No page status or Tamil record changed.'
s=must_replace(s,old,new,'status GR3 summary',1)
start='## Current frontier — Part 003 English glossary reconciliation GR3'
if start not in s: raise SystemExit('status frontier heading missing')
prefix=s.split(start,1)[0]
tail='Part 004 remains blocked until Part 003 completes glossary reconciliation, editorial review, Part review, release report/release-ready synchronization and the final Part closure checkpoint.'
if tail not in s: raise SystemExit('status Part004 tail missing')
suffix=s.split(tail,1)[1]
front='''## Current frontier — Part 003 English glossary reconciliation GR4

Exact next activity: **glossary / recurring-terminology reconciliation scans 322–333 / printed 305–316 — final 12 page-aligned records**.

Compare recurring names, work/section names, controlled literary terms, publication names, chapter labels, citation metadata and repeated English renderings against `GLOSSARY.md` and audited Tamil context. Update `GLOSSARY.md` only for terms actually evidenced in the active source. Do not mechanically force one English word where context requires a different rendering, and do not import terminology from external editions, web sources or memory.

This gate does **not** promote `source-checked` pages to `editorial-reviewed`; passing pages remain `source-checked` until the later editorial-review gate. If GR4 passes, glossary reconciliation becomes **111/111 COMPLETE / CLOSED** and the exact next gate is **Part 003 English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**. Do not begin editorial review during GR4.

'''
s=prefix+front+tail+suffix
sp.write_text(s,encoding='utf-8')

# 4) Synchronize current-frontier control documents. Keep historical gate records intact.
def update_doc(path,repls):
    p=Path(path); t=p.read_text(encoding='utf-8')
    for old,new in repls:
        if old in t: t=t.replace(old,new)
    p.write_text(t,encoding='utf-8')

update_doc('HANDOVER.md',[
('Last refreshed for Kuraloviyam **Part 003 Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check CLOSED; glossary GR1 COMPLETE 33/111, GR2 next**','Last refreshed for Kuraloviyam **Part 003 Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check CLOSED; glossary GR1–GR3 COMPLETE / PASS 99/111, GR4 next**'),
('- English glossary reconciliation: **IN PROGRESS — GR1 + GR2 COMPLETE / PASS, 66/111**;','- English glossary reconciliation: **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**;'),
('- GR1+GR2 changed no English page wording or status and no Tamil record.','- GR1+GR2 changed no English page wording; GR3 changed only `Kaarmegam` → `Karmegam` on English scans 313–314; no status or Tamil record changed.'),
('Perform **Part 003 English Glossary Reconciliation GR3 — scans 289–321 / printed 272–304, 33 pages**.','Perform **Part 003 English Glossary Reconciliation GR4 — scans 322–333 / printed 305–316, final 12 pages**.'),
('If GR3 passes, cumulative glossary reconciliation becomes **99/111** and GR4 is the final **12-page remainder scans 322–333 / printed 305–316**.','If GR4 passes, glossary reconciliation becomes **111/111 COMPLETE / CLOSED** and the next gate is **English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**.')])

update_doc('KURALOVIYAM_ARCHIVAL_GUIDELINES.md',[
('English glossary reconciliation: **IN PROGRESS — GR1 + GR2 COMPLETE / PASS, 66/111**;','English glossary reconciliation: **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**;'),
('Perform **Part 003 English glossary reconciliation GR3 — scans 289–321 / printed 272–304, 33 page-aligned records**.','Perform **Part 003 English glossary reconciliation GR4 — scans 322–333 / printed 305–316, final 12 page-aligned records**.'),
('If GR3 passes, cumulative glossary reconciliation becomes **99/111** and the final GR4 remainder is **scans 322–333 / printed 305–316, 12 pages**.','If GR4 passes, glossary reconciliation becomes **111/111 COMPLETE / CLOSED**; the next gate is **English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**.')])

update_doc('NEXT_CHAT_PROMPT_KURALOVIYAM.md',[
('- glossary reconciliation: **NEXT / not-started**.','- glossary reconciliation: **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**.'),
('## Glossary reconciliation results through GR2 — COMPLETE / PASS','## Glossary reconciliation results through GR3 — COMPLETE / PASS'),
('- cumulative glossary reconciliation **66/111**;','- cumulative glossary reconciliation **99/111**;'),
('- GR1+GR2 page wording changes **0**; page status changes **0**; Tamil changes **0**.','- GR1+GR2 page wording changes **0**; GR3 wording changes **2 English files (scans 313–314), `Kaarmegam` → `Karmegam` only**; page status changes **0**; Tamil changes **0**.'),
('## Exact next activity — Part 003 English Glossary Reconciliation GR3','## Exact next activity — Part 003 English Glossary Reconciliation GR4'),
('Process **scans 289–321 / printed 272–304 — 33 page-aligned records**.','Process **scans 322–333 / printed 305–316 — final 12 page-aligned records**.'),
('glossary reconciliation **66/111**','glossary reconciliation **99/111**'),
('English records **0289–0321**','English records **0322–0333**'),
('during GR3','during GR4'),
('If GR3 passes, cumulative glossary reconciliation becomes **99/111**. GR4 is then the final **12-page remainder scans 322–333 / printed 305–316**.','If GR4 passes, glossary reconciliation becomes **111/111 COMPLETE / CLOSED**. The next gate is **English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**.')])

update_doc('works/kuraloviyam/HANDOVER.md',[
('- glossary reconciliation: **NEXT / not-started**;','- glossary reconciliation: **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**;'),
('## Glossary reconciliation progress — GR2 COMPLETE / PASS 66/111','## Glossary reconciliation progress — GR3 COMPLETE / PASS 99/111'),
('- cumulative glossary reconciliation: **66/111**;','- cumulative glossary reconciliation: **99/111**;'),
('- all English pages remain `source-checked`; GR1+GR2 made **0 English page wording changes / 0 status changes**;','- all English pages remain `source-checked`; GR1+GR2 made **0 English page wording changes**; GR3 changed only **`Kaarmegam` → `Karmegam` on scans 313–314**; status changes remain **0**;'),
('## Exact next activity — English Glossary Reconciliation GR3','## Exact next activity — English Glossary Reconciliation GR4'),
('Process **scans 289–321 / printed 272–304 — 33 PAGE-ALIGNED RECORDS**.','Process **scans 322–333 / printed 305–316 — final 12 PAGE-ALIGNED RECORDS**.'),
('glossary reconciliation remains **66/111 COMPLETE**','glossary reconciliation remains **99/111 COMPLETE**'),
('during GR3','during GR4'),
('If GR3 passes, cumulative glossary reconciliation becomes **99/111** and GR4 is the final **12-page remainder scans 322–333 / printed 305–316**.','If GR4 passes, glossary reconciliation becomes **111/111 COMPLETE / CLOSED** and the next gate is **English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**.')])

update_doc('works/kuraloviyam/README.md',[
('glossary reconciliation IN PROGRESS — GR1 + GR2 COMPLETE / PASS, 66/111; GR3 next','glossary reconciliation IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111; GR4 next'),
('Part 003 English glossary reconciliation GR3 — scans 289–321 / printed 272–304, 33 pages','Part 003 English glossary reconciliation GR4 — scans 322–333 / printed 305–316, final 12 pages')])

update_doc('works/kuraloviyam/indexes/page-map.md',[
('| 003 | 223–333 | 1–111 | scan 223 / printed 206 through scan 333 / printed 316 | **SOURCE INTAKE + Pass 1 + Pass 2A + Pass 2B + Pass 3 COMPLETE — 111/111; Part audit PASS; final metadata/status sync PASS / CLOSED — 111 textual + 111 visual verified; documentation sync COMPLETE; Tamil archival-ready NEXT** |','| 003 | 223–333 | 1–111 | scan 223 / printed 206 through scan 333 / printed 316 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check COMPLETE / CLOSED; glossary GR1 + GR2 + GR3 COMPLETE / PASS — 99/111; GR4 next** |'),
('English glossary reconciliation — **IN PROGRESS: GR1 + GR2 COMPLETE / PASS, 66/111**;','English glossary reconciliation — **IN PROGRESS: GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**;'),
('GLOSSARY RECONCILIATION IN PROGRESS — GR1 + GR2 COMPLETE / PASS, 66/111.','GLOSSARY RECONCILIATION IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111.'),
('Exact next activity: **Part 003 English glossary reconciliation GR3 — scans 289–321 / printed 272–304, 33 pages**. If GR3 passes, cumulative glossary reconciliation becomes **99/111** and GR4 is the final **12-page remainder scans 322–333 / printed 305–316**.','Exact next activity: **Part 003 English glossary reconciliation GR4 — scans 322–333 / printed 305–316, final 12 pages**. If GR4 passes, glossary reconciliation becomes **111/111 COMPLETE / CLOSED** and the next gate is **English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**.')])

update_doc('works/kuraloviyam/metadata/source.md',[
('glossary reconciliation IN PROGRESS — GR1 + GR2 COMPLETE / PASS, 66/111; GR3 next','glossary reconciliation IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111; GR4 next'),
('GR2 scans 256–288 / printed 239–271 COMPLETE 33/33**, cumulative **66/111**. The exact next glossary batch is **GR3 scans 289–321 / printed 272–304**.','GR2 scans 256–288 / printed 239–271 COMPLETE 33/33** and **GR3 scans 289–321 / printed 272–304 COMPLETE 33/33**, cumulative **99/111**. The exact next glossary batch is **GR4 scans 322–333 / printed 305–316, final 12 pages**.')])

update_doc('works/kuraloviyam/translations/en/README.md',[
('- glossary reconciliation: **IN PROGRESS — GR1 COMPLETE 33/111**;','- glossary reconciliation: **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**;'),
('- GR2 **256–288 / 239–271 — COMPLETE / PASS 33/33**;\n- cumulative glossary reconciliation: **66/111**;\n- English pages remain **111 `source-checked`**; GR1+GR2 made **0 page wording changes and 0 status changes**.','- GR2 **256–288 / 239–271 — COMPLETE / PASS 33/33**;\n- GR3 **289–321 / 272–304 — COMPLETE / PASS 33/33**;\n- cumulative glossary reconciliation: **99/111**;\n- English pages remain **111 `source-checked`**; GR1+GR2 made **0 page wording changes**; GR3 changed only **`Kaarmegam` → `Karmegam` on scans 313–314**; status changes remain **0**.'),
('Exact next activity: **Part 003 English glossary reconciliation GR3 — scans 289–321 / printed 272–304, 33 pages**.','Exact next activity: **Part 003 English glossary reconciliation GR4 — scans 322–333 / printed 305–316, final 12 pages**.'),
('If GR3 passes, cumulative glossary reconciliation becomes **99/111** and the final GR4 remainder is **scans 322–333 / printed 305–316, 12 pages**.','If GR4 passes, glossary reconciliation becomes **111/111 COMPLETE / CLOSED** and the next gate is **English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**.')])

print('GR3 completion edits prepared')
