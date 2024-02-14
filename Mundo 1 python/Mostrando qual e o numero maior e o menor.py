num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

#Menor numero
if num1 < num2 and num1 < num3:
    menor = num1
    print('O menor numero e : ', menor)
if num2 < num1 and num2 < num3:
    menor = num2
    print('O menor numero e : ',menor)
if num3 < num2 and num3 < num1:
    menor = num3
    print('O menor numero e : ',menor)

#Maior numero
if num1 > num2 and num1 > num3:
    maior = num1
    print('O Maior numero e : ',maior)
if num2 > num1 and num2 > num3:
    maior = num2
    print('O Maior numero e : ',maior)
if num3 > num1 and num3 > num2:
    maior = num3
    print('O Maior numero e : ',maior)
