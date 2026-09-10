from pathlib import Path
import re

ROOT=Path('works/kuraloviyam')
EN=ROOT/'translations/en'

def must_replace(text, old, new, label, count=1):
    n=text.count(old)
    if n != count:
        raise SystemExit(f'{label}: expected {count} occurrence(s), found {n}: {old[:120]!r}')
    return text.replace(old,new)

def write(path,text):
    Path(path).write_text(text,encoding='utf-8')

# 1) GR4 controlled chapter-label corrections only; statuses remain source-checked.
page_fixes=[
    (EN/'pages/0327-kuraloviyam-310.md',
     'Chapter 109 — Bewilderment at Her Beauty; Kural 1083',
     'Chapter 109 — The Bewildering Power of Beauty; Kural 1083'),
    (EN/'pages/0331-kuraloviyam-314.md',
     'Chapter 4 — Affirming Virtue; Kural 35',
     'Chapter 4 — The Insistence on Virtue; Kural 35'),
]
for p,old,new in page_fixes:
    s=p.read_text(encoding='utf-8')
    if s.count('status: "source-checked"') != 1:
        raise SystemExit(f'{p}: unexpected status state')
    s=must_replace(s,old,new,f'page correction {p}',1)
    p.write_text(s,encoding='utf-8')

# 2) Glossary — add only source-evidenced GR4 controls and durable reconciliation record.
gp=EN/'GLOSSARY.md'; g=gp.read_text(encoding='utf-8')
if '## Part 003 GR4 reconciliation record — scans 322–333' in g:
    raise SystemExit('GR4 glossary record already exists')
g=must_replace(g,
    '## Thirukkural chapter labels first encountered in Part 003 through GR3',
    '## Thirukkural chapter labels first encountered in Part 003 through GR4',
    'glossary Part003 chapter heading',1)
anchor='| ஆள்வினை உடைமை | Diligent Effort | Chapter 62 source-form variant on scan 302; maps to the established controlled label. |'
addition=anchor+'\n| நன்றியில் செல்வம் | Wealth Without Beneficence | Chapter 101 label on scan 329. |\n| வெருவந்த செய்யாமை | Avoiding Tyrannical Severity | Chapter 57 label on scan 333. |'
g=must_replace(g,anchor,addition,'GR4 chapter controls',1)

