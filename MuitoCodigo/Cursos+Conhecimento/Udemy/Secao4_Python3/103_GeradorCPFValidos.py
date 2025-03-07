from random import randint

cpf_gerado = ''

for numero in range(0, 9):
    cpf_gerado += str(randint(0, 9))

soma_conta1 = 0
soma_conta2 = 0

for digito, n in enumerate(range(10, 1, -1)):
    conta = int(cpf_gerado[digito]) * n
    soma_conta1 += conta

digito1 = soma_conta1 * 10
digito1 = digito1 % 11

if digito1 > 9:
    digito1 = 0

cpf_gerado += str(digito1)

for digito, n in enumerate(range(11, 1, -1)):
    conta = int(cpf_gerado[digito]) * n
    soma_conta2 += conta

digito2 = soma_conta2 * 10
digito2 = digito2 % 11

if digito2 > 9:
    digito2 = 0

cpf_gerado += str(digito2)
cpf_gerado = "".join([cpf_gerado[0:3], '.', cpf_gerado[3:6], '.', cpf_gerado[6:9], '-', cpf_gerado[9:]])

print(f'CPF GERADO COM SUCESSO: {cpf_gerado}')
