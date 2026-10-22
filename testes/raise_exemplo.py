idade = -5

try:
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    print("Idade Válida")
except ValueError as erro:
    print(f"Erro: {erro}")