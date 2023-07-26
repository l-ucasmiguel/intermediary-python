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





# Mapeamento e Filtragem de dados em List Comprehension
import pprint                                                                # O módulo 'pprint' é usado para imprimir estruturas de dados de forma mais legível e organizada.

def p(v):
    pprint.pprint(v, sort_dicts=False, width=80)


print('2) Mapeamento e Filtragem de dados em List Comprehension: \n')
print('Lista original:')
lista_de_produtos = [                                                        # Lista de Dicts
    {'nome':'p1','preço':20},
    {'nome':'p2','preço':10},
    {'nome':'p3','preço':30},
]

print(*lista_de_produtos, sep='\n')
print()




print('Lista alterada com aumento em 5%: ')
nova_lista_de_produtos = [
    {**produto, 'aumento 5%': produto['preço'] *1.05}     # Entre {} pq é um novo dict || Usando '**' para desempacotar o dict antigo em um novo || Criando nova chave para 'aumento 5%'
    if produto['preço'] >= 20 else {**produto}            # Se produto['preço'] >= 20 exibir 'aumento 5%', se não retornar o dict original
    for produto in lista_de_produtos
    if (produto['preço'] >= 20 and produto['preço'] * 1.05 > 10)   # Se produto['preço'] >= 20 & produto['preço'] * 1.05 > 10 EXIBIR FILTRADO
]

# If antes do 'for' : antes é de mapeamento, map sempre vai retornar a mesma quantidade de elementos
# If depois do 'for': depois é de filtro, o de filtrar coisas que eu não quero na minha lista,

# print(*nova_lista_de_produtos, sep='\n')
p(nova_lista_de_produtos)



