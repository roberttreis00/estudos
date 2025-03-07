nomes = ['Jublie', 'Fulando', 1, 2, 3, 'Clicano']
tupla = 'Python é maneiro'

a, b, *_, c = nomes

print(a, b, c, *_)
print("  ".join(tupla))