nome_produto = input("Digite o nome do produto: ")
qtd = int(input("Digite a quantidade de produtos: "))
preco = float(input("Digite o preço do produto: "))

subtotal = qtd * preco
imposto = subtotal * 0.12
total = subtotal + imposto

print(f"{" NOTA FISCAL ":=^23}")
print(f"Produto   : {nome_produto}")
print(f"Quantidade: {qtd} unidade(s)")
print(f"Preço Unit: R$ {preco:.2f}")
print(f"Subtotal  : R$ {subtotal:.2f}")
print(f"Imposto   : R$ {imposto:.2f}")
print(f"Total     : {total:.2f}")
print(f"{"":=^23}")
