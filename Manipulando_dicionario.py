 #Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'
#criando uma chave e adicionando ela ao dicionario
pessoa[chave] = 'Luiz Otávio'
#criando uma chave e adicionando ela ao dicionario
pessoa['sobrenome'] = 'Miranda'

#esta acessando o dicionario e dentro dele a chave
print(pessoa[chave])

#alterando o valor da chave de 'luiz otavio' para 'maria'
pessoa[chave] = 'Maria'

#deletando a chave sobrenome
del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

#get tenta obter uma chave e retorna none se a chave nao existir
# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')