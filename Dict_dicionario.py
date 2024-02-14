# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
#outra forma de criar um dicionario
#pessoa = dict

#criei um dicionario e adicionei nome e sobrenome dentro dele
#pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

# print(pessoa, type(pessoa))
#acessando o indice nome dentro do dicionario
print(pessoa['nome'])
#acessando o indice sobrenome dentro do dicionario
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    #acessando o dicionario pessoa e os indices do dicionario
    print(chave, pessoa[chave])