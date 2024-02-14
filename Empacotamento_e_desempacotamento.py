"""
Introdução ao empacotamento e desempacotamento
"""

#_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
#print(nome)

#ele oculta os valores da lista, neste caso este ocultado o indice 'helena' e 'luiz'
#lista, *_ = ['maria', 'helena','luiz']
#print(lista)

#aqui ele esta ocultando o valor 'maria' e 'luiz'
#_, lista, *_ = ['maria','helena','luiz']
#print(lista)

#aqui ele esta ocultando 'maria' e 'helena'
#_,_,lista = ['maria','helena','luiz']
#print(lista)

#isso serve para caso eu nao queria usar esses indices é se caso algum outro programador
#olhar meu codigo ira saber disso

'''
funçao args, Empacotamento e Desempacotamento
'''

#x, y, *resto = 1, 2, 3, 4
#print(x,y,resto)

#def soma(x, y)
#   return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
soma(1, 2, 3, 4, 5, 6)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))
# print(*numeros)
