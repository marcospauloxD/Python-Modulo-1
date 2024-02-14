'''
# 1 forma de importar
from aula99_packages.modulo import soma
# 2 
import aula99_packages.modulo
# 3
from aula99_packages import modulo
# 4: quando ele importar tudo o all dentro do arquivo modulo ira importar o que eu disser
#para importar
from aula99_packages.modulo import *
#importando o path 
from sys import path
#__name_ serve para saber se o nome do arquivo
print(__name__)

#exibindo *path esta desempacotando uma lista  e colocando um separador com uma quebra de linha
#print(path, sep='\n')

#exibindo a soma 
print(soma(3, 4))
#outra forma de exibir a mesma coisa
print(aula99_packages.modulo.soma(5, 1))
#outra forma de exibir
print(modulo.soma(4, 5))

print(variavel)

'''

'''
#as importações devem ser feitas na pasta main
from aula99_package.modulo import variavel, fala_oi

#modulo serve para importar um funcionalidade de dentro do arquivo
#from aula99_package.modulo_b import fala_oi

print(__name__)

fala_oi()


print(variavel)
'''

import aula99_package

#enganando o python para fazer ele acreditar que estou chamando um modulo
#no caso acabei chamando dobra
#print(aula99_package.dobra(2))

print(aula99_package.nova_variavel)
print(aula99_package.soma(2, 2))
print(aula99_package.variavel)