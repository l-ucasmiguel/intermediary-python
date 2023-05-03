"""
Exercício
Crie uma função que tem como objetivo encontrar o primeiro número duplicado em uma lista de inteiros.

Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1]    -> 1, 2 e 3 são duplicados, mas o '3' é o primeiro a se repetir (Retorne 3)
        [1, 2, 3, 4, 5, 6]        -> Não tem duplicados (Retorne -1) 
        [1, 4, 9, 8, ->9<-, 4, 8] -> 4,9,e 8 são duplicados, mas o '9' é o primeiro a se repetir (Retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros = [                             # List que tem várias lists dentro 
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],                        # retorna -1
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],                         # retorna 9
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],                         # retorna 2
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],                         # retorna 8
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],                        # retorna 8
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],                         # retorna 2
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],                      # retorna 2
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],                         # retorna 1
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],                        # retorna 1
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],                         # retorna 2
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],                         # retorna 5
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],                        # retorna -1
]


# Define a função que encontra o primeiro número duplicado na lista
def encontra_primeiro_duplicado(lista_de_inteiros):         # Criando função que usa como parâmetro (lista_de_inteiros)
    numeros_checados = set()                                # É criado uma variável 'numeros_checados' que recebe um 'set()' set vazio, que vai armazenar os números já verificados
    primeiro_duplicado = -1                                 # A variável 'primeiro_duplicado' recebe o valor padrão de -1

    for numero in lista_de_inteiros:                        # 'numero' vai percorrer cada índice na 'lista_de_inteiros', que é a lista atual fora da função, no 'for' global
        if numero in numeros_checados:                      # Se 'numero' que é o índice atual da 'lista_de_inteiros' já estiver no set 'numeros_checados'
            primeiro_duplicado = numero                     # a variável 'primeiro_duplicado' recebe o 'numero' repetido e para
            break
                                                            
        numeros_checados.add(numero)                        # Enquanto o 'numero' não se repetir, 'numero' é adicionado em 'numeros_checados'

    return primeiro_duplicado                               # Nesta linha é retornado o 'primeiro_duplicado', com o valor repetido, ou o valor padrão '-1' caso não tenha repetido


for lista in lista_de_listas_de_inteiros:                   # 'lista' vai percorrer 'lista_de_listas_de_inteiros'
    print(
        lista,                                              # o 'print' vai imprimir a 'lista' atual na tela
        encontra_primeiro_duplicado(lista)                  # aqui vai chamar a função 'encontra_primeiro_duplicado' passando 'lista' como argumento e retornando o valor da função
    )