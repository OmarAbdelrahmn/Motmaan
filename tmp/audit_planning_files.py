from pathlib import Path
import ast
import json
import re
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
markdown = sorted(root.rglob('*.md'))
missing = []
tables = []
for path in markdown:
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    previous = None
    for number, line in enumerate(lines, 1):
        for target in re.findall(r'\]\(([^)]+)\)', line):
            target = unquote(target.strip('<>').split('#')[0])
            if not target or re.match(r'^[a-z]+://', target):
                continue
            candidate = Path(target) if re.match(r'^[A-Za-z]:[/\\]', target) else path.parent / target
            if not candidate.exists():
                missing.append([str(path.relative_to(root)), number, target])
        if line.startswith('|'):
            cells = len(re.split(r'(?<!\\)\|', line)) - 2
            if previous is not None and previous != cells:
                tables.append([str(path.relative_to(root)), number, previous, cells])
            previous = cells
        else:
            previous = None
scripts = []
for path in sorted((root / 'tmp').rglob('*.py')):
    if path.name == Path(__file__).name:
        continue
    ast.parse(path.read_text(encoding='utf-8-sig'))
    scripts.append(str(path.relative_to(root)))
result = {'markdown_count': len(markdown), 'missing_local_targets': missing,
          'table_column_mismatches': tables, 'syntax_checked_only_not_executed': scripts}
print(json.dumps(result, ensure_ascii=False, indent=2))
