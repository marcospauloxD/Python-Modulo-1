nome = str(input('Digite o seu nome: ')).strip().lower()
dividir = nome.split()
print(dividir[0])

dividir2 = nome.split()
# esse menos -1 e como se ele zerase de onde eu quero partir e so considera ate onde seria o ultimo
#nome da lista que eu quero exibir que no casso eu passei como 200
print(dividir2[-1:200:])
