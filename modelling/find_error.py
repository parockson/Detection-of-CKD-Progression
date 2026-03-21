import json

with open('notebook.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

code_cells = [(i, cell) for i, cell in enumerate(nb['cells']) if cell['cell_type'] == 'code']

with open('all_code_cells.txt', 'w', encoding='utf-8') as out:
    for rank, (idx, cell) in enumerate(code_cells):
        src = ''.join(cell['source'])
        out.write(f"=== CODE CELL {rank} (notebook idx {idx}) ===\n")
        out.write(src + "\n\n")

print(f"Extracted {len(code_cells)} code cells to all_code_cells.txt")
