import random
a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')
lista = [a,b,c,d]
'''
random.sample(lista,k=4) o sample percorrer a lista passada e o k=4 e um contador de quantas vezes 
eu quero que a quantidade de nomes apareça
'''
#rand = random.sample(lista, k=4)
random.shuffle(lista)
print('A ordem de apresentação é')
print(lista)