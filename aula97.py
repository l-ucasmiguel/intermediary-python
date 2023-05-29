# Entendendo os seus próprios módulos Python:
# O primeiro módulo executado chama-se __main__, os outros módulos tem os nomes deles
# Você pode importar outro módulo inteiro ou parte do módulo, também podemos importar nossos próprios módulos
# O Python conhece a pasta onde o __main__ está e as pastas abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path

import sys
# print(*sys.path, sep='\n')


import aula97_modulo                                    # Importando um módulo completo e próprio
print('Este módulo se chama ', __name__)


from aula97_modulo import variavel_modulo, soma         # Importando apenas uma variável do módulo e uma função
print(variavel_modulo)
print(soma(2,2))


print(aula97_modulo.variavel_modulo)                    # Para usar variável de outro módulo basta colocar o nome do módulo o '.' e o nome da variável
print(aula97_modulo.soma(8,8))