def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y
#
#
# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#
#     return multiplica


# print(executa(lambda x, y: x + y, 5, 5))

multiplica = executa(lambda m: lambda n: n * m, 2)

print(multiplica(10))
