import random
#random.randrange(0,10) esta percorrendo de 0 a 10 e me retornando um valor aleatorio
rand = random.randrange(0,10)
print('Computador: Pensei em um número,tente advinhar')
escolha = int(input('Digite um numero de 1 a 10: '))
if escolha == rand:
    print('voce acertou o numero que o computador escolheu ')
else:
    print('Voce errou')
print('numero que o computador escolheu: ',rand)