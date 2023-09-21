# Try       -   Tentar.
# Except    -   Exceção
# Else      -   Se não
# Finally   -   Finalmente
# Sempre especificar o 'except' para não mascarar outros erros.

# a = 18
# b = 0 
# c = a / b


try:
    a = 18
    b = 0                                                                   # Esta linha comentada vai fazer ser acionado o 'Except NameError'
    # print(b[0])                                                           # Esta linha vai fazer ser acionado o 'Except TypeError'
    print('Linha 01'[1000])                                                 # Essa linha vai fazer ser acionado o 'Except IndexError'
    c = a / b                                                               # Esta linha vai fazer ser acionado o 'Except ZeroDivisionError'
    print('Linha 02')


except ZeroDivisionError:                                                   # Trata o 'except' 'ZeroDivisionError'
    print('ZeroDivisionError. tentou dividir por zero')


except NameError:                                                           # Trata o 'except' 'NameError'
    print('NameError. nome "b" não está definido')

except (TypeError, IndexError) as error:                                    # O 'as' indica em qual variável eu quero jogar a instância do erro  
    print('TypeError ou IndexError')
    print('Nome:', error.__class__.__name__)                                # Usando o 'as' e o 'error.__class__.__name__', conseguimos descobrir qual foi o nome do erro

except Exception:                                                           # Trata o 'except' 'Exception' que é a maior classe de erro em python, abrange todos os erros
    print('Exception. Erro desconhecido')

print()
print('CONTINUAR')


# Ao colocar entre '()', ou seja, tuplas, é possível passar mais de um erro
# É Possível colocar duas exceções em um except, porém não é recomendado.
