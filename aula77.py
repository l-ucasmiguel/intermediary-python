perguntas= [                                                # Este trecho do código é uma lista de dicionários
    {
        'Pergunta':'Quanto é 2+2?',
        'Opções':['1','2','3','4'],
        'Resposta':'4',
    },
    {
        'Pergunta':'Quanto é 5*5?',
        'Opções':['25','55','10','51'],
        'Resposta':'25'
    },
    {
        'Pergunta':'Quanto é 10/2?',
        'Opções':['4','5','2','1'],
        'Resposta':'5',
    },
]


qtd_acertos = 0 
for pergunta in perguntas:                                  # 'pergunta' é o iterador que está percorrendo o iterável 'perguntas'
    print('Pergunta:',pergunta['Pergunta'])                 # usamos 'pergunta['Pergunta']' para acessar a/o chave/índice 'Pergunta' do dicionário
    print()


    opcoes = pergunta['Opções']                             # variável 'opcoes' recebe 'pergunta[Opções]'
    for i, opcao in enumerate(opcoes):                      # usamos o 'for' para a lista de opções aparecer de forma vertical, o 'i' e o 'enumerate(opcoes)' é para termos um índice
        print(f'{i}) {opcao}')
    print()


    escolha = input('Escolha uma opção: ')                   # Escolher o índice de uma opção | é uma string até aqui


    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)                                # Conta quantas opções tem, len() conta quantos itens tem ao total


    if escolha.isdigit():                                   # Se todos os caracteres digitados na string forem digitos ele executa o código abaixo
        escolha_int = int(escolha)                          # é convertido para número inteiro 


    if escolha_int is not None:                             # Se 'escolha_int' não for None, a linha abaixo é executada
        if escolha_int >= 0 and escolha_int < qtd_opcoes:   # Se o que eu digitei no 'escolha_int' for >= 0 & < qtd_opcoes a linha abaixo é executada
            if opcoes[escolha_int] == pergunta['Resposta']: # Se a opção escolhida 'opcoes[escolha_int]' for igual a resposta certa 'pergunta['Resposta']'
                acertou = True                              # É retornado true 


    print()

    
    if acertou == True:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errado 👎')

    print()

print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas')

