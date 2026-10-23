nome = "Mariana Souza"
cargo = "Analista de Dados"
salario = 7850.50
salario_br = f"{salario:,.2f}".replace(".", "x").replace(",", ".").replace("x", ",") #Troca 7,850.50 --> 7,850x50 --> 7.850x50 --> 7.850,50
tempo = 3
linha = "=" * 30
ficha = "FICHA DO FUNCIONÁRIO"

print(linha)
print(f"{ficha:^30}")
print(linha)
print(f"Nome   : {nome}")
print(f"Cargo  : {cargo}")
print(f"Salário: R$ {salario_br}")
print(f"Tempo  : {tempo} ano(s) de empresa")
print(linha)