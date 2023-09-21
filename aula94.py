# Try       -   Tentar.
# Except    -   Exceção
# Else      -   Se não
# Finally   -   Finalmente 

# Finally é um bloco que sempre será executado, mesmo que ocorra um erro.

try:
    print('ABRIR ARQUIVO')                              # Abrir arquivo
    # 9/0                                               # No processo ocorreu um erro

except ZeroDivisionError:
    print('ZeroDivisionError. DIVIDIU ZERO')            # Mostra o erro, a exceção

else:
    print('Não ocorreu erro.')                          # Meio redundante usar o else, porque o finally pode ser usado para isso | não é comum ser usado

finally:
    print('FECHAR ARQUIVO')                             # Mesmo depois do erro, 'finally' vai executar este bloco



# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions