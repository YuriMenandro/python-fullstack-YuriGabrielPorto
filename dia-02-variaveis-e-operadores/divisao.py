caminhao_carga_maxima = 850
peso_caixa = 32

quant_caixas = caminhao_carga_maxima // peso_caixa

peso_restante = caminhao_carga_maxima % peso_caixa

print(f"Quantidade de caixas que cabem no caminhão: {quant_caixas}")
print(f"Peso restante: {peso_restante} kg.")