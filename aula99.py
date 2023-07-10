# Em Python 'Packages' é uma forma de organizar e estruturar módulos relacionados em um diretório hierárquico. Um pacote é basicamente um diretório
# que contém um arquivo especial chamado '__init__.py'. Esse arquivo é usado para indicar que o diretório é um pacote Python válido.
# Os pacotes são usados para agrupar módulos relacionados em um namespace comum, facilitando a organização, a reutilização e a distribuição de código
# em projetos maiores. Eles ajudam a evitar conflitos de nomes entre módulos, fornecendo um espaço de nomes separado para cada pacote.

# # import aula99_package                                           # import dessa forma não faz nada com packages, só funciona desse modo com módulos
# # print(aula99_package.modulo)



# # 1º FORMA.     Importando package, e importando a função dentro do módulo.
# # Neste caso, apenas o símbolo 'soma_do_produto' é importado do módulo 'aula99_package.modulo'. Isso signfica que apenas a função 'soma_do_produto'
# # estará disponível no namespace atual, outros elementos do módulo não serão importados. 
# from aula99_package.modulo import soma_do_modulo
# print(soma_do_modulo(10,10))                                      # Forma mais prática, porque é só usar o nome da função

# print()





# # 2º FORMA.     Importando package e o módulo completo.
# # Nessa forma de importação, o módulo completo 'aula99_package.modulo' é importado. Para acessar qualquer símbolo do módulo, você precisa usar o nome completo, como
# # 'aula99_package.modulo.soma_do_modulo'. Isso evita a poluição do namespace atual, pois todos os símbolos do módulo são acessíveis apenas usando o prefixo 'aula99_package.modulo'.
# import aula99_package.modulo
# print(aula99_package.modulo.soma_do_modulo(20,20))                # Forma mais difícil. Nome fica muito grande, porque tem que usar o namespace 

# print()





# # 3º FORMA      Importando 'aula99_package' como um todo
# # Nesse caso, o módulo 'aula99_package' é importado como um todo, mas agora você pode acessar os símbolos diretamente sem usar o prefixo 'aula99_package'. Por exemplo,
# # você pode usar 'modulo.soma_do_modulo' para acessar a função 'soma_do_modulo'. Isso permite um código mais conciso e legível em comparação com a opção 2.
# from aula99_package import modulo
# print(modulo.soma_do_modulo(30,30))                               # Dessa forma tem que colocar o nome do módulo primeiro

# print()





# # 4º FORMA,      MÁ PRÁTICA
# # Essa forma de importação usa o asterisco (*) para importar todos os símbolos do módulo 'aula99_package.modulo'. Isso significa que todos os símbolos (variáveis, funções, classes)
# # do módulo serão adicionados diretamente ao namespace atual. Como mencionado anteriormente, essa prática geralmente é desencorajada, pois pode causar conflitos de nome e
# # dificultar a rastreabilidade dos símbolos importados.
# from aula99_package.modulo import *                               # MÁ PRÁTICA 
# print(soma_do_modulo(40,40))
# print(variavel)


# """
# Em geral, é recomendado usar a opção 1 ou a opção 3, dependendo do contexto. A opção 2 pode ser útil quando você precisa acessar vários símbolos do mesmo módulo 
# repetidamente. A opção 4 deve ser evitada devido aos problemas mencionados anteriormente com a poluição do namespace e a falta de clareza.
# """





# from sys import path                                              # Import do módulo sys
# print(__name__)
# print(*path, sep='\n')                                            # Impressão dos diretorios que o módulo 'sys' tem acesso
# --------------------------------------------------------------------------------------------------------------------------------------------------





# Todas as importações dentro do programa tem que estar relativas ao 'main'. E não vão funcionar nos outros módulos, porque o 'main' muda para o principal.

# from aula99_package.modulo import soma_do_modulo, fala_oi           # Importando
# fala_oi()                                                           # Fala oi está no 'módulo2', que vai pro 'modulo1' e depois vem pra cá



# O package pode ser inicializado por um arquivo chamado '__init__.py'


from aula99_package import soma_do_modulo, fala_oi

print(soma_do_modulo(20,10))
fala_oi()

# print(aula99_package.soma_do_modulo(2,2))
# print(aula99_package.nova_variavel)



