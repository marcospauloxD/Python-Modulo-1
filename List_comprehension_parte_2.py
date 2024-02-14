lista = []
for x in range(3):
    for y in range(3):
        #nessa parte precisa adicionar o numero dentro de uma tupla
        #para que possa ser armazenado dentro de uma lista esses
        #dois indices
        lista.append((x,y))
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista =[
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
] 
print(lista)