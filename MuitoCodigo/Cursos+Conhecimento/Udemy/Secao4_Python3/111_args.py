x, y, z, *args = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


def recebe_tudo(x, y, z, *args):
    print(x, y, z, args)


recebe_tudo(1, 2, 5, args)


def soma(*args):
    soma_todos = sum(args)
    print(f'A Soma de tudo da {soma_todos}')
    return soma_todos


soma(1, 90, 5)
