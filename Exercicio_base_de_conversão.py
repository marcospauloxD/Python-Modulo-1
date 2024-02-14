numero = int(input('Digite um numero: '))
conversao = int(input('Escolha a forma de conversão: 1-Binario '))
converter = str(numero)
contador = len(converter)
#converter_numero = int(converter)
print('contador de numero: ',contador)

if conversao == 1:
    if contador == 2:
        for i in range(1):
            variavel = numero / 2
            print(variavel)
            variavel2 = variavel / 2
            print(variavel2)
            variavel3 = variavel2 / 2
            print(variavel3)
            variavel4 = variavel3 / 2
            print(variavel4)
            variavel5 = variavel4 / 2
        print(variavel5)