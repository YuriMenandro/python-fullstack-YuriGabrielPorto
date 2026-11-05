email = " joao.silva@EMPRESA.com.br "

# Remove os espaços do inicio e fim da string
email_sem_espacos = email.strip()

# Transforma a string em apenas minúsculas
email_minusculo = email_sem_espacos.lower()

# Divide o email a partir do @
divisao_email = email_minusculo.split("@")

usuario = divisao_email[0]

dominio = divisao_email[1]

print(f"Email sem espaços: {email_sem_espacos}")
print(f"Email em minusculas: {email_minusculo}")
print(f"Usuário: {usuario}")
print(f"Domínio: {dominio}")