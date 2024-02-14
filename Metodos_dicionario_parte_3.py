# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

#pop ele apaga um indice e entrega o valor dele no final
# nome = p1.pop('nome')
# print(nome)
# print(p1)

#elimina a ultima chave do dicionario
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

#atualiza o dicionario com as informações que você adicionar
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)