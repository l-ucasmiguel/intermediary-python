# Dictionary Comprehension e Set Comprehension
# É a mesma coisa de List Comprehension, mas a gente troca os Colchetes '[]', pelas chaves '{}'
# Parênteses    ()
# Colchetes     []
# Chaves        {}
# Map, retorna uma lista do mesmo tamanho, com valores diferentes, Filtro retorna uma lista com elementos a menos, filtrados.


# 1)
print('1) Exemplo de Dict Comprehension: ')
produto = {
    'Nome':'Caneta azul',
    'Preço':'2.50',
    'Categoria':'Escritório',
}


# dict_comprehension = {                                                        # Com quebra de linha
#     chave:valor.upper()                                                       # Modificando o 'valor' para maiúsculo 
#     if isinstance(valor, str) else valor                                      # Map: Se 'valor' for 'str' ele vai deixar maiúsculo, se não vai retornar somente o valor 
#     for chave, valor                                                          # For vai percorrer em 'produto.items()'
#     in produto.items()
#     if chave != 'Categoria'                                                   # Filter: se 'chave' for diferentede 'categoria'
# }

# Map: if instancia de 'valor' for 'str', 'valor.upper()' se não retorna 'valor'.  Filtragem: if 'chave' for diferente, não mostra
dict_comprehension = {chave:valor.upper() if isinstance(valor,str) else valor for chave, valor in produto.items() if chave != 'Categoria'}              # Sem quebra de linha
print(dict_comprehension)
print('\n'*2)




# 2)
print('2) Aqui criamos um novo dict, a partir de uma lista que parece um dict: ')

lista = [
    ('a','valor a'),
    ('b','valor b'),
    ('c','valor c'),
]

# dc = {                                   # Transformando a 'lista' em 'dict'
#     chave: valor
#     for chave, valor in lista
# }


print(dict(lista))                         # Transformando a 'lista' em 'dict' de uma forma mais simples. Mas a lista precisa ter esse modelo de chave e valor, para funcionar.
print('\n'*2)




# 3)
print('3) Set Comprehension: ')

set_01 = {i*2 for i in range(10)}
print(set_01)
print()

# OR 
print(set(range(10)))