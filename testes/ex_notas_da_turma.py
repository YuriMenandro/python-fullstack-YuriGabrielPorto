notas = []

for i in range(1, 4):
    notas.append(float(input(f"Nota {i}: ")))

    print(max(notas), min(notas))
    print(f"Média: {sum(notas) / len(notas):.2f}")
    print(sorted(notas, reverse=True))