review='## Review rule\n\nNew recurring terms should be added only when actually encountered in audited Tamil records. Do not pre-populate the glossary from external editions or general Thirukkural terminology.'
gr4='''## Part 003 GR4 additional narrative/name and context controls

| Tamil | Default English form | Editorial note |
|---|---|---|
| தமிழறிஞர் மு. வரதராசனார் | Tamil scholar Mu. Varadarasanar | Named commentator cited in the classroom / `வலியறிதல்` discussion on scan 323. |
| இராமன் | Iraaman | Modern household character across scans 324–325. Keep distinct from the Ramayana figure `இராமன்` → **Rama** established on scan 272. |
| அன்னம் | Annam | Iraaman's wife in the chastity vignette across scans 324–325. |
| அமுதம் | Amudham | Iraaman's office colleague in the chastity vignette across scans 324–325. |
| கண்ணன் | Kannan | Neighbour named in the note on scan 325. |
| கற்பு | chastity | Ethical/social noun central to scans 324–325; do not force this rendering onto unrelated senses of `நிறை`. |
| இனியன் | Iniyan | Ezhini's friend in the market / Yama vignette across scans 326–327. |
| எமன் | Yama / Death | Context-aware. Use **Yama** for the named mythic personification in the narrative; the quoted Kural's compressed death-image may naturally use **Death**. |
| திங்கள் சந்தை | Monday market | Scans 326–327. `திங்கள்` here is the weekday Monday, not a monthly-frequency expression. |
| அழுக்காறு | envy | Scan 331 explicitly explains the ethical term as jealousy at another person's prosperity, praise, intelligence, courage or firmness; the narrative also exploits the sound as a figurative river-name. |

## Part 003 GR4 reconciliation record — scans 322–333

GR4 processed the **final 12 consecutive pages: scans 322–333 / printed 305–316**.

- scans **322–333** — glossary / recurring-terminology reconciliation **PASS, 12/12 / FINAL REMAINDER**;
- all **6** Chapter/Kural metadata records in the range were checked against their audited Tamil counterparts; chapter/Kural numbers were correct in all six;
- two pre-existing controlled chapter labels required English reconciliation: scan **327** Chapter 109 `தகையணங்குறுத்தல்` **Bewilderment at Her Beauty → The Bewildering Power of Beauty**, and scan **331** Chapter 4 `அறன் வலியுறுத்தல்` **Affirming Virtue → The Insistence on Virtue**;
- Part-003-first chapter controls added in this final gate: **Wealth Without Beneficence** (`நன்றியில் செல்வம்`, Chapter 101, scan 329) and **Avoiding Tyrannical Severity** (`வெருவந்த செய்யாமை`, Chapter 57, scan 333);
- existing controls reused unchanged include **Knowing One's Strength** (Chapter 48) and **The Worth of a Life-Partner** (Chapter 6);
- context controls recorded for **Mu. Varadarasanar, Iraaman, Annam, Amudham, Kannan, Iniyan, Yama/Death, Monday market, chastity,** and **envy**;
- the distinct modern character `இராமன்` → **Iraaman** is intentionally kept separate from the earlier Ramayana figure `இராமன்` → **Rama**;
- the already source-checked Monday-market sense on scans **326–327** is retained and now made explicit in the glossary;
- English page wording changes during GR4: **2 files — scans 327 and 331, controlled chapter-label reconciliation only**;
- page status changes during GR4: **0**; all 12 pages remain `source-checked`;
- Tamil page / metadata changes during GR4: **0**;
- internal **332→333** genuine continuation remains preserved and closes within Part 003; external **333→334** remains deferred until Part 004 intake;
- no external/published/web English terminology or remembered Kural wording was imported.

'''
g=must_replace(g,review,gr4+review,'insert GR4 glossary record',1)
gp.write_text(g,encoding='utf-8')

# 3) Authoritative English status — close glossary gate and advance to ER1.
sp=EN/'TRANSLATION_STATUS.md'; s=sp.read_text(encoding='utf-8')
s=must_replace(s,'## Part 003 English glossary reconciliation — IN PROGRESS','## Part 003 English glossary reconciliation — COMPLETE / CLOSED','status heading',1)
s=must_replace(s,'- **GR3: scans 289–321 / printed 272–304 — COMPLETE / PASS 33/33**;','- **GR3: scans 289–321 / printed 272–304 — COMPLETE / PASS 33/33**;\n- **GR4: scans 322–333 / printed 305–316 — COMPLETE / PASS 12/12 / FINAL REMAINDER**;','status GR4 bullet',1)
s=must_replace(s,'- cumulative glossary reconciliation: **99/111**;','- cumulative glossary reconciliation: **111/111 COMPLETE / CLOSED**;','status cumulative',1)
s=must_replace(s,'- remaining glossary-reconciliation pages: **12**;','- remaining glossary-reconciliation pages: **0**;','status remaining',1)
s=must_replace(s,'- English page wording changes during GR1+GR2: **0**; GR3: **2 page files (scans 313–314), `Kaarmegam` → `Karmegam` only**;','- English page wording changes during GR1+GR2: **0**; GR3: **2 page files (scans 313–314), `Kaarmegam` → `Karmegam` only**; GR4: **2 page files (scans 327 and 331), controlled chapter-label reconciliation only**;','status wording',1)
s=must_replace(s,'- page status changes during GR1+GR2+GR3: **0**;','- page status changes during GR1+GR2+GR3+GR4: **0**;','status page states',1)
s=must_replace(s,'- Tamil page / metadata changes during GR1+GR2+GR3: **0**.','- Tamil page / metadata changes during GR1+GR2+GR3+GR4: **0**.','status Tamil',1)
gr3para='GR3 checked all **17** Chapter/Kural metadata records in scans **289–321** with **0 numeric or controlled-label mismatches**. It added **Renunciation** and **Cherishing Kindred**, mapped three source-form variants to established chapter controls, recorded recurring GR3 names and the source-printed lexical glosses on scans **293, 310, and 321**, and reconciled `கார்மேகம்` to the existing **Karmegam** spelling on English scans **313–314**. No page status or Tamil record changed.'
gr4para='''GR4 checked all **6** Chapter/Kural metadata records in scans **322–333**. All chapter/Kural numbers matched the audited Tamil records. Two controlled-label inconsistencies were reconciled: scan **327** Chapter 109 to **The Bewildering Power of Beauty**, and scan **331** Chapter 4 to **The Insistence on Virtue**. It added the Part-003-first chapter controls **Wealth Without Beneficence** and **Avoiding Tyrannical Severity**, recorded final-range source-evidenced names/context controls, and made no page-status or Tamil-record change.

**Part 003 English glossary reconciliation is now COMPLETE / CLOSED — 111/111.**'''
s=must_replace(s,gr3para,gr3para+'\n\n'+gr4para,'status GR4 summary',1)
start='## Current frontier — Part 003 English glossary reconciliation GR4'
end='Part 004 remains blocked until Part 003 completes glossary reconciliation, editorial review, Part review, release report/release-ready synchronization and the final Part closure checkpoint.'
if start not in s or end not in s: raise SystemExit('status frontier markers missing')
prefix=s.split(start,1)[0]
suffix=s.split(end,1)[1]
front='''## Current frontier — Part 003 English Editorial Review ER1

Exact next activity: **editorial review scans 223–255 / printed 206–238 — 33 page-aligned records**.

Review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity. Consult the matching audited Tamil whenever an editorial change could affect meaning. Make only source-faithful editorial improvements. Passing pages may move from `source-checked` to `editorial-reviewed`.

Do not begin Part-level review or release work during ER1. After ER1 passes, the next editorial batch is **ER2 scans 256–288 / printed 239–271, 33 pages**.

'''
s=prefix+front+end+suffix
sp.write_text(s,encoding='utf-8')

