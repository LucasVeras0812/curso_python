# Entendendo os seus proprios modulos python
# O primeiro módulo executado chama-se __main__
# Voce pode importar outro modulo inteiro ou parte do modulo
# O python conhece a pasta onde o __main__ está e as pastas abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O ptyhon conhece todos os módulo e pacotes presentes nos caminhos de sys.path

import aula97_m
from aula97_m import variavel_modulo

print("Este módulo se chama", __name__)

print(aula97_m.variavel_modulo)
print(variavel_modulo)