def soma(x, y, z=None):
    if z is None:
        print('Você não passou Z')
        print(f'{x=} | {y=}')
    else:
        print(f'Valor de Z {z=}')
        print(f'{x=} | {y=} | {z=}')


soma(1, 2)
soma(1, 2, 3)
