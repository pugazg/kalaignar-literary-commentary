from pathlib import Path
p=Path('works/kuraloviyam/indexes/page-map.md')
s=p.read_text(encoding='utf-8')
old='| 003 | 223–333 | 1–111 | scan 223 / printed 206 through scan 333 / printed 316 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check COMPLETE / CLOSED; glossary GR1 + GR2 + GR3 COMPLETE / PASS — 99/111; GR4 next** |'
new='| 003 | 223–333 | 1–111 | scan 223 / printed 206 through scan 333 / printed 316 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 next** |'
if s.count(old)!=1:
    raise SystemExit(f'expected page-map row once, found {s.count(old)}')
p.write_text(s.replace(old,new),encoding='utf-8')
print('page-map synchronized')
