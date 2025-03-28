'''
Sistema bancario usando POO
- Privado
+ Metodo
'''
from abc import ABC, abstractmethod


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class PesssoaFiscia(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '001'
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    # Verificar se deu certo as trasações
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        ...

    @staticmethod
    def depositar(valor: float):
        ...


class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques


class Historico:
    def adicionar_transacao(self, Transacao):
        ...


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        ...


class Deposito(Transacao):
    def registrar(self, conta):
        ...


class Saque(Transacao):
    def registrar(self, conta):
        ...

