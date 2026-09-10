from pathlib import Path
import re
from collections import defaultdict

ROOT = Path('works/kuraloviyam')
TA = ROOT / 'pages'
EN = ROOT / 'translations/en/pages'
GLOSSARY = ROOT / 'translations/en/GLOSSARY.md'
OUT = Path('.github/tmp/kuraloviyam-part003-gr2-findings.txt')
TAMIL_RANGE = r'\u0B80-\u0BFF'


def strip_md(s):
    return s.replace('`','').replace('**','').strip()


def parse_glossary():
    rows=[]
    for line in GLOSSARY.read_text(encoding='utf-8').splitlines():
        if not line.startswith('|'):
            continue
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells)<2:
            continue
        ta,en=strip_md(cells[0]),strip_md(cells[1])
        if ta.lower()=='tamil' or set(ta)<=set('-:'):
            continue
        rows.append((ta,en))
    return rows


def variants(s):
    return [p.strip() for p in re.split(r'\s*/\s*', s) if p.strip()]


def occurs_term(text, term):
    return re.search(rf'(?<![{TAMIL_RANGE}]){re.escape(term)}(?![{TAMIL_RANGE}])', text) is not None


def default_candidates(cell):
    vals=[]
    for part in re.split(r'\s*/\s*', cell):
        part=re.sub(r'\s*\([^)]*\)\s*',' ',part).strip()
        if part:
            vals.append(part)
    return vals


def parse_ta(line):
    try:
        left,right=line.split(';',1)
        m=re.search(r'அதிகாரம்\s*-\s*(\d+)\s*-\s*(.+)$',left.strip())
        if not m or '-' not in right:
            return None
        nums=right.split('-',1)[1].strip()
        return m.group(1),m.group(2).strip(),nums
    except ValueError:
        return None


def parse_en(line):
    m=re.search(r'^Chapter\s+(\d+)\s+—\s+([^;]+);\s+Kurals?\s+(.+)$',line)
    if not m:
        return None
    return m.group(1),m.group(2).strip(),m.group(3).strip()


def snippet(text, term, radius=90):
    i=text.find(term)
    if i<0:
        return ''
    s=max(0,i-radius); e=min(len(text),i+len(term)+radius)
    return ' '.join(text[s:e].replace('\n',' ').split())

rows=parse_glossary()
gmap={}
english_gloss='\n'.join(en for _,en in rows).lower()
for ta_cell,en_cell in rows:
    for v in variants(ta_cell):
        gmap[v]=en_cell

chapter_flags=[]
missing_labels=[]
metadata=[]
term_flags=[]
term_hits=[]
capital_hits=defaultdict(set)
english_by_scan={}

stop=set('The A An And Or But If Then So Yet For From To Of In On At By With Without As Is Are Was Were Be Been Being This That These Those It Its He She They We You I His Her Their Our Your My Not No Yes One Two Three Four Five Six Seven Eight Nine Ten Chapter Kural Kurals Source Scan Printed Page English Tamil Part Visual Large Small New Another When While After Before How What Why Who Where Here There Valluvar Thiruvalluvar Kuraloviyam Kalaignar'.split())

