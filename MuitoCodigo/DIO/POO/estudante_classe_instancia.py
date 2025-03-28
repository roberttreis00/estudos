class Estudante:
    nome_escola = 'DIO'

    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso

    def __str__(self):
        return f'{self.nome} faz o curso {self.curso} na escola {self.nome_escola}'


b = Estudante('Carol', 'Informatica')
