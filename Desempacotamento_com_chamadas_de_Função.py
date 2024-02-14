'''
#Desempacotamento em chamadas de metodos
e funções

'''
string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [
       #-0----------1
       ['Maria', 'Helena',], #--0
        #-0
        ['Elaine',], #--1
        #-0--------1--------2
        ['Luiz','João','Eduarda',(0, 10, 20, 30, 40)], #--2
]

#*_ seria o resto da lista
#p= primeiro, ap= antipenultimo, u= ultimo
#p, b, *_, ap, u = lista
#print(p,ap,u)
#print('Maria', 'Helena', 'Eduarda')
'''
esse print(*lista) faz a mesma coisa que 
esse print de cima, ele pega a lista e passa
os valores separados
'''
#print(*lista)
#print(*salas)

#esse end esta fazendo uma quebra de linha no final
#print(*salas, end='\n')

#esse sep parece que separa em colunas a lista
print(*salas, sep='\n')