for scan in range(256,289):
    printed=scan-17
    tp=TA/f'{scan:04d}-kuraloviyam-{printed}.md'
    ep=EN/f'{scan:04d}-kuraloviyam-{printed}.md'
    if not tp.exists() or not ep.exists():
        raise SystemExit(f'missing page pair {scan}')
    ta=tp.read_text(encoding='utf-8')
    en=ep.read_text(encoding='utf-8')
    english_by_scan[scan]=en
    if 'status: "verified"' not in ta or 'visual_fidelity: "verified"' not in ta:
        raise SystemExit(f'Tamil status precondition failed {scan}')
    if en.count('status: "source-checked"') != 1 or en.count('source_tamil_status: "verified"') != 1:
        raise SystemExit(f'English source-check precondition failed {scan}')

    tmeta=[ln.strip() for ln in ta.splitlines() if 'அதிகாரம்' in ln and ('பாடல்' in ln or 'பாடல்கள்' in ln)]
    emeta=[ln.strip() for ln in en.splitlines() if ln.startswith('Chapter ') and ('Kural ' in ln or 'Kurals ' in ln)]
    metadata.append((scan,tmeta,emeta))
    if len(tmeta)!=len(emeta):
        chapter_flags.append((scan,f'count TA={len(tmeta)} EN={len(emeta)}'))
    for i,(tl,el) in enumerate(zip(tmeta,emeta),1):
        a,b=parse_ta(tl),parse_en(el)
        if not a or not b:
            chapter_flags.append((scan,f'parse pair {i}: {tl} || {el}'))
            continue
        tn,tlab,tks=a; enu,elab,eks=b
        if tn!=enu or tks!=eks:
            chapter_flags.append((scan,f'numeric mismatch: {tl} || {el}'))
        default=gmap.get(tlab)
        if default:
            cands=default_candidates(default)
            if cands and not any(elab.lower()==c.lower() for c in cands):
                chapter_flags.append((scan,f'label mismatch {tlab} => {elab}; glossary {default}'))
        else:
            missing_labels.append((scan,tlab,elab))

    for ta_cell,en_cell in rows:
        hit=next((v for v in variants(ta_cell) if v and occurs_term(ta,v)),None)
        if not hit:
            continue
        term_hits.append((scan,hit,en_cell))
        cands=default_candidates(en_cell)
        if cands and not any(c.lower() in en.lower() for c in cands):
            term_flags.append((scan,hit,en_cell,snippet(ta,hit)))

    # Capitalized token candidates from body after front matter; repeated across >=2 scans and absent from glossary.
    body=en.split('---',2)[-1]
    body=re.sub(r'<!--.*?-->',' ',body,flags=re.S)
    body=re.sub(r'`[^`]*`',' ',body)
    for tok in re.findall(r"\b[A-Z][A-Za-z'’-]{2,}\b",body):
        if tok in stop:
            continue
        capital_hits[tok].add(scan)

out=[]
out.append('KURALOVIYAM PART 003 ENGLISH GR2 — COMPACT AUDIT FINDINGS')
out.append('Range: scans 256-288 / printed 239-271')
out.append('Pages audited: 33')
out.append('Expected page status: source-checked')
out.append('')
out.append('CHAPTER / KURAL METADATA')
for scan,tmeta,emeta in metadata:
    for i,tl in enumerate(tmeta):
        el=emeta[i] if i<len(emeta) else '[missing]'
        out.append(f'{scan}: {tl} || {el}')
out.append('')
out.append(f'CHAPTER / CONTROL FLAGS: {len(chapter_flags)}')
out.extend([f'{s}: {m}' for s,m in chapter_flags] or ['[none]'])
out.append('')
unique=[]; seen=set()
for s,t,e in missing_labels:
    if (t,e) not in seen:
        seen.add((t,e)); unique.append((s,t,e))
out.append(f'CHAPTER LABELS EVIDENCED BUT NOT YET IN GLOSSARY: {len(unique)}')
out.extend([f'{s}: {t} => {e}' for s,t,e in unique] or ['[none]'])
out.append('')
out.append(f'GLOSSARY TERM HITS: {len(term_hits)}')
out.append(f'POSSIBLE CONTEXT/DEFAULT FLAGS: {len(term_flags)}')
for s,t,e,ctx in term_flags:
    out.append(f'{s}: {t} => {e}')
    out.append(f'    TA context: {ctx}')
out.append('')
out.append('REPEATED CAPITALIZED ENGLISH TOKENS ABSENT FROM GLOSSARY TEXT (manual name/title review)')
for tok,scans in sorted(capital_hits.items(), key=lambda kv:(-len(kv[1]),kv[0].lower())):
    if len(scans)>=2 and tok.lower() not in english_gloss:
        out.append(f'{tok}: scans {",".join(map(str,sorted(scans)))}')
out.append('')
out.append('SOURCE-PRINTED LEXICAL/GLOSS LINES CONTAINING = OR “means” CUES')
for scan in range(256,289):
    printed=scan-17
    ta=(TA/f'{scan:04d}-kuraloviyam-{printed}.md').read_text(encoding='utf-8')
    for ln in ta.splitlines():
        if '=' in ln or 'என்றால்' in ln or 'பொருள்' in ln:
            st=ln.strip()
            if st and not st.startswith('<!--'):
                out.append(f'{scan}: {st}')

OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text('\n'.join(out)+'\n',encoding='utf-8')
print(OUT.read_text(encoding='utf-8'))
