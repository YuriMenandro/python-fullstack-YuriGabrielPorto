n1 = float(input("nota1: "))
n2 = float(input("nota2: "))
n3 = float(input("nota3: "))

media = (n1 + n2 + n3) / 3
print(f"Média: {media:.2f}")
print(f"Aprovado?  {media >=7}")
print(f"Recuperação? {media<7}")


