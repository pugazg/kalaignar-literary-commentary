from pathlib import Path
import re
import subprocess

STATUS = Path('works/kuraloviyam/translations/en/TRANSLATION_STATUS.md')
README = Path('works/kuraloviyam/translations/en/README.md')
HANDOVER = Path('works/kuraloviyam/HANDOVER.md')
PROMPT = Path('NEXT_CHAT_PROMPT_KURALOVIYAM.md')

# TRANSLATION_STATUS
text = STATUS.read_text(encoding='utf-8')
anchor = '## Part 003 English first-pass drafting — COMPLETE / CLOSED'
pos = text.index(anchor)
prefix, part3 = text[:pos], text[pos:]
old = '- source-check: **not-started**;\n- glossary reconciliation: **not-started**;'
assert old in part3
part3 = part3.replace(old, '- source-check: **IN PROGRESS — 33/111 COMPLETE**;\n- glossary reconciliation: **not-started**;', 1)
frontier = '''## Part 003 English source-check — IN PROGRESS

- **SC1: scans 223–255 / printed 206–238 — COMPLETE 33/33**;
- cumulative source-check: **33/111**;
- current Part-003 English state: **33 `source-checked` + 78 `draft` / 0 source-limited / 0 blocked**;
- remaining source-check pages: **78**.

SC1 compared every page paragraph-by-paragraph / block-by-block against the audited Tamil records. All **33/33** pages passed after source-fidelity reconciliation. Corrections were limited to:

- scan **232 / printed 215** — restored the source page's small statue illustration as factual visual-material metadata;
- scan **247 / printed 230** — reconciled the prose terminology from `pulavi` / `thuni` to the source's explicit `pulavi` / `pinakku`; the separate source gloss `துனி = பிணக்கம்` remains preserved;
- scans **252→253 / printed 235→236** — repaired the split simile for `பித்தவெடி கொண்டுள்ள பாதம்` so the English now reads continuously as a foot scarred by deep fissures and the field cracked by drought.

SC1 page commit: `0811c0ab6e59e863e92a6708b6352226e780cdfb` — `kuraloviyam: Source-check Part 003 English scans 223-255`.

The page-only comparison from workflow checkpoint `9af7226b9fdbc6c03dab51df150defb4326382da` to `0811c0ab6e59e863e92a6708b6352226e780cdfb` is **ahead / non-divergent** and contains exactly **33 modified English page records**, scans **223–255**, with no Tamil page or Tamil metadata change. Twenty-nine pages changed only by status promotion; four page files also contain the source-fidelity corrections above.

The SC1 endpoint **255→256 is CLEAN**.

## Current frontier — Part 003 English Source-check SC2

Exact next activity: **source-check scans 256–288 / printed 239–271 — 33 page-aligned records**.

Compare each English page against its audited Tamil counterpart paragraph-by-paragraph / block-by-block for omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual/non-body page function and cross-page continuity. Only passing pages may move from `draft` to `source-checked`.

Do not perform glossary reconciliation or editorial review during SC2. Do not alter Tamil archival records. Preserve the CLEAN incoming **255→256** boundary and the genuine outgoing **288→289** continuation. If SC2 passes, cumulative source-check becomes **66/111** and SC3 will be **scans 289–321 / printed 272–304 — 33 pages**.

Part 004 remains blocked until Part 003 completes its maintained English workflow and final Part closure checkpoint.'''
part3, n = re.subn(r'## Current frontier — Part 003 English Source-check SC1\n.*\Z', frontier, part3, flags=re.S)
assert n == 1
STATUS.write_text(prefix + part3, encoding='utf-8')

# English README
text = README.read_text(encoding='utf-8')
old = '- current English state: **111 `draft` / 0 source-limited / 0 blocked**;\n- source-check / glossary reconciliation / editorial review / Part review / release: **not-started**.'
assert old in text
text = text.replace(old, '- post-drafting state: **111 `draft` / 0 source-limited / 0 blocked**;\n- source-check: **IN PROGRESS — SC1 COMPLETE 33/111**;\n- current English state: **33 `source-checked` + 78 `draft` / 0 source-limited / 0 blocked**;\n- glossary reconciliation / editorial review / Part review / release: **not-started**.', 1)
new_tail = '''## Part 003 English source-check

SC1 **scans 223–255 / printed 206–238 — COMPLETE 33/33**. The batch passed with **33 `source-checked`**, leaving **78 `draft`** pages. Source-fidelity reconciliation restored scan 232's small statue page function, corrected scan 247's explicit `pulavi` / `pinakku` wording, and repaired the split foot-fissure / drought-field simile across scans 252→253. No Tamil archival record changed.

## Current frontier

Exact next activity: **Part 003 English source-check SC2 — scans 256–288 / printed 239–271, 33 pages**.

Compare every English record against its audited Tamil counterpart paragraph-by-paragraph / block-by-block. Check omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual/non-body page function and cross-page continuity. Only passing pages may move from `draft` to `source-checked`.

If SC2 passes, cumulative source-check becomes **66/111** and SC3 will cover **289–321 / printed 272–304**. Do not begin glossary reconciliation until all Part-003 source-check batches are complete. Part 004 remains blocked until the Part-003 maintained English workflow and final Part closure checkpoint are complete.

See `TRANSLATION_STATUS.md` for the authoritative detailed frontier.'''
text, n = re.subn(r'## Current frontier\n.*\Z', new_tail, text, flags=re.S)
assert n == 1
README.write_text(text, encoding='utf-8')

