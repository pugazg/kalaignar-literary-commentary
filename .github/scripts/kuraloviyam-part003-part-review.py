from pathlib import Path
import re
import subprocess

ROOT = Path('.')
TA = ROOT / 'works/kuraloviyam/pages'
EN = ROOT / 'works/kuraloviyam/translations/en/pages'
REVIEWS = ROOT / 'works/kuraloviyam/translations/en/reviews'
REVIEW_BASE = 'ccb0124e5e66defbcb34bfad854d5f213210cc19'


def fm(text: str, path: Path) -> dict:
    lines = text.splitlines()
    if not lines or lines[0] != '---':
        raise RuntimeError(f'{path}: missing front matter start')
    try:
        end = lines.index('---', 1)
    except ValueError:
        raise RuntimeError(f'{path}: missing front matter end')
    out = {}
    for line in lines[1:end]:
        if not line.strip() or ':' not in line:
            continue
        k, v = line.split(':', 1)
        v = v.strip()
        if len(v) >= 2 and v[0] == v[-1] == '"':
            v = v[1:-1]
        out[k.strip()] = v
    return out


def nums(s: str):
    return tuple(int(x) for x in re.findall(r'\d+', s))


def en_meta(text: str, path: Path):
    out = []
    for line in text.splitlines():
        if not line.startswith('Chapter '):
            continue
        m = re.match(r'^Chapter\s+(\d+)\s+—\s+(.+?);\s+Kurals?\s+([0-9,\s]+)\s*$', line)
        if not m:
            raise RuntimeError(f'{path}: unparsed English Chapter/Kural metadata line: {line!r}')
        out.append((int(m.group(1)), m.group(2).strip(), nums(m.group(3))))
    return out


def ta_meta(text: str, path: Path):
    out = []
    for line in text.splitlines():
        if not line.strip().startswith('அதிகாரம்'):
            continue
        m = re.match(r'^\s*அதிகாரம்\s*-\s*(\d+)\s*-\s*(.+?);\s*பாடல்(?:கள்)?\s*-\s*([0-9,\s]+)\s*$', line)
        if not m:
            raise RuntimeError(f'{path}: unparsed Tamil Chapter/Kural metadata line: {line!r}')
        out.append((int(m.group(1)), m.group(2).strip(), nums(m.group(3))))
    return out


def regex_once(text: str, pattern: str, repl: str, label: str, flags=0) -> str:
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise RuntimeError(f'{label}: expected exactly 1 regex match, found {n}')
    return out


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f'{label}: expected exactly 1 match, found {n}')
    return text.replace(old, new, 1)


def replace_tail(path: Path, marker_pattern: str, new_tail: str) -> None:
    text = path.read_text(encoding='utf-8')
    m = re.search(marker_pattern, text, flags=re.M)
    if not m:
        raise RuntimeError(f'{path}: tail marker not found: {marker_pattern!r}')
    path.write_text(text[:m.start()] + new_tail.rstrip() + '\n', encoding='utf-8')


def boundary_text(scan_a: int, scan_b: int) -> str:
    pa = scan_a - 17
    pb = scan_b - 17
    chunks = []
    for base, scan, printed in ((EN, scan_a, pa), (EN, scan_b, pb), (TA, scan_a, pa), (TA, scan_b, pb)):
        p = base / f'{scan:04d}-kuraloviyam-{printed}.md'
        chunks.append(p.read_text(encoding='utf-8').lower())
    return '\n'.join(chunks)


# 1. Exact page inventory and front-matter alignment.
expected_scans = list(range(223, 334))
expected_names = {scan: f'{scan:04d}-kuraloviyam-{scan-17}.md' for scan in expected_scans}

for base, label in ((TA, 'Tamil'), (EN, 'English')):
    actual = {}
    for p in base.glob('*.md'):
        m = re.match(r'^(\d{4})-kuraloviyam-(\d+)\.md$', p.name)
        if not m:
            continue
        scan = int(m.group(1))
        if 223 <= scan <= 333:
            if scan in actual:
                raise RuntimeError(f'{label}: duplicate scan {scan}')
            actual[scan] = p.name
    if set(actual) != set(expected_scans):
        raise RuntimeError(f'{label}: scan inventory mismatch; missing={sorted(set(expected_scans)-set(actual))}; extra={sorted(set(actual)-set(expected_scans))}')
    for scan, name in expected_names.items():
        if actual[scan] != name:
            raise RuntimeError(f'{label}: scan {scan} filename mismatch {actual[scan]!r} != {name!r}')

