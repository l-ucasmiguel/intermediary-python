# Praticando aula 81, 82
# Funções lambdas

lista_guerreiros = [                                                               # LISTA DE DICIONÁRIOS
    {'nome':'vegeta','poder':'galick ho'},
    {'nome':'sasuke','poder':'chidori'},
    {'nome':'naruto','poder':'rasengan'},
    {'nome':'goku','poder':'kamehameha'},
    {'nome':'homem aranha','poder':'teia'},
    {'nome':'noturno','poder':'teletransporte'},
    {'nome':'ciclope','poder':'laser'},
    {'nome':'orochimaru','poder':'yamata no jutsu'},
    {'nome':'freeza','poder':'supernova'},
    {'nome':'magneto','poder':'magnetismo'},
]


def exibir_guerreiros(item_da_lista):
    for item_que_itera in item_da_lista:
        print(item_que_itera)
    print()
    


organizar_guerreiros = sorted(lista_guerreiros, key=lambda item_que_itera : item_que_itera['nome'])
organizar_guerreiros_2 = sorted(lista_guerreiros, key=lambda item_que_itera : item_que_itera['poder'])


exibir_guerreiros(organizar_guerreiros)
exibir_guerreiros(organizar_guerreiros_2)
