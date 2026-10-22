numeros = [1, 2, 2, 3, 3, 4, 5, 5,]

conjunto = set(numeros)
print(conjunto, len(conjunto))
conjunto.add(6)
conjunto.discard(4)
print(sorted(conjunto), 3 in conjunto)