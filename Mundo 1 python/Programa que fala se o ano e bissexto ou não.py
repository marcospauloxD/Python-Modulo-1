ano = int(input('Digite o ano para saber se ele e bissexto ou não: '))
ano1 = ano % 4
if ano1 == 0:
    print('Este ano e bissexto ')
else:
    print('Este ano não e bissexto')