from datetime import date
atual = date.today().year
idade = int(input('Digite o ano em que você nasceu: '))

resultado = atual - idade
print('Quem nasceu em {} tem {} anos em {}'.format(idade, resultado, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - atual
    print('Ainda falta {} anos para o alistamento1'.format(saldo))
elif idade > 18:
    saldo = atual - 18
    print('Você ja deveria ter se alistado a {} anos'.format(saldo))