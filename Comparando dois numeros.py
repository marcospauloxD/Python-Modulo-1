num = int(input('Digite um número: '))
num1 = int(input('Digite outro número: '))

if num > num1:
    print('{} é o número maior'.format(num))
elif num1 > num:
    print('{} é o número maior '.format(num1))
elif num == num1:
    print('Não existe valor maior, os dois são iguais. ')