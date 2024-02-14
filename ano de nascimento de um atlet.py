from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))

resultado = atual -  ano
print("quem nasceu em {} tera {} em {}".format(ano, resultado, atual))
if resultado > 0 and resultado < 10:
    print('Sua classificação e Mirim')
elif resultado > 9 and resultado < 14:
    print('Sua classificação e Infantil')
elif resultado > 14 and resultado < 20:
    print('Sua classificação e Junior')
elif resultado == 20:
    print('Sua classificação e Senior')
elif resultado > 20:
    print('Sua classificação e Master')