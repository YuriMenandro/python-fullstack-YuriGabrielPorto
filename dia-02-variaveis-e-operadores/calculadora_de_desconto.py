valor_compra = float(input("Digite o valor da compra: "))

desconto = valor_compra * 0.1
valor_final = valor_compra - desconto

print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto recebido: R$ {desconto}")
print(f"Valor final da compra: R$ {valor_final:.2f}")