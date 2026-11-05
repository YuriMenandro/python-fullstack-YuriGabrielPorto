import json

aluno = {
    "nome": "Pedro Henrique",
    "idade": 22,
    "curso": "Full Stack",
    "ativo": True,
    "notas": [8.5, 9.0, 7.5]
}
# Converte o dicionário para json com identação
conversao_json = json.dumps(aluno, indent=2)
print(conversao_json)

# Converte json para dicionário
conversao_dicionario = json.loads(conversao_json)
print(conversao_dicionario)

media = sum(conversao_dicionario['notas']) / len(conversao_dicionario['notas'])
print(f"Aluno: {conversao_dicionario['nome']}")
print(f"Média: {media:.2f}")