# Retorno de valores das funções (return)
# Existem dois tipos de funções
# 1. Funções que podem somente executar ações. Ex.: print
# 2. Funções específicas para retornar valores.



def soma(x,y):                                                                             # 'return' retorna apenas um valor por função
    if x > 10:                                                                             # Se essa condição for true
        return [10,20]                                                                     # o código vai parar aqui 
    return x + y
# 'return' é usado sempre no final da função


# variavel = soma(1,2) 
# variavel = int('1')


primeiro = soma(2,2)
segundo = soma(3,3)
print(primeiro)                                                                            # como 'x' < '10' dentro da função vai ser return 2
print(segundo)                                                                             # como 'x' < '10' dentro da função vai ser return 2

print(soma(11,55))                                                                         # como 'x' > '10'dentro da funçao vai ser return 1












# variavel = print('Luiz')                                                                 # 'print' é uma função que não tem valor, ela exibe um valor
# variavel = None                                                                          # None significa um não valor 
# print(variavel is None)                                                                  # return 'None' is true 