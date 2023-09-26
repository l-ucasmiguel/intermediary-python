"""
Closure e funções que retornam outras funções 
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar                                                   
                                                                    # Sem os '()' eu retorno a função que está na memória, e não executando o corpo dela
                                                                    # Mesmo sem exibir no momento, a variável fica salva no escopo da função
                                                                    # Dessa forma eu adio a execução da função por completo, e com isso também posso adiar
                                                                    # A passagem de parâmetros, como por exemplo 'nome'. Na execução da função 'nome' vai
                                                                    # Ser dinâmico.


falar_bom_dia   = criar_saudacao('Bom dia')
falar_boa_tarde = criar_saudacao('Boa tarde')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia('Maria'))                                       # Usando os '()' agora é executada a função
print(falar_boa_tarde('Jorge'))                                     # Porque ao invés de dar print somente na variável 'falar_boa_tarde'
print(falar_boa_noite('Roben'))                                     # Usamos o '()' para chamar o valor 
print()


for nome in ['Fernan','Juan','Cristiano']:
    print(falar_bom_dia(nome))
    print(falar_boa_tarde(nome))
    print(falar_boa_noite(nome))