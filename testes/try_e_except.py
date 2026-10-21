try:
    numero = int(input("Digite um número: "))
    resultado = 1 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: digite uma número válido")
except ZeroDivisionError:
    print("Erro: não é possível dividir por 0.")
else:
    print("Sucesso!")
finally:
    print("Fim do programa")