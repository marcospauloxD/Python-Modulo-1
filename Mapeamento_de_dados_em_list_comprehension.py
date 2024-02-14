# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'nome': produto['preco'] * 1.05}
    #if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(novos_produtos)
#sep = '\n' serve para dar uma quebra de linha
print(*novos_produtos, sep='\n')