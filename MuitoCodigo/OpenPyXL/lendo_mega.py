import openpyxl
from pprint import pprint
import pandas as pd

planilha = 'MegaPlanilha.xlsx'
ws = openpyxl.load_workbook(planilha)['MEGA SENA']

cell = ws.cell(row=1, column=1).value

print(cell)
# ------

data = {
    'Concurso': [],
    'Game': []
}

for x, linha in enumerate(ws.values):
    if x == 0:
        continue

    game = []
    for coluna, dado in enumerate(linha):
        if coluna == 0:
            data['Concurso'].append(dado)

        if coluna >= 3:
            game.append(dado)

        if coluna == 8:
            data['Game'].append(game)
            break

pprint(data)