status_counts = {}
tamil_status_counts = {}
chapter_label_map = {}
metadata_records = 0
metadata_pages = 0
visual_required_pages = []
visual_material_pages = []
nonbody_source_pages = []
block_metadata_pages = []

for scan in expected_scans:
    printed = scan - 17
    name = expected_names[scan]
    ep = EN / name
    tp = TA / name
    et = ep.read_text(encoding='utf-8')
    tt = tp.read_text(encoding='utf-8')
    ef = fm(et, ep)
    tf = fm(tt, tp)

    if ef.get('source_scan_page') != str(scan):
        raise RuntimeError(f'{ep}: source_scan_page mismatch')
    if ef.get('printed_page') != str(printed):
        raise RuntimeError(f'{ep}: printed_page mismatch')
    if ef.get('source_tamil_file') != f'../../../pages/{name}':
        raise RuntimeError(f'{ep}: source_tamil_file mismatch')
    if ef.get('translation_type') != 'project_translation' or ef.get('language') != 'en':
        raise RuntimeError(f'{ep}: translation identity mismatch')
    if ef.get('source_tamil_status') != 'verified':
        raise RuntimeError(f'{ep}: source_tamil_status not verified')
    status_counts[ef.get('status', '<missing>')] = status_counts.get(ef.get('status', '<missing>'), 0) + 1

    if tf.get('scan_page') != str(scan) or tf.get('printed_page') != str(printed):
        raise RuntimeError(f'{tp}: Tamil scan/printed metadata mismatch')
    if tf.get('language') != 'ta':
        raise RuntimeError(f'{tp}: Tamil language mismatch')
    tamil_status_counts[tf.get('status', '<missing>')] = tamil_status_counts.get(tf.get('status', '<missing>'), 0) + 1
    if tf.get('status') != 'verified' or tf.get('visual_fidelity') != 'verified':
        raise RuntimeError(f'{tp}: Tamil archival state is not fully verified')

    em = en_meta(et, ep)
    tm = ta_meta(tt, tp)
    en_numeric = [(c, n) for c, _label, n in em]
    ta_numeric = [(c, n) for c, _label, n in tm]
    if en_numeric != ta_numeric:
        raise RuntimeError(f'scan {scan}: Chapter/Kural numeric mismatch; EN={en_numeric}; TA={ta_numeric}')
    if em:
        metadata_pages += 1
        metadata_records += len(em)
        if not any(line.startswith('> ') for line in et.splitlines()):
            raise RuntimeError(f'{ep}: Chapter/Kural metadata present without separated English blockquote')
        if not any(line.startswith('> ') for line in tt.splitlines()):
            raise RuntimeError(f'{tp}: Chapter/Kural metadata present without separated Tamil blockquote')
        block_metadata_pages.append(scan)
    for chapter, label, _n in em:
        chapter_label_map.setdefault(chapter, set()).add(label)

    note = tf.get('visual_notes', '').lower()
    if any(k in note for k in ('illustration', 'photograph', 'portrait', 'decorative monument', 'facsimile')):
        visual_required_pages.append(scan)
        if '## Visual material' not in et:
            raise RuntimeError(f'{ep}: source visual note requires English Visual material section')
    if '## Visual material' in et:
        visual_material_pages.append(scan)
    if any(k in note for k in ('stamp', 'footer', 'side vertical')):
        nonbody_source_pages.append(scan)
        lo = et.lower()
        if not any(k in lo for k in ('stamp', 'footer', 'side vertical', 'non-body')):
            raise RuntimeError(f'{ep}: source non-body/page-furniture note not represented in English record')

if status_counts != {'editorial-reviewed': 111}:
    raise RuntimeError(f'English status gate failed: {status_counts}')
if tamil_status_counts != {'verified': 111}:
    raise RuntimeError(f'Tamil status gate failed: {tamil_status_counts}')

inconsistent_labels = {c: sorted(v) for c, v in chapter_label_map.items() if len(v) != 1}
if inconsistent_labels:
    raise RuntimeError(f'controlled Chapter label inconsistency: {inconsistent_labels}')

# Explicitly guard known reconciliations from regression.
all_en = '\n'.join((EN / expected_names[s]).read_text(encoding='utf-8') for s in expected_scans)
for forbidden in ('Kaarmegam', 'once a month'):
    if forbidden in all_en:
        raise RuntimeError(f'forbidden/reconciled wording regressed: {forbidden!r}')

