''''
#lista
#adicionando algo dentro de uma lista

lista = []

lista.append('Ola mundo')
lista.append('Brazil')

print(lista)

'''

'''
#lista
#exibindo o maior e o menor numero

numero = [10, 9, 8, 7, 6]

print('Total: ', len(numero))
print('Menor valor: ', min(numero))
print('Maior valor: ', max(numero))
'''

'''
#Repetição for

notas = []

for i in range(2):
    codigo_aluno = input('RM: ')
    nota = float(input('Nota: '))
    #criando uma segunda lista e armazenando codigo_aluno e nota dentro dessa lista
    resultado = [codigo_aluno, nota]
    #armazenando essa segunda lista dentro da lista notas que é a principal
    notas.append(resultado)
#print('Quantida de notas', len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print (f'O RM: ',{codigo_aluno}, 'Tirou a nota: ',{nota})
'''

'''
#Repetição While

notas = []

contador = 0

while contador <= 2:
    codigo_aluno = input('RM: ')
    nota = float(input('Nota: '))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    #altrenativa: contador = contador + 1
    contador += 1

print('Quantidade de notas: ', len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print(f'O RM',{codigo_aluno},'A nota: ',{nota})
'''

#Dicionarios
'''
#EXEMPLO 1

pessoa = {
    'nome': 'Programador Python',
    'idade': 27,
    'peso': 70.2
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['peso'])
'''
'''
#informações do jogador
player = {
    'nome': 'Guilherme',
    'level': '1',
    'hp': 100,
    'exp': 0,
    'dano': 5,
}

#lista de inimigos
npcs = [
    {'nome': 'Monstrinho', 'dano': 2, 'hp': 50, 'exp': 5},
    {'nome': 'Monstro', 'dano': 5, 'hp': 100, 'exp': 10},
    {'nome': 'Monstrão', 'dano': 10, 'hp': 150, 'exp': 15},
    {'nome': 'Chefão', 'dano': 25, 'hp': 200, 'exp': 20},
]
'''

'''
#Chat de Mensagens

import os
 
mensagens = []

nome = input('Nome: ')

while True:
    #limpando terminal

    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], '-', m['texto'])


    print('________________')

    # Obtendo texto
    texto = input('mensagem: ')
    if texto == 'fim':
        break

    # adicionando mensagem na lista
    mensagens.append({
        
        'nome': nome,
        'texto': texto})
'''

# Funções
'''
def minha_funcao(valor1, valor2):
    return valor1 + valor2
#10 = valor1, 15 = valor2
resposta = minha_funcao(10,15)
print('resposta: ',resposta)
'''

'''
# função que faz a soma de dois valores

def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    #minha_funcao chama a função que faz a soma do valor1 + valor2
    resposta = minha_funcao(valor1, valor2)
    print('O resultado é: ', resposta)
'''

#codigo  sem funcao
fluxo_caixa = []

print('-----------')
print('fluxo de caixa')
print('-----------')
print('1 - Adicionar receita')
print('2 - Adicionar despesa')
print('\n# Digite outro numero para encerrar #\n')

def adicionar_transacao():
    nome = input('Nome: ')
    valor = int(input('Valor: '))
    fluxo_caixa.append({
            'nome': nome,
            'valor': valor
        })
while True:
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()
    else:
        break
#nota fiscal
total = 0
for  fc in fluxo_caixa:
    print('Nome: ', fc['nome'], 'Valor em R$: ',fc['valor'])
    total += fc['valor']
print('Saldo atual: R$: ', total)




