salario = float(input('Digite o valor do seu salario: '))
#aumento = (salario * 0.10) + salario
if salario > 1250:
    aumento = (salario * 0.10) + salario
    print('o seu salario e superior a 1250 e tera um aumento de 10%, passando a ser {}'.format(aumento))
elif salario <= 1250:
    aumento = (salario * 0.15) + salario
    print('Seu salario e inferior a 1250 e téra um aumento de 15% passando a ser {} R$'.format(aumento))
