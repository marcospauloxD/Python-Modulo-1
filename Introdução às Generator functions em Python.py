# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))
'''
def generator(n=0):
    yield 1 
    print('Continuando...')
    yield 2
    print('Mais uma vez')
    yield 3
    print('Vou terminar')
    return 'Acabou'

gen = generator(n=0)
#print(next(gen))
for n in gen:
    print(n)
'''

def generator(n= 0, maximum= 10):
    while True:
        yield n
        n+=1

        if n >= maximum:
            return 'Acabou'
#gen = generator(n=5, maximum=15)
#gen = generator(maximum=1000)
gen = generator()
for n in gen:
    print(n)    