# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
# Se dentro 'except' a gente tiver um 'raise', vai ser relançado o erro



# Está função verifica se o valor passado como argumento 'div' é igual a zero, Se for igual a zero a função gera uma Exceção 'ZeroDivisionError'
# Caso contrário a função retorna true
def nao_aceito_zero(div):
    if div == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero.')
    return True


# Está função verifica se  o valor passado como argumento 'num' é do tipo 'float' ou 'int', para isso ela utiliza 'isinstance(num,(float,int))' que verifica se o objeto é
# uma instância de uma classe ou de qualquer uma de suas subclasses, se 'num' não for do tipo 'float' ou 'int' a função gera uma Exceção 'TypeError' com a mensagem "{num}
# deve ser int ou float." seguida do tipo do objeto enviado. Caso contrário, a função retorna 'True.
def deve_ser_int_ou_float(num):
    tipo_x = type(num)
    if not isinstance(num,(float,int)):
        raise TypeError(
            f'{num} deve ser int ou float. \n'
            f'"{tipo_x.__name__}" enviado'
            )
    return True


# Está função é responsável por executar a divisão de 'num' por 'div'. Antes de realizar a divisão ela chama as funções 'deve_ser_int_ou_float(num)' e 'deve_ser_int_ou_float(div)'
# Para garantir que os argumentos sejam do tipo corretos. Em seguida ela chama a função 'não_aceito_zero(div)' para verificar se 'div' é diferente de zero. Se todas as verificações
# Passarem a função retorna o resultado da divisão entre 'num' e 'div'. 
def divide(num, div):
    deve_ser_int_ou_float(num)
    deve_ser_int_ou_float(div)
    nao_aceito_zero(div)
    return num / div 


print(divide(8,'0'))