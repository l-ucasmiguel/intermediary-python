# Empacotamento e desempacotamento de dicinánrios

"""
No código abaixo, primeiro são definidas duas variáveis 'a' e 'b', que recebem os valores '1' e '2', respectivamente.
Em seguida, ocorre uma operação de empacotamento e desempacotamento de valores, por meio da expressão 'a,b = b,a'. Nessa expressão,
o Python empacota os valores de 'b' e 'a' em uma tupla, troca as posições dos valores e, em seguida, desempacota os valores da tupla
de volta em 'a' e 'b', trocando assim seus valores. após a execução dessa expressão, a variável 'a' passa a ter o valor '2' e a variável
'b' passa a ter o valor '1'. Por fim, a função 'print' é usada para exibir os valores de 'a' e 'b', resultando em '2' '1' sendo impresso no
console."""

# a,b = 1,2                                                # 'a' e 'b' recebem os valores '1' e '2' respectivamente. 
# a,b = b,a                                                # 'a' vai receber o valor de 'b', no caso '2', e 'b' recebe o valor de 'a' no caso '1'
# print(a,b)




# pessoa = {                                               # Dict
#     'nome':'Alice',
#     'sobrenome':'Souza'
# }


# a,b  = pessoa.values()                                   # Usando o método 'values' para pegar os valores, quando não é passado um método, é passado somente as chaves
# print(a,b)

# print()
# print('-'*100)
# print()

# (a1,a2), (b1,b2) = pessoa.items()                        # Desempacotamento interno
# print(a1,a2)
# print(b1,b2)

# print()
# print('-'*100)
# print()

# for chave, valor in pessoa.items():                      # Mesma coisa utilizando 'for'
#     print(chave, valor)




pessoa = {
    'nome':'Alice',
    'sobrenome':'Souza'
}

dados_pessoa = {
    'idade':16,
    'altura':1.6,
}

# Desempacotamento de um dicionário
pessoa_completa = {**pessoa,**dados_pessoa}                # Para extrair dados de um dicinário utilizamos '**'
# print(pessoa_completa)

# args e kargs
# *args     - argumentos não nomeados
# **kwars   - argumentos nomeados, 'kwargs' keyword arguments 

def mostro_argumentos_nomeados(*args, **kwargs):                    # Empacotando os argumentos
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave,valor)                                          # Argumento nomeado KWARGS


# mostro_argumentos_nomeados(1,2, nome='Joana',qualquer='teste')
# mostro_argumentos_nomeados(**pessoa_completa)                     # Desempacotando uma chamada de função


configs = {
    'arg1':1,
    'arg2':2,
    'arg3':3,
    'arg4':4,
}

mostro_argumentos_nomeados(**configs)