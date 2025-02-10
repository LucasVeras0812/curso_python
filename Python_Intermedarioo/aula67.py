"""
Valores padrão para parametros
Ao definir uma função, os parametros podem
ter valores padrão. caso o valor não seja
enviado para o parametro, o valor padrão será 
usádo.
"""

def soma(x, y, z=0):
    print(x + y + z)

soma(1, 2)
soma(3, 5)
soma(100, 200)