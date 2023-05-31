import importlib                                # O 'importlib' é usado para recarregar e manipular módulos
import aula98_modulo

print(aula98_modulo.variavel)


for i in range (10):
    import aula98_modulo                        # O módulo do import é singleton. Singleton significa que só pode existir uma instância daquela coisa no programa.
    print()
    importlib.reload(aula98_modulo)             # 'importlib.reload()' é usado para recarregar o módulo entre parenteses
    print(i)


print('Fim')