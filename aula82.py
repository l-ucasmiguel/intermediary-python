def executa_funcao(funcao, *args):                                   # É uma função que executa outras funções
    return funcao(*args)

def soma(x,y):                                                       # Função que soma dois valores
    return x+y



print(
    executa_funcao(lambda x,y: x+y , 19,1),                          # lambda = def   'x,y' são os argumentos da lambda   'x+y' é a expressão   '2,3' são os argumentos p/ expressão

    executa_funcao(soma,29,1),                                       # A função 'executa_funcao' está executando a função 'soma', os agumentos estão entrando no '*args'

    soma(39,1)                                                       # Chamando a função 'soma'
)



def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

vezes = cria_multiplicador(50)                                   # Estou atribuindo a função 'cria_multiplicador' passando '50' como parâmetro para a variável 'vezes' sem executar
print(vezes(2))                                                  # Aqui a função é executada e o retorno é impresso na tela. 


# duplica = executa_funcao(lambda m: lambda n: n*m, 7)           # Não é indicado usar assim, porque não dá pra ler muito bem 
# print(duplica(9))





print(
    executa_funcao(
        lambda *args: sum(args),                                 # Somando todos '*args' via lambda
        1,2,3,4,5,6,7
    )
)