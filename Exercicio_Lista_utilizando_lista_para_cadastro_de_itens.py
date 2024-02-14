'''
Faça uma lista de compras usando lista = []
O usuario deve ter a possibilidade de inserir, apagar e listar valores  da sua lista
Não permita  que o programa quebre com erros  de indices inexistentes na lista
'''
import os
#lista para armazenamento
lista = []
#pergutando se o cliente deseja cadastrar um item
cadastro = input('Deseja cadastrar um item? [sim] ou [não]: ')
#contador do loop
count = 0
#loop, enquanto o usuario informar [sim] ele vai continuar cadastrando produtos
while cadastro == 'sim' or cadastro == 'siim' or cadastro_novo == 'sim' or cadastro_novo == 'siim':
    #cadastro do produto
    cadastro = input('Insira o nome de um item: ')
    #armazenando produto na lista
    lista.append(cadastro)
    #imprimindo a lista
    print('Sua lista contem estes itens: ', lista)
    #perguntando se o usuario deseja deletar algum item da lista
    deletar = input('Deseja deletar algum item da [sim] ou [não] : ')
    #se o usuario informar que sim ele vai entrar nesse if e vai perguntar qual item ele quer excluir
    if deletar == 'sim' or deletar == 'siim':
        #o usuario vai informar o item a ser excluido
        deletar_item = input('Qual item deseja deletar da lista? : ')
        #excluindo o item
        lista.remove(deletar_item)
        #imprimindo que o item foi excluido
        print(f'O item {deletar_item}, foi exluido da sua lista')
    #cadastrando um novo produto
    cadastro_novo = input('Deseja cadastrar um novo item?: [sim] ou [não]')
    #os.system('cls') serve para limpa o terminal
    os.system('cls')
    #adicionando +1 ao contador do meu loop
    count+=1
#transformando a lista[] em uma lista, para poder enumerar ela a seguir
nova_lista = list(lista)
#enumerando os itens da minha lista
for i in enumerate(nova_lista):
    print('Sua lista contem os seguintes itens: ', i)





