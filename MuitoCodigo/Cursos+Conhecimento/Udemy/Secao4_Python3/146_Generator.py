import sys

generator = (n for n in range(100000000000000000000000))
lista = [n for n in range(100000000)]

print(next(generator))
print(sys.getsizeof(generator))
print(sys.getsizeof(lista))
