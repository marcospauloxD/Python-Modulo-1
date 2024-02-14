#lista = ['maria', 'joão', 'alberto']

#print( lista[0],'\n',lista[1],'\n',lista[2])
#print(lista)

lista = ['maria', 'marcos','joão']

# esta variavel esta percorrendo o tamanho da minha lista
indices = range(len(lista))
#aqui esta atribuindo o valor de indices a indice
for indice in indices:
    # aqui ele imprimi um a um os valores da lista
    print(lista[indice])



#imprimindo indices de forma aleatoria
#import random

#for i in range(1):
    #lista = ['marcos','joao','cleber']
    #pseu = random.choice(lista)
    #print(pseu)