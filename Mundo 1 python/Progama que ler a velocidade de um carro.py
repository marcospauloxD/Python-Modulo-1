vel = int(input('Qual a volocidade do seu carro?: '))
if vel == 80:
    print('Você esta no limite de velocidade')
elif vel > 80:
    vel2 = (vel - 80 ) * 7
    print('Você foi multando em {:.2f} reais'.format(vel2))
else:
    print('Voce nao esta no limite de volicidade')