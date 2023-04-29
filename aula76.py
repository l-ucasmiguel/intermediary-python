"""
DICIONÁRIOS EM PYTHON - (tipo dict)
par de 'chave' e 'valor'.

Dicionários são estruturas de dados do tipo "mapeamento" (mapping), que permite armazenar uma coleção de elementos que são indexados
por chaves únicas. Em outras palavras, um dicionário permite associar valores a chaves para acessá-los de forma rápida e eficiente.

Em Python, os dicionários são representados por chaves "{}" e os elementos são definidos em pares de chave-valor separados por dois pontos ":". Por exemplo:
meu_dicionario = {"chave1": valor1, "chave2": valor2, "chave3": valor3}

CHAVES podem ser consideradas como 'índice' que vimos em list e são do tipo imutável.
Como: str, int, float, bool, tuple, etc. 
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves '{}' ou a classe 'dict' para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
"""

# FORMAS DE UTILIZAR

# personagem = dict(Nome='Naruto',
#                   Golpe='Rasengan')                                             # Menos utilizado


# # OR


# personagem = {'Nome': 'Goku',
#               'Golpe': 'Kamehameha',                                            # Método mais utilizado
#               }


# print(personagem, type(personagem))










# PRATICANDO

# pessoa = {
#     'Nome': 'Roger',
#     'Sobrenome': 'Guedes',
#     'Idade': 26,
#     'Altura': 1.82,
#     'Endereços': [
#         {'rua': 'tal tal', 'numero': '123'},                            # Dentro da lista tem outros dicionários 
#         {'rua': 'outra rua', 'numero': '321'},
#     ],
# }


# print(pessoa, type(pessoa))
# print(pessoa['Sobrenome'])                                            # Especificando qual dado exibir

# print()

# for chave in pessoa:                                                    # 'chave' é o iterador que percorre cada uma das chaves do dict
#     print(chave,':', pessoa[chave])                                     # pessoa[chave] pega o valor atual dentro da chave| PEGANDO DINÂMICAMENTE A CHAVE

# Dessa forma, estamos acessando o 'índice' que ao invés de ser número, é uma string, fica mais fácil de saber o que estou acessando.










# MANIPULANDO CHAVES E VALORES EM DICIONÁRIOS 
# pessoa = {}                                                               # Em dict python, a chave precisa existir, se ela não existir vamos ter uma exceção=erro stop programa

## código ##
## código ##


# pessoa['nome'] = 'Luiz Otávio'                                          # Criando a chave de forma manual

# chave = 'nome'                                                            # Criando a variável que vai se tornar a chave dinâmica

# pessoa[chave]='Fernando'                                                  # Criando chave dinâmica
# pessoa['sobrenome']='Martins'                                             # Definindo 'sobrenome'
# print(pessoa[chave])                                                      # Exibindo a chave 'nome'
# print()


# pessoa[chave]='Maria'                                                     # Alterando valor da chave 'nome' dinâmicamente
# print(pessoa)


# print()
# del pessoa['sobrenome']                                                   # Apagando a chave 'sobrenome'
# print(pessoa)
# print()

# if pessoa.get('sobrenome') is None:                                       # Por padrão ele retorna 'None' se a chave não existir
#     print('Não Existe')
# else:
#     print('Existe')

# O método .get() é usado para acessar um valor em um dicionário. Ele recebe dois parâmetros: a chave que você deseja acessar e um valor padrão que será retornado caso 
# A chave não exista no dicionário.         Ex: valor = dicionario.get('chave1', 'valor_padrao')
# Se não for específicado um valor padrão caso a chave não exista, é retornado None









"""
MÉTODOS ÚTEIS DOS DICIONÁRIOS EM PYTHON | PARTE 01

len         -   Quantas chaves
keys        -   Iterável com as chaves
values      -   Iterável com os valores 
items       -   Iterável com chaves e valores
setdefault  -   Adiciona valor se a chave não existe
"""


# jogador = { 
#     'Nome':'Renato Augusto',
#     'Time':'Corinthians'
# }


# print(len(jogador))                                                # Retorna a quantidade de chaves que tenho no dicionário
# print(jogador.keys())                                              # Retorna as chaves 'dict_keys'
# print(list(jogador.values()))                                      # Retorna os valores 'dict_values' | Também podemos converter para usar como lista 
# print(jogador.items())                                             # Retorna as chaves e os valores 'dict_items'
# print(jogador.setdefault('Idade',35))                              # Define um valor padrão para uma chave que ainda não existe
# print()
# print('Isso é uma tupla ',tuple(jogador.keys()))                   # Podemos converter para tupla ou list
# print()

# for valor in jogador.values():                                     # .values()    'for' para retornar apenas os valores 
#     print(valor)

# print()

# for chave, valor in jogador.items():                               # .items()    'for' para retornar as chaves e os valores
#     print(chave,':', valor)










"""
MÉTODOS ÚTEIS DOS DICIONÁRIOS EM PYTHON | PARTE 02

copy        -   Retorna uma cópia rasa (shallow copy)
get         -   Obtém uma chave
pop         -   Apaga um item com a chave especificada (del)
popitem     -   Apaga o último item adicionado
update      -   Atualiza um dicionário com outro
"""


