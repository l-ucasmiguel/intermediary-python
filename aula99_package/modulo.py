# __all__ = [                                                        # Tudo que fica dentro de __all__ e somente isso é executado quando no módulo main o '*' 
#     'variavel',
#     'soma_do_modulo',
#     'nova_variavel'
# ]



variavel = 'Alguma coisa'
nova_variavel = 'OK'



def soma_do_modulo(x,y):
    return x + y






from aula99_package.modulo_2 import fala_oi                        # Importando um módulo irmão, ou seja, que está no mesmo namespace
fala_oi()                                                          # Chamando a função do 'modulo_2'



# Só é executado tudo que estiver dentro do all, quando é importado '*', o que não é recomendado