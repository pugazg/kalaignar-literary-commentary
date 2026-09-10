from pathlib import Path
import re

ROOT = Path('works/kuraloviyam')
EN = ROOT / 'translations/en/pages'
TA = ROOT / 'pages'
GLOSSARY = ROOT / 'translations/en/GLOSSARY.md'
OUT = Path('.github/tmp/kuraloviyam-part003-gr1-audit.txt')
FINDINGS = Path('.github/tmp/kuraloviyam-part003-gr1-findings.txt')

TAMIL_RANGE = r'\u0B80-\u0BFF'


def strip_md(s: str) -> str:
    return s.replace('`', '').replace('**', '').strip()


def parse_glossary():
    rows = []
    for line in GLOSSARY.read_text(encoding='utf-8').splitlines():
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 2:
            continue
        ta, en = strip_md(cells[0]), strip_md(cells[1])
        if ta.lower() == 'tamil' or set(ta) <= {'-', ':'}:
            continue
        rows.append((ta, en))
    return rows


def variants(cell: str):
    return [p.strip() for p in re.split(r'\s*/\s*', cell) if p.strip()]


def occurs_as_term(text: str, term: str) -> bool:
    return re.search(rf'(?<![{TAMIL_RANGE}]){re.escape(term)}(?![{TAMIL_RANGE}])', text) is not None


def default_candidates(cell: str):
    vals = []
    for part in re.split(r'\s*/\s*', cell):
        part = re.sub(r'\s*\([^)]*\)\s*', ' ', part).strip()
        if part:
            vals.append(part)
    return vals


def parse_ta_chapter(line: str):
    m = re.search(r'அதிகாரம்\s*-\s*(\d+)\s*-\s*([^;]+);\s*பாடல்கள்?\s*-\s*(.+)$', line)
    if not m:
        return None
    return m.group(1), m.group(2).strip(), m.group(3).strip()


def parse_en_chapter(line: str):
    m = re.search(r'^Chapter\s+(\d+)\s+—\s+([^;]+);\s+Kurals?\s+(.+)$', line)
    if not m:
        return None
    return m.group(1), m.group(2).strip(), m.group(3).strip()


glossary = parse_glossary()
glossary_map = {}
for ta_cell, en_cell in glossary:
    for v in variants(ta_cell):
        glossary_map[v] = en_cell

chapter_findings = []
chapter_flags = []
term_hits = []
possible_misses = []

for scan in range(223, 256):
    printed = scan - 17
    ta_path = TA / f'{scan:04d}-kuraloviyam-{printed}.md'
    en_path = EN / f'{scan:04d}-kuraloviyam-{printed}.md'
    if not ta_path.exists() or not en_path.exists():
        raise SystemExit(f'missing page pair {scan}')
    ta = ta_path.read_text(encoding='utf-8')
    en = en_path.read_text(encoding='utf-8')
    if 'status: "verified"' not in ta:
        raise SystemExit(f'Tamil status not verified scan {scan}')
    if 'status: "source-checked"' not in en:
        raise SystemExit(f'English status not source-checked scan {scan}')
    if 'source_tamil_status: "verified"' not in en:
        raise SystemExit(f'English Tamil-source status mismatch scan {scan}')

    ta_metas = [ln.strip() for ln in ta.splitlines() if 'அதிகாரம்' in ln and ('பாடல்' in ln or 'பாடல்கள்' in ln)]
    en_metas = [ln.strip() for ln in en.splitlines() if ln.startswith('Chapter ') and ('Kural ' in ln or 'Kurals ' in ln)]
    chapter_findings.append((scan, ta_metas, en_metas))
    if len(ta_metas) != len(en_metas):
        chapter_flags.append((scan, f'metadata count TA={len(ta_metas)} EN={len(en_metas)}'))
    for i, (tl, el) in enumerate(zip(ta_metas, en_metas), start=1):
        tp, ep = parse_ta_chapter(tl), parse_en_chapter(el)
        if not tp or not ep:
            chapter_flags.append((scan, f'could not parse pair {i}: {tl} || {el}'))
            continue
        tnum, tlabel, tkural = tp
        enum, elabel, ekural = ep
        if tnum != enum or tkural != ekural:
            chapter_flags.append((scan, f'metadata numeric mismatch pair {i}: {tl} || {el}'))
        default = glossary_map.get(tlabel)
        if default:
            candidates = default_candidates(default)
            if candidates and not any(elabel.lower() == c.lower() for c in candidates):
                chapter_flags.append((scan, f'chapter label {tlabel} => {elabel}; glossary default {default}'))

    for ta_cell, en_cell in glossary:
        hit_variant = next((v for v in variants(ta_cell) if v and occurs_as_term(ta, v)), None)
        if not hit_variant:
            continue
        term_hits.append((scan, hit_variant, en_cell))
        cands = default_candidates(en_cell)
        if cands and not any(c.lower() in en.lower() for c in cands):
            possible_misses.append((scan, hit_variant, en_cell))

lines = [
    'KURALOVIYAM PART 003 ENGLISH GR1 AUDIT',
    'Range: scans 223-255 / printed 206-238',
    'Expected page status: source-checked',
    '',
    'CHAPTER / KURAL METADATA IN RANGE',
]
for scan, ta_metas, en_metas in chapter_findings:
    for i, tl in enumerate(ta_metas):
        el = en_metas[i] if i < len(en_metas) else '[missing]'
        lines.append(f'{scan}: TA {tl}')
        lines.append(f'     EN {el}')
lines.extend(['', 'CHAPTER METADATA / CONTROLLED-LABEL FLAGS'])
if chapter_flags:
    for scan, msg in chapter_flags:
        lines.append(f'{scan}: {msg}')
else:
    lines.append('[none]')
lines.extend(['', 'GLOSSARY TERMS EVIDENCED IN RANGE'])
seen = set()
for item in term_hits:
    if item not in seen:
        seen.add(item)
        lines.append(f'{item[0]}: {item[1]} => {item[2]}')
lines.extend(['', 'POSSIBLE CONTEXT/DEFAULT MISMATCHES FOR MANUAL REVIEW'])
seen = set()
for item in possible_misses:
    if item not in seen:
        seen.add(item)
        lines.append(f'{item[0]}: {item[1]} => expected/context default {item[2]}')
if not possible_misses:
    lines.append('[none]')

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')

f = [
    'KURALOVIYAM PART 003 ENGLISH GR1 — COMPACT FINDINGS',
    f'pages audited: 33',
    f'chapter/Kural metadata lines: {sum(len(t) for _, t, _ in chapter_findings)}',
    f'chapter/control flags: {len(chapter_flags)}',
    f'glossary term hits: {len(term_hits)}',
    f'possible context/default flags: {len(possible_misses)}',
    '',
    'CHAPTER FLAGS:',
]
if chapter_flags:
    for scan, msg in chapter_flags:
        f.append(f'{scan}: {msg}')
else:
    f.append('[none]')
f.extend(['', 'TERM FLAGS:'])
seen = set()
for item in possible_misses:
    if item not in seen:
        seen.add(item)
        f.append(f'{item[0]}: {item[1]} => {item[2]}')
if not possible_misses:
    f.append('[none]')
FINDINGS.write_text('\n'.join(f) + '\n', encoding='utf-8')
print(FINDINGS.read_text(encoding='utf-8'))