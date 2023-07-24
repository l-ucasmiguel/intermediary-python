# Mapeamento de dados em list comprehension
print('2) Mapeamento de dados em List Comprehension: \n')


print('Lista original:')
lista_de_produtos = [                                                               # Lista de Dicts
    {'nome':'p1','preço':20},
    {'nome':'p2','preço':10},
    {'nome':'p3','preço':30},
]

print(*lista_de_produtos, sep='\n')
print('\n'*1)




print('Lista alterada com aumento em 5%: ')
nova_lista_de_produtos = [
    {**produto, 'aumento 5%': produto['preço'] *1.05}     # Entre {} pq é um novo dict || Usando '**' para desempacotar o dict antigo em um novo || Criando nova chave para 'aumento 5%'
    if produto['preço'] >= 20 else {**produto}            # Se produto['preço'] >= 20 exibir 'aumento 5%', se não retornar o dict original
    for produto in lista_de_produtos
    if (produto['preço'] >= 20 and produto['preço'] * 1.05 > 10)   # Se produto['preço'] >= 20 & produto['preço'] * 1.05 > 10 EXIBIR FILTRANDO
]

# If antes do 'for' : antes é de mapeamento, map sempre vai retornar a mesma quantidade de elementos
# If depois do 'for': depois é de filtro, o de filtro não tem else, filter, é quando não queremos incluir determinado item se a condição 'for' True

# Filtro, filtrar coisas que eu não quero na minha lista, isto vem depois do 'for', o que for filtro é só 'if' não tem 'else' 
# O que vem a esquerda do 'for' é mapeamento, o que vem a direita do 'for' é filtro

# filter, filtrar coisas que eu não quero na minha lista, 
print(*nova_lista_de_produtos, sep='\n')
