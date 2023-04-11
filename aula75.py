"""
Exercícios:
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
"""

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

# print('Digite um valor para duplicar: ')
# valores_duplicar = duplicar(int(input('Digite um número: ')))
# print(valores_duplicar)

# print('-'*40)

# print('Digite um valor para triplicar: ')
# valores_triplicar = triplicar(int(input('Digite um número: ')))
# print(valores_triplicar)

# print('-'*40)

# print('Digite um valor para quadruplicar: ')
# valores_quadruplicar = quadruplicar(int(input('Digite um número: ')))
# print(valores_quadruplicar)


"""
Explicando o código a cima:

Criamos 3 funções diferentes para cada operação, em seguida criamos um variável para cada função, chamando cada uma delas separadamente, usando
o input soliciatamos ao usuário que ele digite um número que vai ser o argumento passado pra função, a conta vai ser executada dentro da função
e vamos exibir ela com um print.
Essa é uma forma longa e trabalhosa de resolver o exercício.
"""





#####################################################################################################################################################################################





"""
Explicando o código a baixo: 
Esse é um código em Python que cria funções personalizadas para multiplicar números de acordo com o que o usuário digitar.


1- É Definido a função principal e a função interna, e o código segue para o escopo global porque nenhuma função foi chamada ainda.

2- É Criada a variável 'duplicar' que recebe a função principal 'criar_multiplicador', é enviado como argumento o valor digitado pelo usuário, este valor é passado para o 
parâmetro 'numero'.

3- A função principal 'criar_multiplicador' segue sendo executada e chama a função dentro dela 'multiplicar', como essa função ainda não foi chamada, o código retorna para
o escopo global.


4- A função 'print' é executada e chama a nova função 'duplicar', já passando como argumento o dígito (2), que vai como parâmetro para a função 'multiplicar'

5- Com os argumentos da função (A) e da função (B) passados, agora o código interno da função (B) é executado e retorna o resultado, que é impresso na tela
"""



def criar_multiplicador(numero):                                                            # (A) É criada a função 'criar_multiplicador, que usa 'numero' como parâmetro
    def multiplicar(multiplicador):                                                         # (B) Aqui é criada a função 'multiplicar' que usa 'multiplicador' como parâmetro.
        return multiplicador * numero                                                       
    return multiplicar                                                                      


duplicar = criar_multiplicador(int(input('Digite um número para duplicar: ')))              # (A) O número digitado aqui é passado como argumento para a função 'criar_multiplicador'
print(f'O número duplicado é: {duplicar(2)}')                                               # (B) O número que está aqui é passado como argumento para a função 'multiplicar'
print('-'*40)

triplicar = criar_multiplicador(int(input('Digite um número para triplicar: ')))
print(f'O número triplicado é: {triplicar(3)}')
print('-'*40)

quadruplicar = criar_multiplicador(int(input('Digite um número para quadruplicar: ')))
print(f'O número quadruplicado é: {quadruplicar(4)}')