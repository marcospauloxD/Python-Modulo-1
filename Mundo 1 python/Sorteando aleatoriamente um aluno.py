import random
a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')

lista = [a,b,c,d]
ale = random.choice(lista)
'''
Retorna aleatoriamente os nomes dentro da lista

#ale = random.choice([lista])
#ale = random.choice([a,b,c,d])
'''
print('O aluno escolhido foi: ',ale)