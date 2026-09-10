from pathlib import Path
import subprocess

EN = Path('works/kuraloviyam/translations/en/pages')
TA = Path('works/kuraloviyam/pages')


def run(*args):
    return subprocess.check_output(list(args), text=True).strip()


def replace_once(path, old, new):
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{path}: expected one occurrence, found {count}: {old!r}')
    p.write_text(text.replace(old, new, 1), encoding='utf-8')


def replace_tail(path, heading, new_tail):
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    if heading not in text:
        raise SystemExit(f'{path}: heading not found: {heading!r}')
    p.write_text(text.split(heading, 1)[0] + new_tail, encoding='utf-8')


# Validate the final SC4 range before touching it.
for scan in range(322, 334):
    printed = scan - 17
    en = EN / f'{scan:04d}-kuraloviyam-{printed}.md'
    ta = TA / f'{scan:04d}-kuraloviyam-{printed}.md'
    if not en.exists() or not ta.exists():
        raise SystemExit(f'missing English/Tamil pair for scan {scan}')
    et = en.read_text(encoding='utf-8')
    tt = ta.read_text(encoding='utf-8')
    if f'source_scan_page: {scan}' not in et or f'scan_page: {scan}' not in tt:
        raise SystemExit(f'scan mapping mismatch at {scan}')
    if f'printed_page: "{printed}"' not in et or f'printed_page: "{printed}"' not in tt:
        raise SystemExit(f'printed-page mismatch at {scan}')
    if et.count('status: "draft"') != 1:
        raise SystemExit(f'English page is not exactly one draft at {scan}')
    if et.count('source_tamil_status: "verified"') != 1:
        raise SystemExit(f'English Tamil-source status mismatch at {scan}')
    if tt.count('status: "verified"') != 1 or tt.count('visual_fidelity: "verified"') != 1:
        raise SystemExit(f'Tamil archival precondition failed at {scan}')

# Source-check correction 1 — scan 327: திங்கள் சந்தை is Monday market, not monthly market.
replace_once(
    EN / '0327-kuraloviyam-310.md',
    'Why should the market meet only once a month? What is wrong with having it every day?',
    'Why should the market meet only every Monday? Why not have it every day?'
)

# Source-check correction 2 — scans 328→329: restore the physical-page split exactly.
replace_once(
    EN / '0328-kuraloviyam-311.md',
    'She had no mother, no father, no close kin or relatives. She lived alone in her house. There were many young men in that town who longed, “Will she not stand by the doorway? May we not see her beauty even for a moment and carry away some delight in our hearts?”',
    'She had no mother, no father, no close kin or relatives. She lived alone in her house. “Will she not stand by the doorway? May we not see her beauty even for a moment—'
)
p = EN / '0329-kuraloviyam-312.md'
text = p.read_text(encoding='utf-8')
front = '---\n\n'
pos = text.find(front, text.find('---') + 3)
if pos < 0:
    raise SystemExit('scan 329 front matter close not found')
pos += len(front)
continuation = '—and carry away some delight in our hearts?” There were many young men in that town who yearned for this.\n\n'
if continuation in text:
    raise SystemExit('scan 329 continuation already present unexpectedly')
p.write_text(text[:pos] + continuation + text[pos:], encoding='utf-8')

# Source-check correction 3 — scan 333: preserve non-body side furniture in the English archival note.
replace_once(
    EN / '0333-kuraloviyam-316.md',
    '<!-- Source scan page: 333; printed page: 316; direct continuation from scan 332; closes severe-rule / famine vignette with Chapter 57 / Kural 567; external 333→334 boundary deferred until Part 004 intake -->',
    '<!-- Source scan page: 333; printed page: 316; direct continuation from scan 332; closes severe-rule / famine vignette with Chapter 57 / Kural 567; side vertical title/footer furniture excluded from body text; external 333→334 boundary deferred until Part 004 intake -->'
)

# Promote only after all 12 comparisons have passed.
for scan in range(322, 334):
    printed = scan - 17
    p = EN / f'{scan:04d}-kuraloviyam-{printed}.md'
    text = p.read_text(encoding='utf-8')
    if text.count('status: "draft"') != 1:
        raise SystemExit(f'draft status changed unexpectedly at {scan}')
    p.write_text(text.replace('status: "draft"', 'status: "source-checked"', 1), encoding='utf-8')