# 2. Key cross-page boundary checks. These are durable Part controls, not batch assumptions.
for a, b, kind in ((255, 256, 'clean'), (288, 289, 'genuine'), (321, 322, 'clean'), (322, 323, 'genuine'), (332, 333, 'genuine')):
    text = boundary_text(a, b)
    token = f'{a}→{b}'
    if kind == 'clean':
        if token not in text or 'clean' not in text:
            raise RuntimeError(f'boundary {token}: CLEAN evidence not found in paired records')
    else:
        if not ((token in text and ('genuine' in text or 'continuation' in text)) or f'continuation to scan {b}' in text):
            raise RuntimeError(f'boundary {token}: genuine-continuation evidence not found in paired records')

# Part ending and deferred external boundary.
last_en = (EN / expected_names[333]).read_text(encoding='utf-8')
last_ta = (TA / expected_names[333]).read_text(encoding='utf-8')
if '333→334' not in last_en or 'deferred' not in last_en.lower():
    raise RuntimeError('English scan 333 does not preserve deferred external 333→334 boundary')
if '333→334' not in last_ta or 'deferred' not in last_ta.lower():
    raise RuntimeError('Tamil scan 333 does not preserve deferred external 333→334 boundary')

# 3. Durable Part-level review record.
review_path = REVIEWS / 'PART_003_ENGLISH_REVIEW.md'
if review_path.exists():
    raise RuntimeError(f'{review_path}: already exists; refusing to overwrite')

chapter_count = len(chapter_label_map)
visual_required_count = len(visual_required_pages)
visual_material_count = len(visual_material_pages)
nonbody_count = len(nonbody_source_pages)

