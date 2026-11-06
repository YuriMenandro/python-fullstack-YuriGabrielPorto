def converter_moeda(real: float) -> tuple[float, float]:
    """
    Retorna uma tupla com a conversão do real para o dólar e euro.
        
            Args:
                real: valor em reais para conversão.
        
            Returns:
                tuple: uma tupla com o valor da conversão em dólar e euro.
        
            Example:
                >>> converter_moeda(100)
                '(19.41747572815534, 17.921146953405017)'
    """

    valor_usd, valor_eur = real / 5.15, real / 5.58
    resultado = (valor_usd, valor_eur)
    return resultado

real = float(input("Digite um valor em reais: "))
resultado = converter_moeda(real)
print(f"Dólar: ${resultado[0]:.2f} | Euro: €{resultado[1]:.2f}")


