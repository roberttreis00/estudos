class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # metodos de class
    @classmethod
    def criar_idadei_apartir_data(cls, ano, nome):
        idade = 2025 - ano
        return cls(nome, idade)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18


p = Pessoa('Robertt', 24)
print(p.nome, p.idade)

# Assim ele cria uma instancia do objeto uma unica vez inves de
# Pessoa().criar()

p2 = Pessoa.criar_idadei_apartir_data(2000, 'Irineu')
print(p2.nome, p2.idade, p2.maior_idade(p2.idade))
