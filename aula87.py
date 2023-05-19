# isinstace - para saber se o objeto é de determinado tipo 
# Em python existe uma função chamda isinstance 
# isinstance significa é instancia de: 
# Evitar misturar tipos de dados na lista
# Sempre tantar manter as listas ou tuplas em um padrão do mesmo tipo de dados. Exemplo, uma lista de números é para tentar manter só números
# Se usarmos string dentro daquela lista, vamos ter que usar o 'if' e pode quebrar o programa. 


lista = [                                               # Não é uma boa prática de programação, ter um tipo de lista misturada
    'a', 1, 1.1, True, [0,1,2],(1,2),
    {0,1}, {'nome':'Luiz'},
]




for item in lista:
    # Verifica se 'item' é instância de 'set()'. Se 'item' for instância de set(), 'item' add(5) e imprime na tela os valores que são set() e o valor boolean
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))


    # Verifica se 'item' é instância de 'string'. Se 'item' for instância de 'string', 'item.upper()' deixa em maiúsculo o que for string
    elif isinstance(item, str):
        print('STR')
        print(item.upper())


    # Verifica se 'item' é instância de 'int' ou 'float' e imprime 'item', e o 'item*2'
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item *2)
    
    else:
        print('OUTRO')
        print(item)



# Tuplas    ()  são imutáveis
# Listas    []  são mutáveis
# Dicts     {}  são mutáveis
# Set     set() são mutáveis