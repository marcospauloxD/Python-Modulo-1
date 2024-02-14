'''
Usei um def para criar uma calculadora de notas é entregar o resultado de que se o aluno
está aprovado ou reprovado.
'''
'''
lista_cadastro_alunos = []
lista_cadastro_turmas = []
lista_cadastro_notas = []

def cadastro():
    cadastro = input('Informe o seu nome: ')
    lista_cadastro_alunos.append(cadastro)
    turma = input('Infome a sua turma: ')
    lista_cadastro_turmas.append(turma)

    def lernotas():
        for i in range(4):
            nota = float(input('Digie a nota do aluno: '))
            resultado = (nota + nota + nota + nota) / 4
        if resultado > 6:
            print('Voçê está passado, sua média é:',resultado)
        else:
            print('Voçê está reprovado, sua média foi:', resultado)
    lernotas()
'''

lista_nome_alunos = {}
#cadastro de alunos
def cadastro_aluno():
    nome_aluno = input('Digite o nome do aluno: ')
    nota_aluno = float(input('Digite a nota do aluno: '))
    lista_nome_alunos[nome_aluno] = nota_aluno
cadastro_aluno()
print(lista_nome_alunos)

'''
notas={  }

nome = input("Digite o nome do aluno: ")
nota = float(input("Nota dele: "))

if notas.get(nome):
    print("Ja existe o aluno ",nome)
else:
    notas[nome] = nota
print(notas)
'''