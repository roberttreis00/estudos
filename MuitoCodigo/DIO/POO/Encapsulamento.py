# proteção de acesso

class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def extrato(self):
        print(self._saldo)


c1 = Conta()
c1.depositar(100)
c1.extrato()
print(c1._)
