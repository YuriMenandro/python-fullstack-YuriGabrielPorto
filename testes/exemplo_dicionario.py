alunos = [
    {"nome": "Ana", "nota": 9.0},
    {"nome": "Bruno", "nota": 6.7},
]

total = 0
for aluno in alunos:
    print(aluno["nome"], aluno["nota"])
    total += aluno["nota"]
print(f"Média: {total / len(alunos):.2f}")