# e media removendo o maior e menor valor
from random import randint

conjunto_numeros = [randint(0, 100) for x in range(0, randint(0, 20))]


def media_aparada(populacao):
    print(populacao)
    menor = min(populacao)
    maior = max(populacao)
    print(f'Maior: {maior} | Menor: {menor}')
    populacao.remove(menor)
    populacao.remove(maior)

    n = len(populacao)
    soma_total = sum(populacao)

    mean = soma_total / n
    return mean


print(media_aparada(conjunto_numeros))
