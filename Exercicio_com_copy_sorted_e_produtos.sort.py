# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
#produtos = [
#    {'nome': 'Produto 5', 'preco': 10.00},
#    {'nome': 'Produto 1', 'preco': 22.32},
#    {'nome': 'Produto 3', 'preco': 10.11},
#    {'nome': 'Produto 2', 'preco': 105.87},
#    {'nome': 'Produto 4', 'preco': 69.90},
#]
'''
Ordenando por nome

def ordena(o):
    return o['nome']
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos.sort(key=ordena)
print(produtos)
'''
'''
Ordenando por valor

def valor(v):
    return v['preco']
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
produtos.sort(key=valor)
print(produtos)
'''
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
produtos.sort('preco')
print(produtos)
def valor(v):

    novos_produtos = [
        {**produtos, 'nome': produtos['preco' * 0.10]}
    ]
    #novos_produtos.sort(key=valor)
    print(novos_produtos)


#produtos.sort(reverse=True)
#print(produtos)
#nova_lista = produtos.copy()
#print(nova_lista, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)