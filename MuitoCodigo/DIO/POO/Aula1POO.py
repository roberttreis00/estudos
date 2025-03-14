class Bike:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Bi Bi')

    def parar(self):
        print('Parando...')
        print('Bicicleta Parada!')

    def correr(self):
        print('Pegando no tranco e indo')

    def batata(saco_de_batata):
        return saco_de_batata  # retorna a class

    # def __str__(self):  # O que retorna no objeto instanciado
    #     return f'Bike top hein {self.modelo}!'

    def __str__(self):
        return self.__class__.__name__


caloi = Bike('branco', 'Caloi', 2012,800)


caloi.correr()

print(caloi.modelo)
print(caloi)
print(caloi.batata())
