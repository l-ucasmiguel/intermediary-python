# Iterables e Iterators em Python
# Iterável(Iterable) é um item sequêncial que podemos acessar coisas sequêncialmente. Tem a responsabilidade de deter os valores sequêncialmente.
# Iterador(Iterator) a única responsabilidade do iterador é entregar um valor por vez. Ele não sabe o tamanho do iterável, só sabe entregar quem é o próximo.


iterable = ['Eu','Tenho','__iter__']
iterator = iter(iterable)                                      # tem __iter__ e __next__
# print (next(iterator))
# print (next(iterator))
# print (next(iterator))





# Generator expression, são funções que sabem pausar. Todo generator é um iterator, mas um iterator não é um generator

import sys                                                     # Importando módulo 'sys'

lista = [n for n in range(10000)]                            # Criando uma list comprehension
generator = (n for n in range(10000))                        # Criando uma Generator expression, é igual uma list comprehension, mas com '()'

print(sys.getsizeof(lista))                                    # sys.getsizeof() mostra o tamanho em bytes na memória
print(sys.getsizeof(generator))
print()
"""
O generator expression não salva todos os valores na memória, ele te entrega um valor por vez.

A list conforme aumenta a quantidade de elementos, ela vai salvar cada vez mais na memória, porque salva tudo na memória. E como esta na memória, na list é possível
acessar os elementos pelo índice, o que não da pra fazer com generator expression."""

# O generator expression fica parado no primeiro valor até que se chame o próximo. ex: 
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# for n in generator:                                             # Percorre e entrega 1 valor por vez 
#     print (n)