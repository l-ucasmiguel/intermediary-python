"""
Sets - Conjuntos em Python (tipo set)

Conjuntos são ensinados na matemática 
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo diagrama de Venn, Sets em Python são mutáveis, porém aceitam apenas tipo imutáveis como valor interno 
set parece dict por usar {}, mas diferente dos dicionários, set só tem o valor.
"""
# PARTE 01

# Criando um set:
# set(iterável) ou {1,2,3}
# s1 = set('Luiz')
# s1 = set()                    # Set vazio
# s1 = {'luiz',1,2,3}           # Set com dados
# # print(s1)
# s2 = set('jonas')             # Neste caso, essa clase itera sobre cada elemento da string, este recurso é mais utilizado para tuplas e listas ou iteráveis com valores separados
# # print(s2)





# PARTE 02

# Sets são eficientes para remover valores duplicados de iteráveis.
# - eles não tem indexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)

# lista01 = [1,2,3,3,3,3,3,1]             # Criando uma LIST
# set01 = set(lista01)                    # Convertendo a LIST criada em SET
# lista02 = list(set01)                   # Convertendo o SET em LIST
# print(lista02)

# s1 = {1,2,3}
# print(3 in s1)                            # Verificando se o digito 3 está dentro do set s1 
# for numero in s1:
#     print(numero)





# PARTE 03 

# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add('Luiz')                              # '.add()' Adiciona 01 valor por vez
# s1.add(10)                                  # '.add()' Adiciona 01 valor por vez
# s1.update(('Ola mundo', 1,2,3,4))           # '.update()' É usado para mandar vários valores
# # s1.clear()                                # '.clear()' É usado para limpar o set 
# s1.discard('Luiz')                          # '.discard()' é usado para descartar um valor, usando ele próprio como parâmetro
# print(s1)





# PARTE 04

# Operadores úteis:
# (|) É o sinal de União (union) - une
# (&) É o sinal de Intersecção (intersection), itens presente em ambos
# (-) É o sinal de Diferença, itens presentes apenas no set da esquerda 
# (^) É o sinal de Diferença simétrica, itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2
print(s3)