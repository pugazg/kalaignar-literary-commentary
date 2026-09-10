from pathlib import Path
import runpy

try:
    runpy.run_path('.github/scripts/kuraloviyam-part003-gr4-complete.py', run_name='__main__')
except SystemExit as exc:
    msg=str(exc)
    if 'works/kuraloviyam/HANDOVER.md: stale GR4 frontier remains' not in msg:
        raise

p=Path('works/kuraloviyam/HANDOVER.md')
t=p.read_text(encoding='utf-8')

def rep(old,new,label):
    global t
    n=t.count(old)
    if n!=1:
        raise SystemExit(f'{label}: expected 1, found {n}')
    t=t.replace(old,new)

rep('## Glossary reconciliation progress — GR3 COMPLETE / PASS 99/111','## Glossary reconciliation — COMPLETE / CLOSED 111/111','handover glossary heading')
rep('- GR3 **289–321 / printed 272–304 — COMPLETE / PASS 33/33**;','- GR3 **289–321 / printed 272–304 — COMPLETE / PASS 33/33**;\n- GR4 **322–333 / printed 305–316 — COMPLETE / PASS 12/12 / FINAL REMAINDER**;','handover GR4 bullet')
rep('- cumulative glossary reconciliation: **99/111**;','- cumulative glossary reconciliation: **111/111 COMPLETE / CLOSED**;','handover cumulative')
rep('- all English pages remain `source-checked`; GR1+GR2 made **0 English page wording changes**; GR3 changed only **`Kaarmegam` → `Karmegam` on scans 313–314**; status changes remain **0**;','- all English pages remain `source-checked`; GR1+GR2 made **0 English page wording changes**; GR3 changed only **`Kaarmegam` → `Karmegam` on scans 313–314**; GR4 changed only the controlled Chapter 109 and Chapter 4 labels on scans **327** and **331**; status changes remain **0**;','handover wording')

start='## Exact next activity — English Glossary Reconciliation GR4'
if start not in t:
    raise SystemExit('work handover GR4 frontier missing')
prefix=t.split(start,1)[0]
new='''## Exact next activity — English Editorial Review ER1

Process **scans 223–255 / printed 206–238 — 33 PAGE-ALIGNED RECORDS**.

1. fetch live `main` first;
2. confirm Part 003 Tamil remains **ARCHIVAL-READY / CLOSED** and English drafting, source-check and glossary reconciliation are each **111/111 COMPLETE / CLOSED**;
3. read `translations/en/TRANSLATION_GUIDE.md`, `TRANSLATION_STATUS.md`, `GLOSSARY.md`, and English records **0223–0255**, consulting matching audited Tamil wherever an editorial choice could affect meaning;
4. review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity;
5. make only source-faithful editorial improvements; do not import standard/published/web English wording or terminology from memory;
6. passing pages may move from `source-checked` to `editorial-reviewed`;
7. do not alter Tamil files;
8. do not begin Part-level review or release work during ER1;
9. update `TRANSLATION_STATUS.md` and audit the exact changed-file set.

If ER1 passes, the next activity is **Editorial Review ER2 — scans 256–288 / printed 239–271, 33 pages**. External **333→334** remains deferred until Part 004 source intake. Part 004 remains blocked until the maintained English workflow and final Part closure checkpoint are complete.
'''
t=prefix+new
p.write_text(t,encoding='utf-8')

# Final current-frontier validation.
for q in [Path('HANDOVER.md'),Path('NEXT_CHAT_PROMPT_KURALOVIYAM.md'),Path('works/kuraloviyam/HANDOVER.md'),Path('works/kuraloviyam/translations/en/README.md'),Path('works/kuraloviyam/translations/en/TRANSLATION_STATUS.md'),Path('KURALOVIYAM_ARCHIVAL_GUIDELINES.md')]:
    s=q.read_text(encoding='utf-8')
    if 'Exact next activity: **Part 003 English glossary reconciliation GR4' in s or '## Exact next activity — English Glossary Reconciliation GR4' in s or '## Current frontier — Part 003 English glossary reconciliation GR4' in s:
        raise SystemExit(f'{q}: stale executable GR4 frontier remains')
print('GR4 wrapper completed and controls synchronized')
