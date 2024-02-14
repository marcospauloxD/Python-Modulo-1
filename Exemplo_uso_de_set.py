#Utilizando sets

letras = set()
while True:
    letra = input('Digite: ')
    #.add esta adicionando ao set, é .lower esta convertendo letras maisculas para minusculas
    letras.add(letra.lower())

    #se l estiver em letras ele imprimi algo
    if 'l' in letras:
        print('Parabens!!!, você encontrou a letra certa')
        break
    print(letras)