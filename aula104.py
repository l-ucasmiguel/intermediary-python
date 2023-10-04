# Os decoradores são o Syntax Sugar (Açucar Sintático) do Python que são utilizados para fazer o python usar as funções decoradoras em outras funções.

# Sintax Sugar
print('Função decoradora com "Syntax Sugar": \n')


def criar_funcao(funcao):                                                    # (2) É executada a FUNÇÃO DECORADORA e [funcao] recebe [inverte_string]
    def interna(*args, **kwargs):                                            # (3) 
        print('ANTES DE DECORAR')                                            # (4)
        for arg in args:                                                     # (5)
            is_string(arg)                                                   # (6)
        resultado = funcao(*args,**kwargs)                                   # (7)
        print(f'O seu resultado foi {resultado}')                            # (9)
        print('DEPOIS DE DECORAR \n')                                        # (10)
        return resultado                                                     # (11)
    return interna


def is_string(parametro):                                                    # (6)
    if not isinstance(parametro, str):
        raise TypeError('Parâmetro deve ser uma string')


@criar_funcao                                                                #                                                                                          # SYNTAX SUGAR, desta forma o [inverte_string] vai direto para [funcao] como parâmetro
def inverte_string(string):      # Função decorada                           #                                                                                                                            # [inverte_string] vira a funcao [interna] 
    return string[::-1]                                                      # (8)


# Decoração da Função [inverte_string]: A função [inverte_string] é decorada com o decorador [@criar_funcao]
# Isso significa que a função [inverte_string] é passada como argumento para [criar_funcao], criando uma
# versão decorada de [inverte_string]. Nesse ponto, a função [inverte_string] é "envolvida" pela função
# [interna] dentro de [criar_funcao].



invertida = inverte_string('456')                                            # (1) [invertida] recebe/chama a função decorada [inverte_string] passando ['456'] como argumento
print('Print Global:',invertida)                                             # (12)