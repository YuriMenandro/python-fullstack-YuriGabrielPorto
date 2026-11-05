def saudacao(nome):
    """
        Retorna uma mensagem de boas-vindas personalizada.
    
        Args:
            nome (str): Nome da pessoa a ser saudada.
    
        Returns:
            str: String com a mensagem de boas-vindas.
    
        Example:
            >>> saudacao("Ana")
            'Olá, Ana! Seja bem-vinda ao curso.'
        """
    nome = (f"Olá {nome}! Seja bem vindo ao curso.")
    return nome
    

print(saudacao("Carlos"))
print(saudacao("Ana"))
print(saudacao("João"))