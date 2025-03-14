class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def __del__(self):
        print('Apagando')

    def falar(self):
        print('auau')


c = Cachorro('Jubileu', 'Vagabundo')
c.falar()
print(c)
