cont = 0
entrada = int(input('Digite se quer entrar digite 1 ou 0 para sair: '))
while entrada == 1:
    soma1 = int(input('Digite um numero para fazer a sua soma: '))
    soma2 = int(input('Digite um numero para fazer a sua soma: '))
    soma3 = int(input('Digite um numero para fazer a sua soma: '))
    soma4 = int(input('Digite um numero para fazer a sua soma: '))
    soma5 = int(input('Digite um numero para fazer a sua soma: '))
    soma6 = int(input('Digite um numero para fazer a sua soma: '))
    if soma1 % 2 == 0 and soma2 % 2 == 0 and soma3 % 2 == 0 and soma4 % 2 == 0 and soma5 % 2 == 0 and soma6 % 2 == 0:
        total = soma1 + soma2 + soma3 + soma4 + soma5 + soma6
        print(total)
    elif soma1 % 2 == 0 and soma2 % 2 == 0 and soma3 % 2 == 0 and soma4 % 2 == 0 and soma5 % 2 == 0:
        total = soma1 + soma2 + soma3 + soma4 + soma5
        print(total)
    elif soma1 % 2 == 0 and soma2 % 2 == 0 and soma3 % 2 == 0 and soma4 % 2 == 0:
        total = soma1 + soma2 + soma3 + soma4
    elif soma1 % 2 == 0 and soma2 % 2 == 0  and soma3 % 2 == 0:
        total = soma1 + soma2 + soma3
        print(total)
    elif soma1 % 2 == 0 and soma2 % 2 == 0:
        total = soma1 + soma2
        print(total)
    else:
        print('Numero no compativel')
    #print(total)

    saida = int(input('Digite 0 para sair ou 1 para continuar somando os numeros '))
    if saida == 0:
        break
cont+=1
#print(total)