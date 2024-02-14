#Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

# adiciona valor se a chave não existe
pessoa.setdefault('idade', 0)
print(pessoa['idade'])

#len mostra a quantidade de chaves dentro do dicionario
# print(len(pessoa))

#keys retorna as chaves do dicionario
#print(tuple(pessoa.keys()))
# print(list(pessoa.keys()))

#values mostra os valores dentro do dicionario
# print(list(pessoa.values()))

#items retorna a chave e o valor
#list = esta convertendo o dicionario para um alista
# print(list(pessoa.items()))

#percorre a lista e me retorna os valores dentro dela
# for valor in pessoa.values():
#     print(valor)

#retorna a chave e o valor 
# for chave, valor in pessoa.items():
#     print(chave, valor)
