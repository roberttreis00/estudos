s1 = set()
s1.add(1)  # adicionar um valor
s1.update([1, 2, 3, 4])  # adicionar uma iterador valor por valor no set

s1.discard(1)  # elimina o valor

print(s1)
# ----------------------------------------------------------------------------------------------------
# Operadores

s1 = {2, 1, 3}
s2 = {2, 3, 4}

print(s1 | s2)  # união lembrando que set não repete valor
print(s1 & s2)  # Intersecção valores contem tanto em A quanto em B
print(s1 - s2)  # Itens presentes apenas no set da esqueda
print(s1 ^ s2)  # Intens que não estão em ambos
