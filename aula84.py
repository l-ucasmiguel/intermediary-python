# List comprehension em Python
# list comprehension é uma forma rápida para criar listas a partir de iteráveis

# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)                                        # O método 'append' é usado para adicionar um elemento no final de uma lista.
# print(lista)


lista = [numero * 2 for numero in range(10)]                    # A esquerda do 'for' vem a lógica.
print(lista)
