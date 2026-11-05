capital_inicial = float(input("Digite o capital inicial: "))
taxa_juros = float(input("Digite a taxa de juros ao mês: "))
qnt_meses = int(input("Digite o período (tempo) em meses: "))

montante = capital_inicial * (1 + (taxa_juros / 100) * qnt_meses)
juros_total = montante - capital_inicial



print(f"Capital inicial: {capital_inicial:.2f} ")
print(f"Taxa: {taxa_juros:.2f}")
print(f"Período: {qnt_meses}")
print(f"Juros totais: {juros_total:.2f}")
print(f"Montante: {montante:.2f}")