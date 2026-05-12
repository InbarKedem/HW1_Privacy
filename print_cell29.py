import json
nb=json.load(open('HW1_2026.ipynb','r',encoding='utf-8'))
code_cells=[c for c in nb.get('cells',[]) if c.get('cell_type')=='code']
print(f'Total code cells: {len(code_cells)}')
idx=28
print('\n--- Cell 29 source ---')
print(''.join(code_cells[idx].get('source',[])))
