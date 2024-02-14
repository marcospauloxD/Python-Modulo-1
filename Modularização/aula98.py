'''
modulos python só são carregados umas vez, caso precise recarregar o
modulo de novo posso usar o import importlib
'''

#serve para recarregar o modulo
import importlib

import aula98_m

print(aula98_m.nome)

for i in range(10):
    #recarregando o modulo
    importlib.reload(aula98_m)
    print(i)   
print('Fim')
