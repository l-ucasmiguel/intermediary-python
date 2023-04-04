"""
args    -  são argumentos não nomeados 

*args   - (empacotamento e desempacotamento)
(1,2,3) - são tuplas    imutáveis
[1,2,3] - são listas -  mutáveis
"""


# Lembre-te de desempacotamento                                        # 'x' equivale ao primeiro valor da tupla '1'
# x, y, *resto = 1,2,3,4                                               # 'y' equivale ao segundo valor da tupla '2'
# print(x,y, resto)                                                      
# e o restante da tupla eu não quero guardar em variável, então eu empacoto isso em '*resto'




# def soma(x,y):
#     return x + y




# *args é usado para passar uma quantidade ilimitada de argumentos não nomeados.
def soma(*args):                                                       # A convenção em função é usar *args (Argumentos não nomeados)
    print(args)                                                        #
    total = 0                                                          # Acumulador
    for numero in args:
        total += numero                                                # total = total + numero  
    return total


soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3,)

soma_4_5_6 = soma(4,5,6)
print(soma_4_5_6,)




numeros = 1,2,3,4,5,6,7,78,10
outra_soma = soma(*numeros)                                            # Desempacotando, com '*' sem isso iria dar erro, por estar passando tuple 
print(outra_soma)                                                      # E quando chegar na função iria empacotar de novo, gerando erro

print('-' *29)

print(numeros)
print(*numeros)


# print(sum((1,2,3,4,5,6,7,78,10)))                                    # Função que soma



# '*args' empacota o que eu enviar para a função dentro de uma tuple
# ex: '*numeros' desempacota uma tupla para enviar como parâmetro para uma função