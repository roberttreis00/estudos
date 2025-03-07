'''
Custos/ Marca
Planilha contendo todos os produtos ativos na Netshoes E a do saldo do Tiny
API [Netshoes, Zattini] Seller PREÇOS
Retunr planilha para alterar preços automatico

Versão 2.0 Fazendo consultar por API
Mande o email caso queria as funções -> roberttsreis00@gmail.com
'''

import xlrd
import pandas as pd
from Custos_Produtos_ALL import CustoProdutosALL
from ConsultaApiZattini import consulta_api_zattini
from ApiNetshoesFuction import consulta_api_netshoes

# GET Dados saldo estoque disponível do Tiny
EstoqueTiny = 'saldos-em-estoque.xls'
DF_Estoque_Tiny = xlrd.open_workbook(EstoqueTiny, ignore_workbook_corruption=True)
DF_Estoque_Tiny_PD = pd.read_excel(DF_Estoque_Tiny)

ColunaSKU1 = DF_Estoque_Tiny_PD.iloc[:, 0]
ColunaEstoqueDisponivel = DF_Estoque_Tiny_PD.iloc[:, 4]

SaldoEstoqueDisponivel = dict()

for x, y in zip(ColunaSKU1, ColunaEstoqueDisponivel):
    SaldoEstoqueDisponivel[x] = y

# Get Produtos Netshoes
produtos_netshoes = 'export1741023621141.xlsx'

df = pd.read_excel(produtos_netshoes)
data = dict()

ColunaIDNetshoes = df.iloc[:, 2]
ColunaSKUTiny = df.iloc[:, 12]

for x, y in zip(ColunaSKUTiny, ColunaIDNetshoes):
    data[x] = y


def calculos(sku, dat1, custo_lucro_esperado):
    if dat1['Seller'] in marcas:
        return

    # Calcula o Ajuste
    novoDE = dat1['Preco de'] - 0.50
    novoPara = dat1['Preco Para'] - 0.50

    # Calculos
    taxamkt = novoPara * 0.25
    imposto = novoPara * 0.12
    lucro = novoPara - (custo_lucro_esperado[0] + taxamkt + imposto + 3)
    porcentagem_lucro = lucro * 100 / novoPara

    if porcentagem_lucro >= custo_lucro_esperado[1]:
        return sku, novoDE, novoPara, dat1['Seller']


# Função para pega custos dos produtos
def custo_produto(sku):
    for custo_data in CustoProdutosALL.values():
        lucro_esperado = custo_data['% de Lucro Esperada']
        custos_para_verificar = custo_data['Skus e Custos']

        for sku_pai, custo in custos_para_verificar.items():
            if sku.startswith(sku_pai):
                return custo, lucro_esperado


# Marca para evitar comparar preços
marcas = ['Netshoes', 'Olympikus', 'Fila', 'Loja Oficial Umbro', 'DEMOCRATA CALÇADOS', 'DAKOTA',
          'Zattini']

# Planilha alterar Preços
PrecoAlterar = {
    'Sku Seller': [],
    'Preço De': [],
    'Preço Por': [],
    'Seller': [],
}

# Analisar e pegar Preços
for sku_seller, id_netshoes in data.items():

    # Verifica se tem saldo ou se está zerado
    try:
        if SaldoEstoqueDisponivel[sku_seller] <= 1:
            continue
    except KeyError:
        continue  # Aqui zerado

    # Descorir o custo do produto
    custo = custo_produto(sku_seller)

    if custo is None:
        continue

    dados1 = consulta_api_netshoes(id_netshoes)
    dados2 = consulta_api_zattini(id_netshoes)
    sellers = []
    dat1 = None
    dat2 = None

    if dados1 is not None:
        dat1 = calculos(sku_seller, dados1, custo)
        if dat1 is not None:
            seller_atual = str(dat1[3])
            sellers.append(seller_atual)

    if dados2 is not None:
        dat2 = calculos(sku_seller, dados2, custo)
        if dat2 is not None:
            seller_atual = str(dat2[3])
            sellers.append(seller_atual)

    if "ANDARE CALÇADOS" in sellers:
        continue

    if dat1 is not None:
        PrecoAlterar['Sku Seller'].append(dat1[0])
        PrecoAlterar['Preço De'].append(str(dat1[1]))
        PrecoAlterar['Preço Por'].append(str(dat1[2]))
        PrecoAlterar['Seller'].append(str(dat1[3]))

    if dat2 is not None:
        PrecoAlterar['Sku Seller'].append(dat2[0])
        PrecoAlterar['Preço De'].append(str(dat2[1]))
        PrecoAlterar['Preço Por'].append(str(dat2[2]))
        PrecoAlterar['Seller'].append(str(dat2[3]))

pd.DataFrame(PrecoAlterar).to_excel('ImportaNovosprecos.xlsx', index=False)
