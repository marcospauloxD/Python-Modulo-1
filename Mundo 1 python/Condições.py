#Simplificando
#carro = int(input('Digite quantos anos tem o seu carro: '))
#print('carro novo'if carro <= 3 else print('carro velho'))

#carro = int(input('Digite quantos anos tem o seu carro: '))
#if carro <= 3:
    #print('Carro novo')
#else:
    #print('Carro velho')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
result = (n1+n2) / 2

if result >= 6:
    print('Sua media foi {},é você esta aprovado'.format(result))
else:
    print('Sua media foi {},é você esta reprovado'.format(result))