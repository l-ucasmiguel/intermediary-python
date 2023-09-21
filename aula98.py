import importlib                                # O 'importlib' é usado para recarregar e manipular módulos
import aula98_modulo


print(aula98_modulo.variavel)


for i in range (10):
    import aula98_modulo                        # O módulo do import é singleton. Singleton significa que só pode existir uma instância daquela coisa no programa.
    print()
    print(i)                                    # 'importlib.reload()' é usado para recarregar o módulo entre parenteses, sem isso o que tem dentro do módulo externo
    importlib.reload(aula98_modulo)             # Não vai se repetir, mesmo estando dentro do for 


print('Fim')


