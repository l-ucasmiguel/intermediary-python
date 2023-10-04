# EXERCÍCIO - ADIANDO EXECUÇÃO DE FUNÇÕES
# Sempre que tiver as palavras, adiar, pausar, esperar, você não quer executar na hora 
# CLOSURES - Função interna reconhece o seu entorno, percebe a função principal 


def soma (x,y):
    return x + y


def multiplica(x,y):
    return x * y


def criar_funcao(funcao, x):                                 # 1) 'funcao' recebe 'soma' e 'x' recebe '5'
    def funcao_interna(y):                                   # 3) 'y' recebe '10' 
        return funcao(x,y)                                   # 4) Retorna 'funcao(x,y)', que agora é 'soma(5,10)' 
    return funcao_interna                                    # 2) Retorna a 'funcao_interna' sem os '()', porquê não queremos executar agora




soma_com_cinco = criar_funcao(soma,5)                        # 'soma_com_cinco' é criada chamando a função 'criar_funcao(soma, 5)' | Passando 'soma' para 'funcao' e '5' para 'x'
print(soma_com_cinco(10),'\n')                               # Chamar o 'soma_com_cinco' no print, é como chamar a função 'criar_funcao', mas como ela já está sendo executada
                                                             # Ela continua e chama a função 'funcao_interna' passando como parâmetro '10' para 'y'


multiplica_por_dez = criar_funcao(multiplica,10)             # Mesmo processo
print(multiplica_por_dez(50))