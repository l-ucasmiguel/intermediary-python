# 01) Introdução a List Comprehension
# List comprehension é uma forma rápida para criar listas a partir de iteráveis

print('1) Introdução a List Comprehension: \n')
lista = []
for numero in range(11):                                                   # Criando uma list usando 'for', 'append' e 'range'
    lista.append(numero)
print('Criando uma lista usando "for", "append" e "range": ')
print(lista,'\n'*1)




# List comprehension
# lista = [                                                                  # Utilizar quebra de linha para ficar mais fácil a visualização quando o código fica grande
#     numero * 7                                                             # As expressões sempre ficam a esquerda do código, no começo. E as condições sempre ficam a 
#     for numero in range(11)                                                # direita, no final.

lista = [ numero * 8 for numero in range(11)]

print('Criando uma lista usando "list comprehension": ')
print(lista)
print('\n')
print('-'*63)
print('\n')






# 02) Mapeamento de dados em list comprehension
print('2) Mapeamento de dados em List Comprehension: ')
print()


# O Mapeamento de dados é feito usando a sintaxe da list comprehension para transformar cada elemento de uma lista original de acordo com uma expressão fornecida.
produtos = [
    {'nome':'p1','preço':20},
    {'nome':'p2','preço':10},
    {'nome':'p3','preço':30},
]

# Mapeamento em list comprehension é ter uma lista, e querer gerar uma nova lista talvez transformando os dados mas tendo que manter o mesmo tamanho das listas
novos_produtos = [                                                          # list comprehension
    # {'nome':produto['nome'],'preço':produto['preço']}                     # Mapeamento
    {**produto, 'preço': produto['preço'] * 1.05}                           # Usando '**' para desempacotar | Aumentando o preço dos produtos em 5%
    if produto['preço'] >20 else {**produto}                                # Só aumenta o preço do que for > 20
    for produto in produtos
    if (produto['preço'] >= 20 and produto['preço'] *1.05) > 10             # Filtro
]

"""
Filtro, filtrar coisas que eu não quero na minha lista, isto vem depois do 'for', o que for filtro é só 'if' não tem 'else' 
O que vem a esquerda do 'for' é mapeamento, o que vem a direita do 'for' é filtro
"""


# print(novos_produtos)
print(*novos_produtos, sep='\n')                                          # Usando '*' para desempacotar e 'sep='\n'' para quebra de linha
# print(novos_produtos)

print('-'*100)
# Filtro
lista = [n for n in range(10) if n < 5]                                   # 'if' do filtro sempre depois do 'for'
print(lista)











# import pprint                                                             # O módulo 'pprint' é usado para imprimir estruturas de dados de forma mais legível e organizada.

# def p(v):
#     pprint.pprint(v, sort_dicts=False, width=40)