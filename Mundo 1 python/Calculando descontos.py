preco = float(input('Quall o preço do produto: R$'))
desconto = preco - (preco * 5 / 100)
print('O produto que custava {}, com 5% de desconto vai sair por {}'.format(preco,desconto))