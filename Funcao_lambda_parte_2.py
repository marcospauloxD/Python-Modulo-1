'''
def executa(funcao, *args):
    return funcao(*args)



def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

#exibindo e fazendo a soma de dois numero
print(executa(lambda x ,y: x + y, 2, 3))
'''
def executa(funcao, *args):
    return funcao(*args)


def calculo(a, b):
    return a + b

print(executa(lambda a, b: a + b, 3, 5))