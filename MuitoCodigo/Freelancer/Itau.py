import pdfplumber
import pandas as pd
import re

pdf_file = 'Itau 11-2024.pdf'

inicio = True
pdf_parser = {
    'DATA': list(),
    'Histórico': list(),
    'Documento': list(),
    'Valor Debito (Soma)': list(),
    'Valor Credíto (Subtrai)': list(),
    '': list(),
}

with pdfplumber.open(pdf_file) as file:
    pages = file.pages

    for page in pages:
        page = page.extract_table()
        for row in page:
            if 'Extrato' in row[0]:
                ano = row[0][-4:]

            try:
                data = row[0] + f"/{ano}"
            except NameError:
                continue

            is_data = re.match(r'\d+/\d+/\d+', data)

            if is_data:
                pdf_parser['DATA'].append(data)
                pdf_parser['Histórico'].append(row[3])
                pdf_parser['Documento'].append(row[4])
                pdf_parser[''].append('')

                if len(row) == 10:
                    valor = row[6]
                else:
                    valor = row[5]
                if valor:
                    valor_convertido = valor.replace('.', '')
                    if '-' in valor:
                        valor_convertido = valor_convertido.replace('-', '')
                        pdf_parser['Valor Credíto (Subtrai)'].append(valor_convertido)
                        pdf_parser['Valor Debito (Soma)'].append('')
                    else:
                        valor_convertido = valor.replace('.', '')
                        pdf_parser['Valor Debito (Soma)'].append(valor_convertido)
                        pdf_parser['Valor Credíto (Subtrai)'].append('')
                else:
                    pdf_parser['Valor Debito (Soma)'].append('')
                    pdf_parser['Valor Credíto (Subtrai)'].append('')


df = pd.DataFrame(pdf_parser)
df.to_csv('itau.csv', index=False, sep=";", encoding="utf-8-sig")