# HANDOVER
text = HANDOVER.read_text(encoding='utf-8')
old = '- current English state: **111 `draft` / 0 source-limited / 0 blocked**;\n- source-check: **not-started**;'
assert old in text
text = text.replace(old, '- post-drafting state: **111 `draft` / 0 source-limited / 0 blocked**;\n- source-check: **IN PROGRESS — SC1 COMPLETE 33/111**;\n- current English state: **33 `source-checked` + 78 `draft` / 0 source-limited / 0 blocked**;', 1)
new_tail = '''## Source-check SC1 — COMPLETE 33/33

SC1 covers **scans 223–255 / printed 206–238**. All 33 records now carry `status: "source-checked"` after paragraph/block comparison against the audited Tamil records. Source-fidelity corrections were limited to scan 232 visual metadata, scan 247 `pulavi` / `pinakku` terminology, and the scans 252→253 split foot-fissure / drought-field simile. No Tamil file or metadata changed.

SC1 page commit: `0811c0ab6e59e863e92a6708b6352226e780cdfb`. Its page-only audit from `9af7226b9fdbc6c03dab51df150defb4326382da` contains exactly **33 English page records and no Tamil changes**. Endpoint **255→256 is CLEAN**.

## Exact next activity — English Source-check SC2

Process **scans 256–288 / printed 239–271 — 33 page-aligned records**.

1. fetch live `main` first;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm `translations/en/TRANSLATION_STATUS.md` records SC1 **COMPLETE — 33/111 cumulative**;
4. read English records **0256–0288** and matching audited Tamil records completely;
5. compare paragraph-by-paragraph / block-by-block for omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual/non-body page function and cross-page continuity;
6. preserve the audited Tamil wording as source authority; do not import standard/published/web English Kural text;
7. make only source-fidelity corrections needed to pass source-check;
8. only passing pages may move from `status: "draft"` to `status: "source-checked"`;
9. preserve the CLEAN incoming **255→256** boundary and inspect the genuine outgoing **288→289** continuation without treating it as a narrative break;
10. do not alter Tamil files;
11. do not begin glossary reconciliation or editorial review during SC2;
12. update `translations/en/TRANSLATION_STATUS.md` and audit the exact changed-file set.

If SC2 passes, source-check becomes **66/111** and SC3 will be **scans 289–321 / printed 272–304 — 33 pages**.

Part 004 remains blocked until Part 003 completes its maintained English workflow and final Part closure checkpoint.'''
text, n = re.subn(r'## Exact next activity — English Source-check SC1\n.*\Z', new_tail, text, flags=re.S)
assert n == 1
HANDOVER.write_text(text, encoding='utf-8')

# NEXT_CHAT_PROMPT
text = PROMPT.read_text(encoding='utf-8')
old = '- current Part-003 English state: **111 `draft` / 0 source-limited / 0 blocked**.\n- remaining undrafted pages: **0**.\n- Part 003 English source-check / glossary reconciliation / editorial review / Part review / release: **not-started**.'
assert old in text
text = text.replace(old, '- Part 003 English source-check SC1: **COMPLETE 33/33 — scans 223–255 / printed 206–238**.\n- cumulative source-check: **33/111**.\n- current Part-003 English state: **33 `source-checked` + 78 `draft` / 0 source-limited / 0 blocked**.\n- remaining undrafted pages: **0**.\n- glossary reconciliation / editorial review / Part review / release: **not-started**.', 1)
new_tail = '''## SC1 result — COMPLETE / PASS

SC1 **scans 223–255 / printed 206–238 — 33/33 source-checked**. The source-fidelity pass made only three correction loci: scan 232 visual-material restoration; scan 247 `pulavi` / `pinakku` terminology; and the scans 252→253 split foot-fissure / drought-field simile. No Tamil record changed. Page commit: `0811c0ab6e59e863e92a6708b6352226e780cdfb`. The **255→256 boundary is CLEAN**.

## Exact next activity — Part 003 English Source-check SC2

Process **scans 256–288 / printed 239–271 — 33 page-aligned records**.

Requirements:

1. fetch live `main` first and preserve newer durable work;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm `translations/en/TRANSLATION_STATUS.md` records SC1 **COMPLETE — 33/111 cumulative**;
4. read English records **0256–0288** and the matching audited Tamil records completely;
5. compare each page paragraph-by-paragraph / block-by-block for omissions, additions, meaning drift, names, titles, quotations, Kural wording/lineation, visual/non-body page function and cross-page continuity;
6. correct only source-fidelity issues supported by the audited Tamil records;
7. keep `source_tamil_status: "verified"` and promote only passing pages from `draft` to `source-checked`;
8. preserve incoming **255→256 CLEAN** and the genuine outgoing **288→289** continuation;
9. do not alter any Tamil page record or Tamil metadata;
10. do not begin glossary reconciliation or editorial review during SC2;
11. update `translations/en/TRANSLATION_STATUS.md` after the batch;
12. audit the exact changed-file set before advancing.

If SC2 passes, Part-003 English source-check becomes **66/111**. The next batch will be **SC3: scans 289–321 / printed 272–304 — 33 pages**.

Part 004 remains blocked until Part 003 completes the maintained English workflow and final Part closure checkpoint.'''
text, n = re.subn(r'## Exact next activity — Part 003 English Source-check SC1\n.*\Z', new_tail, text, flags=re.S)
assert n == 1
PROMPT.write_text(text, encoding='utf-8')

changed = sorted(line.strip() for line in subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines() if line.strip())
expected = sorted([
    'NEXT_CHAT_PROMPT_KURALOVIYAM.md',
    'works/kuraloviyam/HANDOVER.md',
    'works/kuraloviyam/translations/en/README.md',
    'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md',
])
if changed != expected:
    raise SystemExit(f'unexpected control changed-file set: {changed}')
