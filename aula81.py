# Função lambda em Python:
# A função lambda é uma função como qualquer outra em Python. São funções anônimas ou seja não tem nome, e contém apenas uma linha. Tudo deve ser contido dentro de uma expressão.
# Sintaxe da função lambda:
#       --- lambda arguments: expression ---
# arguments são os argumentos da função separados por vírgulas e expression é a expressão que a função lambda retorna.



# As funções lambda são úteis quando você precisa passar uma função como um argumento para outra função. Por exemplo, você
# pode usar uma função lambda para ordenar uma lista de dicionários com base em uma chave específica. como no exemplo abaixo:
lista_pessoas = [
    {'nome':'Luiz','idade':'29'},
    {'nome':'Maria','idade':'40'},
    {'nome':'Daniel','idade':'19'},
    {'nome':'Eduardo','idade':'20'},
    {'nome':'Aline','idade':'25'},
    
]


# Está função recebe 'lista' como parâmetro e exibe cada item da lista
def exibir(lista):
    for item in lista:                                                  # 'item' itera sobre cada elemento da 'lista' e imprime a lista atual na tela
        print(item)
    print()



# Organizando dict com a função .sorted()
# É criada uma variável e utilizado o método '.sorted()' dentro de '.sorted()' passamos a lista 'lista_pessoas', com a função lambda

# Na linha abaixo é criada uma nova lista chamada de 'l1', que recebe a função 'sorted()', está função é usada para ordenar 'lista_pessoas', o argumento 'key' é usado para especi-
# car a função lambda, que é usada para indicar o critério de ordenação. No exemplo, o critério é uma função lambda que recebe um dicionário 'item' e retorna 'item['nome']'
# Desta forma, a 'lista_pessoas' será ordenada de acordo com os valores associados à chave 'nome' de cada dicionário, em ordem alfábetica. A lista 'l1' é, portanto uma nova
# lista ordenada em ordem alfabética com base no nome de cada pessoa.
l1 = sorted(lista_pessoas,key=lambda item: item['nome'])
l2 = sorted(lista_pessoas,key=lambda item: item['idade'])               # Na lista 'l2' acontece a mesma coisa que na 'l1', mas dessa vez é ordenado com base na chave 'idade'



exibir(l1)                                                              # Chama a função 'exibir passando 'l1' como argumento, 
exibir(l2)

# print(lista_pessoas)                                                  # Lista original permanece inalterada









# .sorted() é uma FUNÇÃO embutida que retorna uma nova lista ordenada e não modifica a lista original. Sorted retorna uma nova cópia da sua lista, mas uma cópia rasa.
# .sort() é um MÉTODO de lista e modifica a lista original.

# Organizando lista com o método .sort()
# lista = [4,32,1,34,5,6,6,21]
# lista.sort(reverse=True)                                              #.sort() organiza de forma crescente  | .sort(reverse=True) organiza de forma decrescente