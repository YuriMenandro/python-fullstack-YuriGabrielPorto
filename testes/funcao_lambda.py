soma = lambda x, y: x + y
quadrado = lambda x: x ** 2

print(soma(5, 3), quadrado(3))

pessoas = [("Ana", 67), ("Bruno", 21), ("Carla", 35)]
print(sorted(pessoas, key = lambda p: p[1]))