#frase = 'Curso Em Video Python'
#print(frase[3])
#print(frase[3:13])
#print(frase[:13])
#print(frase[0:])
#print(frase[1:15])
#print(frase[1:15:2])
#print(frase[1::2])
#print(frase[::2])

#caso eu precise dar um print em uma frase grande e so olocar print(''' e a frase''')
#print('''Não fui, na infância, como os outros
#e nunca vi como os outros viam.
#Minhas paixões eu não podia
#tirar das fontes igual à deles;
#e era outro o canto, que acordava
#o coração de alegria
#Tudo o que amei, amei sozinho.''')






#len mostra o comprimento da frase
#frase = 'ola mundo'
#print (len(frase))

#count serve para fazer a contagem de quantas vezes aparece alguma letra que eu especifiquei
#frase = 'ola mundo'
#print(frase.count('o'))

#find serve para encontrar alguma palavra que voce especificou, e retorna em que momento ela começou,
#caso find retorne o valor de -1 e por que ele nao encontrou a string
#frase = 'Meu mundo'
#frase.find('un')

#Em find eu posso falar qual palavra que quero procurar que e o caso do nome.find('silva')
#E ate que posiçao eu quero que busque essa palavra, se ele encontrar vai me retorar com o valor
#De 0 e se nao com o valor de -1
#nome = str(input('Digite o seu nome: ')).strip().lower()
#print(nome.find('silva'[0:45]))

#nome = str(input("Digite uma frase: ")).strip()
# nome.rfind('a') ele esta buscando a ultima vez que a letra "a" aparece na minha frase e
#me retornar o ultima posiçao dela, [::] serve para eu passar o intervalo que eu quero que ele
#busque essa letra no caso o "a"
#print('É ela aparece pela ultima vez em {}'.format(nome.rfind('a'[::])))

#in serve para saber se certa palavra existe dentro da frase,se sim ele retorna True, caso nao exista
# ele ira retornar o valor de -1
#frase = 'meu mundo'
#print ('mundo' in frase)

#replace serve para trocar determinado nome por outro
#frase = 'ola mundo'
#print(frase.replace('ola', 'oi'))
#caso eu queria mudar de ola para oi e salvar e so colocar
#frase = frase.replace('ola', 'oi')
#print(frase)


#upper deixa as letras minusculas maiusculas e mantem as maiusculas
#frase = 'ola mundo'
#print(frase.upper())
#print(frase.upper().count('O'))

#lower ele transforma as paralavras maiusculas em minusculas e mantem as minusculas
#frase = 'OLA MUNDO'
#print(frase.lower().find('mundo'))

#capitalize ele coloca todos os caracteres em minusculo menos o primeiro caractere
#frase = 'OLA Mundo'
#frase.capitalize()

#title ele faz uma analise de quantas palavras tem a frase e coloca em maiusculo a primeira ele de cada
#palavra
#frase = 'ola mundo, ola mundo'
#frase.title()

#strip ele remove espaços inuteis no inicio e no fim da frase
#rstrip ele so remove o final das frases
#lstrip remove os espaços da esquerda
#frase = '  ola mundo   '
#frase.strip()

#split ele gera uma lista com todas as palavras de uma frase
#frase = 'ola mundo ola mundo oi oi'
#print(frase.split())
#Aqui esta mostrando o primeiro indice da lista
#dividido = frase.split()
#print(dividido[0])
#posso pedir para mostrar a letra que forma a palavra
#print(dividido[0][2])

#join da um espaço entre cada letra
#frase = 'olaas asdsd asdqwe'
#'-'.join(frase)
#' '.join(frase)

