# Versão Incorreta

# Print("Bem-vindo ao curso de Python")
# nome = "Carlos
# print("Aluno: " + nome)
# print(Curso de Python)

# Versão Corrigida

print("Bem-vindo ao curso de Python") # A função print estava em maiúscula (Print). O Python é case sensitive e diferencia letras maiúsculas de minúsculas, Print gera erro porque a função não existe.
nome = "Carlos" # As aspas não estavam fechadas no final do valor da variável e isso gera um erro de sintaxe.
print("Aluno: " + nome)
print("Curso de Python") # Sem aspas o python lê como uma variável de sintaxe inválida já que não permite espaços.