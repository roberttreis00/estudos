class ContaBancaria:
    def __init__(self, nome_titular):
        self.nome_titular = nome_titular
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f'+{valor}')

    def sacar(self, valor):
        if self.saldo >= abs(valor):
            self.saldo += valor
            self.operacoes.append(f'{valor}')
        else:
            self.operacoes.append(f'Saque não permitido')

    def extrato(self):
        print(f'Operações: {", ".join(self.operacoes)};', f'Saldo: {self.saldo}')


nome_titular = input().strip()
# nome_titular = 'Robertt'

conta = ContaBancaria(nome_titular)

# entrada_transacoes = '100, -50, 200, -300'
entrada_transacoes = input().strip()

transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)
    else:
        conta.sacar(valor)

conta.extrato()
