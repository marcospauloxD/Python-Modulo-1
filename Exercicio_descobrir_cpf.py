'''
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

'''
'''
#Lista dos valores do cpf
lista_valores = []

valor_cpf_0 = int(input('Digite o primeiro numero do seu cpf: '))
if valor_cpf_0 < 10:
    calculo = valor_cpf_0 * 11
    lista_valores.append(calculo)

valor_cpf_1 = int(input('Digite o primeiro numero do seu cpf: '))
if valor_cpf_1 < 10:
    calculo = valor_cpf_1 * 10
    lista_valores.append(calculo)

valor_cpf_2 = int(input('Digite o primeiro numero do seu cpf: '))
if valor_cpf_2 < 10:
    calculo = valor_cpf_2 * 9
    lista_valores.append(calculo)

valor_cpf_3 = int(input('Digite o primeiro numero do seu cpf: '))
if valor_cpf_3 < 10:
    calculo = valor_cpf_3 * 8
    lista_valores.append(calculo)

valor_cpf_4 = int(input('Digite o primeiro numero do seu cpf: '))
if valor_cpf_4 < 10:
    calculo = valor_cpf_4 * 7
    lista_valores.append(calculo)

valor_cpf_5 = int(input('Digite o primeiro numero do seu cpf: '))
if valor_cpf_5 < 10:
    calculo = valor_cpf_5 * 6
    lista_valores.append(calculo)

valor_cpf_6 = int(input('Digite o primeiro numero do seu cpf: '))
if valor_cpf_6 < 10:
    calculo = valor_cpf_6 * 5
    lista_valores.append(calculo)

valor_cpf_7 = int(input('Digite o primeiro numero do seu cpf: '))
if valor_cpf_7 < 10:
    calculo = valor_cpf_7 * 4
    lista_valores.append(calculo)

valor_cpf_8 = int(input('Digite o primeiro numero do seu cpf: '))
if valor_cpf_8 < 10:
    calculo = valor_cpf_8 * 3
    lista_valores.append(calculo)

valor_cpf_9 = int(input('Digite o primeiro numero do seu cpf: '))
if valor_cpf_9 < 10:
    calculo = valor_cpf_9 * 2
    lista_valores.append(calculo)
#somando cada valor do cpf e multiplicando
soma = (lista_valores[0] + lista_valores[1] + lista_valores[2] + lista_valores[3] 
        + lista_valores[4] + lista_valores[5] + lista_valores[6] + lista_valores[7] + 
        lista_valores[8] + lista_valores[9]) * 10
resto_da_divisao = int(soma % 11)
print(f'Os dois ultimos digitos do seu cpf são: {valor_cpf_9}{resto_da_divisao}')
if resto_da_divisao > 9:
    resto_da_divisao = 0
    print('O penultimo numero do seu cpf é: ', resto_da_divisao)
    print('O ultimo digito do seu cpf é: ', resto_da_divisao)
else:
    ('erro')
'''
#metodo replace para alterar algo dentro da string ex:
#no caso estou substituindo o ponto por um espaço em branco
#cpf_enviado_usuario = '746.824.890-70'.replace('.', '')

#Expressão regular
#import re
#re.sub esta falando que quer substituir algo
#(r'[^0-9],'', esta falando que tudo de 0 ha 9 deve ser substituido para nada ''
#cpf_enviado_usuario = re.sub(r'[^0-9],'','746.824.890-70')
#sum retorna a soma dos valores da lista: ex: sum(lista)
'''
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
import re
import sys

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')

'''


import re

lista_valores = []

cpf = input('Digite somente os 9 primeiros digitos do seu cpf: ')
cpf_usuario = re.sub(r'[^0-9]''.','-', cpf)
#pegando o valor do cpf e transformando em string
cpf_str = str(cpf)
lista_valores.append(cpf_str)
#contando a quantidade de strings presentes na variavel
contador = len(cpf_str)
print(contador)
#se ela for maior que 9 deveria quebrar o codigo
if contador > 9:
    print('Você passou a quantidade de 9 digitos')
#se não vem para esse else
else:
 print(lista_valores.index(0))
1
