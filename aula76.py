# Dicionários em Python (tipo dict)

# Dicionários são estruturas de dados do tipo par de 'chave' e 'valor'.

# CHAVES podem ser consideradas como 'índice' que vimos em list e são do tipo imutável.
# Como: str, int, float, bool, tuple, etc. 
# O valor pode ser de qualquer tipo, incluindo outro dicionário.
# Usamos as chaves '{}' ou a classe 'dict' para criar dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list




# personagem = {'Nome': 'Goku',
#               'Golpe': 'Kamehameha',                                            # Método mais utilizado
#               }

# # OR

# personagem = dict(Nome='Naruto',
#                   Golpe='Rasengan')                                             # Menos utilizado


# print(personagem, type(personagem))




# pessoa = {
#     'Nome': 'José Ricardo',
#     'Sobrenome': 'Freitas',
#     'Idade': 87,
#     'Altura': 1.7,
#     'Endereços': [
#         {'rua': 'tal tal', 'numero': '123'},
#         {'rua': 'outra rua', 'numero': '321'},
#     ],
# }


# # print(pessoa, type(pessoa))
# print(pessoa['Nome'])

# print()

# for chave in pessoa:
#     print(chave, pessoa[chave])                                     # Pegando dinamicamente a chave




# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome_completo'

pessoa[chave]='Joaquim Lima'
pessoa['sobrenome']='Josefim'
del pessoa['sobrenome']

print(pessoa[chave])

print(pessoa)

