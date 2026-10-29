"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno: Yuri Gabriel Porto Corrêa
Data    : 29/10/26
=============================================================

INSTRUÇÕES:
  1. Substitua <SEU NOME COMPLETO AQUI> e <DATA DE ENTREGA> acima.
  2. Implemente cada função no espaço indicado com # SUA SOLUÇÃO AQUI.
  3. Não apague os comentários de orientação.
  4. Execute o arquivo para testar suas soluções antes de enviar.
  5. Salve este arquivo como modulo-02/exercicios.py, na sua cópia
     do repositório do curso.

COMO EXECUTAR:
  python exercicios.py
=============================================================
"""


# ==============================================================
# EXERCÍCIO 01 – Classificador de Temperatura
# Conceitos: if / elif / else, float(), input()
# ==============================================================
def ex01_classificador_temperatura():
    """
    Lê uma temperatura em Celsius e exibe sua classificação.

    Faixas:
        < 0        → ❄️ Congelante
        0  a 14   → 🥶 Frio
        15 a 24   → 😊 Agradável
        25 a 34   → ☀️ Quente
        >= 35     → 🔥 Muito quente
    """
    # SUA SOLUÇÃO AQUI
    temperatura = float(input("Digite a temperatura (°C): "))

    if temperatura < 0:
        print("Congelante!")
    elif temperatura <= 14:
        print("Frio!")
    elif temperatura <= 24:
        print("Agradável!")
    elif temperatura <= 34:
        print("Quente!")
    else:
        print("Muito quente!")


# ==============================================================
# EXERCÍCIO 02 – Validador de Acesso
# Conceitos: if aninhado, comparação de strings
# ==============================================================
def ex02_validador_acesso():
    """
    Solicita usuário e senha e valida o acesso.

    Credenciais corretas:
        usuário → "admin"
        senha   → "iteam2025"
    """
    # SUA SOLUÇÃO AQUI
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if usuario == "admin":
        if senha == "iteam2025":
            print("Acesso Liberado")
        else:
            print("Acesso Negado")
    else:
        print("Acesso Negado")


# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    # SUA SOLUÇÃO AQUI
    numero = int(input("Digite um número inteiro: "))

    for i in range(1, 11):
        print(f"{numero} x {i:>2} = {numero * i:>5}")


# ==============================================================
# EXERCÍCIO 04 – Contador Regressivo
# Conceitos: while, print com end=
# ==============================================================
def ex04_contador_regressivo():
    """
    Solicita um número inteiro positivo e faz a contagem
    regressiva até 0, finalizando com '🚀 Lançamento!'.
    """
    # SUA SOLUÇÃO AQUI
    numero = int(input("Digite um número positivo: "))

    if numero <= 0:
        print("Digite um número inteiro positivo")
    else:
        while numero >= 0:
            print(numero, end=", ")
            numero -= 1
        print("Lançamento!")
        



# ==============================================================
# EXERCÍCIO 05 – Buscador com break
# Conceitos: for, break, enumerate()
# ==============================================================
def ex05_buscador_break():
    """
    Percorre o estoque e localiza 'Monitor', exibindo
    sua posição. Usa break ao encontrar o item.
    """
    estoque = ["Teclado", "Mouse", "Webcam", "Monitor", "Headset", "Notebook"]

    # SUA SOLUÇÃO AQUI
    
    for posicao, periferico in enumerate(estoque):
        if periferico == "Monitor":
            print(f"Posição {posicao}: {periferico}")
            break




# ==============================================================
# EXERCÍCIO 06 – Filtro de Dados com continue
# Conceitos: for, continue, None, acumuladores
# ==============================================================
def ex06_filtro_continue():
    """
    Percorre a lista de leituras, ignora os valores None
    com continue e calcula soma, média e total ignorado.
    """
    leituras = [12.5, None, 8.3, None, 15.0, 9.7, None, 11.2, 6.8, None]

    # SUA SOLUÇÃO AQUI
    soma = 0
    ignore = 0
    numeros_validos = 0

    for i in leituras:
        if i is None:
            ignore += 1
            continue

        soma += i
        numeros_validos += 1

    media = soma / numeros_validos
    print(f"Soma total: {soma}")
    print(f"Média: {media:.2f}")
    print(f"Total de valores ignorados: {ignore}")
        


# ==============================================================
# EXERCÍCIO 07 – Validação de Entrada com while
# Conceitos: while True, break, if/elif/else, float()
# ==============================================================
def ex07_validacao_nota():
    """
    Solicita a nota do aluno repetidamente até receber
    um valor válido (0.0 a 10.0), então exibe o conceito.

    Conceitos:
        9.0 a 10.0 → A – Excelente
        7.0 a 8.9  → B – Bom
        5.0 a 6.9  → C – Regular
        < 5.0      → D – Insuficiente
    """
    # SUA SOLUÇÃO AQUI
    while True:
        nota = float(input("Digite sua nota: "))

        if nota < 0 or nota > 10:
            print("Digite uma nota entre 0 e 10.")
        else:
            if nota >= 9:
                print("A - Excelente")
            elif nota >= 7:
                print("B - Bom")
            elif nota >= 5:
                print("C - Regular")
            else:
                print("D - Insuficiente")
            break



# ==============================================================
# EXERCÍCIO 08 – Calculadora com try/except
# Conceitos: try/except/else/finally, ValueError, ZeroDivisionError
# ==============================================================
def ex08_calculadora_segura():
    """
    Solicita dois números e uma operação (+, -, *, /).
    Trata: ValueError, ZeroDivisionError, operação inválida.
    Usa else para exibir o resultado e finally para encerrar.
    """
    # SUA SOLUÇÃO AQUI
    try:
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        operacao = input("Digite qual a operação deseja (+, -, *, /): ")

        if operacao == "+":
            resultado = n1 + n2
        elif operacao == "-":
            resultado = n1 - n2
        elif operacao == "*":
            resultado = n1 * n2
        elif operacao == "/":
            resultado = n1 / n2
        else:
            raise ValueError

    except ValueError:
        print("Erro: Operação ou número inválido.")      
    except ZeroDivisionError:
        print("Não é possível dividir um número por zero.")
        
    else:
        print(f"Resultado da operação: {resultado:.2f}")
        
    finally:
        print("Finalizando programa...")


# ==============================================================
# EXERCÍCIO 09 – Padrão Numérico com for aninhado
# Conceitos: for aninhado, range(), print com end=
# ==============================================================
def ex09_padrao_numerico():
    """
    Gera o triângulo crescente:
        1
        1 2
        1 2 3
        ...
        1 2 3 4 5

    Desafio extra: gera também o triângulo decrescente logo abaixo.
    """
    # SUA SOLUÇÃO AQUI
    for linha in range(1, 6):
        for numero in range(1, linha + 1):
            print(numero, end=" ")
        print()

    for linha in range(4, 0, -1):
        for numero in range(1, linha + 1):
            print(numero, end=" ")
        print()

    



# ==============================================================
# EXERCÍCIO 10 – Jogo de Adivinhação
# Conceitos: while, contador, random, if/elif/else
# ==============================================================
def ex10_jogo_adivinhacao():
    """
    O computador sorteia um número entre 1 e 100.
    O usuário tem 7 tentativas para adivinhar.
    A cada erro, indica se o número é maior ou menor.
    """
    import random
    numero_secreto = random.randint(1, 100)
    # SUA SOLUÇÃO AQUI
    print("Adivinhe o número sorteado entre 1 e 100")
    contador = 1
    acerto = False
    while contador <= 7:
        tentativa = int(input(f"Tentativa {contador}: "))
        contador += 1

        if tentativa > numero_secreto:
            print(f"Tente um número menor que {tentativa}")
        elif tentativa < numero_secreto:
            print(f"Tente um número maior que {tentativa} ")
        else:
            print("Parabéns você acertou")
            acerto = True
            break

    if not acerto:
        print(f"O número sorteado era {numero_secreto}. Tente Novamente")





# ==============================================================
# EXERCÍCIO 11 – Verificador de Número Primo
# Conceitos: for, break, try/except, otimização com √n
# ==============================================================
def ex11_numero_primo():
    """
    Solicita um número inteiro positivo e verifica se é primo.
    Usa break ao encontrar o primeiro divisor.
    Trata ValueError e números negativos/zero.
    Otimização: verifica divisores somente até √n.
    """
    # SUA SOLUÇÃO AQUI
    import math

    try:
        numero = int(input("Digite um número positivo: "))
        if numero <= 0:
            raise ValueError
    except ValueError:
        print("Digite um número positivo inteiro")
    else:
        primo = numero > 1
        raiz_quadrada = int(math.sqrt(numero))
        for i in range(2, raiz_quadrada + 1):
            if numero % i == 0:
                primo = False
                break
        if primo:
            print(f"{numero} é primo")
        else:
            print(f"{numero} não é primo")




    


# ==============================================================
# EXERCÍCIO 12 – Analisador de Senha Forte
# Conceitos: for, if, booleanos, métodos de string
# ==============================================================
def ex12_analisador_senha():
    """
    Analisa se uma senha atende aos critérios de segurança:
        - Mínimo 8 caracteres
        - Pelo menos 1 maiúscula
        - Pelo menos 1 minúscula
        - Pelo menos 1 dígito
        - Pelo menos 1 caractere especial: !@#$%^&*

    Exibe relatório com ✅ ou ❌ para cada critério.
    """
    # SUA SOLUÇÃO AQUI
    minimo_caractere = False
    tem_maiuscula = False
    tem_minuscula = False
    tem_um_digito = False
    tem_caractere_especial = False

    senha = input("Digite uma senha: ")

    if len(senha) >= 8:
        minimo_caractere = True

        
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_um_digito = True
        elif caractere in "!@#$%^&*":
            tem_caractere_especial = True


    print(f"Mínimo de 8 caracteres: {"✅" if minimo_caractere else  "❌"}")
    print(f"Pelo menos 1 maiúscula: {"✅" if tem_maiuscula else  "❌"}")
    print(f"Pelo menos 1 minúscula: {"✅" if tem_minuscula else  "❌"}")
    print(f"Pelo menos 1 dígito: {"✅" if tem_um_digito else  "❌"}")    
    print(f"Pelo menos 1 caractere especial: {"✅" if tem_caractere_especial else  "❌"}")        
            




# ==============================================================
# EXERCÍCIO 13 – Simulador de Caixa Eletrônico
# Conceitos: while, //, if/else, try/except
# ==============================================================
def ex13_caixa_eletronico():
    """
    Solicita um valor de saque (múltiplo de R$10, máx R$3.000).
    Calcula o menor número de cédulas: R$200, R$100, R$50, R$20, R$10.
    Trata entradas inválidas.
    """
    cedulas = [200, 100, 50, 20, 10]

    # SUA SOLUÇÃO AQUI
    try:
        valor = int(input("Digite o valor do saque: "))
    except ValueError:
        print("Digite um número inteiro")
    else:
        if valor > 3000:
            print("Digite o valor que deseja sacar até R$3.000")
        elif valor <= 0:
            print("Saque inválido: não é possível sacar um valor menor ou igual a zero")
        elif valor % 10 != 0:
            print("Digite um número múltiplo de 10")
        else:
            total_cedulas = 0
            cont = 0

            while valor != 0:
                if valor >= cedulas[cont]:
                    total_cedulas += valor // cedulas[cont]
                    quant_notas = valor // cedulas[cont]
                    print(f"Notas de {cedulas[cont]}: {quant_notas}")
                    valor = valor % cedulas[cont]
                cont+= 1
            print(f"O menor número de cédulas é: {total_cedulas}")
            

# ==============================================================
# EXERCÍCIO 14 – Leitura de Múltiplos Dados com Tratamento
# Conceitos: while, break, continue, try/except, pass
# ==============================================================
def ex14_leitura_notas_turma():
    """
    Lê notas de uma turma até o usuário digitar 'fim'.
    Ignora notas inválidas com continue + mensagem de aviso.
    Ao encerrar, exibe: total, média, maior e menor nota.
    """
    notas = []

    # SUA SOLUÇÃO AQUI
    while True:
        entrada = input("Digite uma nota: ")

        if entrada == "fim": # Minha condição para finalizar o loop.
            break   

        try:
            nota = float(entrada) # Conversão da nota para float (número real).

        except ValueError: # Mostra uma mensagem caso der ValueError e continua o loop.
            print("Nota inválida")
            continue

        if nota < 0 or nota > 100: # Verifica se a nota está entre 0 e 100, se for falso exibe uma mensagem e continua o loop.
            print("O valor da nota deve ser entre 0 e 100")
            continue

        notas.append(nota) # Adiciona nota a lista

    if len(notas) == 0: # Exibe uma mensagem caso nenhuma nota for digitada
        print("Nenhuma nota digitada.")
    else:
        print(f"Quantidade total de notas: {len(notas)}")
        print(f"Soma das notas: {sum(notas)}")
        print(f"Média: {sum(notas) / len(notas):.2f}")
        print(f"Maior nota: {max(notas)}")
        print(f"Menor nota: {min(notas)}")

# ==============================================================
# EXERCÍCIO 15 – Desafio Final: Menu de Sistema
# Conceitos: while True, if/elif/else, break, continue, try/except
# ==============================================================
def ex15_menu_sistema():
    """
    Menu interativo que permanece ativo até o usuário sair.

    Opções:
        [1] Conversor de temperatura (Celsius → Fahrenheit)
        [2] Verificador de número primo (versão simplificada)
        [3] Analisador de senha (apenas comprimento e dígito)
        [4] Calculadora segura (só +, -, *, /)
        [0] Sair

    Usa try/except em toda entrada do usuário.
    """
    while True:
        print("\n" + "=" * 29)
        print("   SISTEMA ITEAM - MENU    ")
        print("=" * 29)
        print("[1] Conversor de temperatura")
        print("[2] Verificador de número primo")
        print("[3] Analisador de senha")
        print("[4] Calculadora segura")
        print("[0] Sair")
        print("=" * 29)

        # SUA SOLUÇÃO AQUI — leia a opção e implemente cada funcionalidade
        try:
            opcao = int(input("Digite uma opção: "))

            if opcao < 0 or opcao > 4:
                raise ValueError    
        except ValueError:
            print("Digite uma opção válida.")
        else:
            match opcao:
                case 0:
                    print("Finalizando o programa")
                    break
                case 1:
                    try:
                        celsius = float(input("Digite o valor da temperatura (°C): "))
                    except ValueError:
                        print("Erro: digite um número real")
                    else:
                        fahrenheit = (celsius * 9 / 5) + 32
                        print(f"{celsius:.2f} °C = {fahrenheit:.2f} °F")
                case 2:
                    try:
                        numero = int(input("Digite um número inteiro positivo: "))
                        if numero <= 0:
                            raise ValueError
                    except ValueError:
                        print("Erro: digite um número inteiro positivo")
                    else:
                        primo = numero > 1
                        for i in range(2, numero):
                            if numero % i == 0:
                                primo = False
                                break
                        if primo:
                            print(f"{numero} é primo")
                        else:
                            print(f"{numero} não é primo")
                case 3:
                    senha = input("Digite uma senha: ")
                    tamanho = len(senha)

                    digito = False
                    for caractere in senha:
                        if caractere in "0123456789":
                            digito = True
                            break
                    print(f"Mínimo de 8 caracteres: {"✅" if tamanho >= 8 else "❌"}")
                    print(f"Pelo menos 1 dígito: {"✅" if digito else "❌"}")
                case 4:
                    try:
                        n1 = float(input("Digite o primeiro número: "))
                        n2 = float(input("Digite o segundo número: "))
                        operacao = input("Digite uma operação (+, -, *, /): ")

                        if operacao == "+":
                            resultado = n1 + n2
                        elif operacao == "-":
                            resultado = n1 - n2
                        elif operacao == "*":
                            resultado = n1 * n2
                        elif operacao == "/":
                            resultado = n1 / n2
                        else:
                            raise ValueError

                    except ValueError:
                        print("Digite um número e uma operação válida!")
                    except ZeroDivisionError:
                        print("Não é possível dividir por zero.")
                    else:
                        print(f"Resultado: {resultado:.2f}")
                


                        



            



# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno: Yuri Gabriel Porto Corrêa")
    print("=" * 50)

    # Descomente linha por linha conforme for resolvendo:
    ex01_classificador_temperatura()
    ex02_validador_acesso()
    ex03_tabuada()
    ex04_contador_regressivo()
    ex05_buscador_break()
    ex06_filtro_continue()
    ex07_validacao_nota()
    ex08_calculadora_segura()
    ex09_padrao_numerico()
    ex10_jogo_adivinhacao()
    ex11_numero_primo()
    ex12_analisador_senha()
    ex13_caixa_eletronico()
    ex14_leitura_notas_turma()
    ex15_menu_sistema()
