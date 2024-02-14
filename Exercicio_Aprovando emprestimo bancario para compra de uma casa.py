casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salario: '))
anos = int(input('Digite a quantidade de anos que deseja pagar a casa: '))


divisao = (casa / anos) / 12
prestacao = salario * 30 / 100
print('Você tera que pagar {:.2f} por mes, durante {} anos para quintar a casa '.format(divisao,anos))
if divisao <= prestacao:
    print('Voce pode adquirir o emprestimo para comprar a casa ')
elif divisao > prestacao:
    print('Você não pode adquirir o emprestimo ')

