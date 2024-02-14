frase = str(input('Digite algo: ')).strip().lower()
print('A letra "a" aparece {} vezes'.format(frase.count('a'[0:])))
print('Ela aparece pela primeira vez em {}'.format(frase.find('a'[0])))
print('É ela aparece pela ultima vez em {}'.format(frase.rfind('a'[::])))