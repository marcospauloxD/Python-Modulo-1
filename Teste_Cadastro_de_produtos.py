

entrada = input('Deseja cadastrar uma pessoa?, s[sim] ou n[não]')
lista_pessoas = []
cont = 0
while entrada == 'sim':
    nome = input('Digite o nome da pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))
    lista_pessoas.append(nome)
    lista_pessoas.append(idade)
    novo_cadastro = input('Deseja cadastrar outra pessoa? s[sim] n[não]')
    if novo_cadastro == 'nao' or novo_cadastro == 'não':
        print('lista a baixo')
        for nome,idade in enumerate(lista_pessoas):
            print(nome,idade)
        break
    cont += 1
