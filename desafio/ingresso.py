idade = int(input("Idade: "))
est = input("Estudante (s/n)?") == "s"

if idade < 12 or idade >= 60:
    preco = 10
elif est:
    preco = 15
else:
    preco = 30
print(f"Ingresso: R$ {preco:.2f}")