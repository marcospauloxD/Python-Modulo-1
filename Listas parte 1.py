"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
#string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
string = 'ABCDE' # #5 carateres-(len) len faz contagens

# o que essa lista esta retornando true ou falsy
#print(bool([])) # falsy

# tipo de lista
#print(lista, type(lista))

#os indices dessa lista tanto podem ser acessados de forma positiva ou negativa
#---------0----1----------2---------3---4--
#       '-5'  '-4'      '-3'      '-2' '-1'
lista = [123, True, 'Luiz Otavio', 1.2, []]

#aqui ele vai alterar o indice 'Luiz Otavio' para 'Maria'
#lista[-3] = 'Maria'
#print(lista)

# se quiser eu posso checar o tipo de valor que estou mandado imprimir na lista
#print(lista[2], type(lista[2]))