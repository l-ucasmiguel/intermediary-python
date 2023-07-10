# List Comprehension

print(list(range(10)))                                                    # Criando uma lista usando 'range'



lista = []
for numero in range(10):                                                  # Criando uma list usando 'for'
    lista.append(numero)
# print(lista)



# List comprehension                                                      # Criando uma lista usando List Comprehension
lista = [numero for numero in range(10)]                                  # Sempre o que está a esquerda em List Comprehension é o que vai ser add no final da lista.
print(lista)