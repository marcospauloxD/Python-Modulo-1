import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
#nessa lista os valores ja estão todos dentro da memoria 
lista = [n for n in range(10)]
#generator = função que entrega um valor por vez, função que sabe pausar
generator = (n for n in range(10))
#sys.getsizeof = ve o tamanho da lista em bytes
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
#aqui o generator vai me entregar um numero para cada next
print(next(generator))
print(next(generator))

#as vantagens da lista e que eu posso acessar os indices dela
#generator não tem tamanho nem indice, então não posso acessar
#um indice [0] por exemplo, posso fazer um len no generator
#porque ele não esta na memoria