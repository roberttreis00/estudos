def numero_multiplica(numero, qtd):
    return numero * qtd


print(numero_multiplica(4, 3))


# ------------------------------------------------------------------------------------------------
def gera_funcao(qtd):
    def multiplicar(numero):
        return numero * qtd
    return multiplicar


triplicar = gera_funcao(3)
print(triplicar(3))
