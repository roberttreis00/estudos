'''
DEPOSITO
    NÃO PODE SER NEGATIVO
SAQUE
    3 SAQUES DIARIOS, MAX $500
EXTRATO
    TODAS AS OPERAÇÕES REALIZADAS
'''
from random import uniform, randint
from datetime import datetime
from pprint import pprint
import os

data_atual = datetime.now().strftime("%d/%m/%y")


def gerador_9numeros():
    numeros = "".join([str(randint(0, 9)) for x in range(0, 9)])
    return numeros


ContaUser = {
    'CONTA': gerador_9numeros(),
    'AG': '24',
    'SALDO': round(uniform(10, 1600), 2),
    'QTD SAQUES': 3,
    'LIMITE DE SAQUE': 500,
}

Extrato = list()


def deposito():
    os.system('cls')
    valor_deposito = float(input("Digite o valor que gostaria de depositar: "))

    if valor_deposito <= 0:
        print('ERRO DEPOSITO UM VALOR MAIOR DO QUE ZERO!')
        return

    OP = gerador_9numeros()
    Extrato.append(
        f'OP: {OP} | DEPOSITO DE R${valor_deposito} REALIZADO {data_atual} | SALDO ANTERIOR: R$ {ContaUser["SALDO"]}')
    ContaUser['SALDO'] += valor_deposito


def sacar():
    os.system('cls')
    print(f'SALDO R${ContaUser["SALDO"]}')
    valor_sacar = float(input("Digite o valor que gostaria de sacar: "))
    taxa = 0

    if valor_sacar > ContaUser['SALDO']:
        print('ERRO SALDO INSUFICIENTE!')
        return

    if valor_sacar >= ContaUser['LIMITE DE SAQUE']:
        print('ERRO LIMITE DE SAQUE R$500, SAQUE NÃO PERMITIDO')
        return

    if ContaUser['QTD SAQUES'] == 0:
        print('ERRO SEUS SAQUES DISPONIVEIS ACABOU O PROXIMO SAQUE CUSTARÁ R$3.50 ACEITA? '
              '\n DIGITE 1: ACEITAR \n DIGITE 2: NÃO \n')
        taxa = int(input('>>>'))

        if taxa == 1:
            taxa = 3.50
        else:
            return

    ContaUser['SALDO'] -= valor_sacar + taxa
    if ContaUser['QTD SAQUES'] > 0:
        ContaUser['QTD SAQUES'] -= 1
    print(f'SAQUE REALIZADO NOVO SALDO: R${round(ContaUser["SALDO"], 2)}')
    OP = gerador_9numeros()
    Extrato.append(
        f'OP: {OP} | SAQUE DE R${valor_sacar} REALIZADO {data_atual} | SALDO ANTERIOR: R$ {ContaUser["SALDO"]}')


def extrato():
    os.system('cls')
    print(f'''
        CONTA: {ContaUser['CONTA']},
        AG: {ContaUser['AG']},
        SALDO: R${ContaUser['SALDO']},
        QUANTIDADE SAQUES: {ContaUser['QTD SAQUES']},
        LIMITE DE SAQUES: R${ContaUser['LIMITE DE SAQUE']},
    ''')
    for operacao in Extrato:
        print(operacao)


opcoes_banco = {
    1: deposito,
    2: sacar,
    3: extrato,
}


def menu():
    while True:
        servico = int(input('''
            Qual a operação gostaria de fazer: 
            Digite 1: Depositar $$$
            Digite 2: Sacar $$$
            Digite 3: Ver Extrato $$$
            Digite 4: Sair
        >>>'''))
        if servico == 4:
            os.system('cls')
            print("FIM DA OPERAÇÂO BANCARIA")
            break

        opcoes_banco[servico]()


menu()
