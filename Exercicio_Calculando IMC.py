altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

calculo = peso / (altura * altura)
print('Seu peso e {}'.format(calculo))
if calculo < 18.5:
    print('Você esta abaixo do peso')
elif calculo > 18.5 and calculo < 26:
    print('Seu peso e ideal')
elif calculo > 25 and calculo < 31:
    print('Você esta com sobrepeso')
elif calculo > 30 and calculo < 41:
    print('Você esta com obesidade')
elif calculo > 40:
    print('Você esta com obesidade morbida')