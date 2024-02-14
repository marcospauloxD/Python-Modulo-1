# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
#
# print(list(range(10)))
'''
como normalmente se faria uma lista

lista1 = []
for numero in range(10):
    lista1.append(numero)
print('lista 1: ', lista1)
'''

'''
nessa parte de baixo esta sendo utilizado o list comprehension
'''
#lista2 = [numero * 2 for numero in range(10)]
#print('lista 2: ', lista2)

#lista3 = [numero for numero in range(10)]
#print('lista 3: ', lista3)

lista = [numero for numero in range(10)]
print(lista)