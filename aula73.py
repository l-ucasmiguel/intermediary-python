"""
Higher Order Functions 
Funções de primeira classe
Funções é da mesma classe de variáveis, números do que qualquer outra coisa em python
"""

def saudacao(msg, nome):                                    # 1- É criado a função 'saudacao', com os parâmetros 'msg' e 'nome'
    return f'{msg}, {nome}!'                                # 2- É retornado como string a 'msg' e o 'nome'


def executa(funcao, *args):                                 # 3- É criado a função 'executa', com os parâmetros 'funcao' e '*args'. que é usado para argumentos não nomeados
    return funcao(*args)                                    # 4- É retornado uma função, a 'funcao(*args)' com '*args' como parâmetro 
                                                            # No passo 3 '*args' empacota e no passo 4 '*args' desempacota


print(                                                      # 5- Usamos o 'print' e em seguida chamamos a função 'executa' usando a função 'saudacao' como argumento
    executa(saudacao, 'Bom dia', 'Luiz')                    # Usamos 'Bom dia', e 'Luiz' como argumento da função 'saudacao', que equivale aos parâmetros 'msg' e 'nome'
    )

print(
    executa(saudacao, 'Boa tarde', 'Juan')
    )

"""
Explicação:
Eu posso passar funções como argumentos de outras funções, e também posso retornar funções de dentro de uma função.
Função é um tipo de dado em python que a gente pode fazer o que quiser, posso jogar em uma variável, podemos passar como parâmetro de outras funções e podemos retornar
de dentro de outras funções.

Termos técnicos: Higher Order Functions e First-Class Functions
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
"""