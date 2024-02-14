"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754

https://en.wikipedia.org/wiki/Double-precision_floating-point_format

https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)



#numero_1 = 0.1
#numero_2 = 0.7
#numero_3 = numero_1 + numero_2
#print(numero_3)

#resultado final já formatado de um numero decimal
#rint(f'{numero_3:.2f}')

#função round, recebe o primeiro numero, e no segundo argumento
#você passa o numero de casas decimais ex:
#print(round(numero_3, 2))






