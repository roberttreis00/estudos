# Funções de primeira classe | Podemos colocar uma funcao em uma variavel x = funcao

def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(funcao, *args):  # Higher-order_function
    return funcao(*args)


x = executa(saudacao, 'Bom dia', 'Irineu')  # First-Class Functions

print(x)

