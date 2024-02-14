# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
#
lista = [
     {'nome': 'Luiz', 'sobrenome': 'miranda'},
     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
     {'nome': 'Daniel', 'sobrenome': 'Silva'},
     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
     {'nome': 'Aline', 'sobrenome': 'Souza'},
 ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
#
## sort Ordena a lista
#lista.sort()
## sorted cria uma nova lista ordenada, porem como uma copia rasa
#sorted(lista)
## reverse muda a ordem da lista
#lista.sort(reverse=True)
#

'''
def ordena(item):
    return item['nome']

lista.sort(key=ordena)

for item in lista:
    print(item)
'''

'''
o codigo de baixo e igual a o de cima
'''

'''
lista.sort(key=lambda item: item['nome'])

for item in lista:
    print(item)


'''

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)