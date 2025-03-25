from tempfile import TemporaryDirectory
import pandas as pd
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

data = {
    'Batata': ['1.99', '2.99'],
    'Arroz': ['5.99', '29.90'],
}
dt = pd.DataFrame(data)

# Cria um diretorio temporario
with TemporaryDirectory() as temp_dir:
    print('Local do diretorio', temp_dir)
    dt.to_excel(f"{temp_dir}/planilhaTemporario.xlsx", index=False, engine='openpyxl')
    ws['A1'] = 'TESTE'
    wb.save(f'{temp_dir}/planilhaopenpyxl.xlsx')

    input('Continua: ')
