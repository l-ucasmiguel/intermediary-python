"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.

Existe o escopo local e global:
1. O escopo global é o escpo onde todo o código é alcançavel
2. O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.

Não temos acesso a nomes de escopos internos nos escopos externos
A palavra global faz uma variável do escopo externo ser a mesma do escopo interno
"""


x = 2                                                                          # Definindo variável no escopo global


def escopo():                                                                  # Criando Função 
    # global x                                                                   # Usando 'global' para se referir a variável 'x' global
    x = 4                                                                      # Alterando a variável 'x' global para '4'

    def outra_funcao():                                                        # Criando outra Função, dentro de uma função
        x = 6                                                                  # Definindo valores para variáveis de escopo local 'x' = '6'
        y = 7                                                                  # Definindo valores para variáveis de escopo local 'y' = '7'
        print(x,y)                                                             # Imprimir o valor de 'x' e 'y' do escopo local da função 'outra_funcao'

    outra_funcao()                                                             # Chamando a função 'outra_funcao()' dentro da função 'escopo()'
    print(x)                                                                   # Imprimir o valor de 'x' do escopo local da função 'escopo()'


print(x)                                                                       # Imprimir o valor de 'x' do escopo global


escopo()                                                                       # Chamando a função 'escopo()' ela vai seguir o passo a passo
                                                                               # que é, se referir ao 'x' global e mudar o valor dele
                                                                               # criar outra função 'outra_funcao()' e definir o valor de 'x' e 'y'
                                                                               # dentro dela(print), depois chamar a função 'outra_funcao' e por fim 
                                                                               # imprimir o valor de 'x' da funcao 'escopo()', que por ter mudado
                                                                               # também é o valor de 'x' do escopo global

print(x)                                                                       # imprimir o valor de 'x' do escopo global




"""
Eu não consigo manipular coisas que estão dentro da função, de fora da função.
se 'x' por exemplo não estiver definido no escopo local, o algoritmo vai buscar o 'x' mais próximo, seja de outro escopo local que vem antes
ou seja do escopo global, de dentro pra fora eu tenho acesso, de fora pra dentro não tem acesso.

Manipular a variável global dentro da execução da função é uma má prática de programação, pois deixa o código confuso.
"""