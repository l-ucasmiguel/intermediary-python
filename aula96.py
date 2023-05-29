# Módulo padrão do Python ('import', 'from', 'as', '*')
# https://docs.python.org/3/py-modindex.html
# É muito comum ouvir por ai que o python já vem com as pilhas incluídas, porque ele vem com muitos módulos por padrão.

# 1- INTEIRO
# Importar o módulo inteiro não muda nada na performance do programa
# Inteiro       - Para importar um módulo inteiro basta usar: import nome_modulo
# Vantagens     - Você tem o namespace do módulo 
# Desvantagens  - Nomes grandes

import sys                                                            # Importando o módulo inteiro

plataform = 'A minha plataforma'                                      # Criando uma variável e definindo o valor dela
print(sys.platform)                                                   # Neste caso 'sys' é o namespace. Quando importamos o módulo inteiro temos o namespace do módulo
print(plataform)                                                      # Protegendo o que tiver dentro do módulo, neste exemplo protegendo a variável 'plataform' do módulo 'sys' 
print()




# 2- EM PARTES
# Partes        - Para importar somente partes do módulo basta usar: from nome_modulo import objeto1 objeto2
# Vantagens     - Nomes pequenos 
# Desvantagens  - Sem o namespace do módulo 

from sys import exit, platform                                        # Importando em partes o módulo 'sys', somente a parte do 'exit' e 'platform'

platform = 'TESTE'                                                    # Em partes não temos o namespace do módulo protegendo o objeto, neste caso temos que tomar cuidado para 
print(platform)                                                       # Não redefinir o valor dele, como neste caso.
print()





# 3- FORMA DIFERENTE
# alias 1       - import nome_modulo as apelido 
# alias 2       - from nome_modulo import objeto as apelido
# Vantagens     - Você pode reservar nomes para seu código
# Desvantagens  - Pode ficar fora do padrão da linguagem

import sys as novosys                                                 # Se importamos um módulo e criamos um variável com o nome dele, o python vai sobrescrever e o módulo não
sys = 'alguma coisa'                                                  # vai funcionar. Para funcionar podemos mudar o nome da variável, ou mudar o nome do módulo com
print(novosys.platform)                                               # 'as'. Como no exemplo na linha 41. É recomendado mudar a variável neste caso, isso é apenas um exemplo.
print(sys)
print()





# 4- MÁ PRÁTICA
# Má prática    - from nome_modulo import*
# Vantagens     - Importa tudo de um módulo
# Desvantagens  - Importa tudo de um módulo

# from sys import all
from sys import *                                                       # Esta forma é uma má prática porque nada fica protegido pelo namespace e pode facilmente sobrescrever algo
print(platform)                                                         # Também fica obscuro porque não fica claro de onde está vindo os objetos
exit()