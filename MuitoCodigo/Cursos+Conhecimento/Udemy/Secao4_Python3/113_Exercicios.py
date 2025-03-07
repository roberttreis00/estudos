# função que multiplica todos os números

def multi(*args):
    cont = 1

    for numero in args:
        cont *= numero

    print(cont)
    return cont


def impar_par(numero):
    par_ou_impar = 'PAR' if numero % 2 == 0 else 'IMPAR'

    cont = numero % 2

    if not cont:
        print(f'Seu número é PAR {numero=}')
    else:
        print(f'Seu número é IMPAR {numero}')

    return par_ou_impar


multi(1, 2, 3, 4, 5)
impar_par(63)
