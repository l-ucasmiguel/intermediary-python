# Valores Truthy e Falsy (Verdadeiro e Falso),             Tipos Mutáveis e imutáveis
# Mutáveis      lista[]     dict{}         set()
# Imutáveis     tupla()     string("")     inteiro(0)      float(0.0)      None    False    range(0, 10)
# Todos esses valores abaixo, vazio/desta forma são considerados 'Falsy', ao contrário deles é 'Truthy', com exceção do 'None' que não tem o inverso

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE', falsy('TESTE'))
print()

print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))

