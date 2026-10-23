dobrados = []

for n in range(1, 6):
    dobrados.append(n * 2)

#list comprehension
dobrados = [n * 2 for n in range(1, 6)]
pares = [n for n in range(10) if n % 2 == 0]

print(dobrados, pares)