review = f'''# Part 003 English Review — Kuraloviyam

## Gate result

**PASS**

This record closes the **Part-level English review** gate for `குறளோவியம்` Part 003 / overall scans **223–333 / printed 206–316**.

Review base: `{REVIEW_BASE}`

The review evaluates the completed project-created English layer as a whole after first-pass drafting, source-check, glossary reconciliation and editorial review. It does not reopen the closed Tamil source pass and it does not promote any page to `release-ready`.

## Authority and controls

The review used:

- the audited Tamil page records under `works/kuraloviyam/pages/`;
- the matching English records under `works/kuraloviyam/translations/en/pages/`;
- `TRANSLATION_GUIDE.md`;
- `GLOSSARY.md`;
- `TRANSLATION_STATUS.md`;
- the completed SC1–SC4, GR1–GR4 and ER1–ER4 durable history;
- `works/kuraloviyam/indexes/page-map.md` for Part structure, page functions and continuity;
- `PART_002_ENGLISH_REVIEW.md` as the structural precedent for this gate.

The closed Part 003 PDF was **not reopened**. No standard Thirukkural wording, published English translation, web text, another commentator or remembered conventional rendering was imported.

## 1. Page presence and alignment — PASS

The Part-level inventory audit confirms:

- Tamil Part 003 page records: **111 / 111 present**;
- English Part 003 page records: **111 / 111 present**;
- scan sequence: **223 through 333 complete**;
- printed-page sequence: **206 through 316 complete**;
- filename alignment: **111 / 111 matching**;
- English `source_tamil_file` links: **111 / 111 exact**;
- missing English page records: **0**;
- extra Part 003 English page records: **0**.

Every English record retains the exact overall-scan and printed-page mapping of its audited Tamil counterpart.

## 2. Final English status state — PASS

Final Part 003 English page statuses before release are:

- `editorial-reviewed`: **111**;
- `source-checked`: **0**;
- `draft`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**;
- `release-ready`: **0**.

Every English page also retains `source_tamil_status: "verified"` and `translation_type: "project_translation"`.

This is the expected pre-release state. No page status is changed during this Part-level review.

## 3. Tamil/source integrity — PASS

The paired Tamil layer remains closed at:

- textual `verified`: **111 / 111**;
- visual fidelity `verified`: **111 / 111**;
- unresolved source-limited or needs-review page records: **0**.

The Part-level English review made no Tamil body, metadata or status change.

## 4. Controlled terminology, names and Kural metadata — PASS

The whole-Part audit found **{metadata_records} Chapter/Kural metadata record(s) across {metadata_pages} English page(s)**, representing **{chapter_count} distinct Chapter number(s)** in Part 003.

For every metadata record:

- English Chapter number matched the audited Tamil `அதிகாரம்` number;
- English Kural number(s) matched the audited Tamil `பாடல்` / `பாடல்கள்` number(s);
- repeated Chapter numbers used one internally consistent controlled English Chapter label;
- Kural text remained separated as Markdown blockquote material from Kalaignar's surrounding prose.

No unresolved controlled-label conflict was found. Previously reconciled distinctions remain intact, including the source-supported **Karmegam** spelling, **Monday market** sense, Part-003 chapter controls, recurring narrative names and context-aware love-poetics terminology.

## 5. Page functions, visual material and non-body material — PASS

The audit found **{visual_required_count} Tamil page record(s)** whose archival notes explicitly identify an illustration/portrait/photograph/facsimile/decorative visual requiring English visual representation. All **{visual_required_count}/{visual_required_count}** carry `## Visual material` in the matching English record.

Across Part 003, **{visual_material_count} English page record(s)** carry an explicit `## Visual material` section. Pages whose Tamil archival notes identify stamps, footer material or side-vertical page furniture were also checked; **{nonbody_count}** such source page record(s) were represented without folding that material into ordinary prose.

Visual descriptions remain factual archival descriptions, not invented captions.

## 6. Cross-page continuity and boundaries — PASS

The accumulated source-check/editorial continuity decisions remain coherent at Part scale. Key durable relationships reconfirmed include:

- incoming **222→223 — CLEAN** from Part 003 intake;
- **255→256 — CLEAN**;
- **288→289 — genuine continuation**, closed on scan 289;
- **321→322 — CLEAN**;
- **322→323 — genuine continuation**;
- **332→333 — genuine continuation**, closed on scan 333.

The review does not treat workflow batch edges as narrative boundaries unless the audited records support that classification.

## 7. Part-ending boundary — DEFERRED EXTERNAL CHECK

Scan **333 / printed 316** closes the final severe-rule / famine vignette and the supplied Part 003 split.

The adjacent **333→334** split boundary remains explicitly **deferred until Part 004 source intake**, because Part 004 has not yet been onboarded as the controlling adjacent source. This review does not infer what begins on scan 334.

The deferred external boundary does not prevent the internally complete Part 003 English review from passing.

## 8. Documentation consistency — PASS

The pre-review controls correctly recorded editorial review as **111/111 COMPLETE / CLOSED** and Part-level review as the next gate. This review found no page-layer contradiction requiring English wording or status remediation.

Post-gate synchronization advances the live controls to record this Part-level review as **PASS / CLOSED** and the **Part 003 English release report** as the exact next gate.

## Final decision

**PART 003 PART-LEVEL ENGLISH REVIEW: PASS**

Part 003 is eligible to proceed to the **Part 003 English release report** gate.

At the end of this review:

- English pages remain **111 `editorial-reviewed`**;
- `release-ready` remains **0/111**;
- no English page wording was changed by the Part-level review;
- no page status was changed by the Part-level review;
- no Tamil page record was changed;
- no external/published/web English wording was imported;
- the internal Part ending at scan 333 is closed;
- external **333→334** remains explicitly deferred until Part 004 intake.

The next gate must create `PART_003_ENGLISH_RELEASE_REPORT.md`, decide release approval, and only then may eligible pages be promoted to `release-ready`.
'''
review_path.parent.mkdir(parents=True, exist_ok=True)
review_path.write_text(review, encoding='utf-8')

# 4. Synchronize live controls to Part-review PASS / release-report next.
path = ROOT / 'HANDOVER.md'
text = path.read_text(encoding='utf-8')
text = regex_once(text, r'^Last refreshed for Kuraloviyam .*$', 'Last refreshed for Kuraloviyam **Part 003 Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary + editorial review COMPLETE / CLOSED 111/111; Part-level English review PASS / CLOSED; release report next**: **2026-09-10**.', 'root HANDOVER headline', flags=re.M)
path.write_text(text, encoding='utf-8')

