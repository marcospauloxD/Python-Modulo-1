soma = 0
cont = 0
for f in range(3):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(soma)