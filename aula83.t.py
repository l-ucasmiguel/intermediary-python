# Praticando aula 83
# Empacotamento e desempacotamento de dicionários e *args e **kargs

comidas_tipicas_br_01 = {                                                 # Criando dict 01
    'Amazonas:':'Matrinxã',
    'Bahia:':'Acarajé',
    'São paulo:':'Virado a paulista',
}

comidas_tipicas_br_02 = {                                                 # Criando dict 02
    'Rio de Janeiro:':'Camarão com Chuchu',
    'Minas Gerais:':'Tutu a Mineira',
    'Pernambuco:':'Buchada de Bode',
}

comidas_br = {**comidas_tipicas_br_01, **comidas_tipicas_br_02}           # Unindo dict 01 e 02



# for estado, comida in comidas_br.items():                               # Exibindo cada item em uma linha
    # print(estado, comida)




def nomeado_ou_nao_nomeado(*args, **kargs):
    print('Não nomeados: ', args)
    
    print('\nNomeados:')
    for chave, valor in comidas_br.items():
        print(chave, valor)

nomeado_ou_nao_nomeado(20, 313, **comidas_br)