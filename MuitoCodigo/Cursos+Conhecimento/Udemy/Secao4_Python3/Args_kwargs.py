dados1 = {
    'nome': 'Jubileu',
    'curso': 'informatica'
}

dados2 = {
    'fruta': 52,
    'coisa': 'grande'
}


def empacotar_tupla(*args):
    print(args)


def desempacotar(**kwargs):
    print(kwargs)


desempacotar(dados1=dados1)
