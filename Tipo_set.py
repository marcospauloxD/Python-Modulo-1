# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

#Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
#nao garante a ordem dos elementos
#s1 = set()  # vazio
#s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
#removendo valores duplicados de uma lista
#lista = [ 1, 2, 3, 3, 3, 3, 3, 1]
#s1 = set(lista)
#lista_2 = list(s1)
#print(s1)

# Métodos úteis:
# add, update, clear, discard
#s1 = set()
#adiciona um valor a set, porem so pode ser um valor por vez
#s1.add(1)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

set_1 = {1, 2, 3}
set_2 = {4, 5, 6}
# fez a união dos dois sets
#set_3 = set_1 | set_2
#faz a intersecção de Itens presentes em ambos os sets
#s3 = set_1 & set_2

#vai mostrar os itens que estão presentes apenas no set da esquerda
#s3 = set_1 - set_2

# retorna os itens que não estão presente em ambos
s3 = set_1 ^ set_2
print(s3)