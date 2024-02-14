#copy - retorna uma cópia rasa (shallow copy)
#aponta um dicionario para o dicionario e acabe sendo
#o mesmo valor

#faz uma copia da lista
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
#indica que d2 esta apontando para o dicionario d1
d2 = d1.copy()
#vai copiar os valores de d1 para d2, vai ser uma copia permanente
#d2 = copy.deepcopy(d1)


#no caso se alterar d2 tambem irar alterar d1  
d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)