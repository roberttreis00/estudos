import pdfplumber
import re
import pandas as pd
import unicodedata


def remo_carc(texto):
    texto_normalizado = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8')
    texto_sem_acentos = ''

    for c in texto_normalizado:
        if c.isalnum() or c in ' _' or c == '.':
            texto_sem_acentos += c
    return texto_sem_acentos


pdf_file = 'Extrato Bradesco 2024-10-11-12 _03012025_143537.pdf'

inicio = True
pdf_parser = {
    'DATA': list(),
    'Documento': list(),
    'Histórico': list(),
    'Valor Debito (Soma)': list(),
    'Valor Credíto (Subtrai)': list(),
    '': list(),
}
fim = False

with pdfplumber.open(pdf_file) as file:
    pages = file.pages
    data_inicial = ''
    linha_inicio = ''
    linha_meio = ''

    for page in pages:

        tables = page.extract_text().split('\n')
        if inicio:
            inicio = False
            tables = tables[5:]

        for row in tables:
            if "Total" in row:
                fim = True
                break

            if fim:
                break

            data = re.match(r'\d+/\d+/\d+', row)

            if data:
                data_inicial = data.group()

            row = row.replace(data_inicial, '').strip()

            # print(linha_inicio, '\n',linha_meio, '\n', outra_linha, '\n')
            if row[0].isdigit() and row[-1].isalpha():
                outra_linha = row

                pdf_parser[''].append('')
                pdf_parser['DATA'].append(data_inicial)

                linha_inicio = linha_inicio.split(' ')
                pdf_parser['Documento'].append(linha_inicio[0])

                pdf_parser['Histórico'].append(linha_meio.strip() + ' ' + outra_linha)
                linha_inicio.pop()
                valor = linha_inicio[-1].replace(".", '').strip().replace('-', '')
                valor_calculo = float(valor.replace(',', '.'))

                if valor_calculo > 0:
                    pdf_parser['Valor Credíto (Subtrai)'].append(valor)
                    pdf_parser['Valor Debito (Soma)'].append('')
                else:
                    pdf_parser['Valor Credíto (Subtrai)'].append('')
                    pdf_parser['Valor Debito (Soma)'].append(valor)

                linha_inicio = ''
                outra_linha = ''
                linha_meio = ''
                continue

            if row[0].isdigit():
                linha_inicio = row
            else:
                row_atual = row.split(' ')

                if not row_atual[0][0].isdigit() and row[-1][-1].isdigit():
                    if not linha_meio:
                        pdf_parser['DATA'].append(data_inicial)
                        linha = row.split(" ")
                        linha.pop()
                        valor = linha[-1].replace(".", '')
                        try:
                            valor_calculo = float(valor.replace(',', '.'))
                        except ValueError:
                            pdf_parser['Histórico'][-1] += " "
                            pdf_parser['Histórico'][-1] += remo_carc(" ".join(linha))

                        if valor_calculo > 0:
                            pdf_parser['Valor Debito (Soma)'].append(valor.replace('-', ''))
                            pdf_parser['Valor Credíto (Subtrai)'].append('')
                        else:
                            pdf_parser['Valor Debito (Soma)'].append('')
                            pdf_parser['Valor Credíto (Subtrai)'].append(valor.replace('-', ''))

                        linha.pop()
                        x = linha[-1]
                        if x.isalpha():
                            pdf_parser['Valor Credíto (Subtrai)'].pop()
                            pdf_parser['Valor Debito (Soma)'].pop()
                            pdf_parser['DATA'].pop()
                            continue

                        pdf_parser['Documento'].append(x)
                        pdf_parser['Histórico'].append(remo_carc(" ".join(linha)))
                        pdf_parser[''].append('')

                        continue

                outra_linha = row

                if not linha_inicio or data and outra_linha:
                    linha_meio = row
                else:
                    pdf_parser['DATA'].append(data_inicial)

                    linha_inicio = linha_inicio.split(' ')
                    pdf_parser['Documento'].append(linha_inicio.pop(0))

                    pdf_parser['Histórico'].append(remo_carc(linha_meio) + ' ' + remo_carc(outra_linha))

                    valor = linha_inicio[0].replace(".", '')
                    valor_calculo = float(valor.replace(',', '.'))

                    if valor_calculo > 0:
                        pdf_parser['Valor Debito (Soma)'].append(valor.replace('-', ''))
                        pdf_parser['Valor Credíto (Subtrai)'].append('')
                    else:
                        pdf_parser['Valor Debito (Soma)'].append('')
                        pdf_parser['Valor Credíto (Subtrai)'].append(valor.replace('-', ''))

                    pdf_parser[''].append('')

                    linha_inicio = ''
                    outra_linha = ''
                    linha_meio = ''

df = pd.DataFrame(pdf_parser)
df.to_csv('bradesco.csv', index=False, sep=";", encoding="utf-8-sig")
