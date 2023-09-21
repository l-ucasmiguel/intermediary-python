# dir, hasattr e getattr em Python

string = 'Luiz'
metodo = 'upper'


# print(dir(string))

if hasattr(string, metodo):                                                 # Se 'string' tiver o método 'upper'
    print('Existe upper')                                                   # imprima
    print(getattr(string, metodo)())                                        
    # print(string.upper())
else:
    print('Não existe o método', metodo)






# dir()     -> Mostra todos os atributos e  métodos do objeto atual
# hasattr() -> Verifica se existe o método no objeto, sintaxe: hasattr(objeto, 'método')
# getattr() -> Pega o método de alguma variável, pega dinâmicamente