# 4) English README — close glossary and advance frontier.
rp=EN/'README.md'; r=rp.read_text(encoding='utf-8')
r=must_replace(r,'## Part 003 English glossary reconciliation — IN PROGRESS','## Part 003 English glossary reconciliation — COMPLETE / CLOSED','EN README heading',1)
r=must_replace(r,'- GR3 **289–321 / 272–304 — COMPLETE / PASS 33/33**;','- GR3 **289–321 / 272–304 — COMPLETE / PASS 33/33**;\n- GR4 **322–333 / 305–316 — COMPLETE / PASS 12/12 / FINAL REMAINDER**;','EN README GR4',1)
r=must_replace(r,'- cumulative glossary reconciliation: **99/111**;','- cumulative glossary reconciliation: **111/111 COMPLETE / CLOSED**;','EN README cumulative',1)
r=must_replace(r,'- English pages remain **111 `source-checked`**; GR1+GR2 made **0 page wording changes**; GR3 changed only **`Kaarmegam` → `Karmegam` on scans 313–314**; status changes remain **0**.','- English pages remain **111 `source-checked`**; GR1+GR2 made **0 page wording changes**; GR3 changed only **`Kaarmegam` → `Karmegam` on scans 313–314**; GR4 changed only the controlled Chapter 109 and Chapter 4 labels on scans **327** and **331**; status changes remain **0**.','EN README wording',1)
r=must_replace(r,'Exact next activity: **Part 003 English glossary reconciliation GR4 — scans 322–333 / printed 305–316, final 12 pages**.','Exact next activity: **Part 003 English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**.','EN README frontier',1)
r=must_replace(r,'Use `GLOSSARY.md` and audited Tamil context to reconcile recurring names, literary/structural terms, publication names, chapter labels, citation metadata and repeated English renderings. Add glossary entries only when evidenced in the active source. This gate does **not** promote pages to `editorial-reviewed`; pages remain `source-checked` until editorial review.','Review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity. Consult audited Tamil whenever an editorial change could affect meaning. Passing pages may move from `source-checked` to `editorial-reviewed`.','EN README instructions',1)
r=must_replace(r,'If GR4 passes, glossary reconciliation becomes **111/111 COMPLETE / CLOSED** and the next gate is **English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.','If ER1 passes, the next editorial batch is **ER2 — scans 256–288 / printed 239–271, 33 pages**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.','EN README next',1)
rp.write_text(r,encoding='utf-8')

