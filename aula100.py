# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preço crescente (do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# for i in produtos:
#     print()
#     print(produtos)

# Para resolver esse exercício, preciso rever.

# 1- FUNÇÃO LAMBDA                                          CHECK
# 2- PACKAGES                                               CHECK
# 3- LIST COMPREHENSION
# 4- ROUND()


import copy                                                                               # Importando módulo copy 

from aula100_dados import produtos                                                        # Importando a lista 'produtos' do package 'aula100_dados'

# novos_produtos = [
#     {**p, 'preço': round(p['preço'] * 1.1, 2)}
#     for p in copy.deepcopy(produtos)
# ] 




# O asterisco (*) antes do nome da lista 'produtos' descompacta os elementos da lista como argumentos separados para a função 'print()'
# O parâmetro sep='\n' é passado para a função 'print()', onde '\n' é o caractere de nova linha. Isso define que cada elemento da lista será impresso em uma nova linha.
print(*produtos, sep='\n')                             
print()       
# print(*novos_produtos, sep='\n')


























































