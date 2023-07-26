# Jeito Simples um 'for' dentro do outro
print('1) Forma simples com um "for" dentro do outro: ')
lista = []
for x in range(3):                                      # O laço 'for x' é executado primeiro
    for y in range(3):                                  # Entra no 'laço y' e só sai quando acabar a iteração, ai volta pro 'x' até se encerrar 
        lista.append((x,y))
print(lista,'\n'*2)




# List Comprehension com mais de um for 
print('2) List Comprehension com mais de um "for": ')
lista = [(x,y) for x in range(3) for y in range(3) ]      # Para ter acesso a duas variáveis aqui, é so colocar uma tupla '(x,y)'
print(lista,'\n'*2)





# Mesma coisa do código acima, mas com quebra de linha
print('3) List comprehension com mais de um "for", mas com quebra de linha: ')
lista = [(x,y)                                            # Um 'for' dentro de outro com list comprehension 
        for x in range(3)                                 # Para ter acesso a duas variáveis aqui, é so colocar uma tupla ()
        for y in range(3)]
print(lista, '\n'*2)




# List Comprehension dentro do valor em uma List Comprehension:
print('4) List Comprehension dentro do valor em uma List Comprehension:')               # Na hora de jogar o valor dentro da lista, eu fiz outra list comprehension
lista = [ [(x,letra) for letra in 'Lua'] for x in range(3)]                             # Para cada 'x' do 'for', se repete 'letra'
print(lista)