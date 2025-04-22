# numeros primos com yield

def conferir_numero_primo(n):
    # Econtrar os divisores
    qtd_divisores = 0
    for x in range(1, n+1):
        if n % x == 0:
            qtd_divisores += 1

    if qtd_divisores > 2:
        return False
    else:
        return n


def numero_primos(contador=1, qtd_numeros_primos=1):
    n = 1

    while contador <= qtd_numeros_primos:
        n += 1
        y = conferir_numero_primo(n)
        if y:
            contador += 1
            yield y


numeros_primos_lista = []

for numero_primo in numero_primos(qtd_numeros_primos=14**2):
    print(numero_primo)
    numeros_primos_lista.append(numero_primo)

print()
print(len(numeros_primos_lista))
