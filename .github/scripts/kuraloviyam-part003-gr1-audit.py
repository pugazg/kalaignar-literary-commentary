from pathlib import Path
import re

ROOT = Path('works/kuraloviyam')
EN = ROOT / 'translations/en/pages'
TA = ROOT / 'pages'
GLOSSARY = ROOT / 'translations/en/GLOSSARY.md'
OUT = Path('.github/tmp/kuraloviyam-part003-gr1-audit.txt')
FINDINGS = Path('.github/tmp/kuraloviyam-part003-gr1-findings.txt')


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


def default_candidates(cell: str):
    vals = []
    for part in re.split(r'\s*/\s*', cell):
        part = re.sub(r'\s*\([^)]*\)\s*', ' ', part).strip()
        if part:
            vals.append(part)
    return vals


glossary = parse_glossary()
chapter_findings = []
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

    ta_meta = next((ln.strip() for ln in ta.splitlines() if 'அதிகாரம்' in ln and ('பாடல்' in ln or 'பாடல்கள்' in ln)), None)
    en_meta = next((ln.strip() for ln in en.splitlines() if ln.startswith('Chapter ') and ('Kural ' in ln or 'Kurals ' in ln)), None)
    if ta_meta or en_meta:
        chapter_findings.append((scan, ta_meta or '[none]', en_meta or '[none]'))

    for ta_cell, en_cell in glossary:
        hit_variant = next((v for v in variants(ta_cell) if v and v in ta), None)
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
for scan, ta_meta, en_meta in chapter_findings:
    lines.append(f'{scan}: TA {ta_meta}')
    lines.append(f'     EN {en_meta}')
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
    f'chapter/Kural metadata records: {len(chapter_findings)}',
    f'glossary term hits: {len(term_hits)}',
    f'possible context/default flags: {len(possible_misses)}',
    '',
    'CHAPTER / KURAL METADATA:',
]
for scan, ta_meta, en_meta in chapter_findings:
    f.append(f'{scan}: {ta_meta} || {en_meta}')
f.extend(['', 'FLAGS:'])
seen = set()
for item in possible_misses:
    if item not in seen:
        seen.add(item)
        f.append(f'{item[0]}: {item[1]} => {item[2]}')
if not possible_misses:
    f.append('[none]')
FINDINGS.write_text('\n'.join(f) + '\n', encoding='utf-8')
print(FINDINGS.read_text(encoding='utf-8'))