path = ROOT / 'KURALOVIYAM_ARCHIVAL_GUIDELINES.md'
text = path.read_text(encoding='utf-8')
text = replace_once(text, '- English editorial review: **COMPLETE / CLOSED — 111/111**; current page state **111 editorial-reviewed + 0 source-checked**; Part review / release are not started.', '- English editorial review: **COMPLETE / CLOSED — 111/111**; current page state **111 editorial-reviewed + 0 source-checked**; Part-level English review: **PASS / CLOSED**; release report: **next**.', 'guidelines Part003 English state')
path.write_text(text, encoding='utf-8')
replace_tail(path, r'^### Exact next content stage$', '''### Exact next content stage

Perform the **Part 003 English release report** gate. Use `translations/en/reviews/PART_003_ENGLISH_REVIEW.md` as the authoritative prior gate (**PASS / CLOSED**), confirm all **111** English pages remain `editorial-reviewed`, decide release approval, and if approved promote only the eligible Part-003 English page statuses to `release-ready` without changing approved body wording.

Create `translations/en/reviews/PART_003_ENGLISH_RELEASE_REPORT.md`, audit that page-layer changes are status-token-only, and synchronize final Part-003 English closure controls. External **333→334** remains deferred until Part 004 source intake. Do not begin Part 004 until Part 003 release-ready synchronization and the final Part closure checkpoint are complete.''')

path = ROOT / 'NEXT_CHAT_PROMPT_KURALOVIYAM.md'
text = path.read_text(encoding='utf-8')
text = replace_once(text, '- editorial review: **111/111 COMPLETE / CLOSED**; Part review / release: **not-started**.', '- editorial review: **111/111 COMPLETE / CLOSED**; Part-level English review: **PASS / CLOSED**; release report / release-ready: **not-started**.', 'next prompt durable state')
path.write_text(text, encoding='utf-8')
replace_tail(path, r'^## Exact next activity — Part 003 whole-Part English review$', '''## Exact next activity — Part 003 English release report

Run the **whole-Part release gate for scans 223–333 / printed 206–316 — 111 English records**.

Requirements:

1. fetch live `main` first and preserve newer durable work;
2. read `translations/en/reviews/PART_003_ENGLISH_REVIEW.md` completely and confirm it remains **PASS / CLOSED**;
3. confirm exactly **111 `editorial-reviewed`** pages and zero `source-checked`, `draft`, source-limited, blocked or release-ready pages before promotion;
4. confirm Tamil Part 003 remains **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**;
5. decide release approval from the maintained project workflow only; do not import external/published/web English wording;
6. if approved, promote all 111 eligible English pages from `status: "editorial-reviewed"` to `status: "release-ready"` with **no body-text, Kural, visual-description, metadata-other-than-status, filename or Tamil changes**;
7. create `works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_RELEASE_REPORT.md`;
8. audit the exact page-layer diff and synchronize final Part-003 English closure controls;
9. do not begin Part 004 during the release gate; external **333→334** remains deferred until Part 004 source intake.

If the release gate passes, Part 003 English becomes **111/111 release-ready / RELEASE COMPLETE / CLOSED** and the final Part-003 checkpoint may be synchronized. Only after that closure may Part 004 source intake begin when its controlling source is supplied.''')

path = ROOT / 'works/kuraloviyam/HANDOVER.md'
text = path.read_text(encoding='utf-8')
text = replace_once(text, '- Part review / release: **not-started**.', '- Part-level English review: **PASS / CLOSED**; release report / release-ready: **not-started**.', 'work handover Part review state')
path.write_text(text, encoding='utf-8')
replace_tail(path, r'^## Exact next activity — Part 003 whole-Part English review$', '''## Part 003 Part-level English review — PASS / CLOSED

Durable record: `translations/en/reviews/PART_003_ENGLISH_REVIEW.md`.

Whole-Part checks passed for exact 111/111 Tamil/English inventory and filename alignment, all 111 pre-release English statuses, Chapter/Kural numeric alignment and controlled labels, Kural block separation, visual/non-body page functions, and accumulated continuities through scan 333. No English page wording/status or Tamil record changed during the Part-level review.

## Exact next activity — Part 003 English release report

1. fetch live `main` first;
2. read `translations/en/reviews/PART_003_ENGLISH_REVIEW.md` and confirm **PASS / CLOSED**;
3. confirm all 111 Part-003 English pages remain `editorial-reviewed` and no page is already `release-ready`;
4. if the release decision is approved, promote only `status: "editorial-reviewed"` → `status: "release-ready"` on the 111 eligible English pages;
5. make **0 approved-body, Kural, visual-description, filename or Tamil changes**;
6. create `translations/en/reviews/PART_003_ENGLISH_RELEASE_REPORT.md` and audit the status-only page diff;
7. synchronize final Part-003 English closure controls;
8. keep Part 004 blocked during this gate; external **333→334** remains deferred until Part 004 intake.

After a passing release gate and final Part-003 closure synchronization, Part 004 source intake may begin only when the controlling Part 004 source is supplied.''')

