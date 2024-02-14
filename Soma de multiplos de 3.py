soma = 0
cont = 0
for f in range(1, 501, 2):
    if f % 3 == 0:
        soma = soma + f
        'Para simplificar poderia colocar soma += f'
        'a mesma coisa com cont que seria cont += 1'
        cont = cont + 1
print('A soma de todos os {} numeros e {}'.format(cont,soma))