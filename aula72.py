# Exercícios com funções 

"""
1- Crie uma função que multiplica todos os argumentos não nomeados recebidos
2- Retorne o total para uma variável e mostre o valor da variável 
"""


print('Multiplicando os números: ')
def mult(*args):
    total = 1
    for numero in args:
        total *= numero                                                                 # total = numero * total
    return total

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite outro número: '))

multiplicacao = mult(numero1,numero2,numero3)
print(f'A multiplicacão dos números {numero1}x{numero2}x{numero3}= ', multiplicacao)


print('-'*88)
"""
1- Crie uma função que fala se o número é par ou ímpar 
2- Retorne se o número é par ou ímpar
"""


print('Verificando se o número é ímpar ou par: ')
def impar_par(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'                                                          # Não precisa do 'else' porque se o primeiro 'return' não for atingido, vai ser o próximo


print(impar_par(int(input('Digite um número: '))))