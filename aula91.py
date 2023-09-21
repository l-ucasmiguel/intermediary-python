# Introdução às Generator Expression em Python
# Toda generator function usa a palavra 'yield'
# Toda função que tem 'yield' é uma generation function

# # Generator Function
# def generator(n=0):
#     yield 1                                       # 'yield' agora é o 'return'. | yield pausa a função aqui 
#     print('Continuando...')
#     yield 2
#     print('Mais uma...')
#     yield 3 
#     print('Vou terminar')
#     return 'ACABOU'                               # Quando a gente chama o 'next' em um lugar que já acabou, o 'return' é atingido como 'StopIteration' e retorna o que tem lá


# gen = generator(n=0)
# # print(next(gen))                                # Esse 'next' é para o primeiro 'yield 1'
# # print(next(gen))                                # Esse 'next' é para o segundo 'yield 2', e volta pra função na linha em que pausou o 'yield 1'
# # print(next(gen))                                # Esse 'next' é para o terceiro 'yield 3', e volta pra função na linha em que pausou o 'yield 2'
# # print(next(gen))                                # Esse 'next' volta pra onde estava pausado em 'yield 3' e imprime na tela o 'print' e o 'return' como 'StopIteration'

# # Fazendo a mesma coisa dinâmicamente
# for n in gen:
#     print(n)





def generator (n=0, maximum=10):                    # Criando uma Generator Function
    
    while True:                                     # Enquanto for verdade, loop infinito
        yield n                                     # Pausa e retorna n 

        n += 1                                      # n + 1 

        if n > maximum:                             # Se n for > que o maximum, stop
            return



gen = generator(n=2, maximum=12)                    # Criando a variável 'gen' que recebe a função 'generator' e passa o 'maximum=1000000' como argumento
for n in gen:                                       # Chamando a função com 'for', ela sempre pausa no yield e retorna de lá 
    print(n)