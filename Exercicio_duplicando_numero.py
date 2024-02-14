'''
def multiplicacao():
    numero = int(input('Digite um numero para ser duplicado: '))
    duas_vezes = numero * 2
    tres_vezes = numero * 3
    quatro_vezes = numero * 4

    print(f'O numero que voce digitou: {numero}, o dobro dele: {duas_vezes}\n O triplo: {tres_vezes}, o quadruplo: {quatro_vezes}')
multiplicacao()
'''
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))


