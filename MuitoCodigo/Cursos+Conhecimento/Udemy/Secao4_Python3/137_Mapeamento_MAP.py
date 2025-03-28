produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

y = list(map(lambda x: x['preco'] * 1.10, produtos))

print(y)
