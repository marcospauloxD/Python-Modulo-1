termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

cont = 0
for f in range(0, 10):
    #termo = int(input('Primeiro termo: '))
    #razao = int(input('Razão: '))
    total = razao
    total1 = razao + razao
    total2 = razao + razao + razao
    total3 = razao + razao + razao + razao
    total4 = razao + razao + razao + razao + razao
    cont+=1
#print('O termo e {} e a razao e {}: '.format(termo,razao))
print('O termo e {} e a razao e {}: '.format(termo,razao))
print('Sequancia:{},{},{},{},{},{}'.format(termo,total,total1,total2,total3,total4))