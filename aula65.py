"""
Introdução às funções (def) em Python

Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.

Por padrão, funções Python retornam None (nada)
"""

# Definindo função 
def saudacao(nome='sem nome'):                  # 'nome' é o parâmetro. Caso não for passado nenhum valor, neste caso vai ser usado o 'sem nome'
    print(f'Bom dia, {nome}')

saudacao()
saudacao('Maria')                               # 'Maria' é o Argumento
saudacao('João')
saudacao(input('Digite seu nome: '))