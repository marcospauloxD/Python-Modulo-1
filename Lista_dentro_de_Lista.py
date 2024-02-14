"""
Lista de listas e seus índices
"""

salas = [
       #-0----------1
       ['Maria', 'Helena',], #--0
        #-0
        ['Elaine',], #--1
        #-0--------1--------2
        ['Luiz','João','Eduarda',(0, 10, 20, 30, 40)], #--2
]

#print(salas)
#para acessar um indice e um valor dentro dessa lista
#print(salas[1][0]) #esta acessando o indice 1 'Elaine'
#outro exemplo
#print(salas[2][2]) #esta acessando o indice 2 'Eduarda'
#outro exemplo
#print(salas[0][1])  #esta buscando o valor 'Helena'
#pegando uma tupla de dentro da lista 
#print(salas[2][3][2])
'''
 para cada sala em salas, este for maior esta me 
 motrando as salas
'''
for sala in salas:
    print(f'A sala é {sala}')
    #este esta exibindo o nome dos alunos dentro da sala
    for aluno in sala:
        print(aluno)