expected_pages = {str(EN / f'{scan:04d}-kuraloviyam-{scan-17}.md') for scan in range(322, 334)}
changed = set(run('git', 'diff', '--name-only').splitlines())
if changed != expected_pages:
    raise SystemExit(f'SC4 page changed-file audit failed: {sorted(changed ^ expected_pages)}')

for scan in range(322, 334):
    printed = scan - 17
    p = EN / f'{scan:04d}-kuraloviyam-{printed}.md'
    text = p.read_text(encoding='utf-8')
    if text.count('status: "source-checked"') != 1 or 'status: "draft"' in text:
        raise SystemExit(f'final source-check status failed at {scan}')
    if text.count('source_tamil_status: "verified"') != 1:
        raise SystemExit(f'source Tamil status altered at {scan}')

page_base = run('git', 'rev-parse', 'HEAD')
subprocess.check_call(['git', 'add', *sorted(expected_pages)])
subprocess.check_call(['git', 'commit', '-m', 'kuraloviyam: Source-check Part 003 English scans 322-333'])
page_commit = run('git', 'rev-parse', 'HEAD')

# Synchronize the live English/frontier controls after source-check closure.
replace_once(
    'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md',
    '- source-check: **IN PROGRESS — 99/111 COMPLETE**;',
    '- source-check: **111/111 COMPLETE / CLOSED**;'
)
replace_tail(
    'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md',
    '## Part 003 English source-check — IN PROGRESS\n',
    f'''## Part 003 English source-check — COMPLETE / CLOSED

- **SC1: scans 223–255 / printed 206–238 — COMPLETE 33/33**;
- **SC2: scans 256–288 / printed 239–271 — COMPLETE 33/33**;
- **SC3: scans 289–321 / printed 272–304 — COMPLETE 33/33**;
- **SC4: scans 322–333 / printed 305–316 — COMPLETE 12/12 / FINAL REMAINDER**;
- cumulative source-check: **111/111 COMPLETE / CLOSED**;
- current Part-003 English state: **111 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;
- remaining source-check pages: **0**.

SC4 compared all final 12 English records against their audited Tamil counterparts paragraph-by-paragraph / block-by-block. All **12/12** passed after source-fidelity reconciliation. Corrections were limited to:

- scan **327 / printed 310** — corrected the recurring `திங்கள் சந்தை` reference from the unsupported `once a month` to the source-faithful **Monday market** sense;
- scans **328→329 / printed 311→312** — restored the physical-page split in the doorway/beauty sentence so scan 328 ends where the audited Tamil page ends and scan 329 resumes the sentence;
- scan **333 / printed 316** — recorded the source-visible side vertical title/footer as page furniture excluded from body text, while preserving the genuine **332→333** continuation and Part close.

SC4 page commit: `{page_commit}` — `kuraloviyam: Source-check Part 003 English scans 322-333`.

The SC4 page-only comparison from `{page_base}` to `{page_commit}` contains exactly **12 modified English page records**, scans **322–333**, with no Tamil page or Tamil metadata change. Eight pages changed only by status promotion; four page files also carry the source-fidelity corrections above.

The incoming **321→322 boundary is CLEAN**. The internal **332→333** relationship remains a genuine continuation closed on scan 333. Part 003 ends at scan **333 / printed 316**; external **333→334** remains deferred until Part 004 source intake.

## Current frontier — Part 003 English glossary reconciliation GR1

Exact next activity: **glossary / recurring-terminology reconciliation scans 223–255 / printed 206–238 — 33 page-aligned records**.

Compare recurring names, work/section names, controlled literary terms, publication names, chapter labels, citation metadata and repeated English renderings against `GLOSSARY.md` and the audited Tamil context. Update `GLOSSARY.md` only for terms actually evidenced in Part 003. Do not mechanically force one English word where context requires a different rendering, and do not import terminology from external editions, web sources or memory.

This gate does **not** promote `source-checked` pages to `editorial-reviewed`; passing pages remain `source-checked` until the later editorial-review gate. Do not begin editorial review during GR1.

Part 004 remains blocked until Part 003 completes glossary reconciliation, editorial review, Part review, release report/release-ready synchronization and the final Part closure checkpoint.
'''
)

