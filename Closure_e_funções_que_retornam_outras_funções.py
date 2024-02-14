"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar()

falar_bom_dia = criar_saudacao('bom dia', 'luiz')
print(falar_bom_dia)
falar_boa_noite = criar_saudacao('boa noite', 'luiz')
print(falar_boa_noite)

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))