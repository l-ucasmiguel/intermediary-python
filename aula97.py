# Entendendo os seus próprios módulos Python:
# O primeiro módulo executado chama-se __main__, os outros módulos tem os nomes deles
# Você pode importar outro módulo inteiro ou parte do módulo, também podemos importar nossos próprios módulos
# O Python conhece a pasta onde o __main__ está e as pastas abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path
# Em Python pastas são chamadas de packages e os arquivos de modules


import sys

# print(*sys.path, sep='\n')
# Está linha vai mostrar todos os diretórios do caminho de busca do módulo (sys.path), isso é útil para ver quais diretórios estão incluídos no caminho de busca de módulos, o que 
# é importante para a importação de módulos em seus programas


print('1) Este módulo se chama ', __name__,' [ATUAL]\n')        # 1) Executando no módulo atual


import aula97_modulo                                            # 2) Importando um módulo completo e próprio


from aula97_modulo import variavel_modulo, soma                 # 3) Importando apenas uma variável do módulo e uma função
print('3)',variavel_modulo)
print('O resultado da soma é:',soma(2,2),'\n')


print('4)', aula97_modulo.variavel_modulo)                      # 4) Para usar variável de outro módulo basta colocar o nome do módulo o '.' e o nome da variável
print('O resultado da soma é:',aula97_modulo.soma(8,8))
