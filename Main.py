def gerar_variacoes_senha(senha):
    variacoes = []
    
  
    variacoes.append(senha)

    variacoes.append(senha.lower())
  
    variacoes.append(senha.upper())
    
    variacoes.append(senha.capitalize())
    
    # Adiciona uma variação com um número aleatório de 0 a 9 no meio
    for i in range(10):
        for j in range(len(senha)):
            senha_com_numero = senha[:j] + str(i) + senha[j+1:]
            variacoes.append(senha_com_numero)
    
    return variacoes
  
def repetir_codigo(senha):
    for _ in range(1000):
        todas_variacoes = gerar_variacoes_senha(senha)
        for variacao in todas_variacoes:
            print(variacao)

entrada = input("Digite uma senha: ")
repetir_codigo(entrada)
