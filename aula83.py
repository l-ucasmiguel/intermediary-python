# Empacotamento e desempacotamento de dicionários

"""
No código abaixo, primeiro são definidas duas variáveis 'a' e 'b', que recebem os valores '1' e '2', respectivamente.
Em seguida, ocorre uma operação de empacotamento e desempacotamento de valores, por meio da expressão 'a,b = b,a'. Nessa expressão,
o Python empacota os valores de 'b' e 'a' em uma tupla, troca as posições dos valores e, em seguida, desempacota os valores da tupla
de volta em 'a' e 'b', trocando assim seus valores. após a execução dessa expressão, a variável 'a' passa a ter o valor '2' e a variável
'b' passa a ter o valor '1'. Por fim, a função 'print' é usada para exibir os valores de 'a' e 'b', resultando em '2' '1' sendo impresso no
console."""


# # EXEMPLO:
# a,b = 1,2                                                                  # 'a' e 'b' recebem os valores '1' e '2' respectivamente. 
# a,b = b,a                                                                  # 'a' vai receber o valor de 'b', no caso '2', e 'b' recebe o valor de 'a' no caso '1'
# print(a,b)





# # EXEMPLO PRÁTICO 01
# pessoa = {                                                                 # Dict
#     'nome':'Alice',
#     'sobrenome':'Souza'
# }


# a,b  = pessoa.values()                                                     # Neste caso usando 'pessoa.values()', 'a' recebe a chave 'nome' e 'b' recebe a chave 'sobrenome'
# print(a,b,'\n')


# (a1,a2), (b1,b2) = pessoa.items()                                          # Desempacotamento internamente
# print(a1,a2)
# print(b1,b2,'\n')


# for chave, valor in pessoa.items():                                        # Mesma coisa utilizando 'for'
#     print(chave, valor)





# EXEMPLO PRÁTICO 02
# Criando dicionário
pessoa = {
    'nome':'Alice',
    'sobrenome':'Souza'
}

dados_pessoa = {
    'idade':16,
    'altura':1.6,
}



# """
# args e kargs:
#     *args     - argumentos não nomeados
#     **kwars   - argumentos nomeados, 'kwargs' keyword arguments
# """



# Desempacotamento de um dicionário
pessoa_completa = {**pessoa,**dados_pessoa}                               # Para extrair dados de um dicionário utilizamos '**'
# print(pessoa_completa)
print()



# Função que mostra o que são os argumentos nomeados e não nomeados
def mostro_argumentos_nomeados(*args, **kwargs):                          # Empacotando os argumentos
    print('NÃO NOMEADOS:', args)                                          # Se eu mandar algum argumento não nomeado, ele vem aqui em 'args'

    for chave, valor in kwargs.items():
        print(chave,valor)                                                # Argumento nomeado 'kwargs' é aqui



mostro_argumentos_nomeados(1,2, nome='Joana',idade=29)
print()
mostro_argumentos_nomeados(**pessoa_completa)                             # Desempacotando uma chamada de função
print()


configs = {
    'arg1':1,
    'arg2':2,
    'arg3':3,
    'arg4':4,
}

mostro_argumentos_nomeados(15, 20, **configs)