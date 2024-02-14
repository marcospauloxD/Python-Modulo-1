"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria','Helena','Luiz']
lista.append('João')

#lista_enumerada = enumerate(lista)
#aqui ele mostra o primeiro indice 0 = maria
#print(next(lista_enumerada))

#acessando o item da lista enumerada
#for item in lista_enumerada:
    #print(item)
#uma forma de contornar lista_enumerada = enumerate(lista)
#assim eu posso imprimir quantas vezes eu quiser a mesma lista
#for item in enumerate(lista):
    #print(item)
#for item in enumerate(lista):
    #print(item)
#for item in enumerate(lista):
    #print(item)

'''
para nao precisar fazer varios for para cada um imprimir uma coisa posso simplismente imprir as duas
juntas em um for só, assim ele irar me mostrar o indice e o nome.
'''
#for indice, nome in enumerate(lista):
    #print(indice,nome)



'''
caso eu so quisesse dar um print na lista poderia converter ela em list
no caso seria:
'''
#lista = ['Maria','Helena','Luiz']
#lista.append('João')
#lista_enumerada = list(enumerate(lista))
#print(lista_enumerada)

'''
tambem posso fazer o enumerate começar a partir de onde eu quiser no caso
se eu quiser que ele comece a contar a partir do numero 10:
'''
#lista = ['Maria','Helena','Luiz']
#lista_enumerada = list(enumerate(lista, start=10))
#print(lista_enumerada)

#for tupla_enumerada in enumerate(lista):
    #print('for da tupla')
    #for valor in tupla_enumerada:
        ##\t faz a mesma função que dar um tab
        #print(f'\t{valor}')