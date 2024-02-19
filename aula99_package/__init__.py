# Este arquivo é executado assim que o módulo é importado

print (
    'Você importou o ', __name__,'\n'
)


def dobra(x):
    return x*2

# Este é um dos poucos casos que é recomendado usar o 'import *', para importar tudo dos seguintes módulos
from aula99_package.modulo import *
from aula99_package.modulo_2 import *


# from .modulo import nova_variavel, variavel, soma_do_modulo