"""FORMA 'NORMAL' DE COPIAR, QUE NA VERDADE NÃO COPIA, FAZ REFERÊNCIA AO MESMO LOCAL DA MEMÓRIA"""

# dicionario1 = {                                                                   # Criando um novo dicionário
#     'c1':1,                                                                       # chave01
#     'c2':2,                                                                       # chave02
# }

# dicionario2 = dicionario1                                                         # Ele não está copiando, e sim fazendo uma refêrencia


# print(f'Este é o Dicionário 01 ORIGINAL  |      {dicionario1}')
# print(f'Este é o Dicionário 02 CÓPIA     |      {dicionario2}')                   # Exibindo Dicionário 02, a cópia rasa 
# print('-'*62)


# print('Alterando o valor do Dicionário 02')
# dicionario2['c1'] = 1000                                                          # Mudando o valor do Dicionário 02
# print(f'Este é o Dicionário 02           |      {dicionario2}')
# print('-'*62)


# print('Altera também o valor do Dicionário 01')                                   # Muda também o Dicionário 01, porque é o mesmo dicionário na memória
# print(f'Este é o Dicionário 01           |      {dicionario1}') 










"""
SHALLOW COPY:
Quando tem valor mutável 'dict or list' ele não vai fazer essa cópia, ele vai fazer com que os dois dicionários apontem pra mesma lista na memória.
Por padrão o '.copy()' faz uma cópia rasa (shallow copy).    Exemplo:
"""


# dicionario1 = {                                                         # Criando um novo dicionário
#     'c1':1,
#     'c2':2,
#     'lista':[0,2,4,6],
# }

# dicionario2 = dicionario1.copy()                                        # Fazendo shallow copy (cópia rasa) | shallow copy copia tudo que é imutável

# dicionario2['c1'] = 7                                                   # Alterando o 'dicionario02'
# dicionario2['lista'][1] = 99                                            # Alterando uma 'list' ou 'dict' com .copy(), vai alterar o 'dicionario1' e 'dicionario2'
#                                                                         # Porque 'list' e 'dict' é mutável, esse trecho do código apenas faz referência, não copia em si 
# print(f'Este é o dicionário 01 {dicionario1}')
# print(f'Este é o dicionário 02 {dicionario2}')                          # Desta forma o 'dicionario02' é alterado e o 'dicionario01' não, mas dentro da lista, os dois são alterados










"""
DEEP COPY:
É uma cópia profunda, é um tipo de cópia de um objeto que cria uma nova instância desse objeto com todos os seus valores e atributos copiados para uma nova variável.
Ao contrário de uma cópia rasa (shallow copy), que apenas copia as referências dos objetos originais, uma deep copy copia os objetos completos, incluindo quaisquer 
objetos aninhados dentro deles.
"""
# import copy


# dicionario1 = {                                                          # Criando um novo dicionário
#     'c1':1,
#     'c2':2,
#     'lista':[0,2,4,6],
# }

# dicionario2 = copy.deepcopy(dicionario1)                                 # Usando 'copy.deepcopy()' cópia profunda

# dicionario2['c1'] = 7                                                    # Alterando 'dicionário02'
# dicionario2['lista'][1] = 99                                             # Alterando 'list' no 'dicionário02' (Mutável)
# # Desta forma um dicionário já não afeta mais o outro.

# print(f'Este é o dicionário 01 {dicionario1}')
# print(f'Este é o dicionário 02 {dicionario2}')










"""
MÉTODOS ÚTEIS DOS DICIONÁRIOS EM PYTHON | PARTE 03

get         -   Obtém uma chave
pop         -   Apaga um item com a chave especificada (del)
popitem     -   Apaga o último item adicionado
update      -   Atualiza um dicionário com outro
"""




p1 = {
    'nome':'Cssio',
    'sobrenome':'Ramos',
}


# GET
# É usado para obter uma chave, retorna None por padrão quando não tem a chave especificada, Com 'get' podemos definir um valor padrão, como na linha abaixo:
# print(p1.get('nome', 'Não Existe'))



# POP
# O método POP apaga a chave especificada e também pode guardar o seu valor na variável criada, como no exemplo abaixo:
# nome_pop = p1.pop('nome')
# print(nome_pop)
# print(p1)



# POPITEM
# O Método POPITEM elimina a última chave no dicionário, e também pode guardar o seu valor na variável criada.
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)



# UPDATE
# O método UPDATE atualiza o seu dicionário. Update pode receber um iterável que se comporta como um dicionário, exemplo: list or tuple, com chave e valor.
# p1.update({
#     'nome':'Cassio',
#     'idade':'TRINTA E CINCO',
#     'time':'',                                                   # 1º jeito de como usar, mais organizado e demora mais 
#     'altura':'',
    
# })

# p1.update(time='Corinthians')                                    # 2º jeito de como usar, mais rápido e menos organizado

# tupla = ('idade','35'),('altura', 1.96)                          # 3º jeito de usar, usando com tuple, jeito mais complicado
# p1.update(tupla)
# p1.update((('cor do cabelo', 'preto'),('idolo?','SIM')))         # Outra forma com tuplas

# lista = ['É campeão mundial?','Sim'],['Já se machucou?','Sim']   # 4º jeito de usar, usando com list, mais complicado 
# p1.update(lista)

# print(p1)