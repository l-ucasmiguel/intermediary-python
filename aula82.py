def executa(funcao, *args):                                  # É uma função que executa outras funções
    return funcao(*args)


def soma(x,y):                                               # Função que soma dois valores
    return x+y


print(
    executa(lambda x,y: x+y , 2,3),                          # lambda = def      x,y: é a expressão/return      'x+y' é a expressão      '2,3' são os argumentos

    executa(soma,2,3),                                       # A função 'executa' está executando a função 'soma', os agumentos estão entrando no '*args'

    soma(2,3)                                                # Chamando a função 'soma'
)



# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

duplica = executa(lambda m: lambda n: n*m, 4)
print(duplica(4))


print(
    executa(
        lambda *args: sum(args),                             # Somando todos '*args' via lambda
        1,2,3,4,5,6,7
    )
)