km = float(input('Digite a distancia em km: '))

km1 = km * 0.50
km2 = km * 0.45
if km <= 200:
    print('Você ira pagar R${:.2f}  '.format(km1))
elif km >= 201:
    print('Você ira pagar R${:.2f} '.format(km2))
