# Variáveis livres e conceito de nonlocal

# 'locals' é uma função que serve para ver quais são as variáveis locais
# 'globals' faz a mesma coisa, mas para ver as variáveis globais
# 'nonlocal' serve para indicar a uma função interna que aquela variável não é local, assim a função interna vai buscar a variável no escopo global
# '__code__.co_freevars' serve para ver quais são as variáveis livres




# Conceito de free var

# def fora(x):
#     a = x*5                                                # Está é a uma variável livre(free var ), porquê ela não está definida dentro da função interna 

#     def dentro():
#         # print(locals())
#         print(dentro.__code__.co_freevars)
#         return a 
#     return dentro


# var_teste = fora(10)
# var_teste2 = fora(20)


# print(var_teste())
# print(var_teste2())




def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):                        # o valor padrão a concatenar se não for enviado nada é '', uma string vazia.
        nonlocal valor_final
        valor_final +=  valor_a_concatenar                     # 'valor_final' não é deste escopo, aqui eu só posso ler ela, não consigo alterar o valor
        return valor_final
    return interna 


var = concatenar('')
print(var('a'))
print(var('b'))
print(var('c'))
print()

final = var()                                                  # Por estar aqui, está variável acaba armazenando todos os valores concatenados até agora
print('ESTE É O FINAL [',final,']')