replace_once(
    'works/kuraloviyam/translations/en/README.md',
    '- source-check: **IN PROGRESS — SC1 + SC2 + SC3 COMPLETE 99/111**;\n- current English state: **99 `source-checked` + 12 `draft` / 0 source-limited / 0 blocked**;\n- glossary reconciliation / editorial review / Part review / release: **not-started**.',
    '- source-check: **111/111 COMPLETE / CLOSED**;\n- current English state: **111 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;\n- glossary reconciliation: **NEXT / not-started**;\n- editorial review / Part review / release: **not-started**.'
)
replace_tail(
    'works/kuraloviyam/translations/en/README.md',
    '## Part 003 English source-check\n',
    f'''## Part 003 English source-check — COMPLETE / CLOSED

- SC1 **223–255 / 206–238 — COMPLETE 33/33**;
- SC2 **256–288 / 239–271 — COMPLETE 33/33**;
- SC3 **289–321 / 272–304 — COMPLETE 33/33**;
- SC4 **322–333 / 305–316 — COMPLETE 12/12 / FINAL REMAINDER**;
- cumulative source-check: **111/111 COMPLETE / CLOSED**;
- current English state: **111 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.

SC4 source-fidelity reconciliation corrected the Monday-market sense on scan **327**, restored exact page alignment across **328→329**, and recorded scan **333** side title/footer furniture as non-body material. No Tamil archival record changed. Incoming **321→322 is CLEAN**; genuine **332→333** remains preserved and closes within Part 003.

SC4 page commit: `{page_commit}`.

## Current frontier

Exact next activity: **Part 003 English glossary reconciliation GR1 — scans 223–255 / printed 206–238, 33 pages**.

Use `GLOSSARY.md` and audited Tamil context to reconcile recurring names, literary/structural terms, publication names, chapter labels, citation metadata and repeated English renderings. Add glossary entries only when evidenced in the active source. This gate does **not** promote pages to `editorial-reviewed`; pages remain `source-checked` until editorial review.

After GR1, continue with GR2 under the current 33-page cadence. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.

See `TRANSLATION_STATUS.md` for the authoritative detailed frontier.
'''
)

replace_once(
    'works/kuraloviyam/HANDOVER.md',
    '- source-check: **IN PROGRESS — SC1 + SC2 + SC3 COMPLETE 99/111**;\n- current English state: **99 `source-checked` + 12 `draft` / 0 source-limited / 0 blocked**;\n- glossary reconciliation: **not-started**;',
    '- source-check: **COMPLETE / CLOSED — 111/111**;\n- current English state: **111 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;\n- glossary reconciliation: **NEXT / not-started**;'
)
replace_tail(
    'works/kuraloviyam/HANDOVER.md',
    '## Source-check progress — SC1 + SC2 + SC3 COMPLETE 99/111\n',
    f'''## Source-check progress — COMPLETE / CLOSED 111/111

- SC1 **223–255 / printed 206–238 — COMPLETE 33/33**;
- SC2 **256–288 / printed 239–271 — COMPLETE 33/33**;
- SC3 **289–321 / printed 272–304 — COMPLETE 33/33**;
- SC4 **322–333 / printed 305–316 — COMPLETE 12/12 / FINAL REMAINDER**.

All Part-003 English records now carry `status: "source-checked"`. SC4 source-fidelity corrections were limited to scan **327**, the **328→329** physical-page split, and scan **333** page-furniture metadata. No Tamil file or metadata changed.

SC4 page commit: `{page_commit}`. Incoming **321→322 is CLEAN**. Internal **332→333** remains a genuine continuation and closes on scan 333. External **333→334** remains deferred until Part 004 source intake.

## Exact next activity — English Glossary Reconciliation GR1

Process **scans 223–255 / printed 206–238 — 33 PAGE-ALIGNED RECORDS**.

1. fetch live `main` first;
2. confirm Part 003 Tamil remains **ARCHIVAL-READY / CLOSED** and English source-check remains **111/111 COMPLETE / CLOSED**;
3. read `translations/en/GLOSSARY.md` and the relevant English/Tamil records completely;
4. compare recurring names, work/section names, controlled literary terms, publication names, chapter labels, citation metadata and repeated English renderings against the glossary and audited Tamil context;
5. update `GLOSSARY.md` only for terms actually evidenced in Part 003;
6. do not mechanically force one English word where context requires another rendering;
7. do not import standard/published/web English wording or terminology from memory;
8. this gate does **not** promote `source-checked` pages to `editorial-reviewed`;
9. do not alter Tamil files;
10. do not begin editorial review during GR1;
11. update `TRANSLATION_STATUS.md` and audit the exact changed-file set.

After GR1, continue glossary reconciliation under the current 33-page cadence. Part 004 remains blocked until glossary reconciliation, editorial review, Part-level review, release report/release-ready synchronization and the final Part closure checkpoint are complete.
'''
)