path = ROOT / 'works/kuraloviyam/README.md'
text = path.read_text(encoding='utf-8')
text = regex_once(text, r'^\| 003 \| 223–333 \|.*$', '| 003 | 223–333 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary + editorial review COMPLETE / CLOSED — 111/111; Part-level English review PASS / CLOSED; release report next** |', 'work README Part003 row', flags=re.M)
text = regex_once(text, r'^## Part 003 —.*$', '## Part 003 — TAMIL ARCHIVAL-READY / CLOSED; ENGLISH PRE-RELEASE REVIEW PASS / RELEASE REPORT NEXT', 'work README Part003 heading', flags=re.M)
path.write_text(text, encoding='utf-8')
replace_tail(path, r'^## Current durable state$', '''## Current durable state

- Part 003 Tamil: **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**;
- Part 003 English drafting: **111/111 COMPLETE / CLOSED**;
- Part 003 English source-check: **111/111 COMPLETE / CLOSED**;
- Part 003 English glossary reconciliation: **111/111 COMPLETE / CLOSED**;
- Part 003 English editorial review: **111/111 COMPLETE / CLOSED**;
- Part 003 English Part-level review: **PASS / CLOSED**;
- current Part-003 English state: **111 `editorial-reviewed` / 0 `release-ready` / 0 source-checked / 0 draft / 0 source-limited / 0 blocked**;
- release report / final release-ready synchronization: **not-started**.

## Current frontier

**Next activity: Part 003 English release report.** Use `translations/en/reviews/PART_003_ENGLISH_REVIEW.md` as the passing prior gate. If release is approved, promote the 111 eligible English pages from `editorial-reviewed` to `release-ready` with status-token-only page changes, create `PART_003_ENGLISH_RELEASE_REPORT.md`, and synchronize final Part closure controls.

External **333→334** remains deferred until Part 004 source intake. Do not begin Part 004 during the release gate.''')

path = ROOT / 'works/kuraloviyam/indexes/page-map.md'
text = path.read_text(encoding='utf-8')
text = regex_once(text, r'^\| 003 \| 223–333 \| 1–111 \|.*$', '| 003 | 223–333 | 1–111 | scan 223 / printed 206 through scan 333 / printed 316 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary + editorial review COMPLETE / CLOSED — 111/111; Part-level English review PASS / CLOSED; release report next** |', 'page-map Part003 row', flags=re.M)
path.write_text(text, encoding='utf-8')

path = ROOT / 'works/kuraloviyam/metadata/source.md'
text = path.read_text(encoding='utf-8')
text = regex_once(text, r'^\| 003 \| 223–333 \| 111 \| `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333\.pdf` \|.*$', '| 003 | 223–333 | 111 | `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf` | **supplied; Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary + editorial review COMPLETE / CLOSED — 111/111; Part-level English review PASS / CLOSED; release report next** |', 'source metadata Part003 row', flags=re.M)
start = text.find('Historical Part-003 Pass-1 cadence was')
end = text.find('## Front-matter observations')
if start < 0 or end < 0 or end <= start:
    raise RuntimeError('source metadata live-progress markers not found')
text = text[:start] + '''Historical Part-003 Pass-1 cadence was **11 physical scans per normal iteration**, followed by a one-page final remainder at scan 333. Tamil source intake through archival-ready are closed. The maintained English layer has completed first-pass drafting **111/111**, source-check **111/111**, glossary reconciliation **111/111**, editorial review **111/111**, and the whole-Part English review is **PASS / CLOSED**. The exact next gate is the **Part 003 English release report**; pre-release state remains **111 editorial-reviewed / 0 release-ready**. External **333→334** remains deferred until Part 004 source intake.\n\n''' + text[end:]
path.write_text(text, encoding='utf-8')

