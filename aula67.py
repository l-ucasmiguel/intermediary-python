"""
Valores padrão para parâmetros

Ao definir uma função, os parâmetros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.

Refatorar: Significa editar o seu código.
"""

# def soma(x,y,z=0):                                                            # 'z' terá o valor padrão '0' | '0' por padrão retorna 'false'
#     if z:
#         print(f'{x=} {y=} {z=}', x+y+z)
#     else:
#         print(f'{x=} {y=}', x+y)


# soma(6,4)
# soma(7,3)
# soma(8,2)
# soma(9,1,0)                                                                  # então nesta situação, o 'z'='0' não vai ser exibido, 'false'








# Toda vez que eu enviar um parâmetro que tem um valor padrão, todos os outros que vierem após, precisam ter um valor padrão também
def soma(x,y,z=None):                                                          # 'z' terá o valor padrão 'None' | None por padrão é 'false'
    if z is not None:                                                          # Se 'z' não for 'None' | 'None' = nenhum, 
        print(f'{x=} {y=} {z=}', x+y+z)
    else:
        print(f'{x=} {y=}', x+y)


soma(6,4)
soma(7,3)
soma(8,2)
soma(9,1,0)                                                                    # Neste caso é exibido porque 'z' não é 'None' e sim '0'
soma(z=0,x=9,y=1)                                                              # Neste caso é exibido porque 'z' não é 'None' e sim '0'

