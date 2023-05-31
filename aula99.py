# Em Python 'Packages' é uma forma de organizar e estruturar módulos relacionados em um diretório hierárquico. Um pacote é basicamente um diretório
# que contém um arquivo especial chamado '__init__.py'. Esse arquivo é usado para indicar que o diretório é um pacote Python válido.
# Os pacotes são usados para agrupar módulos relacionados em um namespace comum, facilitando a organização, a reutilização e a distribuição de código
# em projetos maiores. Eles ajudam a evitar conflitos de nomes entre módulos, fornecendo um espaço de nomes separado para cada pacote.


# 1º FORMA.     Importando package, e importando a função dentro do módulo.
from aula99_package.modulo import soma_do_modulo
print(soma_do_modulo(10,10))                                      # Forma mais prática, porque é só usar o nome da função


print()


# 2º FORMA.     Forma mais difícil
import aula99_package.modulo
print(aula99_package.modulo.soma_do_modulo(20,20))                # Nome fica muito grande, porque tem que usar o namespace 


print()


# 3º FORMA      Importando o módulo inteiroa
from aula99_package import modulo
print(modulo.soma_do_modulo(30,30))                               # Dessa forma tem que colocar o nome do módulo primeiro


print()


# 4 FORMA,      MÁ PRÁTICA
from aula99_package.modulo import *                               # MÁ PRÁTICA 
print(soma_do_modulo(40,40))
print(variavel)


# from sys import path                                            # Import do módulo sys
# print(*path, sep='\n')                                          # Impressão dos diretorios que o módulo 'sys' tem acesso 


# import aula99_package                                           # Não faz nada 
# print(aula99_package.modulo)