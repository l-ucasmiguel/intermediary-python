# Aula 84
# Introdução a List Comprehension
print('Exemplo 01) \n')
lista = []
for numero in range(11):                                                   # Criando uma list usando 'for', 'append' e 'range'
    lista.append(numero)
print('Criando uma lista usando "for", "append" e "range": ')
print(lista,'\n'*1)




# List comprehension
lista = [                                                                  # Utilizar quebra de linha para ficar mais fácil a visualização quando o código fica grande
    numero * 7                                                             # As expressões sempre ficam a esquerda do código, no começo. E as condições sempre ficam a 
    for numero in range(11)                                                # direita, no final.
]
print('Criando uma lista usando "list comprehension": ')
print(lista)
print('\n')
print('-'*63)
print('\n')






print('Exemplo 02) \n')
# Imagine que você precise criar uma lista com 20 números aleatórios inteiros, entre 0 e 10. Como você faria?

import random                                           # Importando lib random
random.randint(0,10)                                    # Pede para que os números random que vão ser gerados sejam entre 0 e 10

print('Lista com 20 números aleatórios: ')
numeros = []                                            # É criada uma lista vazia
for i in range(20):                                     # É feito um 'for' com 20 iterações
    num_aleatorio = random.randint(0,10)                # Gerando um inteiro aleatório entre 0 e 10
    numeros.append(num_aleatorio)                       # Os números inteiros gerados na linha acima, é passado pra cá com 'append'

print(numeros,'\n')




# Com List Comprehension
print('Lista com 20 números aleatórios usando "list comprehension": ')
lista_de_compressao = [random.randint(0,10) for _ in range(20)]            # O que está antes do 'for' é pra executar a cada iteração
print(lista_de_compressao)                                                 # Quando não estamos utilizando a variável do 'for', podemos substituir pelo '_'
print('\n')
print('-'*63)
print('\n')






print('Exemplo 03) \n')
# Imagine que já tenha uma lista de inteiros (vamos utilizar a lista que criamos no exemplo anterior) e queria obter uma nova lista a partir dela,
# que contenha apenas números pares

print('Lista feita com base na última lista, mas somente com os números pares: ')

nova_lc = [i for i in lista_de_compressao if i%2 == 0 ]                    # Se o resto da divisão (módulo) for = 0, ou seja, se o número for par, inserir ele na lista
print(nova_lc)
print('\n')
print('-'*63)
print('\n')






print('Exemplo 04) \n')
# Imagine que você tenha uma string, e deseje remover todos os caracteres que não forem letra e nem espaço

print('String a ser organizada: ')
texto = 'P4yth)on] &l@ang**`uague'                                             # [STRING]
print(texto,'\n')
nova_lista = [letra for letra in texto if letra.isspace() or letra.isalpha()]  # 'isspace()' serve para verificar se tem espaço, 'isalpha()' serve para verificar se é alfabeto. [LIST]

converter = ''.join(nova_lista)                                                # Juntamos a lista com 'join()' e convertemos em uma string
print('Nova string filtrada: ')
print(converter)
print('\n')
print('-'*63)
print('\n')






print('Exemplo 05) \n   Desafio)')
print('Converta uma lista de datas em string para o formato datetime: \n')
# Você tem uma lista com várias datas em formato de string, e deseja convertê-las para o formato datetime do python, o que vai te permitir
# Muito mais flexibilidade para lidar com as datas. Como você poderia fazer isso usando list comprehension?

import datetime                                                                                     # Importando o módulo datetime

datas_string = ['01/08/2021','17/08/2000','04/05/1997','31/01/2000','26/10/2000']                   # Criando uma lista com string de datas
datas_datetime = [datetime.datetime.strptime(data, '%d/%m/%Y') for data in datas_string]            # Convertendo as strings para datetime com 'strptime'
datas_formatadas = [data.strftime('%d/%m/%Y') for data in datas_datetime]                           # Usando 'strftime' para formatar 
print(*datas_formatadas, sep='\n')