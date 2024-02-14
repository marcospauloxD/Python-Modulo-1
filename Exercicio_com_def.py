#utilizando *args
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)


#adivinhando se um numero e par ou impar
'''
def calculo():
    impar_par = int(input('Informe um numero: '))
    if impar_par % 2 == 0:
        return f'{impar_par} é par'
    return f'{} é impar'
calculo()
'''