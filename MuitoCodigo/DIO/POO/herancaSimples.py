class Veiculo:
    def __init__(self, cor, placa, rodas):
        self.cor = cor
        self.placa = placa
        self.rodas = rodas

    def ligar_motor(self):
        print('Ligando motor')

    def __str__(self):
        return self.cor


class Moto(Veiculo):
    ...


class Caminhao(Veiculo):
    def __init__(self, cor, placa, rodas, carregado):
        super().__init__(cor, placa, rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print('Sim' if self.carregado else 'Não', 'Estou carregado')


c1 = Caminhao('branco', 'bcl-2563', 8, True)
print(c1.esta_carregado())
print(c1)
