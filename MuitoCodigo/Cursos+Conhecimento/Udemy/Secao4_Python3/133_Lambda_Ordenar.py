from random import randint

y = [randint(0, 100) for x in range(0, 10)]

print(y)
print(list(filter(lambda x: x < 50, y)))
print('-' * 50)

# ---------------------------------------------------------------------------------------------

lista_nomes = [
    {'nome': 'Luiz', 'Sobrenome': 'Miranda'},
    {'nome': 'Robertt', 'Sobrenome': 'Siqueira'},
    {'nome': 'Ana', 'Sobrenome': 'Carla'},
]

#
lista_nomes.sort(key=lambda x: x['Sobrenome'])

print(lista_nomes)
