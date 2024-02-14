preco = float(input('Digite o valor do produto: '))
pagamento = int(input('1- A vista'
                      
                       '2- A vista no cartão'
                      
                       '3- Em ate 2x preço normal'
                      
                       '4- 3x vezes ou mais no cartão com acrescimo de 20%: '))

if pagamento == 1:
    pag = preco - (preco * 10 / 100)
    print('O valor com este desconto ficou {}'.format(pag))
elif pagamento == 2:
    pag = preco - (preco * 5 / 100)
    print('valor com este desconto ficou {}'.format(pag))
elif pagamento == 3:
    print('valor final e {} '.format(preco))
elif pagamento == 4:
    pag = preco + (preco * 20 / 100)
    print('valor final e {}'.format(pag))