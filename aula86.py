# Dictonary Comprehension e Set Comprehension

produto = {
    'nome':'Caneta Azul',
    'preço': 2.5,
    'categoria':'Escritório',
}


# for valor, chave in produto.items():
#     print(valor,chave)


# Dictonary Comprehension
dc = {
    chave: valor.upper()                                                        # Modificando o 'valor' para maiúsculo 
    if isinstance(valor, str) else valor                                        # Se 'valor' for 'str' ele vai deixar maiúsculo, se não vai retornar somente o valor 
    for chave, valor 
    in produto.items()
    if chave != 'categoria'                                                     # filter | se 'chave' for diferentede 'categoria'
}

# print(dc)



lista = [
    ('a','valor a'),
    ('b','valor b'),
    ('c','valor c'),
]

# print(lista)

dc = {                                              # Transformamos uma lista em dict 
    chave: valor
    for chave, valor in lista
}
# print(dc)

print(dict(lista))                                  # Forma mais simples de transformar list em dict, desde que seja no modelo 'chave' 'valor'
print()



# Set Comprehension
s1 = {2 ** i for i in range(10)}
print(s1)
# OR 
# print(set(range(10)))






# () tupple
# [] list
# {} dict