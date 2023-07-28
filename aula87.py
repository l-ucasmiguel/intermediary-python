# 'isinstace' - serve para saber se um objeto é de um determinado tipo
# 'elif' é usado para ter reservado um 'else' como default
# Evitar misturar tipos de dados na lista
# Sempre tantar manter as listas ou tuplas em um padrão do mesmo tipo de dados. Exemplo, uma lista de números é para tentar manter só números
# Se usarmos string dentro daquela lista, vamos ter que usar o 'if' e pode quebrar o programa. 
lista = [
    'a', 1, 1.1, True, [0,1,2],(1,2),{0,1},{'nome':'luiz'}
]
# print(type(lista[7]))



for item in lista:
# Verifica se 'item' é instância de 'string'. Se 'item' for instância de 'string', 'item.upper()' deixa em maiúsculo o que for string
    if isinstance(item,str):
        print('Str:',item.upper(), isinstance(item,str))
        print()

# Verifica se 'item' é instância de 'set()'. Se 'item' for instância de set(), 'item' add(5) e imprime na tela os valores que são set() e o valor boolean
    elif isinstance(item,set):
        print()
        item.add(5)
        print('Set:',item, isinstance(item, set))

# Verifica se 'item' é instância de 'int' ou 'float' e imprime 'item', e o 'item*2'
    elif isinstance(item,(float,int)):
        print('Int or Float',item, item*2)
        print('-'*20)

    else:
        print()
        print('Outro:')
        print(item)




# Tuplas    ()  são imutáveis
# Listas    []  são mutáveis
# Dicts     {}  são mutáveis
# Set     set() são mutáveis