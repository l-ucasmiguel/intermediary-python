"""
Higher Order Functions 
Funções de primeira classe
Funções é da mesma classe de variáveis, números do que qualquer outra coisa em python
"""

def saudacao(msg, nome):                                        # 1- É criado a função 'saudacao', com os parâmetros 'msg' e 'nome'
    return f'{msg}, {nome}!'                                    # 2- É retornado como string a 'msg' e o 'nome'


def executa(funcao, *args):                                     # 3- É criado a função 'executa', com os parâmetros 'funcao' e '*args'. que é usado para argumentos não nomeados
    return funcao(*args)                                        # 4- É retornado uma função, a 'funcao(*args)' com '*args' como parâmetro

print(                                                          # 5- Usamos o print e em seguida chamamos a função 'executa' usando a função 'saudacao' como argumento
    executa(saudacao, 'Bom dia', 'Luiz')                        # E usamos 'Bom dia', e 'Luiz' Como argumento da função 'saudacao'
    )

print(
    executa(saudacao, 'Boa tarde', 'Juan')
    )

"""
Explicação:




A função 'executa' usa como parâmetro 'funcao' e '*args' e retorna o argumento de 'funcao' e '*args', que no nosso caso é, no 'print'
chamamos a função 'executa' com os argumentos 'saudacao' é a primeira função, em seguida é passado os argumentos 'bom dia' e 'Luiz', que
vão parar no parâmetro de 'executa'
"""