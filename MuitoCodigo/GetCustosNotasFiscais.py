import os
from bs4 import BeautifulSoup
from pprint import pprint

notas = 'Ciente/'
produtos_all = dict()

for nota in os.listdir(notas):
    caminho_nota = os.path.join(notas, nota)

    with (open(caminho_nota, 'r') as file):
        bs = BeautifulSoup(file, 'xml')
        valor_total_nota = bs.find('vPag').get_text()
        produtos = bs.find_all('det')

        # pega os dados de cada variacao
        for produto in produtos:
            ean = produto.find_next('cEANTrib').get_text()
            qtd_comprada = int(float(produto.find_next('qCom').get_text()))
            custo_und = float(produto.find_next('vUnTrib').get_text())

            try:
                if produtos_all[ean][0][1] != custo_und:
                    produtos_all[ean].append([qtd_comprada, custo_und])

                produtos_all[ean][0][0] += qtd_comprada

            except KeyError:
                produtos_all[ean] = [[qtd_comprada, custo_und]]

pprint(produtos_all)
