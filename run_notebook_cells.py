import json
import sys
import traceback
import os

nb_path = 'HW1_2026.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = [c for c in nb.get('cells', []) if c.get('cell_type') == 'code']

globals_dict = {}
# Use non-interactive backend for matplotlib to avoid GUI
try:
    import matplotlib
    matplotlib.use('Agg')
except Exception:
    pass

print(f'Found {len(cells)} code cells. Executing sequentially...')

for i, cell in enumerate(cells, start=1):
    source = ''.join(cell.get('source', []))
    # Remove IPython magics and shell (!) lines
    filtered_lines = []
    for line in source.splitlines():
        stripped = line.lstrip()
        if stripped.startswith('%'):
            filtered_lines.append(f"# IPython magic skipped: {line}\n")
        elif stripped.startswith('!'):
            filtered_lines.append(f"# Shell command skipped: {line}\n")
        else:
            filtered_lines.append(line)
    code = '\n'.join(filtered_lines)
    print('\n' + '='*40)
    print(f'Executing cell {i}/{len(cells)}...')
    try:
        compiled = compile(code, f'<cell {i}>', 'exec')
        exec(compiled, globals_dict)
        print(f'Cell {i} executed successfully.')
    except Exception as e:
        print(f'Error executing cell {i}: {e}')
        traceback.print_exc()
        # Stop on first error to mimic manual step-by-step debugging
        sys.exit(1)

print('\nAll code cells executed successfully.')
