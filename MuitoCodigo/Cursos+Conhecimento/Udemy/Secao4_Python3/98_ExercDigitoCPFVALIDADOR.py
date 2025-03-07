import re

cpf = input('Digite um CPF: ')
soma_conta1 = 0
soma_conta2 = 0
cpf_digitos = cpf.replace('.', '').replace('-', '')

for digito, n in enumerate(range(10, 1, -1)):
    conta = int(cpf_digitos[digito]) * n
    soma_conta1 += conta

for digito, n in enumerate(range(11, 1, -1)):
    conta = int(cpf_digitos[digito]) * n
    soma_conta2 += conta

digito1 = soma_conta1 * 10
digito1 = digito1 % 11

digito2 = soma_conta2 * 10
digito2 = digito2 % 11

if digito1 > 9:
    digito1 = 0

if digito2 > 9:
    digito2 = 0

print(f'Primeiro digito do CPF: {digito1}')
print(f'Segundo digito do CPF: {digito2}')

print(re.sub("[^0-9]", "", cpf))  # Substituir valores usando RE
