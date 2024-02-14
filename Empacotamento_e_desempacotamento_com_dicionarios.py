# args = argumentos não nomeados
#kwargs = argumentos nomeados
# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
#print(a,b)


#values tras as keys
#a,b = pessoa.values()
#print (f'nome: {a} é sobrenome: {b}')

#itens tras uma tupla com nome e valor e sobrenome e valor
#a,b = pessoa.items()
#print(a,b)

#mostra a tupla e o valor nela como nome aline ou sobrenome souza
#(a1, a2), (b1, b2) = pessoa.items()
#print(a1, a2)
#print(b1, b2)

#tambem podia ser feito desse jeito
#for chave, valor in pessoa.items():
    #print(chave, valor)

#Unindo dois dicionarios
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoas = {
    'idade': 16,
    'altura': 1.60
}
#** serve para adicionar um dicionario dentro de outro, depois da virgula estou
#criando outra chave dentro do dicionarios
#caso eu mude o nome 'chave' para algum nome que ja existe detro do dicionario
#como 'nome', ele ira mudar o nome e tambem o valor da chave

#pessoa_completa = {**pessoa, 'chave' : 1}
pessoa_completa = {**pessoa, **dados_pessoas}
#print(pessoa_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    #tem que ter cuidado com os args 
    print('NÃO NOMEADOS: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)
#esse 1 e 2 como não estão nomeados vão ir parar la no print de não nomeados
#no caso no args 
#mostro_argumentos_nomeados(1, 2,nome='joana', qlq=123)1

#desempacotando o dicionario pessoa_completa
#mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)