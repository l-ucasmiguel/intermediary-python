# Função lambda em Python:
# A função lambda é uma função como qualquer outra em Python. São funções anônimas ou seja
# não tem nome, e contém apenas uma linha. Tudo deve ser contido dentro de uma expressão.
# Sintaxe da função lambda:

# lambda arguments: expression
# 'arguments' são os argumentos da função separados por vírgulas e 'expression' é a expressão
# que a função lambda retorna. A função lambda é indicada em situações que precisamos de uma
# função simples e rápida, ou quando queremos passar parâmetros para outra função.


# Função convencional
def funcao(arg1, arg2):
    return arg1 + arg2

a = funcao(111,111)
print(a)

print()

# Função lambda
a = lambda x,y: x * y
print(a(50,10))
print('\n'*2)






# As funções lambda são úteis quando você precisa passar uma função como um argumento para outra
# função. Por exemplo, você pode usar uma função lambda para ordenar uma lista de dicionários
# com base em uma chave específica. como no exemplo abaixo:
lista_pessoas = [
    {'nome':'Luiz','idade':'29'},
    {'nome':'Maria','idade':'40'},
    {'nome':'Daniel','idade':'19'},
    {'nome':'Eduardo','idade':'20'},
    {'nome':'Aline','idade':'25'},
    
]



# Está função recebe 'lista' como parâmetro, neste momento não tem nada em lista. O código vai
# seguir e exibir cada item da lista. O 'item' itera sobre cada elemento da 'lista' e imprime
# a lista atual na tela.
def exibir(lista):
    for item in lista:
        print(item)
    print()



# Organizando dictionary list com a função .sorted()
# Na linha abaixo é criada uma nova lista chamada de 'l1', que recebe a função 'sorted()' e
# dentro passamos a 'lista_pessoas', que vai ser organizada pela função lambda. O argumento
# 'key' é usado para especificar a função lambda, que é usada para indicar o critério de
# ordenação.

# No exemplo, o critério é uma função lambda, que dentro recebe 'item' e retorna 'item[nome].
# Desta forma, a 'lista_pessoas' será ordenada de acordo com os valores associados à chave 'nome'
# de cada dicionário, em ordem alfabética. A lista 'l1' é portanto, uma nova lista ordenada em 
# Ordem alfabética com base no nome de cada pesssoa.
l1 = sorted(lista_pessoas,key=lambda item: item['nome'])
l2 = sorted(lista_pessoas,key=lambda item: item['idade'])
# Na lista 'l2' acontece a mesma coisa que na 'l1', mas dessa vez é ordenado com base na chave
# 'idade'


exibir(l1)                                                              # Chama a função 'exibir passando 'l1' como argumento, 
exibir(l2)

# print(lista_pessoas)                                                  # Lista original permanece inalterada









# .sorted() é uma FUNÇÃO embutida que retorna uma nova lista ordenada e não modifica a lista original. Sorted retorna uma nova cópia da sua lista, mas uma cópia rasa. SHALLOW COPY
# .sort() é um MÉTODO de lista e modifica a lista original. DEEP COPY

# Organizando lista com o método .sort()
# lista = [4,32,1,34,5,6,6,21]
# lista.sort(reverse=True)                                              #.sort() organiza de forma crescente  | .sort(reverse=True) organiza de forma decrescente