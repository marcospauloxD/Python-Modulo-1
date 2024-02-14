"""
split e join com list e str
split - divide uma string (list) em determinados caracteres
join - une uma string
"""
#frase = 'Olhar só que,coisa interessante'
#split faz a quebra das palavras nos espaços em branco
#lista_palavras = frase.split()
#print(lista_palavras)
'''
se quiser eu posso pedir para o split fazer a quebra na virgula
da frase
'''
#lista_palavras = frase.split(',')
#print(lista_palavras)

'''
outra forma de alterar seria fazendo um for

'''
#for i,frase in enumerate(lista_palavras):
    #print(lista_palavras[i])

'''
strip = que significar cortas os espaços do começo e do fim
de uma frase ex:

rstrip = vai cortar os espaços a direita 

lstrip = que vai cortar os espaços da esquerda
'''
#for i,lista_palavras in enumerate(lista_palavras):
    #print(lista_palavras[i].strip())
    #print(lista_palavras[i].rstrip())
    #print(lista_palavras[i].lstrip())
'''
join = faz a união de strings
'' este e o separador, caso eu queira separar algo preciso passar
um valor como '-' assim ele vai separar cada letra com um - ex:
'''
#se eu passar assim ele nao vai separar pois não tem um separador
#dentro de ''
#frases = ''.join('abc')
frases = '-'.join('abc')
print(frases)