# Yield from
# Quando tem mais de 1 'yield' na função, ele continua executando até o último

def gen1():                                             # Criando função 'gen1'
    yield 1
    yield 2
    yield 3


def gen2():                                             # Criando função 'gen2'
    yield 4
    yield 5
    yield 6

def gen3():                                             # Criando a função 'gen3'
    yield from gen2()                                   # Esse 'yield' retorna o 'gen2'
    yield 7
    yield 8
    yield 9


g = gen1()                                              # 'g' recebe a função 'gen1'
h = gen3()                                              # 'h' recebe a função 'gen3'

for numero in g:                                        # 'numero' percorre 'g' e executa a função 'gen1'
    print(numero)                                       # imprime o 'numero' na tela 

for numero in h:                                        # 'numero' percorre 'h' e executa a função 'gen3', e dentro dela é chamada a função 'gen2'
    print(numero)