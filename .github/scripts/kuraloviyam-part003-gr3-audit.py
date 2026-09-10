from pathlib import Path
import re
from collections import defaultdict

ROOT=Path('works/kuraloviyam')
TA=ROOT/'pages'
EN=ROOT/'translations/en/pages'
GLOSSARY=ROOT/'translations/en/GLOSSARY.md'
OUT=Path('.github/tmp/kuraloviyam-part003-gr3-findings.txt')
TAMIL_RANGE=r'\u0B80-\u0BFF'

def strip_md(s): return s.replace('`','').replace('**','').strip()
def variants(s): return [p.strip() for p in re.split(r'\s*/\s*',s) if p.strip()]
def occurs(text,term): return re.search(rf'(?<![{TAMIL_RANGE}]){re.escape(term)}(?![{TAMIL_RANGE}])',text) is not None

def parse_glossary():
    rows=[]
    for line in GLOSSARY.read_text(encoding='utf-8').splitlines():
        if not line.startswith('|'): continue
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells)<2: continue
        ta,en=strip_md(cells[0]),strip_md(cells[1])
        if ta.lower()=='tamil' or not ta or set(ta)<=set('-:'): continue
        rows.append((ta,en))
    return rows

def candidates(cell):
    vals=[]
    for part in re.split(r'\s*/\s*',cell):
        part=re.sub(r'\s*\([^)]*\)\s*',' ',part).strip()
        if part: vals.append(part)
    return vals

def parse_ta(line):
    try:
        left,right=line.split(';',1)
        m=re.search(r'அதிகாரம்\s*-\s*(\d+)\s*-\s*(.+)$',left.strip())
        if not m or '-' not in right: return None
        return m.group(1),m.group(2).strip(),right.split('-',1)[1].strip()
    except ValueError: return None

def parse_en(line):
    m=re.search(r'^Chapter\s+(\d+)\s+—\s+([^;]+);\s+Kurals?\s+(.+)$',line)
    return (m.group(1),m.group(2).strip(),m.group(3).strip()) if m else None

def snippet(text,term,radius=100):
    i=text.find(term)
    if i<0: return ''
    return ' '.join(text[max(0,i-radius):min(len(text),i+len(term)+radius)].replace('\n',' ').split())

rows=parse_glossary(); gmap={}; english_gloss='\n'.join(e for _,e in rows).lower()
for tc,ec in rows:
    for v in variants(tc): gmap[v]=ec

chapter_flags=[]; missing_labels=[]; metadata=[]; term_flags=[]; term_hits=[]; capitals=defaultdict(set); explicit=[]
stop=set('The A An And Or But If Then So Yet For From To Of In On At By With Without As Is Are Was Were Be Been Being This That These Those It Its He She They We You I His Her Their Our Your My Not No Yes One Two Three Four Five Six Seven Eight Nine Ten Chapter Kural Kurals Source Scan Printed Page English Tamil Part Visual Large Small New Another When While After Before How What Why Who Where Here There Valluvar Thiruvalluvar Kuraloviyam Kalaignar'.split())

