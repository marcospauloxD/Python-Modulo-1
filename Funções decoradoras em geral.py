# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

#função decoradora
def criar_funcao(func):
    #criando uma função que vai executar o retorno de func e eu retorno no final
    # o def interno
    def interna(*args, **kwargs):
        print('vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado  foi: {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

#faz uma troca da função inverte_string por criar_funcao assim executa tudo o que esta
#dentro desta função na função inverte_string
@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def e_string(param):
    if not isinstance(param,str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string)

#invertendo string
invertida = inverte_string_checando_parametro('123')
print(invertida)

