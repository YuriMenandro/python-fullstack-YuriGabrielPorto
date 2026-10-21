frase = input("Digite uma frase: ")
vogais = 0
print(frase)
for letra in frase:
    if letra in "aeiouAEIOU":
        vogais += 1
print(f"Vogais: {vogais}")

