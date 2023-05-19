# Generator expression, Iterables e Iterators em Python

# Iterável é um item sequêncial que podemos acessar coisas sequêncialmente. Tem a responsabilidade de deter os valores sequêncialmente.
# Iterador a única responsabilidade do iterador é entregar um valor por vez. Ele não sabe o tamanho do iterável, só sabe entregar quem é o próximo .

iterable = ['Eu','Tenho','__iter__']
iterator = iter(iterable)                               # tem __iter__ e __next__


print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))