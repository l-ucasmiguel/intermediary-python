lista = []                                      # Um 'for' dentro do outro
for x in range(3):
    for y in range(3):
        lista.append((x,y))


lista = [(x,y)                                  # Um 'for' dentrode outro com list comprehension 
        for x in range(3)                       # Para ter acesso a duas variáveis aqui, é so colocar uma tupla 
        for y in range(3)]

lista = [
        [(x,letra) for letra in 'ANA']          # Para cada 'x' do 'for', se repete 'letra'
        for x in range(3)]
        

print(lista)