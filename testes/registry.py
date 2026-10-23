operacoes = {
    "soma": lambda a, b: a + b,
    "subtracao": lambda a, b: a - b,
    "multiplicacao": lambda a, b: a * b
}

operacao, a, b = "soma", 6, 7
funcao = operacoes.get(operacao)
print(funcao(a, b) if funcao else "Operação Inválida")

operacoes["divisao"] = lambda a, b: a / b
print(operacoes["divisao"] (8, 2))