# 5) Synchronize current-frontier high-level controls; historical gate evidence remains untouched.
# Guidelines
gdp=Path('KURALOVIYAM_ARCHIVAL_GUIDELINES.md'); d=gdp.read_text(encoding='utf-8')
d=must_replace(d,'- English glossary reconciliation: **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**;','- English glossary reconciliation: **COMPLETE / CLOSED — 111/111**;','guidelines glossary',1)
d=must_replace(d,'Perform **Part 003 English glossary reconciliation GR4 — scans 322–333 / printed 305–316, final 12 page-aligned records**. Use the audited Tamil records and `GLOSSARY.md`; add or refine only source-evidenced terminology; do not import external/published/web wording; do not promote English statuses or begin editorial review; do not alter closed Tamil records.','Perform **Part 003 English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 page-aligned records**. Review readability and consistency against the controlled glossary and audited Tamil context; consult Tamil whenever a change could affect meaning; passing pages may move from `source-checked` to `editorial-reviewed`; do not begin Part-level review or release work during ER1; do not alter closed Tamil records.','guidelines frontier',1)
d=must_replace(d,'If GR4 passes, glossary reconciliation becomes **111/111 COMPLETE / CLOSED**; the next gate is **English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.','If ER1 passes, continue with **English Editorial Review ER2 — scans 256–288 / printed 239–271, 33 pages**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.','guidelines next',1)
gdp.write_text(d,encoding='utf-8')

# Work README simple current-state replacements.
wp=ROOT/'README.md'; w=wp.read_text(encoding='utf-8')
w=w.replace('glossary reconciliation IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111; GR4 next','glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 next')
w=w.replace('GLOSSARY RECONCILIATION IN PROGRESS','GLOSSARY RECONCILIATION CLOSED; EDITORIAL REVIEW NEXT')
w=w.replace('glossary reconciliation **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**','glossary reconciliation **COMPLETE / CLOSED — 111/111**')
w=w.replace('glossary reconciliation: **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**','glossary reconciliation: **COMPLETE / CLOSED — 111/111**')
wp.write_text(w,encoding='utf-8')

# Metadata source and page-map carry only live-state summaries.
for p in [ROOT/'metadata/source.md', ROOT/'indexes/page-map.md']:
    t=p.read_text(encoding='utf-8')
    t=t.replace('glossary reconciliation IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111; GR4 next','glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 next')
    t=t.replace('glossary reconciliation **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**','glossary reconciliation **COMPLETE / CLOSED — 111/111**')
    t=t.replace('glossary reconciliation is now in progress with **GR1 scans 223–255 / printed 206–238 COMPLETE 33/33**, **GR2 scans 256–288 / printed 239–271 COMPLETE 33/33**, and **GR3 scans 289–321 / printed 272–304 COMPLETE 33/33**, cumulative **99/111**. The exact next glossary batch is **GR4 scans 322–333 / printed 305–316**.','glossary reconciliation is **COMPLETE / CLOSED — 111/111** through final GR4 scans **322–333 / printed 305–316**. The exact next English gate is **Editorial Review ER1 scans 223–255 / printed 206–238**.')
    p.write_text(t,encoding='utf-8')

# Root and work handovers: replace maintained-state bullets/frontier text.
for p in [Path('HANDOVER.md'), ROOT/'HANDOVER.md']:
    t=p.read_text(encoding='utf-8')
    t=t.replace('English glossary reconciliation: **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**;','English glossary reconciliation: **COMPLETE / CLOSED — 111/111**;')
    t=t.replace('glossary reconciliation remains **99/111 complete**','glossary reconciliation is **111/111 COMPLETE / CLOSED**')
    t=t.replace('glossary reconciliation remains 99/111 complete','glossary reconciliation is 111/111 COMPLETE / CLOSED')
    t=t.replace('Perform **Part 003 English Glossary Reconciliation GR4 — scans 322–333 / printed 305–316, final 12 pages**.','Perform **Part 003 English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**.')
    t=t.replace('If GR4 passes, glossary reconciliation becomes **111/111 COMPLETE / CLOSED**; the next gate is **English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**.','If ER1 passes, continue with **English Editorial Review ER2 — scans 256–288 / printed 239–271, 33 pages**.')
    t=t.replace('do not promote page statuses or begin editorial review during GR4','review source-faithful readability and consistency; passing pages may move to `editorial-reviewed`; do not begin Part-level review during ER1')
    p.write_text(t,encoding='utf-8')

