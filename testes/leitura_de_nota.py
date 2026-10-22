while True:
    texto = input("Nota (0 a 10): ")
    try:
        nota = float(texto)
    except ValueError:
        print("Apenas números")
        continue
    if 0 <= nota <= 10:
        break
    print("Fora da faixa")
print(f"Nota: {nota}")


