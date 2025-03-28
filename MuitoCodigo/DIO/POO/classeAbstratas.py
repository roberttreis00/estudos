from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):

    @abstractmethod  # isso obriga a class que herda a implementar esses metodos
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    # Nova forma de uso
    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando TV')

    def desligar(self):
        print('Desligando TV')

    @property
    def marca(self):
        return 'Paraguai'


c1 = ControleTV()
c1.ligar()
c1.desligar()
print(c1.marca)