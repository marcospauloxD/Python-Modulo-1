nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Você esta reprovado, sua media foi {}'.format(media))

elif media > 5 and media < 6.10:
    print('Você esta de recuperação, sua media foi {}'.format(media))
else:
    print('Você esta aprovado, sua media foi {}'.format(media))