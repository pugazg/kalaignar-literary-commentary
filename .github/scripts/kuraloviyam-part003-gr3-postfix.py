from pathlib import Path

def replace_once(path,old,new,label):
    p=Path(path); t=p.read_text(encoding='utf-8')
    n=t.count(old)
    if n!=1: raise SystemExit(f'{label}: expected 1 occurrence, found {n}')
    p.write_text(t.replace(old,new),encoding='utf-8')

replace_once('works/kuraloviyam/translations/en/TRANSLATION_STATUS.md',
'- **GR2: scans 256–288 / printed 239–271 — COMPLETE / PASS 33/33**;\n- cumulative glossary reconciliation: **99/111**;',
'- **GR2: scans 256–288 / printed 239–271 — COMPLETE / PASS 33/33**;\n- **GR3: scans 289–321 / printed 272–304 — COMPLETE / PASS 33/33**;\n- cumulative glossary reconciliation: **99/111**;',
'status GR3 bullet')

replace_once('NEXT_CHAT_PROMPT_KURALOVIYAM.md',
'- GR2 **256–288 / printed 239–271 — 33/33 PASS**;\n- cumulative glossary reconciliation **99/111**;',
'- GR2 **256–288 / printed 239–271 — 33/33 PASS**;\n- GR3 **289–321 / printed 272–304 — 33/33 PASS**;\n- cumulative glossary reconciliation **99/111**;',
'prompt GR3 bullet')

replace_once('works/kuraloviyam/HANDOVER.md',
'- GR2 **256–288 / printed 239–271 — COMPLETE / PASS 33/33**;\n- cumulative glossary reconciliation: **99/111**;',
'- GR2 **256–288 / printed 239–271 — COMPLETE / PASS 33/33**;\n- GR3 **289–321 / printed 272–304 — COMPLETE / PASS 33/33**;\n- cumulative glossary reconciliation: **99/111**;',
'work handover GR3 bullet')
replace_once('works/kuraloviyam/HANDOVER.md',
'3. read `translations/en/GLOSSARY.md` and the matching English/Tamil records **0289–0321**;',
'3. read `translations/en/GLOSSARY.md` and the matching English/Tamil records **0322–0333**;',
'work handover GR4 records')

replace_once('HANDOVER.md',
'3. confirm Tamil remains closed, source-check remains 111/111 closed, and glossary reconciliation remains 66/111 complete;',
'3. confirm Tamil remains closed, source-check remains 111/111 closed, and glossary reconciliation remains **99/111 complete**;',
'root handover cumulative')
replace_once('HANDOVER.md',
'7. do not promote page statuses or begin editorial review during GR3;',
'7. do not promote page statuses or begin editorial review during GR4;',
'root handover gate name')
replace_once('HANDOVER.md',
'If GR3 passes, cumulative glossary reconciliation becomes **99/111**; GR4 is the final **12-page remainder scans 322–333 / printed 305–316**.',
'If GR4 passes, glossary reconciliation becomes **111/111 COMPLETE / CLOSED**; the next gate is **English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**.',
'root handover next condition')

print('GR3 control postfix complete')
