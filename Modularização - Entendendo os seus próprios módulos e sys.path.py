# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import sys

import aula97_m
from aula97_m import variavel_modulo


print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')
#Importando um modulo de dentro da aula97
print(aula97_m.variavel_modulo)
#Como importar coisas do seu próprio módulo (ponto de vista do __main)