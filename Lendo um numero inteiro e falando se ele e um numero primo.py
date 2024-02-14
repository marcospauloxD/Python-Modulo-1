num = int(input('Digite um número: '))
total = 0
for f in range(1, num + 1):
    if num % f == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(f), end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('É um número primo')
else:
    print('Não é um número primo')