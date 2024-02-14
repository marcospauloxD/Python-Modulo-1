import random

num = int(input('Digite um dos numero 1- Pedra, 2- Papel, 3- Tesoura: '))
a = random.randrange(1,4,1)

if num == 1 and a == 2:
    if num == 1:
        print('Você escolheu Pedra')
    if num == 2:
        print('Você escolheu Papel')
    if num == 3:
        print('Você escolheu Tesoura')
    if a == 1:
        print('O computador escolheu Pedra')
    if a == 2:
        print('O computador escolheu Papel')
    if a == 3:
        print('O computador escolheu Tesoura')

    print('O computador ganhou')

elif num == 2 and a == 1:
    if num == 1:
        print('Você escolheu Pedra')
    if num == 2:
        print('Você escolheu Papel')
    if num == 3:
        print('Você escolheu Tesoura')
    if a == 1:
        print('O computador escolheu Pedra')
    if a == 2:
        print('O computador escolheu Papel')
    if a == 3:
        print('O computador escolheu Tesoura')
    print('Você ganhou do computador')
elif num == 1 and a == 3:
    if num == 1:
        print('Você escolheu Pedra')
    if num == 2:
        print('Você escolheu Papel')
    if num == 3:
        print('Você escolheu Tesoura')
    if a == 1:
        print('O computador escolheu Pedra')
    if a == 2:
        print('O computador escolheu Papel')
    if a == 3:
        print('O computador escolheu Tesoura')
    print('Você ganhou do computador')
elif num == 3 and a == 1:
    if num == 1:
        print('Você escolheu Pedra')
    if num == 2:
        print('Você escolheu Papel')
    if num == 3:
        print('Você escolheu Tesoura')
    if a == 1:
        print('O computador escolheu Pedra')
    if a == 2:
        print('O computador escolheu Papel')
    if a == 3:
        print('O computador escolheu Tesoura')
    print('O computador ganhou')
elif num == 2 and a == 3:
    if num == 1:
        print('Você escolheu Pedra')
    if num == 2:
        print('Você escolheu Papel')
    if num == 3:
        print('Você escolheu Tesoura')
    if a == 1:
        print('O computador escolheu Pedra')
    if a == 2:
        print('O computador escolheu Papel')
    if a == 3:
        print('O computador escolheu Tesoura')
    print('O computador ganhou')
elif num == 3 and a == 2:
    if num == 1:
        print('Você escolheu Pedra')
    if num == 2:
        print('Você escolheu Papel')
    if num == 3:
        print('Você escolheu Tesoura')
    if a == 1:
        print('O computador escolheu Pedra')
    if a == 2:
        print('O computador escolheu Papel')
    if a == 3:
        print('O computador escolheu Tesoura')
    print('Você ganhou do computador')
elif num == 1 and a == 1:
    print('Foi empate pois os dois escolheram pedra')
elif num == 2 and a == 2:
    print('Foi empate pois os dois escolherem papel')
elif num == 3 and a == 3:
    print('Foi empate pois os dois escolheram tesoura')