produtos = {"caneta": 2.5, "caderno": 18.0, "mochila": 120.0}
print(produtos.items)

com_desc = {n: p * 0.9 for n, p in produtos.items()}
caros = [n for n, p in produtos.items() if p > 10]

print(com_desc)
print(caros)