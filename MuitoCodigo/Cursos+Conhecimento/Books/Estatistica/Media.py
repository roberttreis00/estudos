from random import randint

conjunto_numeros = [randint(0, 100) for x in range(0, randint(0, 20))]


def media(populacao):
    print(populacao)
    n = len(populacao)
    soma_total = sum(populacao)

    mean = soma_total / n
    return mean


print(media(conjunto_numeros))