# Next-chat prompt: make ER1 the executable frontier and preserve the closure facts.
np=Path('NEXT_CHAT_PROMPT_KURALOVIYAM.md'); n=np.read_text(encoding='utf-8')
n=n.replace('## Glossary reconciliation results through GR3 — COMPLETE / PASS','## Glossary reconciliation — COMPLETE / CLOSED')
n=n.replace('- cumulative glossary reconciliation **99/111**;','- GR4 **322–333 / printed 305–316 — 12/12 PASS / FINAL REMAINDER**;\n- cumulative glossary reconciliation **111/111 COMPLETE / CLOSED**;')
n=n.replace('GR1+GR2 page wording changes **0**; GR3 wording changes **2 English files (scans 313–314), `Kaarmegam` → `Karmegam` only**; page status changes **0**; Tamil changes **0**.','GR1+GR2 page wording changes **0**; GR3 wording changes **2 English files (scans 313–314), `Kaarmegam` → `Karmegam` only**; GR4 wording changes **2 English files (scans 327 and 331), controlled chapter-label reconciliation only**; page status changes **0**; Tamil changes **0**.')
start='## Exact next activity — Part 003 English Glossary Reconciliation GR4'
if start not in n: raise SystemExit('next-chat GR4 heading missing')
prefix=n.split(start,1)[0]
new='''## Exact next activity — Part 003 English Editorial Review ER1

Process **scans 223–255 / printed 206–238 — 33 page-aligned records**.

Requirements:

1. fetch live `main` first and preserve newer durable work;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm English drafting, source-check and glossary reconciliation are each **111/111 COMPLETE / CLOSED**;
4. read `translations/en/TRANSLATION_GUIDE.md`, `GLOSSARY.md`, and English records **0223–0255** with their matching audited Tamil records where meaning-sensitive editorial decisions arise;
5. review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity;
6. make only source-faithful editorial improvements; do not import standard/published/web English Kural wording, another edition's terminology, or memory;
7. passing pages may move from `source-checked` to `editorial-reviewed`;
8. do not alter any Tamil page record or Tamil metadata;
9. do not begin Part-level review or release work during ER1;
10. update `TRANSLATION_STATUS.md` and audit the exact changed-file set before advancing.

If ER1 passes, the next activity is **Editorial Review ER2 — scans 256–288 / printed 239–271, 33 pages**. Part 004 remains blocked until Part 003 completes editorial review, Part review, release report/release-ready synchronization and final Part closure. External **333→334** remains deferred until Part 004 source intake.
'''
n=prefix+new
np.write_text(n,encoding='utf-8')

# Validations.
for p in [EN/'pages/0327-kuraloviyam-310.md',EN/'pages/0331-kuraloviyam-314.md']:
    t=p.read_text(encoding='utf-8')
    if t.count('status: "source-checked"') != 1:
        raise SystemExit(f'{p}: status changed unexpectedly')
for p in [Path('HANDOVER.md'),Path('NEXT_CHAT_PROMPT_KURALOVIYAM.md'),ROOT/'HANDOVER.md',EN/'README.md',EN/'TRANSLATION_STATUS.md',Path('KURALOVIYAM_ARCHIVAL_GUIDELINES.md')]:
    t=p.read_text(encoding='utf-8')
    if 'Part 003 English glossary reconciliation GR4' in t or 'Glossary Reconciliation GR4' in t:
        raise SystemExit(f'{p}: stale GR4 frontier remains')

print('GR4 durable changes prepared successfully')
