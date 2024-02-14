import math
angulo =float(input('Digite o valor o seno: '))

seno = math.sin(math.radians(angulo))
print('O seno é {:.2f}'.format(seno))
cosseno = math.cos(math.radians(angulo))
print('O cosseno é {:.2f}'.format(cosseno))
tangente = math.tan(math.radians(angulo))
print('E a tangente é {:.2f}'.format(tangente))