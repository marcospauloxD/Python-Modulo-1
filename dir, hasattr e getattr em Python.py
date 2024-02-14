# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'strip'
#metodo2 = 'upper'
#metodo3 = 'lower'

if hasattr(string, metodo):
    print('Existe upper')
    #executanado o metodo upper
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)