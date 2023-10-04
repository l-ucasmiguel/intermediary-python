# FUNÇÕES DECORADORAS E DECORADORES

# Decorar             -> Adicionar/ Remover/ Restringir/ Alterar.
# Funções decoradoras -> São funções que decoram outras funções.
# args                -> São argumentos posicionais não nomeados, e são usados para passar uma quantidade ilimitada de argumentos não nomeados. Geralmente usado em tuple e list.
# kargs               -> São argumentos nomeados, geralmente usado em dicts
# Funções decoradas requer a aplicação de closure



print('Função decoradora "Fazendo na mão": \n')

def criar_funcao(funcao):                                                    # (2) É executada a função [criar_funcao] e a função [inverte_string] é o argumento recebido
    def interna(*args, **kwargs):                                            # (5) Ao chamar [checando_parametro] voltamos a [interna] e [args] recebe [123] como parâmetro
        print('ANTES DE DECORAR')                                            # (6) Imprime na tela [ANTES DE DECORAR] antes do loop
        for arg in args:                                                     # (7) [arg] itera sobre o único argumento passado, que é [args] [123], para cada argumento no loop [is_string] é chamado para verificar se o argumento é uma string
            is_string(arg)                                                   # (8) [is_string] é uma função que passa [arg] como argumento.
        resultado = funcao(*args,**kwargs)                                   # (10) [funcao] é o [inverte_string] A função [inverte_string] é chamada com [123] como argumento, e seu resultado invertido é armazenado na variável [resultado].
        print(f'O seu resultado foi {resultado}')                            # (12) A função [interna] imprime o [resultado], que é a string invertida '321'.
        print('DEPOIS DE DECORAR \n')                                        # (13) Imprime na tela [DEPOIS DE DECORAR]
        return resultado                                                     # (14) A função [interna] retorna a string invertida [321]
    return interna                                                           # (3) Retorna a função [interna] mas sem executar, apenas salvando os valores 




def is_string(parametro):                                                    # (9) É uma função criada para verificar se [parametro] é uma string, neste caso recebe [123]
    if not isinstance(parametro, str):                                       # Se o [parametro] não for string uma exceção [type error] é levantada
        raise TypeError('Parâmetro deve ser uma string')                     # Com uma mensagem personalizada.




def inverte_string(string):                                                  # (11) É uma função criada para inverter a string com fatiamento
    return string[::-1]




checando_parametro = criar_funcao(inverte_string)                            # (1) [checando_parametro] recebe/chama a funcao [criar_funcao] com a funcao
                                                                             # [inverte_string] sendo passada como argumento.




invertida = checando_parametro('123')                                        # (4) [invertida] recebe/chama a funcao [checando_parametro] com ['123'] sendo passado
                                                                             # como argumento




print('Print Global:',invertida,'\n')                                        # (15) Finalmente, você imprime o valor de [invertida], que é a string '321'
                                                                             # resultante da execução da função decorada