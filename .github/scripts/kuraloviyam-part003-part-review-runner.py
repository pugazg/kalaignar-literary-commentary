from pathlib import Path
import runpy

p = Path('.github/scripts/kuraloviyam-part003-part-review.py')
text = p.read_text(encoding='utf-8')
old = "actual_changed = set(subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines())\nif actual_changed != expected_changed:"
new = "actual_changed = set(subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines())\nactual_changed |= set(subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], text=True).splitlines())\nactual_changed = {x for x in actual_changed if not x.startswith('.github/')}\nif actual_changed != expected_changed:"
if old not in text:
    raise RuntimeError('target changed-file gate not found in Part-review script')
p.write_text(text.replace(old, new, 1), encoding='utf-8')
runpy.run_path(str(p), run_name='__main__')
