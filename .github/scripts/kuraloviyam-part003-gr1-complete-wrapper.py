from pathlib import Path

path = Path('.github/scripts/kuraloviyam-part003-gr1-complete.py')
code = path.read_text(encoding='utf-8')
old = 'Chapter 112 label on scans 55 and 71.'
new = 'Chapter 112 label cited on scans 55 and 71.'
if code.count(old) != 1:
    raise SystemExit(f'wrapper precondition failed: expected 1 occurrence, found {code.count(old)}')
code = code.replace(old, new, 1)
exec(compile(code, str(path), 'exec'))