for scan in range(289,322):
    printed=scan-17
    tp=TA/f'{scan:04d}-kuraloviyam-{printed}.md'; ep=EN/f'{scan:04d}-kuraloviyam-{printed}.md'
    if not tp.exists() or not ep.exists(): raise SystemExit(f'missing page pair {scan}')
    ta=tp.read_text(encoding='utf-8'); en=ep.read_text(encoding='utf-8')
    if 'status: "verified"' not in ta or 'visual_fidelity: "verified"' not in ta: raise SystemExit(f'Tamil precondition failed {scan}')
    if en.count('status: "source-checked"')!=1 or en.count('source_tamil_status: "verified"')!=1: raise SystemExit(f'English precondition failed {scan}')
    tmeta=[x.strip() for x in ta.splitlines() if 'அதிகாரம்' in x and ('பாடல்' in x or 'பாடல்கள்' in x)]
    emeta=[x.strip() for x in en.splitlines() if x.startswith('Chapter ') and ('Kural ' in x or 'Kurals ' in x)]
    metadata.append((scan,tmeta,emeta))
    if len(tmeta)!=len(emeta): chapter_flags.append((scan,f'count TA={len(tmeta)} EN={len(emeta)}'))
    for tl,el in zip(tmeta,emeta):
        a,b=parse_ta(tl),parse_en(el)
        if not a or not b:
            chapter_flags.append((scan,f'parse: {tl} || {el}')); continue
        tn,tlab,tks=a; enu,elab,eks=b
        if tn!=enu or tks!=eks: chapter_flags.append((scan,f'numeric mismatch: {tl} || {el}'))
        default=gmap.get(tlab)
        if default:
            cs=candidates(default)
            if cs and not any(elab.lower()==c.lower() for c in cs): chapter_flags.append((scan,f'label mismatch {tlab} => {elab}; glossary {default}'))
        else: missing_labels.append((scan,tlab,elab))
    for tc,ec in rows:
        hit=next((v for v in variants(tc) if occurs(ta,v)),None)
        if not hit: continue
        term_hits.append((scan,hit,ec))
        cs=candidates(ec)
        if cs and not any(c.lower() in en.lower() for c in cs): term_flags.append((scan,hit,ec,snippet(ta,hit)))
    body=en.split('---',2)[-1]; body=re.sub(r'<!--.*?-->',' ',body,flags=re.S); body=re.sub(r'`[^`]*`',' ',body)
    for tok in re.findall(r"\b[A-Z][A-Za-z'’-]{2,}\b",body):
        if tok not in stop: capitals[tok].add(scan)
    for ln in ta.splitlines():
        st=ln.strip()
        if st and not st.startswith('<!--') and ('=' in st or 'என்றால்' in st or 'பொருள்' in st): explicit.append((scan,st))

unique=[]; seen=set()
for s,t,e in missing_labels:
    if (t,e) not in seen: seen.add((t,e)); unique.append((s,t,e))

out=['KURALOVIYAM PART 003 ENGLISH GR3 — COMPACT AUDIT FINDINGS','Range: scans 289-321 / printed 272-304','Pages audited: 33','Expected page status: source-checked','', 'CHAPTER / KURAL METADATA']
for scan,tm,em in metadata:
    for i,tl in enumerate(tm): out.append(f'{scan}: {tl} || {em[i] if i<len(em) else "[missing]"}')
out += ['',f'CHAPTER / CONTROL FLAGS: {len(chapter_flags)}'] + ([f'{s}: {m}' for s,m in chapter_flags] or ['[none]'])
out += ['',f'CHAPTER LABELS EVIDENCED BUT NOT YET IN GLOSSARY: {len(unique)}'] + ([f'{s}: {t} => {e}' for s,t,e in unique] or ['[none]'])
out += ['',f'GLOSSARY TERM HITS: {len(term_hits)}',f'POSSIBLE CONTEXT/DEFAULT FLAGS: {len(term_flags)}']
for s,t,e,c in term_flags: out += [f'{s}: {t} => {e}',f'    TA context: {c}']
out += ['','REPEATED CAPITALIZED ENGLISH TOKENS ABSENT FROM GLOSSARY TEXT (manual name/title review)']
for tok,scans in sorted(capitals.items(),key=lambda kv:(-len(kv[1]),kv[0].lower())):
    if len(scans)>=2 and tok.lower() not in english_gloss: out.append(f'{tok}: scans {",".join(map(str,sorted(scans)))}')
out += ['','SOURCE-PRINTED LEXICAL/GLOSS LINES CONTAINING = OR “means” CUES']
out += [f'{s}: {ln}' for s,ln in explicit]
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text('\n'.join(out)+'\n',encoding='utf-8'); print(OUT.read_text(encoding='utf-8'))
