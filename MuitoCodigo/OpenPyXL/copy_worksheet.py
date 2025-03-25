import openpyxl

wb = openpyxl.load_workbook('testes1.xlsx')  # get planilha
sheet = wb['mercado']  # get qual planilha nós queremos

ws = wb.active
ws.title = 'mercado teste'  # nomeia a planilha que vai ser copiada
wb.copy_worksheet(sheet)

wb.save('testes1.xlsx') # Salva
