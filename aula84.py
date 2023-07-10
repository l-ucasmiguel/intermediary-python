# List comprehension em Python
# list comprehension é uma forma rápida para criar listas a partir de iteráveis

# import pprint                                                     # O módulo 'pprint' é usado para imprimir estruturas de dados de forma mais legível e organizada.

# def p(v):
#     pprint.pprint(v, sort_dicts=False, width=40)

print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)                                        # O método 'append' é usado para adicionar um elemento no final de uma lista.
# print(lista)


# Exemplo de list comprehension
lista = [numero * 2 for numero in range(10)]                    # A esquerda do 'for' vem a lógica/expressão.
print(lista)
print('-'*100)
print()




# # Mapeamento de dados em list comprehension
# produtos = [
#     {'nome':'p1','preço':20},
#     {'nome':'p2','preço':10},
#     {'nome':'p3','preço':30},
# ]

# # Mapeamento em list comprhesion é ter uma lista, e querer gerar uma nova lista talvez transformando os dados mas tendo que manter o mesmo tamanho das
# # listas
# novos_produtos = [                                                # list comprehension
#     # {'nome':produto['nome'],'preço':produto['preço']}           # Mapeamento
#     {**produto, 'preço': produto['preço'] * 1.05}                 # Usando '**' para desempacotar | Aumentando o preço dos produtos em 5%
#     if produto['preço'] >20 else {**produto}                      # Só aumenta o preço do que for > 20
#     for produto in produtos
#     if (produto['preço'] >= 20 and produto['preço'] *1.05) > 10   # Filtro
# ]

# """
# Filtro, filtrar coisas que eu não quero na minha lista, isto vem depois do 'for', o que for filtro é só 'if' não tem 'else' 
# O que vem a esquerda do 'for' é mapeamento, o que vem a direita do 'for' é filtro
# """


# # print(novos_produtos)
# print(*novos_produtos, sep='\n')                                  # Usando '*' para desempacotar e 'sep='\n'' para quebra de linha
# # p(novos_produtos)

# print('-'*100)
# # Filtro
# lista = [n for n in range(10) if n < 5]                           # 'if' do filtro sempre depois do 'for'
# print(lista)