path = ROOT / 'works/kuraloviyam/translations/en/README.md'
text = path.read_text(encoding='utf-8')
text = replace_once(text, '- Part review / release: **not-started**.', '- Part-level review: **PASS / CLOSED**; release report / release-ready: **not-started**.', 'English README Part review state')
path.write_text(text, encoding='utf-8')
replace_tail(path, r'^## Current frontier$', '''## Part 003 Part-level English review — PASS / CLOSED

Durable record: `reviews/PART_003_ENGLISH_REVIEW.md`.

The whole-Part gate passed with **111/111** Tamil/English page inventory and filename alignment, exactly **111 `editorial-reviewed`** pre-release pages, controlled Chapter/Kural metadata and labels, Kural-block separation, visual/non-body page-function checks and accumulated continuity checks. The Part-level review changed no English page wording/status and no Tamil record.

## Current frontier

Exact next activity: **Part 003 English release report**.

Use the passing Part-level review as the authoritative prior gate. If release is approved, promote exactly the 111 eligible English page statuses from `editorial-reviewed` to `release-ready` with no approved wording or Tamil changes, create `reviews/PART_003_ENGLISH_RELEASE_REPORT.md`, and audit the page diff as status-token-only.

Part 004 remains blocked until Part 003 release-ready synchronization and final Part closure. External **333→334** remains deferred until Part 004 source intake.''')

path = ROOT / 'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md'
text = path.read_text(encoding='utf-8')
text = replace_once(text, '- Part-level review / release: **not-started**.', '- Part-level review: **PASS / CLOSED**; release report / release-ready: **not-started**.', 'translation status Part review summary')
path.write_text(text, encoding='utf-8')
replace_tail(path, r'^## Current frontier — Part 003 whole-Part English review$', f'''## Part 003 Part-level English review — PASS / CLOSED

Durable record: `works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_REVIEW.md`.

Review base: `{REVIEW_BASE}`.

Whole-Part result:

- Tamil page inventory/alignment: **111/111 PASS**;
- English page inventory/alignment: **111/111 PASS**;
- pre-release English status state: **111 `editorial-reviewed` / 0 release-ready / 0 source-checked / 0 draft / 0 source-limited / 0 blocked**;
- Chapter/Kural metadata alignment: **{metadata_records} record(s) across {metadata_pages} page(s), PASS**;
- controlled Chapter-label consistency: **PASS across {chapter_count} distinct Chapter number(s)**;
- Kural-block separation: **PASS**;
- visual/non-body page functions: **PASS**;
- accumulated continuity and Part ending through scan 333: **PASS**;
- English page wording changes during Part review: **0**;
- English page status changes during Part review: **0**;
- Tamil changes during Part review: **0**.

External **333→334** remains deferred until Part 004 source intake.

## Current frontier — Part 003 English release report

Exact next activity: run the whole-Part release gate for **111 English records, scans 223–333 / printed 206–316**. Read the passing `PART_003_ENGLISH_REVIEW.md`, confirm all pages remain eligible and `editorial-reviewed`, decide release approval, and if approved promote only the page `status` token to `release-ready`. Create `PART_003_ENGLISH_RELEASE_REPORT.md` and verify the page-layer diff contains **111 status-only English page changes, 0 approved-body changes and 0 Tamil changes**.

Do not begin Part 004 during the release gate. Part 004 remains blocked until Part 003 final release-ready synchronization and closure are complete.''')

# Exact durable changed-file gate: review record + nine live controls; no page/Tamil changes.
expected_changed = {
    'HANDOVER.md',
    'KURALOVIYAM_ARCHIVAL_GUIDELINES.md',
    'NEXT_CHAT_PROMPT_KURALOVIYAM.md',
    'works/kuraloviyam/HANDOVER.md',
    'works/kuraloviyam/README.md',
    'works/kuraloviyam/indexes/page-map.md',
    'works/kuraloviyam/metadata/source.md',
    'works/kuraloviyam/translations/en/README.md',
    'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md',
    'works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_REVIEW.md',
}
actual_changed = set(subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines())
if actual_changed != expected_changed:
    raise RuntimeError(f'changed-file gate failed; missing={sorted(expected_changed-actual_changed)}; extra={sorted(actual_changed-expected_changed)}')
if any(p.startswith('works/kuraloviyam/pages/') or p.startswith('works/kuraloviyam/translations/en/pages/') for p in actual_changed):
    raise RuntimeError('Part-level review must not change Tamil or English page records')

print(f'PART003_REVIEW_PASS scans=111 metadata_records={metadata_records} metadata_pages={metadata_pages} chapters={chapter_count} visual_required={visual_required_count} visual_sections={visual_material_count} nonbody_source_pages={nonbody_count} changed_files={len(actual_changed)}')
