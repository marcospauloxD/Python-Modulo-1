r1 = int(input("Digite o primeiro numero: "))
r2 = int(input('Digite o segundo numero: '))
r3 = int(input('Digite o terceiro numero: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('pode se formar um triangulo')
else:
    print('não pode formar um triangulo')