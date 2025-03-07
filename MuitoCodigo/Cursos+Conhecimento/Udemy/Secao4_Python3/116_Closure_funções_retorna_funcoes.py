# Função que retorna função
def create_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'

    return saudar


def bom_dia(nome):
    return create_saudacao('Bom dia', nome)


print(bom_dia('Robertt')())
