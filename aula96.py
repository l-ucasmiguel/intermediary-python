# Módulo padrão do Python ('import', 'from', 'as', 'sys','*')
# https://docs.python.org/3/py-modindex.html
# É muito comum ouvir por ai que o python já vem com as pilhas incluídas, porque ele vem com muitos módulos por padrão.

# 1- INTEIRO
# Importar o módulo inteiro não muda nada na performance do programa
# Inteiro       - Para importar um módulo inteiro basta usar: import nome_modulo
# Vantagens     - Você tem o namespace do módulo 
# Desvantagens  - Nomes grandes
# Cuidado para o nome da variável criada não ser uma palavra reservada do módulo, como no exemplo abaixo 'plataform'

import sys                                                              # Importando o módulo inteiro

print("\n1) Essa é a forma de importar usando o 'import sys':")
plataform = 'A minha plataforma é '                                     # Criando uma variável e definindo o valor dela
# print(sys.platform)                                                   # Neste caso 'sys' é o namespace. Quando importamos o módulo inteiro temos o namespace do módulo
print(plataform, sys.platform)                                          # Protegendo o que tiver dentro do módulo, neste exemplo protegendo a variável 'plataform' do módulo 'sys' 
print()




# 2- EM PARTES
# Partes        - Para importar somente partes do módulo basta usar: from nome_modulo import objeto1 objeto2
# Vantagens     - Nomes pequenos 
# Desvantagens  - Sem o namespace do módulo 

from sys import exit, platform                                        # Importando em partes o módulo 'sys', somente a parte do 'exit' e 'platform'

print("2) Essa é a forma de importar usando o 'from nome_do_modulo_ import item':")
platform = 'Nova Platform'                                            # Em partes não temos o namespace do módulo protegendo o objeto, neste caso temos que tomar cuidado para 
print(platform)                                                       # Não redefinir o valor dele, como neste caso, que criamos a variável 'platform' e por isso não
print()                                                               # Podemos acessar o 'platform' do módulo




# 3- FORMA DIFERENTE
# alias 1       - import nome_modulo as apelido 
# alias 2       - from nome_modulo import objeto as apelido
# Vantagens     - Você pode reservar nomes para seu código
# Desvantagens  - Pode ficar fora do padrão da linguagem

import sys as novosys                                                       # Se importamos um módulo e criamos um variável com o nome dele, o python vai sobre screver e o módulo não
sys = 'alguma coisa'                                                        # vai funcionar. Para funcionar podemos mudar o nome da variável, ou mudar o nome do módulo com
print("3) Essa é a forma de importar e dar apelido para o módulo padrão:")  # 'as'. Como no exemplo na linha 44. É recomendado mudar a variável neste caso, isso é apenas um exemplo.
print(novosys.platform, "       <- Este é o módulo padrão renomeado para 'novosys'")
print(sys, "<- Esta é a nossa variável com o nome de 'sys'")
print()




# 4- MÁ PRÁTICA
# Má prática    - from nome_modulo import*
# Vantagens     - Importa tudo de um módulo
# Desvantagens  - Importa tudo de um módulo

# from sys import all
from sys import *                                                       # Esta forma é uma má prática porque nada fica protegido pelo namespace e pode facilmente sobrescrever algo
print(platform)                                                         # Também fica obscuro porque não fica claro de onde está vindo os objetos
exit()