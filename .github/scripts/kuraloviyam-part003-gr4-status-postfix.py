from pathlib import Path
p=Path('works/kuraloviyam/translations/en/TRANSLATION_STATUS.md')
s=p.read_text(encoding='utf-8')
old='- glossary reconciliation: **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**;'
new='- glossary reconciliation: **111/111 COMPLETE / CLOSED**;'
if s.count(old)!=1:
    raise SystemExit(f'expected stale summary once, found {s.count(old)}')
p.write_text(s.replace(old,new),encoding='utf-8')
print('status summary synchronized')
