# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}
#chave = 'nome','preco','categoria', é valor = 'Caneta Azul', 2.5, 
# 'Escritorio', estou exibindo eles la no print
for chave, valor in produto.items():
    print(chave,valor)


dc = {
    chave: valor.upper()
    #isinstance = verifica se o valor for do tipo str, ele executa o if
    # else ele vai executar o valor
    if isinstance(valor, str) else valor
    #essa parte de baixo e o contrario de str
    #if isinstance(valor, (int, float)) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista
}

s1 = {2 ** i for i in range(10)}
print(s1)