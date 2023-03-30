"""
Argumentos nomeados e não nomeados em funções Python:

Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x,y,z):                                                # 'x' e 'y' são os parâmetros 
    print(f'{x=} {y=} z={z} | x + y + z =', x+y+z)

soma(2,6,3)                                                     # Argumento posicional 
soma(y=6,x=2,z=3)                                               # Argumento nomeado 
soma(2,y=6,z=9)                                                 # Misturado tem uma regra, todos os argumentos que vierem depois, tem que estar nomeado



# É recomendado não misturar, ou usar somente o Argumento posicional, ou somente o Argumento nomeado 