replace_once(
    'NEXT_CHAT_PROMPT_KURALOVIYAM.md',
    '- Part 003 English source-check SC3: **COMPLETE 33/33 — scans 289–321 / printed 272–304**.\n- cumulative source-check: **99/111**.\n- current Part-003 English state: **99 `source-checked` + 12 `draft` / 0 source-limited / 0 blocked**.\n- remaining undrafted pages: **0**.\n- glossary reconciliation / editorial review / Part review / release: **not-started**.',
    '- Part 003 English source-check SC3: **COMPLETE 33/33 — scans 289–321 / printed 272–304**.\n- Part 003 English source-check SC4: **COMPLETE 12/12 — scans 322–333 / printed 305–316 / FINAL REMAINDER**.\n- cumulative source-check: **111/111 COMPLETE / CLOSED**.\n- current Part-003 English state: **111 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.\n- remaining undrafted pages: **0**.\n- glossary reconciliation: **NEXT / not-started**.\n- editorial review / Part review / release: **not-started**.'
)
replace_tail(
    'NEXT_CHAT_PROMPT_KURALOVIYAM.md',
    '## Source-check results through SC3 — COMPLETE / PASS\n',
    f'''## Source-check results through SC4 — COMPLETE / CLOSED

- SC1 **223–255 / 206–238 — 33/33 source-checked**;
- SC2 **256–288 / 239–271 — 33/33 source-checked**;
- SC3 **289–321 / 272–304 — 33/33 source-checked**;
- SC4 **322–333 / 305–316 — 12/12 source-checked / FINAL REMAINDER**;
- cumulative source-check **111/111 COMPLETE / CLOSED**;
- current English state **111 source-checked / 0 draft / 0 source-limited / 0 blocked**.

SC4 source-fidelity corrections were limited to scan **327** (Monday-market sense), scans **328→329** (exact physical-page continuation), and scan **333** (side title/footer page furniture). The page-only gate changed exactly 12 English records and no Tamil record. Incoming **321→322 is CLEAN**; **332→333** remains a genuine continuation closed on scan 333.

SC4 page commit: `{page_commit}`.

## Exact next activity — Part 003 English Glossary Reconciliation GR1

Process **scans 223–255 / printed 206–238 — 33 page-aligned records**.

Requirements:

1. fetch live `main` first and preserve newer durable work;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm `translations/en/TRANSLATION_STATUS.md` records source-check **111/111 COMPLETE / CLOSED**;
4. read `translations/en/GLOSSARY.md` and English records **0223–0255** with their matching audited Tamil records;
5. reconcile recurring names, work/section names, controlled literary terms, publication names, chapter labels, citation metadata and repeated English renderings against the glossary and audited Tamil context;
6. update `GLOSSARY.md` only for terms actually evidenced in Part 003;
7. do not mechanically force one English rendering where context requires a different one;
8. do not import standard/published/web English Kural wording, another edition's terminology, or memory;
9. this gate does **not** promote `source-checked` pages to `editorial-reviewed`;
10. do not alter Tamil page records or Tamil metadata;
11. do not begin editorial review during GR1;
12. update `translations/en/TRANSLATION_STATUS.md` and audit the exact changed-file set before advancing.

Part 004 remains blocked until Part 003 completes glossary reconciliation, editorial review, Part review, release report/release-ready synchronization and final Part closure. External **333→334** remains deferred until Part 004 source intake.
'''
)

expected_controls = {
    'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md',
    'works/kuraloviyam/translations/en/README.md',
    'works/kuraloviyam/HANDOVER.md',
    'NEXT_CHAT_PROMPT_KURALOVIYAM.md',
}
changed = set(run('git', 'diff', '--name-only').splitlines())
if changed != expected_controls:
    raise SystemExit(f'SC4 control changed-file audit failed: {sorted(changed ^ expected_controls)}')

subprocess.check_call(['git', 'add', *sorted(expected_controls)])
subprocess.check_call(['git', 'commit', '-m', 'kuraloviyam: Close Part 003 English source-check'])

# Push both durable commits together. Temporary workflow/script cleanup happens separately.
subprocess.check_call(['git', 'push', 'origin', 'main'])
