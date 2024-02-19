# EXERCÍCIO

# Aumente os preços dos produtos em 10%, gerando novos_produtos por deep copy (cópia profunda).
# Ordene os produtos por nome em ordem decrescente, gerando produtos_ordenados_por_nome por deep copy.
# Ordene os preços em ordem crescente, gerando produtos_ordenados_por_preco por deep copy.


import copy                                                     # Importando módulo copy
from aula100_dados import produtos                              # Importando a lista 'produtos' do módulo 'produtos_modulo'


print('1) LISTA ORIGINAL: ')                                    # Exibe a lista original 
print(*produtos, sep='\n')                                      # '*' está sendo usado para desempacotar a lista orignal
print()




novos_produtos = [                                              # 'p' está entre '{}' para criar um novo dict e '**' serve para desempacotar o dict
    {**p, 'preço': round (p['preço']*1.1 , 2)}                  # 'p' é um novo dict, e 'preço': p['preço'] * 1.1 é usado para atualizar o 'preço' em 10% a cada iteração
    for p in copy.deepcopy(produtos)                            # 'copy.deepcopy(produtos)' para criar e já percorrer a lista cópia
]
                                                                # O que está antes do 'for' é pra executar a cada iteração
                                                                # round é usado para arredondar valores float
                                                                # '**' desempacota dicts, e '*' desempacota listas




# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
print('2) LISTA DEEP COPY COM AUMENTO EM 10%: ')
print(*novos_produtos, sep='\n')                                # Exibe uma cópia da lista original, modificada com aumento em 10%
print()




# Ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
print('3) LISTA DEEP COPY EM ORDEM DECRESCENTE NO "PRODUTO":')                              # Mesma coisa mas usando uma função lambda para ordenar o 'produto' em ordem descresente
produtos_ordenados_por_nome = sorted(copy.deepcopy(novos_produtos), key=lambda p: p['nome'], reverse=True)
print(*produtos_ordenados_por_nome, sep='\n')
print()




print('4) LISTA DEEP COPY EM ORDEM CRESCENTE DE PREÇO:')                                    # Mesma coisa mas usando uma função lambda para ordenar o 'preço' em ordem crescente
produtos_ordenados_por_preco = sorted(copy.deepcopy(novos_produtos), key=lambda p: p['preço'])
print(*produtos_ordenados_por_preco, sep='\n')
print()


