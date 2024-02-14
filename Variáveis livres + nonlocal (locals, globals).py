#Variaveis livres + nonlocal
#(locals), (globals)
'''
def fora(x):
    # esse e 'a' e considerada uma variavel livre porque ela não esta definida
    #dentro do escopo da função 'dentro'
    #a = 1
    #agora a passou a ser x
    a = x
    def dentro():

        #vai me dizer qual variavel é local
        #print('Variavel local: ', locals)

        #vou ter acesso as variaveis livres
        print('Variavel livre:', dentro.__code__.co_freevars)

        return a
    return dentro

#criei uma função e chamei a função 'fora' dentro dessa função que retorna a função
#dentro sem executar a função dentro
#dentro = fora()
#irei chamar a função fora(x)
dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())
'''

#print(globals())
#print(locals())

def concatenar(string_inicial):
    #meu valor final ira pegar essa string inicial
    valor_final = string_inicial

    #esse valor_a_concatenar não esta fazendo nada
    def interna(valor_a_concatenar):
        #aqui estou falando que o valor_final não é uma variavel local
        nonlocal valor_final
        #vai fazer a+b, depois a+b+c, depois a+b+c+d
        valor_final += valor_a_concatenar
        #valor_final só irá retorna a string inicial
        return valor_final
    return interna

#criei uma variavel 'c' que recebe o def 'concatenar' é a
#letra que eu escolhi que é 'a'
c = concatenar('a')

print(c('b'))
print(c('c'))
print(c('d'))