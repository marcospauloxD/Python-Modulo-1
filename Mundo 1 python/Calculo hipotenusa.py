
''' Forma tradicional de se calcular a hipotenusa
a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente: '))
hi = (a ** 2 + b ** 2) ** (1/2)
print('O cateto oposto e {}, o cateto adjacente e {}, e a hipotenusa e {}'.format(a,b,hi))'''

import math
a = float(input('Digite o valor do cateto aposto: '))
b = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(a, b)
print('O cateto oposto e {}, o cateto adjacente e {}, e a hipotenusa e {:.2f}'.format(a,b,hi))